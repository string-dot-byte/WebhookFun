import os
import json

try:
    import requests
except (ModuleNotFoundError):
    os.system('pip install requests')

print('''
    Options:
        1. Delete webhook
        2. Edit webhook
        3. Send webhook message
        4. Edit webhook message
        5. Delete webhook message
        6. Get webhook message
''')

option = int(input('Select option > '))

if option not in [1, 2, 3, 4, 5, 6]:
    print('Lol that\'s not a valid option.')
    exit()

webhookUrl = input('Insert webhook url > ')
if option == 1:
    requests.delete(webhookUrl)
    print('\nDeleted webhook  :)')
elif option == 2:
    name = input('\nInsert webhook name > ')
    avatar = input('Insert avatar url > ')

    json = {'name': name, 'avatar': avatar}
    r = requests.patch(webhookUrl, json = json)
    print(r)
elif option == 3:
    while True:
        content = input('\nInsert content > ')
        tts = input('TTS? (true/false) > ')

        if tts.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup']:
            tts = True
        else:
            tts = False

        data = {'content': content, 'tts': tts}
        requests.post(webhookUrl, json = data)

        repeat = input('Send another message? (yes/no) > ')
        if not repeat.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup']:
            break
elif option == 4:
    while True:
        messageId = input('Insert message ID > ')
        newContent = input('Insert new content > ')
        json = {'content': newContent}
        requests.patch(webhookUrl + '/messages/' + messageId, json = json)

        repeat = input('Edit another message? (yes/no) >')
        if not repeat.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup']:
            break
elif option == 5:
    while True:
        messageId = input('Insert message ID > ')
        requests.delete(webhookUrl + '/messages/' + messageId)

        repeat = input('Delete another message? (yes/no) > ')
        if not repeat.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup']:
            break
elif option == 6:
     while True:
        messageId = input('Insert message ID > ')
        print(requests.get(webhookUrl + '/messages/' + messageId).json()['content'])

        repeat = input('View another message? (yes/no) > ')
        if not repeat.lower() in ['true', 't', 'y', 'yes', 'yeah', 'yup']:
            break
