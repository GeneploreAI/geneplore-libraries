from geneplore_api import api_sync as api

api.api_key = ''

conversation = []

while True:
    conversation.append(api.Chat.ConversationMessage('user', input('You: ')))
    resp, cost = api.Chat.OpenAI("gpt-3.5-turbo-0613", conversation)
    conversation.append(api.Chat.ConversationMessage(resp.role, resp.content))
    print(resp.content)