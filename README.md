## Latex Equations to PNG image : Telegram bot 

This bot works inline in personal as well as group chats to convert LaTeX equations to PNG image using https://math.now.sh API.

You can access the bot using https://t.me/latexpngbot

The bot is hosted in IBM Cloud. Hence the `manifest.yml` and `Procfile`  were added to this repo.

### How to use the bot

 

### How to fork and use the bot for yourself

1. Fork the repo. Add `config.ini` with following content.

```
[BOTINFO]
usid = < add your user ID here >
token = < add bot token obtained from botfather in Telegram >
```

2. Install the dependencies from requirements.txt
	`pip3 install -r requirements.txt`

3. Run the bot using `python3 bot.py` 

4. Start the bot from your account.



### References

1. https://lovemewithoutall.github.io/it/deploy-python-bot-on-IBM-bluemix/
2. https://cloud.ibm.com/docs/apps?topic=apps-create-deploy-app-cli
3. https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinebot.py
4. https://stackoverflow.com/questions/60915575/send-a-local-photo-from-inline-mode-in-a-telegram-bot
