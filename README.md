# The-Google-Meet-Bot

This is telegram bot made to attend all your lectures and attend meets. It joins lectures based on number of students in the meet and not on time. Sends screenshots after logging in and joining meet.
There is no need to start your laptop for any functions. Everything happens remotely.

## Telegram Bot Commands

- /start -- Startup
- /meet https://meet.google.com/jeo-upir-iop -- Provide the link for your meet
- /login abc@gmail.com password -- Provide your google user name and password so the bot can log you in
- /ping -- get the screenshot of what the is doing
- /help -- helper template

## What you have to do

- Clone `(git clone https://github.com/ameyachavan007/The-Google-Meet-Bot.git)` the code from the repository add a `.env` file and provide enviornment variables like chatId as userId, bot token as BOT_TOKEN and USER_AGENT.
- Install requirements.txt `pip install -r requirements.txt`

__* It is recommended that you deploy bot on your PC, instead of deploying it on Heroku. Deploying to Heroku will take some time. The bot freezes after 24hrs of inactivity. We have included Procfile already for your convenience. *__

# Disclaimer

We do not recommend using this project for skipping online classes. This project was made in order to see how automation works and how it can even be implemented in everyday life.

Classes are important and respect your teachers :slightly_smiling_face:.
