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

## Supported Models
- ChatGPT
- Claude

