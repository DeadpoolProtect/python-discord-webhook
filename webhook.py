import requests
import json

def send_discord_message(webhook_url, message, username):
    data = {
        'content': message,
        'username': username
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print('Failed to send message. Status code: ' + str(response.status_code))


webhook_url = input('Entrez l\'URL du Webhook Discord : ')


message = input('Entrez le message à envoyer : ')


repeat = input('Voulez-vous répéter le message ? (oui/non) : ')

if repeat.lower() == 'oui':
    repeat_count = int(input('Combien de fois voulez-vous répéter le message ? : '))
    username = 'haxor'

    for _ in range(repeat_count):
        send_discord_message(webhook_url, message, username)
else:
    username = 'haxor'
    send_discord_message(webhook_url, message, username)
