import requests
from time import sleep

global OFFSET
OFFSET = 0

botToken = ""

global requestURL
global sendURL

requestURL = "http://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "http://api.telegram.org/bot" + botToken + "/sendMessage"
print(requestURL)


def update(url):
    global OFFSET

    try:
        update_raw = requests.get(url + "?offset=" + str(OFFSET))
        update = update_raw.json()
        result = extract_result(update)


        if result != False:
            OFFSET = result['update_id'] + 1
            return result
        else:
            return False

    except requests.exceptions.ConnectionError:
        pass


def extract_result(dict):
    result_array = dict['result']

    if result_array == []:
        return False
    else:
        result_dic = result_array[0]
        return result_dic


def send_message(chatId, message):
    requests.post(sendURL + "?chat_id=" + str(chatId) + "&text=" + message)





while True:
    newmessage = update(requestURL)

    if newmessage != False:
        chattype = newmessage['message']['chat']['type']
        if chattype == "group":
            if 'new_chat_participant' in newmessage['message']:
                membername = newmessage['message']['new_chat_participant']['first_name']
                chatid = newmessage['message']['chat']['id']
                send_message(chatid, "Hallöchen, " + membername + " und Willkommen im Rheinland Stammtisch ^-^ Hier in der Gruppe, gibt es wichtige Infos zu unseren Veranstaltungen, Anmeldung zur Teilnahme, Mitfahrgelegenheiten- oder Übernachtungsmöglichkeitensuche und Ähnliches. Für Smalltalk, bitten wir dich unserer flauschigen Labergruppe beizutreten 👉🏻 https://t.me/joinchat/SgLKPOJf3PGUzc9X Für ganz gesprächige und Gamer-Fällbälle, gibt es unseren Discord-Server 👉🏻 https://discord.gg/DGtKpBw Falls du nur Infos willst, findest du hier unseren Info Kanal 👉🏻 https://t.me/Rheinland_Stammtisch_Infokanal. Du siehst, es steht also ganz viel Platz bereit um dich vorzustellen und die Mitglieder kennen zu lernen ^^ Bitte beachte, dass alle aufgelisteten Chats SFW-Chats sind. Desweiteren gelten für alle Chats grundlegende Benimmregeln, die Vermeidung von Rassismus, Mobbing, Beleidigungen aber auch Spam ist nicht erwünscht.  Wenn du eine Anweisung von einem Admin erhälst, bitte halte dich an diese! Grundsätzlich beißen die Admins nicht, wir knabbern im Notfall aber gerne. 😘 Wir wünschen dir viel Spaß!")

    sleep(1)
