# WebhookFun
Delete, Rename, Change avatar and Send message webhook without authorization

Requires `requests` installed along with `os` and `json` which should already be a default package installed.
Run `pip install requests` in cmd to download.

Run the python file and you will be prompted 6 options which are pretty obvious on how to respond to.

![image](https://user-images.githubusercontent.com/68619882/124368184-961bad00-dc2c-11eb-8dc6-418e0be4ba11.png)


All of them obviously require webhook url.

---

## Delete webhook
Input the webhook's url and then it automatically deletes.


## Edit webhook

`Edit webhook` requires the new name (limited to 80 characters) and avatar url. Can't change the webhook's channel as that requires authorization to it. 
The image url must be like so:

![image](https://user-images.githubusercontent.com/68619882/122314412-2300ff80-cee6-11eb-8f6d-a12ed15e8b83.png)


## Send message

This requires obviously the message to be sent and also asks if you would like the message to be TTS (text to speech).


## Edit webhook message

Input the message ID to edit it's message on.


## Delete webhook message

Input the message ID to delete it.


## Get webhook message

To read a message sent by the webhook. Requires the message's ID.

---

Just for eductional purposes and fun. Do not use this tool if you do not have the mutual consent to the target's webhook owner.
Not responsible for any abuse using my tool.

**DO NOT ABUSE DISCORD RATE LIMITS!!! RESPECT A MAXIMUM OF 30 REQUESTS PER MINUTE!!!**

<3
