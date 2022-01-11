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
import csv
from django.db import models
import telepot
import time
import string
from random import choices

User = get_user_model()

token = settings.TOKEN
secret = settings.SECRET
# webhook_url = f"https://goblin.cypherspot.dev/telegram/{secret}/"
# webhook_url = f"https://32d3-160-152-42-163.ngrok.io/telegram/"
# bot = telepot.Bot(token)
# if webhook_url != bot.getWebhookInfo()['url']:
#     bot.setWebhook(webhook_url)



# Create your views here.
def index(request):
   
    context = {}
    return render(request, 'main/index.html', context)



# def index(request):
#     csrf_token = get_token(request)
#     user = ""
#     if request.user.is_authenticated:
#         address = request.user
#         if User.objects.filter(address=address).exists():
#             user = User.objects.get(address=address)
#     context = {"csrftoken": csrf_token, "user": user}
#     return render(request, 'main/index.html', context)


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


@csrf_exempt
def telegram(request):
    if request.method == "POST":
        if token:
            try:
                payload = json.loads(request.body.decode('utf-8'))
            except ValueError:
                return HttpResponseBadRequest('Invalid request body')
            
            chat_id = payload['message']['chat']['id']
            fname = payload["message"]["chat"]["first_name"]
            cmd = payload['message'].get('text')  # command
            commands = {
                '/start': _start,
                '/help': _help,
                '/bountyoptions': _bountyoptions,
                '/twitter': _twitter(chat_id),
                '/twitterlink': _tw_link(chat_id),
                '/mytwitter': _mytwitter(chat_id),
                '/changetwitter': _twitter(chat_id),
                '/telegram': _tele(chat_id),
                '/mytelegram': _mytele(chat_id),
                '/changetele': _tele(chat_id),
                '/facebook': _facebook(chat_id),
                '/myfacebook': _myfacebook(chat_id),
                '/changeface': _facebook(chat_id),
                '/instagram': _instagram(chat_id),
                '/myinstagram': _myinstagram(chat_id),
                '/changeinsta': _instagram(chat_id),
                '/youtube': _youtube(chat_id),
                '/myyoutube': _myyoutube(chat_id),
                '/changetube': _youtube(chat_id),
                '/reddit': _reddit(chat_id),
                '/myreddit': _myreddit(chat_id),
                '/changereddit': _reddit(chat_id),
                '/ethaddress': _ethaddress(chat_id),
                '/myethaddress': _myethaddress(chat_id),
                '/changeeth': _ethaddress(chat_id),
                '/mylink': _mylink(chat_id, fname),
                '/reflist': _reflist(chat_id),
                '/top': _top(chat_id),
                '/clear': _clear(chat_id),
                # '/sheldoncooper': _exports(chat_id),
            }
            if payload['message'].get('entities'):
                if Command.objects.filter(chat_id=chat_id).exists():
                    comma = Command.objects.get(chat_id=chat_id)
                    comma.command = cmd.split()[0].lower()
                    comma.save()
                else:
                    Command.objects.create(chat_id=chat_id, command=cmd.split()[0].lower())
            func = commands.get(cmd.split()[0].lower()) 
            link = Link.objects.all()
            for lin in link:
                gen_c = lin.gen_c
                if func and cmd.endswith(gen_c):
                    if cmd.startswith('/start'):
                        command, pay = cmd.split(" ")
                        print(pay, "the pay")
                        print(chat_id, "chatting")
                        link = Link.objects.get(gen_c=pay)
                        chat = Link.objects.filter(chat_id=chat_id)
                        if link and not chat:
                            link.referal += 1
                            link.save()
                            try:
                                bot.sendMessage(chat_id, func, parse_mode='Markdown')
                            except:
                                bot.sendMessage(chat_id, func(), parse_mode='Markdown')
                            time.sleep(1)
                            # bot.sendMessage(chat_id, "You have been added to your referal")
                        elif link and chat:
                            bot.sendMessage(chat_id, "User already exist")
                        return JsonResponse({}, status=200)
                    return JsonResponse({}, status=200)
                elif func and not cmd.endswith(gen_c):
                    try:
                        bot.sendMessage(chat_id, func, parse_mode='Markdown')
                    except:
                        bot.sendMessage(chat_id, func(), parse_mode='Markdown')
                else:
                    if Command.objects.filter(chat_id=chat_id).exists():
                        comma = Command.objects.get(chat_id=chat_id)
                        if comma.command == "/twitter":
                            bot.sendMessage(chat_id, _twitter_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetwitter":
                            bot.sendMessage(chat_id, _changetwitter_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/twitterlink":
                            bot.sendMessage(chat_id, _changetwitterlink_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/telegram":
                            bot.sendMessage(chat_id, _tele_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetele":
                            bot.sendMessage(chat_id, _changetele_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/facebook":
                            bot.sendMessage(chat_id, _facebook_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeface":
                            bot.sendMessage(chat_id, _changeface_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/instagram":
                            bot.sendMessage(chat_id, _instagram_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeinsta":
                            bot.sendMessage(chat_id, _changeinsta_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/youtube":
                            bot.sendMessage(chat_id, _youtube_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetube":
                            bot.sendMessage(chat_id, _changetube_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/reddit":
                            bot.sendMessage(chat_id, _reddit_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changereddit":
                            bot.sendMessage(chat_id, _changereddit_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/ethaddress":
                            bot.sendMessage(chat_id, _ethaddress_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeeth":
                            bot.sendMessage(chat_id, _changeeth_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        else:
                            bot.sendMessage(chat_id, error_msg)
                return JsonResponse({}, status=200)
            # Only to use at the begining
            else:
                if func :
                    try:
                        bot.sendMessage(chat_id, func, parse_mode='Markdown')
                        # bot.sendMessage(chat_id, "halo3", parse_mode='Markdown')
                    except:
                        bot.sendMessage(chat_id, func(), parse_mode='Markdown')
                else:
                    if Command.objects.filter(chat_id=chat_id).exists():
                        comma = Command.objects.get(chat_id=chat_id)
                        if comma.command == "/twitter":
                            bot.sendMessage(chat_id, _twitter_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetwitter":
                            bot.sendMessage(chat_id, _changetwitter_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/twitterlink":
                            bot.sendMessage(chat_id, _changetwitterlink_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/telegram":
                            bot.sendMessage(chat_id, _tele_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetele":
                            bot.sendMessage(chat_id, _changetele_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/facebook":
                            bot.sendMessage(chat_id, _facebook_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeface":
                            bot.sendMessage(chat_id, _changeface_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/instagram":
                            bot.sendMessage(chat_id, _instagram_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeinsta":
                            bot.sendMessage(chat_id, _changeinsta_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/youtube":
                            bot.sendMessage(chat_id, _youtube_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changetube":
                            bot.sendMessage(chat_id, _changetube_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/reddit":
                            bot.sendMessage(chat_id, _reddit_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changereddit":
                            bot.sendMessage(chat_id, _changereddit_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/ethaddress":
                            bot.sendMessage(chat_id, _ethaddress_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        elif comma.command == "/changeeth":
                            bot.sendMessage(chat_id, _changeeth_cn(chat_id, cmd.split()[0].lower()), parse_mode='Markdown')
                        else:
                            bot.sendMessage(chat_id, error_msg)
            return JsonResponse({}, status=200)
        else :
            return HttpResponseForbidden('Invalid token')


class Command(models.Model):
    chat_id = models.IntegerField(default=0)
    command = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.chat_id}'

class Email(models.Model):
    chat_id = models.IntegerField(default=0)
    email = models.EmailField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Telegram(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Tweet(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    tw_link = models.CharField(max_length=400, default="mytweetlink")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Facebook(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Instagram(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Youtube(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Reddit(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Ethaddress(models.Model):
    chat_id = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Link(models.Model):
    chat_id = models.CharField(max_length=400, unique=True)
    twitter = models.CharField(max_length=400, default="tweetuser")
    telegram = models.CharField(max_length=400, default="teleuser")
    facebook = models.CharField(max_length=400, default="facebookuser")
    instagram = models.CharField(max_length=400, default="instagramuser")
    youtube = models.CharField(max_length=400, default="youtubeuser")
    reddit = models.CharField(max_length=400, default="reddituser")
    ethaddress = models.CharField(max_length=400, default="ethuser")
    fname = models.CharField(max_length=400)
    gen_c = models.CharField(max_length=400, unique=True)
    referal = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)
        if self.gen_c:
            pass
        else:
            self.gen_c = self.generate_short_link()    
        
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        gen_c = "".join(choices(characters, k=8))

        if Link.objects.filter(gen_c=gen_c).exists():
            return self.generate_short_link()

        return gen_c

    def save(self, *args, **kwargs):
        self.telegram = Telegram.objects.get(chat_id=self.chat_id).username
        self.twitter = Tweet.objects.get(chat_id=self.chat_id).username
        self.facebook = Facebook.objects.get(chat_id=self.chat_id).username
        self.instagram = Instagram.objects.get(chat_id=self.chat_id).username
        self.youtube = Youtube.objects.get(chat_id=self.chat_id).username
        self.reddit = Reddit.objects.get(chat_id=self.chat_id).username
        self.ethaddress = Ethaddress.objects.get(chat_id=self.chat_id).address
        super(Link, self).save(*args, **kwargs)
        
# 1070834749 Duke_of_python


def _help():
    return """
/twitter \\- Input your twitter username
/clear \\- clear Referal List
/reflist \\- view my Referrals List
/mylink \\- get my affiliate link
/start \\- start
"""

# func that sends msg to the usr
def send_msg(chat_id, msg_text):
    response = bot.sendMessage(chat_id, msg_text)
    return response

# Telegram
def _mytele(chat_id):
    chat_id = chat_id
    if Telegram.objects.filter(chat_id=chat_id).exists(): 
        result = Telegram.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username \\- {} \n /changetele \\- to change telegram username".format(user)
        return tot
    else:
        msg = "You do not have a telegram handle \n Click here /telegram"
        return msg

def _tele(chat_id):
    msg = "Input your telegram username"
    return msg

def _tele_cn(chat_id, text):
    try:
        Telegram.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changetele_cn(chat_id, text):
    try:
        result = Telegram.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"

#twitter
def _mytwitter(chat_id):
    chat_id = chat_id
    if Tweet.objects.filter(chat_id=chat_id).exists(): 
        result = Tweet.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username - {} \n /changetwitter - to change twitter username".format(user)
        return tot
    else:
        msg = "You do not have a twitter handle \n Click here /twitter"
        return msg

def _twitter(chat_id):
    msg = "Input your twitter username"
    return msg

def _tw_link(chat_id):
    msg = "Input your retwitter link"
    return msg

def _twitter_cn(chat_id, text):
    try:
        Tweet.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changetwitter_cn(chat_id, text):
    try:
        result = Tweet.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"

def _changetwitterlink_cn(chat_id, text):
    try:
        result = Tweet.objects.get(chat_id=chat_id)
        result.tw_link =  text
        result.save()
    except:
        return "An error occurred"
    return "Your retweet link is saved"

# Facebook
def _myfacebook(chat_id):
    chat_id = chat_id
    if Facebook.objects.filter(chat_id=chat_id).exists(): 
        result = Facebook.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username \\- {} \n /changeface \\- to change facebook username".format(user)
        return tot
    else:
        msg = "You do not have a facebook handle \n Click here /facebook"
        return msg

def _facebook(chat_id):
    msg = "Input your Facebook username"
    return msg

def _facebook_cn(chat_id, text):
    try:
        Facebook.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changeface_cn(chat_id, text):
    try:
        result = Facebook.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"

# Instagram
def _myinstagram(chat_id):
    chat_id = chat_id
    if Instagram.objects.filter(chat_id=chat_id).exists(): 
        result = Instagram.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username \\- {} \n /changeinsta \\- to change Instagram username".format(user)
        return tot
    else:
        msg = "You do not have a instagram handle \n Click here /instagram"
        return msg

def _instagram(chat_id):
    msg = "Input your Instagram username"
    return msg

def _instagram_cn(chat_id, text):
    try:
        Instagram.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changeinsta_cn(chat_id, text):
    try:
        result = Instagram.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"

# Youtube
def _myyoutube(chat_id):
    chat_id = chat_id
    if Youtube.objects.filter(chat_id=chat_id).exists(): 
        result = Youtube.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username \\- {} \n /changetube \\- to change Youtube username".format(user)
        return tot
    else:
        msg = "You do not have a youtube handle \n Click here /youtube"
        return msg

def _youtube(chat_id):
    msg = "Input your Youtube username"
    return msg

def _youtube_cn(chat_id, text):
    try:
        Youtube.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changetube_cn(chat_id, text):
    try:
        result = Youtube.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"

# Reddit
def _myreddit(chat_id):
    chat_id = chat_id
    if Reddit.objects.filter(chat_id=chat_id).exists(): 
        result = Reddit.objects.get(chat_id=chat_id)
        user = result.username
        tot = "Your username \\- {} \n /changereddit \\- to change Reddit username".format(user)
        return tot
    else:
        msg = "You do not have a reddit handle \n Click here /reddit"
        return msg

def _reddit(chat_id):
    msg = "Input your Reddit username"
    return msg

def _reddit_cn(chat_id, text):
    try:
        Reddit.objects.create(chat_id=chat_id, username=text)
    except:
        return "An error occurred"
    return "Username is saved"

def _changereddit_cn(chat_id, text):
    try:
        result = Reddit.objects.get(chat_id=chat_id)
        result.username =  text
        result.save()
    except:
        return "An error occurred"
    return "Username is saved"


# Bsc address
def _myethaddress(chat_id):
    chat_id = chat_id
    if Ethaddress.objects.filter(chat_id=chat_id).exists(): 
        result = Ethaddress.objects.filter(chat_id=chat_id)[0]
        # result = Ethaddress.objects.get(chat_id=chat_id)
        address = result.address
        tot = "Your username \\- {} \n /changeeth \\- to change bsc address".format(address)
        return tot
    else:
        msg = "You do not have a bsc address \n Click here /ethaddress"
        return msg

def _ethaddress(chat_id):
    msg = "Enter your wallet address"
    return msg

def _ethaddress_cn(chat_id, text):
    try:
        Ethaddress.objects.create(chat_id=chat_id, address=text)
    except:
        return "An error occurred"
    return "Address is saved"

def _changeeth_cn(chat_id, text):
    try:
        result = Facebook.objects.get(chat_id=chat_id)
        result.address = text
        result.save()
    except:
        return "An error occurred"
    return "Address is saved"


# the referral link
def _mylink(chat_id, fname):
    chat_id = chat_id
    fname = fname
    if Link.objects.filter(chat_id=chat_id).exists():
        links = Link.objects.get(chat_id=chat_id)
        # print("it is here")
        gen_c = links.gen_c
        msg = "https://telegram.me/cypherSpotBot?start={}".format(gen_c)
        # send_msg(chat_id, msg)
        return msg
    else:
        try:
            # print("starting")
            l = Link.objects.create(chat_id=chat_id, fname=fname)
            # print(l, "sad")
            # print("ending")
        except:
            return "Complete your task and fill in your details to get your link"
        lin = Link.objects.get(chat_id=chat_id)
        gen = lin.gen_c
        msg = "https://telegram.me/cypherSpotBot?start={}".format(gen)
        # send_msg(chat_id, msg)
        return msg
    return "That is your referral link"


def _reflist(chat_id):
    chat_id = chat_id
    if Link.objects.filter(chat_id=chat_id).exists():
        link = Link.objects.get(chat_id=chat_id)
        reflist = link.referal
        msg = "You have " + str(reflist) + " referrals"
        return msg
    return "You haven't gotten your referral link yet"

def _top(chat_id):
    # link = Link.query.order_by(Link.referal.desc()).all()
    link = Link.objects.order_by("-referal")
    for lin in link[:10]:
        return str(lin.fname) + " " + str(lin.referal)

    return "You haven't gotten your referral link yet"


def _clear(chat_id):
    chat_id = chat_id
    if Link.objects.filter(chat_id=chat_id).exists():
        link = Link.objects.get(chat_id=chat_id)
        link.referal = 0
        link.save()
        msg = "Your referal list has been cleared"
        return msg
    return "You haven't gotten your referral link yet"


# def _exports(chat_id):
#     # link = db.engine.execute('SELECT * FROM link')
#     link = Link.objects.all()
#     with open("wub.csv", "w") as csv_file:
#         fieldnames = ['id', 'chat_id', 'email', 'twitter', 'telegram',
#         'facebook', 'ethaddress', 'fname', 'gen_c', 'referal', 'pub_date']
#         writer = csv.writer(csv_file)
#         writer.writerow(fieldnames)
#         for lin in link:
#             writer.writerow(lin)
#     msg =  "file exported to wub\\.csv"
#     return msg


error_msg= """
/twitter \\- Input your twitter username
/clear \\- clear Referral List
/reflist \\- view my Referrals List
/mylink \\- get my affiliate link
/start \\- start
"""