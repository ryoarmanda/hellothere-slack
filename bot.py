import os
import time
from slackclient import SlackClient

try:
	# If you're running with environment variables
	bot_token = os.environ['HELLOTHERE_TOKEN']
except:
	# If you're running without environment variables
	bot_token = "Insert the bot's API token here"

# Template for the welcome text
text = "Hello and welcome to the group, <@userId>!"

# The channel that the bot would send the message to
channel = "#general"

def handle(output_list):
	for output in output_list:
		if (output) and ("type" in output) and ("team_join" in output["type"]):
			greet(output["user"]["id"])

def greet(userId):
	user_mention = "<@" + userId + ">"
	bot.rtm_send_message(channel, text.replace("<@userId>", user_mention))

if __name__ == "__main__":
	bot = SlackClient(bot_token)
	if bot.rtm_connect():
		while True:
			handle(bot.rtm_read())
			time.sleep(1)
	else:
		print "Connection failed."