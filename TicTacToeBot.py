import telebot
from random import randint

with open('BotFile.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n')
final = None
used = []

bot = telebot.TeleBot('6735978760:AAEDgNkzBJY0rXrLrN8cz12BM9tCNMbK3gk')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот, для которого еще не придумали конкретного применения, рад поработать на вас, "
                          "но не забывайте - 'время - деньги'")
    used.clear()


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "здесь могла быть ваша реклама")


@bot.message_handler(commands=['clear'])
def clean(message):
    used.clear()
    bot.reply_to(message, 'игра начинается заново')


def examination(message, st):
    if st in data:
        if st not in used:
            if st[0] == final or final is None:
                return True
            else:
                bot.reply_to(message, '<<город должен начинаться на "' + str(final) + '">>')
                return False
        else:
            bot.reply_to(message, '<<город уже был назван>>')
            print(used)
            return False
    else:
        bot.reply_to(message, '<<не является известным городом>>')
        return False


def last_and_initial(st):
    t = []
    for i in range(len(st) - 1, -1, -1):
        if len(t) == 0:
            for elem in data:
                if elem[0] == st[i]:
                    t.append(elem)
        else:
            return st[i + 1]


@bot.message_handler(content_types=['text'])
def texting(message):
    st = message.text.lower()
    if examination(message, st):
        used.append(st)
        final = last_and_initial(st)
        t = []
        for elem in data:
            if elem[0] == final:
                t.append(elem)
        # print(t)
        city = t[randint(0, len(t) - 1)]
        final = last_and_initial(city)
        used.append(city)
        bot.send_message(message.from_user.id, city)

    # bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True)
