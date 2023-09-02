from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#bot = ChatBot('chatbot',read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])


def index(request):
    return render(request, 'chat/index.html')


def getResponse(request):
    # Add your code here
    userMessage = request.Get.get('userMessage')
    return HttpResponse(userMessage)
