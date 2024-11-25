# API Chatbots
A Python library that simplifies interactions with various Large Language Model APIs including ChatGPT, Claude, and Gemini.

## Usage
### Managing Conversation Context
The library maintains conversation history automatically. Each interaction is stored in the context:

```python
chatbot = ChatGPT(api_key="your_api_key")
chatbot.add_user_message("Hello, how are you?")
chatbot.respond()
print(chatbot.get_latest_message())
```