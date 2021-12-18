import telepot
from .under import _start, _bountyoptions
import csv
import time
import string
from random import choices
# from main.models import Email, Tweet, Telegram, Facebook, Ethaddress, Link
from django.db import models
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



token = '1306743577:AAFN6ckiseuRbtjtFgJA2fumYC8OHv_EFHA'

# initialise the bot
bot = telepot.Bot(token)


class Email(models.Model):
    chat_id = models.IntegerField(default=0)
    email = models.EmailField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Tweet(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Telegram(models.Model):
    chat_id = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Facebook(models.Model):
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
    email = models.CharField(max_length=400, default="john@gmail.com")
    twitter = models.CharField(max_length=400, default="tweetuser")
    telegram = models.CharField(max_length=400, default="teleuser")
    facebook = models.CharField(max_length=400, default="facebookuser")
    ethaddress = models.CharField(max_length=400, default="ethuser")
    fname = models.CharField(max_length=400)
    gen_c = models.CharField(max_length=400, unique=True)
    referal = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.gen_c = self.generate_short_link()
        self.email = self.emails()
        self.twitter = self.twitters()
        self.telegram = self.telegrams()
        self.facebook = self.facebooks()
        self.ethaddress = self.eth()
        super(Link, self).save(*args, **kwargs)


    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        gen_c = "".join(choices(characters, k=8))

        link = self.objects.filter(gen_c=gen_c)

        if link:
            return self.generate_short_link()

        return gen_c

    def emails(self):
        update = last_update()
        chat_id = get_chat_id(update)
        result = Email.objects.filter(chat_id=chat_id)
        return result.email

    def twitters(self):
        update = last_update()
        chat_id = get_chat_id(update)
        result = Tweet.objects.filter(chat_id=chat_id)
        return result.username

    def telegrams(self):
        update = last_update()
        chat_id = get_chat_id(update)
        result = Telegram.objects.filter(chat_id=chat_id)
        return result.username

    def facebooks(self):
        update = last_update()
        chat_id = get_chat_id(update)
        result = Facebook.objects.filter(chat_id=chat_id)
        return result.username

    def eth(self):
        update = last_update()
        chat_id = get_chat_id(update)
        result = Ethaddress.objects.filter(chat_id=chat_id)
        return result.address



# func that get user id
def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id


# func that get message text
def get_text(update):
    text = update["message"]["text"]
    return text


# func that gets the last update
def last_update():
    response = bot.getUpdates()
    total_updates = len(response) - 1
    return response[total_updates]  # get the last recorded message


# func that sends msg to the usr
def send_msg(chat_id, msg_text):
    response = bot.sendMessage(chat_id, msg_text)
    return response


def _help():
    return """
/twitter \\- Input your twitter username
/clear \\- clear Referal List
/reflist \\- view my Referrals List
/mylink \\- get my affiliate link
/start \\- start
"""


def _feed():
    return "feedddd"


def _email():
    update = last_update()
    chat_id = get_chat_id(update)
    result = Email.objects.filter(chat_id=chat_id)
    if result: 
        email = result.email.replace(".", "\\.")
        tot = "Your email \\- {} \n /changeemail \\- to change email ".format(email)
        return tot
    else:
        msg = "Enter your email address"
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, msg)
        x = update["update_id"]
        response = bot.getUpdates(offset=(x + 1), timeout=3600)
        total_updates = len(response) - 1
        try:
            text = response[total_updates]["message"]["text"]
            Email.objects.create(chat_id=chat_id, email=text)
        except:
            return "An error occurred"
        return "Email is saved"


def _changeemail():
    update = last_update()
    msg = "Enter your email address"
    chat_id = update["message"]["chat"]["id"]
    bot.sendMessage(chat_id, msg)
    x = update["update_id"]
    response = bot.getUpdates(offset=(x + 1), timeout=3600)
    total_updates = len(response) - 1
    try:
        text = response[total_updates]["message"]["text"]
        result = Email.objects.filter(chat_id=chat_id)
        result.email  = text
        result.save()
        return "Email is saved"
    except:
        return "An error occurred"


def _twitter():
    update = last_update()
    chat_id = get_chat_id(update)
    result = Tweet.objects.filter(chat_id=chat_id)
    if result: 
        user = result.username.replace("_", "\\_")
        tot = "Your username \\- {} \n /changetwitter \\- to change twitter username".format(user)
        return tot
    else:
        msg = "Input your twitter username"
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, msg)
        x = update["update_id"]
        response = bot.getUpdates(offset=(x + 1), timeout=3600)
        total_updates = len(response) - 1
        try:
            text = response[total_updates]["message"]["text"]
            Tweet.objects.create(chat_id=chat_id, username=text)
        except:
            return "An error occurred"
        return "Twitter username is saved"


