import requests
from time import sleep

global OFFSET
OFFSET = 0

botToken = "1684884714:AAH2HqAyXE5iYVabQkDs2CwJJXTHco5QHYM"

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



# this the old definition from the while loop
#chatid = newmessage['message']['chat']['id']
#
chatID = "-473189809"

# Trying to Send Simple Message "Hello World" with function "send_message"
send_message(chatID,"Cyrix gay")


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
