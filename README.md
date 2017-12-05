# HelloThere

HelloThere is a simple slackbot to welcome new users. Written in basic Python, this bot would send a welcome message to a channel that can both be customized.

# Requirements

Python 2.7+

# Preparation

1. Create a new custom bot integration in your workspace, noting the bot's API Token
2. Insert the API token accordingly

If you're using environment variables, you should save the token on `HELLOTHERE_TOKEN`. Otherwise, put the token on the line in `bot.py` that said `"Insert the bot's API token here"`

3. If you want to customize the template text and the channel, edit `bot.py` on respective places

If you want to mention the newly joined user, just write `<@userId>`. Later on the bot will change it to the actual user ID. The format for channel is `#channel-name`, e.g. `#general`.

4. Invite the bot to the channel that was written on the previous step
5. Run the script! (see Installation below)

# Installation

    pip install slackclient
    python bot.py
