from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
    chatbot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('/home/bel024b/PErsonal/EME-offline-chatbot-using-YML/data/'):
        convData = open(r'/home/bel024b/PErsonal/EME-offline-chatbot-using-YML/data/' + file,
                        encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        print("Training completed")


setup()

# bot= ChatBot('Bot')
# #bot.set_trainer(ListTrainer)
# trainer = ListTrainer('Bot')
#
# for files in os.listdir ('/home/bel024b/PErsonal/EME-offline-chatbot-using-YML/data/'):
#     data = open ('/home/bel024b/PErsonal/EME-offline-chatbot-using-YML/data/' +files, 'r').readlines()
#     trainer.train('Bot')
#
# while True:
#     message =input('You:')
#     reply =bot.get_response(message)
#     print('ChatBot:',reply)
#     if message.strip() == 'Bye':
#         print('ChatBot: Bye')
#         break