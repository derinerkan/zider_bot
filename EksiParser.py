from lxml import html, etree
import requests
import TelegramBot
import re
from html.parser import HTMLParser
import random


class MyHTMLParser(HTMLParser):
    text = ''

    def handle_starttag(self, tag, attrs):
        # print(tag + ' ' + str(attrs))
        if tag == 'a':
            self.text = attrs[0][1]

    def get_last(self):
        return self.text


def puanla(string):
    keywords = ('rakı', 'kadın', 'kız', 'erkek', 'erkeğ', 'efendi', 'piç', 'yanlız', 'yalnız', 'seviş', 'ayak', 'hatun',
                'güzel', 'tipsiz', 'hatun', 'brad pitt', 'haram', 'popo', 'kezban', 'tayt', 'çirkin', 'sivas', 'seks',
                "30 yaş üstü", )
    score = 0
    for key in keywords:
        exp = '.' + key + '.'
        matches = re.findall(exp, string)
        if matches is not None:
            score = score + len(matches)
    return score


def tuple_puanla(item):
    return item[2]


def main(id):
    url = 'https://eksisozluk.com/basliklar/gundem'
    page = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    parser = MyHTMLParser()

    gundem = tree.xpath('//*[@id="content-body"]/ul')
    print(str(gundem))
    basliklar = list()
    for i in gundem[0]:
        # print(str(i[0].text))
        parser.feed(str(etree.tostring(i)))
        # print(parser.get_last())
        # print(puanla(str(i[0].text)))
        basliklar.append((str(i[0].text), parser.get_last(), puanla(str(i[0].text)) + random.random()))
    print('\n'.join({str(i) for i in sorted(basliklar, key=tuple_puanla)}))
    print("----------------------------")
    print(str(max(basliklar, key=lambda p: p[2])))

    bot = TelegramBot.Bot()
    print('https://eksisozluk.com' + max(basliklar, key=lambda p: p[2])[1])
    print(bot.send_message(id, 'https://eksisozluk.com' + max(basliklar, key=lambda p: p[2])[1]))
    # text = '\n'.join({i[0].text for i in gundem[0]})
    # print(text)
    # bot.send_message(-1001309568370, text)
