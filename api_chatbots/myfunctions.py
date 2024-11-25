from openai import OpenAI

class ChatGPT():
    def __init__(self, api_key: str, system_prompt: str = "You are a helpful assistant.", model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.context = []
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