def _changetwitter():
    update = last_update()
    msg = "Input your twitter username"
    chat_id = update["message"]["chat"]["id"]
    bot.sendMessage(chat_id, msg)
    x = update["update_id"]
    response = bot.getUpdates(offset=(x + 1), timeout=3600)
    total_updates = len(response) - 1
    try:
        text = response[total_updates]["message"]["text"]
        result = Tweet.objects.filter(chat_id=chat_id)
        result.username =  text
        result.save()
        return "Twitter username is saved"
    except:
        return "An error occurred"


def _tele():
    update = last_update()
    chat_id = get_chat_id(update)
    result = Telegram.objects.filter(chat_id=chat_id)
    if result: 
        user = result.username.replace("_", "\\_")
        tot = "Your username \\- {} \n /changetele \\- to change telegram username".format(user)
        return tot
    else:
        msg = "Input your telegram username"
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, msg)
        x = update["update_id"]
        response = bot.getUpdates(offset=(x + 1), timeout=3600)
        total_updates = len(response) - 1
        try:
            text = response[total_updates]["message"]["text"]
            Telegram.objects.create(chat_id=chat_id, username=text)
        except:
            return "An error occurred"
        return "Telegram username is saved"


def _changetele():
    update = last_update()
    msg = "Input your telegram username"
    chat_id = update["message"]["chat"]["id"]
    bot.sendMessage(chat_id, msg)
    x = update["update_id"]
    response = bot.getUpdates(offset=(x + 1), timeout=3600)
    total_updates = len(response) - 1
    try:
        text = response[total_updates]["message"]["text"]
        result = Telegram.objects.filter(chat_id=chat_id)
        result.username = text
        result.save()
        return "Telegram username is saved"
    except:
        return "An error occurred"


def _facebook():
    update = last_update()
    chat_id = get_chat_id(update)
    result = Facebook.objects.filter(chat_id=chat_id)
    if result: 
        user = result.username.replace("_", "\\_")
        tot = "Your username \\- {} \n /changeface \\- to change facebook username".format(user)
        return tot
    else:
        msg = "Input your Facebook name"
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, msg)
        x = update["update_id"]
        response = bot.getUpdates(offset=(x + 1), timeout=3600)
        total_updates = len(response) - 1
        try:
            text = response[total_updates]["message"]["text"]
            Facebook.objects.create(chat_id=chat_id, username=text)
        except:
            return "An error occurred"
        return "Facebook name is saved"


def _changeface():
    update = last_update()
    msg = "Input your Facebook name"
    chat_id = update["message"]["chat"]["id"]
    bot.sendMessage(chat_id, msg)
    x = update["update_id"]
    response = bot.getUpdates(offset=(x + 1), timeout=3600)
    total_updates = len(response) - 1
    try:
        text = response[total_updates]["message"]["text"]
        result = Facebook.objects.filter(chat_id=chat_id)
        result.username = text
        result.save()
        return "Facebook name is saved"
    except:
        return "An error occurred"


def _ethaddress():
    update = last_update()
    chat_id = get_chat_id(update)
    result = Ethaddress.objects.filter(chat_id=chat_id)
    if result: 
        address = result.address
        tot = "Your username \\- {} \n /changeeth \\- to change ethaddress username".format(address)
        return tot
    else:
        msg = "Enter your erc 20 waallet address"
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, msg)
        x = update["update_id"]
        response = bot.getUpdates(offset=(x + 1), timeout=3600)
        total_updates = len(response) - 1
        try:
            text = response[total_updates]["message"]["text"]
            Ethaddress.objects.create(chat_id=chat_id, address=text)
        except:
            return "An error occurred"
        return "Your wallet address is saved"


def _changeeth():
    update = last_update()
    msg = "Enter your erc 20 waallet address"
    chat_id = update["message"]["chat"]["id"]
    bot.sendMessage(chat_id, msg)
    x = update["update_id"]
    response = bot.getUpdates(offset=(x + 1), timeout=3600)
    total_updates = len(response) - 1
    try:
        text = response[total_updates]["message"]["text"]
        result = Ethaddress.objects.filter(chat_id=chat_id)
        result.address = text
        result.save()
        return "Your wallet address is saved"
    except:
        return "An error occurred"


