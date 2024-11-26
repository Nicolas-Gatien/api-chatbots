[![PyPI version](https://badge.fury.io/py/api-chatbots.svg)](https://pypi.org/project/api-chatbots/)

# API Chatbots
A Python library that simplifies interactions with various Large Language Model APIs including ChatGPT, Claude, and Gemini.

## Usage
### Managing Conversation Context
The library maintains conversation history automatically. Each interaction is stored in the context:

```python
from api_chatbots import ChatGPT

# Initialize the chatbot with your API key
chatbot = ChatGPT(api_key="your_api_key")

# Add a user message to the conversation
chatbot.add_user_message("Hello, how are you?")

# Generate a response
chatbot.respond()

# Get the latest message
print(chatbot.get_latest_message())
```

### Single Prompt Instances
If you only need to prompt a chatbot once, you can use the `prompt` function instead of instantiating a full chatbot.

```python
from api_chatbots import prompt, ChatGPT, Claude

turtles = prompt(ChatGPT(api_key="your_api_key"), "Generate a paragraph about Turtles")
print(turtles)

tigers = prompt(Claude(api_key="your_api_key"), "Generate a paragraph about Tigers")
print(tigers)
```

### Loading API Keys From .env
`api_chatbots` will pull OpenAI and Anthropic API keys from the `.env` file.
```.env
OPENAI_API_KEY='your-api-key'
ANTHROPIC_API_KEY='your-api-key'
```
If the API key is set, you can declare a ChatGPT or Claude instance without directly passing the API key:
```python
bot = ChatGPT(api_key='your-api-key')
# becomes:
bot = ChatGPT()
```

## Supported Models
- ChatGPT
- Claude

