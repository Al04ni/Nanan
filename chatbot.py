from chatterbot import ChatBot

bot = ChatBot(
    'Nanan', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
    )

print('Welcome, am Nanan your chatbot developed by chatterbot.')
#Getting responses from our chatbot
while True:
    try:
        bot_response = bot.get_response(input())
        print(bot_response)
    
    except(KeyboardInterrupt,EOFError, SystemError):
        break