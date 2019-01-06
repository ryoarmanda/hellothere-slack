# HelloThere

HelloThere is a simple slackbot to welcome new users, with customizable welcome message and channel to send it to.

# Requirements

Python 2.7 and above

# Preparation

1. Clone or download all the files in this repository
2. Create a new custom bot integration in your workspace and note down the bot's API Token
3. Insert the API token accordingly

> If you're using environment variables, you should save the token on `HELLOTHERE_TOKEN`. Otherwise, put the token on the line in `bot.py` that said `"Insert the bot's API token here"`

4. If you want to customize the template text and the channel, edit `bot.py` on respective places

> If you want to mention the newly joined user, write `<@userId>`. Later on the bot will change it to the actual user ID. The format for channel is `#channel-name`, e.g. `#general`.

5. Invite the bot to the channel from previous step

# Installation

    pip install slackclient
    python bot.py
