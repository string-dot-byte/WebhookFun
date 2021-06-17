# WebhookFun
Delete, Rename, Change avatar and Send message webhook without authorization

Requires `requests` installed.
Run `pip install requests` in cmd to download.

Run the python file and you will be prompted 5 options which are pretty obvious on how to respond to.

![image](https://user-images.githubusercontent.com/68619882/122406236-aeae7680-cf4e-11eb-98d3-62a563e1677a.png)


All of them obviously require webhook url.

---

## Delete webhook
Nothing needed other than the url.


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


---

Open for Pull requests on this project and issues encountered.

---

Just for eductional purposes and fun. Do not use this tool if you do not have the mutual consent to the target's webhook owner.
Not responsible for any abuse using my tool.

<3
