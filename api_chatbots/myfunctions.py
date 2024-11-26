from openai import OpenAI
from anthropic import Anthropic
from abc import ABC, abstractmethod
from copy import deepcopy
class ChatBotInterface(ABC):
    @abstractmethod
    def add_user_message(self, message: str):
        pass
    
    @abstractmethod
    def add_assistant_message(self, message: str):
        pass
    
    @abstractmethod
    def respond(self, temperature: float = 1):
        pass
    
    @abstractmethod
    def get_latest_message(self):
        pass

class ChatGPT(ChatBotInterface):
    def __init__(self, api_key: str, system_prompt: str = "You are a helpful assistant.", model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.context = []
        self.system_prompt = system_prompt
        self.add_system_message(system_prompt)
        self.model = model

    def add_system_message(self, message: str):
        self.add_to_context(message, "system")

    def add_user_message(self, message: str):
        self.add_to_context(message, "user")

    def add_assistant_message(self, message: str):
        self.add_to_context(message, "assistant")

    def add_to_context(self, message: str, role: str):
        self.context.append({"role": role, "content": message})

    def respond(self, temperature: float = 1):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.context,
            temperature=temperature,
        )
        message = response.choices[0].message.content
        self.add_assistant_message(message)

        return message
    
    def get_latest_message(self):
        return self.context[-1]["content"]
    
class Claude(ChatBotInterface):
    def __init__(self, api_key: str, system_prompt: str = "You are a helpful assistant.", model: str = "claude-3-5-sonnet-20240620"):
        self.api_key = api_key
        self.client = Anthropic(api_key=api_key)
        self.system_prompt = system_prompt
        self.context = []
        self.model = model

    def add_user_message(self, message: str):
        self.add_to_context(message, "user")

    def add_assistant_message(self, message: str):
        self.add_to_context(message, "assistant")

    def add_to_context(self, message: str, role: str):
        self.context.append({"role": role, "content": message})

    def respond(self, temperature: float = 1, max_tokens: int = 1000):
        response = self.client.messages.create(
            model=self.model,
            messages=self.context,
            system=self.system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        message = response.content[0].text
        self.add_assistant_message(message)
        return message
    
    def get_latest_message(self):
        return self.context[-1]["content"]

def prompt(chatbot: ChatBotInterface, prompt: str):
    new_instance = chatbot.__class__(
        api_key=chatbot.api_key,
        system_prompt=chatbot.system_prompt,
        model=chatbot.model
    )
    new_instance.context = chatbot.context.copy()
    new_instance.add_user_message(prompt)
    return new_instance.respond()