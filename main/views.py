from django.shortcuts import render, redirect
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from main.utils import saveData
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from .under import _start, _bountyoptions
import json
import telepot
# import time

User = get_user_model()

token = settings.TOKEN
secret = settings.SECRET
webhook_url = "https://localhost:8000/telegram/" + secret
bot = telepot.Bot(token)
print('edomodo')
print(bot.getWebhookInfo()['url'], "dear")
# if webhook_url != bot.getWebhookInfo()['url']:
print(bot.getWebhookInfo()['url'], "deasrrf")
# time.sleep(3)
# bot.setWebhook(webhook_url)
print(bot.getWebhookInfo()['url'], "deasrrf")
    

# bot.setWebhook(url=url)


# Create your views here.
def index(request):
    csrf_token = get_token(request)
    user = ""
    if request.user.is_authenticated:
        address = request.user
        if User.objects.filter(address=address).exists():
            user = User.objects.get(address=address)
    context = {"csrftoken": csrf_token, "user": user}
    return render(request, 'main/index.html', context)


def echo(request):
    data = json.loads(request.body.decode("utf-8"))
    username = data['username']
    address = data['address']
    if User.objects.filter(address=address).exists():
        user = authenticate(address=address, password=address)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            print("authenticated")
        else:
            # No backend authenticated the credentials
            print("Not authenticated")
    else:
        user = User.objects.create_user(username=username, address=address, password=address)
        us = authenticate(address=address, password=address)
        if us is not None:
            login(request, us)
    context = {}
    return render(request, 'main/index.html', context)


@login_required(login_url='/')
def dashboard(request):
    if request.user.is_authenticated:
        address = request.user
        if User.objects.filter(address=address).exists():
            user = User.objects.get(address=address)
    context = { "user": user}
    return render(request, 'main/dashboard.html', context)


@login_required(login_url='/')
def admins(request):
    if request.user.is_authenticated:
        address = request.user
        if User.objects.filter(address=address).exists():
            user = User.objects.get(address=address)
            if user.is_superuser:
                num_user = user.get_num_users()
            else:
                redirect(to='/')
    context = { "num_user": num_user}
    return render(request, 'main/admins.html', context)


@login_required(login_url='/')
def game(request):
    context = {}
    return render(request, 'main/Goblin_hunter/index.html', context)


@csrf_exempt
def give(request):
    if request.user.is_authenticated :
        data = json.loads(request.body.decode("utf-8"))
        # print(data)
        levelSelected = data['levelSelected']
        score = data['score']
        coin_total = data['coin_total']
        box_total = data['box_total']
        saveData(request.user, levelSelected, score, coin_total, box_total)
    context = {}
    return render(request, 'main/index.html', context)


def logout_view(request):
    logout(request)
    return redirect(to ="/")


def telegram(request):
    if request.method == "POST":
        print(request)
        if token:
            try:
                payload = json.loads(request.body.decode('utf-8'))
            except ValueError:
                return HttpResponseBadRequest('Invalid request body')
            
            chat_id = payload['message']['chat']['id']
            cmd = payload['message'].get('text')  # command
            commands = {
                '/start': _start,
                '/bountyoptions': _bountyoptions,
            }
            print(cmd, "man")
            func = commands.get(cmd.split()[0].lower())
            if func:
                bot.sendMessage(chat_id, func(), parse_mode='Markdown')
            else:
                bot.sendMessage(chat_id, 'I do not understand you, Sir!')
            return JsonResponse({}, status=200)
        else :
            return HttpResponseForbidden('Invalid token')

