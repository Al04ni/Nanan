from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Nanan', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
    )

#Training our bot
trainer = ListTrainer(bot)
trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome',
])

print('Welcome, am Nanan your chatbot developed by chatterbot.')

#Getting responses from our chatbot
while True:
    try:
        bot_response = bot.get_response(input())
        print(bot_response)
    
    except(KeyboardInterrupt,EOFError, SystemError):
        break