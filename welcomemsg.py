import requests
from time import sleep

global OFFSET
OFFSET = 0

botToken = ""
welcometext = "welcometext.txt"

global requestURL
global sendURL

requestURL = "http://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "http://api.telegram.org/bot" + botToken + "/sendMessage"
print(requestURL)

def read_from_file(file):
    from pathlib import Path
    txt = Path(file).read_text()
    return txt

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

def readfromfile(welcometext):
    from pathlib import Path
    text = Path(welcometext).read_text('utf-8')
    return text


while True:
    newmessage = update(requestURL)

    if newmessage != False:
        chattype = newmessage['message']['chat']['type']
        if chattype == "group":
            if 'new_chat_participant' in newmessage['message']:
                membername = newmessage['message']['new_chat_participant']['first_name']
                chatid = newmessage['message']['chat']['id']
                send_message(chatid, readfromfile(welcometext)) 
    sleep(1)
