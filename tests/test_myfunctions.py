import os
import pytest
from api_chatbots.myfunctions import ChatGPT, Claude
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@pytest.fixture
def chatgpt():
    return ChatGPT(api_key=OPENAI_API_KEY)

@pytest.fixture
def claude():
    return Claude(api_key=ANTHROPIC_API_KEY)

class TestChatGPT:
    def test_initialization(self, chatgpt):
        assert chatgpt.api_key == OPENAI_API_KEY
        assert len(chatgpt.context) == 1  # Should have system message
        assert chatgpt.context[0]["role"] == "system"

    def test_add_messages(self, chatgpt):
        chatgpt.add_user_message("Hello")
        chatgpt.add_assistant_message("Hi there!")
        
        assert len(chatgpt.context) == 3  # system + user + assistant
        assert chatgpt.context[1]["role"] == "user"
        assert chatgpt.context[1]["content"] == "Hello"
        assert chatgpt.context[2]["role"] == "assistant"
        assert chatgpt.context[2]["content"] == "Hi there!"

    def test_get_latest_message(self, chatgpt):
        chatgpt.add_user_message("Test message")
        assert chatgpt.get_latest_message() == "Test message"

    @pytest.mark.integration
    def test_respond(self, chatgpt):
        response = chatgpt.respond(temperature=0.7)
        assert isinstance(response, str)
        assert len(response) > 0

class TestClaude:
    def test_initialization(self, claude):
        assert claude.api_key == ANTHROPIC_API_KEY
        assert len(claude.context) == 0  # No initial context
        assert claude.system_prompt == "You are a helpful assistant."

    def test_add_messages(self, claude):
        claude.add_user_message("Hello")
        claude.add_assistant_message("Hi there!")
        
        assert len(claude.context) == 2
        assert claude.context[0]["role"] == "user"
        assert claude.context[0]["content"] == "Hello"
        assert claude.context[1]["role"] == "assistant"
        assert claude.context[1]["content"] == "Hi there!"

    def test_get_latest_message(self, claude):
        claude.add_user_message("Test message")
        assert claude.get_latest_message() == "Test message"

    @pytest.mark.integration
    def test_respond(self, claude):
        claude.add_user_message("Hello")
        response = claude.respond(temperature=0.7)
        assert isinstance(response, str)
        assert len(response) > 0


