import TelegramBot
import time
import random
import EksiParser


def main():
    bot = TelegramBot.Bot()
    print('Dikkat: Hızlanıyor')
    while True:
        updates = bot.get_fresh_updates(timeout=30)
        print('Kontrol edildi')
        for i in updates['result']:
            print('Gelen update: ' + str(i))
            if 'message' in i.keys():
                id = i['message']['chat']['id']
                text = reply()
                if 'text' in i['message'].keys() and i['message']['text'] == '/info':
                    bot.send_message(id, "https://eksisozluk.com/ziya-ider--427567")
                    bot.send_message(id, "Henüz özelliklerin çoğu implement edilmedi, komut yazmayın. Özel mesajları siklerim grupları siklemem.")
                    bot.send_message(id, "Yoklamaya imza atmayın sikerim")
                    print(str(id) + 'chatine bilgi mesajı gönderildi')
                elif 'text' in i['message'].keys() and i['message']['text'] == '/eksi':
                    EksiParser.main(id)
                elif ('text' in i['message'].keys() and i['message']['text'] == '/random') or id > 0:
                    bot.send_message(id, text)
                    print('Mesaj gönderildi:' + text + ' Alan kanal: ' + str(id))
                if 'from' in i['message'].keys():
                    if 'username' in i['message']['from'].keys():
                        print("İsim: " + str(i['message']['from']['username']))
                    else:
                        print('İsim:' + str(i['message']['from']))


# randomly produce a zider reply
def reply():
    if random.random() > 0.5:  # Sen söyle
        komponent = list(
            {"JFETin base akımı", "R2 nin direnci", "BJTnin betası", "Diyodun voltajı", "Kolektördeki voltaj",
             "1 kilohertzteki reaktans", "Burdaki gain"})
        return komponent[random.randrange(len(komponent))] + " nedir o zaman sen söyle bakiyim sen değil arkandaki"
    else:  # Funny circuit
        komponent = list({"the diode is off ", "the BJT is forward active ", "the diode current is 10 milliamps ",
                          "the JFET is forward biased ", "the MOSFET is not sat ", "the resistor current goes up "})
        sonuc = list({"there is no more current", "the BJT becomes sat", "the JFET is off", "the output is 5 volt",
                      "the beta is 200", "the current is higher", "the diode turns off"})
        return "This is a funny circuit actually, when " + komponent[random.randrange(len(komponent))] + \
               sonuc[random.randrange(len(sonuc))]


main()
