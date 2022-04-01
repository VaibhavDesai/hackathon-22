import os
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys

# Retrieve required details from environment variables
bot_email = os.getenv("TEAMS_BOT_EMAIL")
teams_token = os.getenv("TEAMS_BOT_TOKEN")
bot_url = os.getenv("TEAMS_BOT_URL")
bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

# If any of the bot environment variables are missing, terminate the app
if not bot_email or not teams_token or not bot_url or not bot_app_name:
    print(
        "sample.py - Missing Environment Variable. Please see the 'Usage'"
        " section in the README."
    )
    if not bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_token:
        print("TEAMS_BOT_TOKEN")
    if not bot_url:
        print("TEAMS_BOT_URL")
    if not bot_app_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
#   Note: the `approved_users=approved_users` line commented out and shown as reference
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    # approved_users=approved_users,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},
    ],
)


# Create a custom bot greeting function returned when no command is given.
# The default behavior of the bot is to return the '/help' command response
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I am here to share and analyze your productivity over past weeks.".format(sender.firstName)
    response.markdown += "See what I can do by asking for **/help**."
    return response


# Create functions that will be linked to bot commands to add capabilities
# ------------------------------------------------------------------------
def yet_to_implement(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    return "Pending...." + incoming_msg;

def jira(incoming_msg):
    """
   Sample function to do some action.
   :param incoming_msg: The incoming message object from Teams
   :return: A text or markdown based reply
   """
    return "here you go --> https://jira-eng-gpk2.cisco.com/jira/secure/RapidBoard.jspa?rapidView=4320"


# Set the bot greeting.
bot.set_greeting(greeting)

# Add new commands to the bot.

bot.add_command("/rest/applinks/1.0/manifest","*",yet_to_implement)
bot.add_command("jira-guide","*",yet_to_implement)
bot.add_command("wap-data-wizards","*",yet_to_implement)
bot.add_command("cmc","*",yet_to_implement)
bot.add_command("personal-insights","*",yet_to_implement)
bot.add_command("cmc-qa","*",yet_to_implement)
bot.add_command("cmc-prod","*",yet_to_implement)
bot.add_command("hello-world","*",yet_to_implement)
bot.add_command("wap-kms","*",yet_to_implement)
bot.add_command("webex-pulse","*",yet_to_implement)
bot.add_command("wpns","*",yet_to_implement)
bot.add_command("kubed-vault","*",yet_to_implement)
bot.add_command("csb","*",yet_to_implement)
bot.add_command("control-hub","*",yet_to_implement)
bot.add_command("rmc","*",yet_to_implement)
bot.add_command("jira","*",jira)
bot.add_command("jenkins","*",yet_to_implement)
bot.add_command("jenkins-kubed","*",yet_to_implement)

# Every bot includes a default "/echo" command.  You can remove it, or any
# other command with the remove_command(command) method.
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
