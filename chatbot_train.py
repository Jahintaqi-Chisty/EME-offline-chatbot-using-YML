from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('EME',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('F:/DiuUniversity/AI Research/Chatterbot/Chatbot_Project-master/Chatbot_Project-master/data'):
        convData = open(r'F:/DiuUniversity/AI Research/Chatterbot/Chatbot_Project-master/Chatbot_Project-master/data/' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        #print("Training completed")


setup()