def _mylink():
    update = last_update() 
    chat_id = get_chat_id(update)
    fname = update["message"]["chat"]["first_name"]
    print(fname, chat_id)
    links = Link.objects.filter(chat_id=chat_id)
    if links:
        gen_c = links.gen_c
        msg = "https://telegram.me/cypherSpotBot?start={}".format(gen_c)
        send_msg(chat_id, msg)
    else:
        try:
            Link.objects.create(chat_id=chat_id, fname=fname)
        except:
            return "An error occurred"
        lin = Link.objects.filter(chat_id=chat_id)
        gen = lin.gen_c
        ms = "https://telegram.me/cypherSpotBot?start={}".format(gen)
        send_msg(chat_id, ms)
    return "That is your referral link"


def _reflist():
    update = last_update()
    chat_id = get_chat_id(update)
    link = Link.objects.filter(chat_id=chat_id)
    reflist = link.referal
    msg = "You have " + str(reflist) + " referals"
    return msg


def _top():
    # link = Link.query.order_by(Link.referal.desc()).all()
    link = Link.objects.order_by("-referal")
    for lin in link[:10]:
        return str(lin.fname) + " " + str(lin.referal)


def _clear():
    update = last_update()
    chat_id = get_chat_id(update)
    link = Link.objects.filter(chat_id=chat_id)
    link.referal = 0
    link.save()
    return "Your referal list has been cleared"


def _export():
    # link = db.engine.execute('SELECT * FROM link')
    link = Link.objects.all()
    with open("wub.csv", "w") as csv_file:
        fieldnames = ['id', 'chat_id', 'email', 'twitter', 'telegram',
        'facebook', 'ethaddress', 'fname', 'gen_c', 'referal', 'pub_date']
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
        for lin in link:
            writer.writerow(lin)
    return "file exported to wub\\.csv"


error_msg= """
/twitter \\- Input your twitter username
/clear \\- clear Referal List
/reflist \\- view my Referrals List
/mylink \\- get my affiliate link
/start \\- start
"""

# the main func 
def main():
    update_id = last_update()["update_id"]
    while True:
        update = last_update()
        if update_id == update["update_id"]:
            commands = {
                '/start': _start,
                '/help': _help,
                '/feed': _feed,
                '/bountyoptions': _bountyoptions,
                '/email': _email,
                '/twitter': _twitter,
                '/telegram': _tele,
                '/facebook': _facebook,
                '/ethaddress': _ethaddress,
                '/mylink': _mylink,
                '/reflist': _reflist,
                '/top': _top,
                '/clear': _clear,
                '/sheldoncooper': _export,
                '/changeemail': _changeemail,
                '/changetwitter': _changetwitter,
                '/changetele': _changetele,
                '/changeface': _changeface,
                '/changeeth': _changeeth
            }
            if token:
                chat_id = get_chat_id(update)
                cmd = get_text(update)  # command
                func = commands.get(cmd.split()[0].lower())
                link = Link.objects.all()
                for lin in link:
                    gen_c = lin.gen_c
                    if func and cmd.endswith(gen_c):
                        if cmd.startswith('/start'):
                            command, payload = cmd.split(" ")
                            # link = Link.query.filter_by(gen_c=payload).first()
                            link = Link.objects.filter(gen_c=payload)[0]
                            # chat = Link.query.filter_by(chat_id=chat_id).first()
                            chat = Link.objects.filter(chat_id=chat_id)[0]
                            if link and not chat:
                                link.referal += 1
                                link.save()
                                try:
                                    bot.sendMessage(chat_id, func(), parse_mode='MarkdownV2')
                                except:
                                    bot.sendMessage(chat_id, "Do not add special characters \n only use alphabets and numbers")
                                time.sleep(1)
                                # bot.sendMessage(chat_id, "You have been added to your referal")
                            elif link and chat:
                                bot.sendMessage(chat_id, "User already exist")
                # else:
                    elif func and not cmd.endswith(gen_c):
                        try:
                            bot.sendMessage(chat_id, func(), parse_mode='MarkdownV2')
                        except:
                            bot.sendMessage(chat_id, "Do not add special characters \n only use alphabets and numbers")
                    else:
                        bot.sendMessage(chat_id, error_msg)
                # Only to use at the begining
                # else:
                #     if func :
                #         try:
                #             bot.sendMessage(chat_id, func(), parse_mode='MarkdownV2')
                #         except:
                #             bot.sendMessage(chat_id, "Do not add special characters \n only use alphabets and numbers")
                #     else:
                #         bot.sendMessage(chat_id, error_msg)
            update_id += 1


main()