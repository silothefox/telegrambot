import requests
from time import sleep

global OFFSET
OFFSET = 0

botToken = "1684884714:AAH2HqAyXE5iYVabQkDs2CwJJXTHco5QHYM"
chatID = "-473189809"

global requestURL
global sendURL

requestURL = "http://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "http://api.telegram.org/bot" + botToken + "/sendMessage"
print(requestURL)


def send_message(chatId, message):
    requests.post(sendURL + "?chat_id=" + str(chatId) + "&text=" + message)


send_message(chatID,"Cyrix gay")

# Create a Simple loop
while True:
    send_message(chatID,"Simple 5s loop")
    sleep(5)

# Leaving tihs for future reference
#while True:
#    newmessage = update(requestURL)
#
#    if newmessage != False:
#        chattype = newmessage['message']['chat']['type']
#        if chattype == "group":
#            if 'new_chat_participant' in newmessage['message']:
#                membername = newmessage['message']['new_chat_participant']['first_name']
#                chatid = newmessage['message']['chat']['id']
#                send_message(chatid, "Herzlich willkommen, " + membername + " !")
#
#    sleep(1)
