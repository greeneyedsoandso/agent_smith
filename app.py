#!/usr/bin/env python3
# slackbot PoC JDSmith
"""hello there"""
import os
import random
# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.command("/doggo")
# set this up in the Slack API console to make it work
def doggo_command(ack, body):
    user_id = body["user_id"]
    id_number = random.randint(1, 233)
    link = f"https://placedog.net/800/640?id={str(id_number)}"
    payload = {"blocks": [{"type": "image", "title": {"type": "plain_text",
                                                                 "text": "Dogs make it better"},
                                      "image_url": link,
                                      "alt_text": "Doggo"}]}
    ack(payload)


@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"You hear that <@{user_id}>?... That is the sound of inevitability.")


@app.event("app_mention")
def event_test(say):
    say("Mister Anderson")


# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click",
                },
            }
        ],
        text=f"Hey there <@{message['user']}>!",
    )


# Listens to incoming messages that contain "puppy"
@app.message("puppy")
def message_puppy(say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {"type": "image",
             "title": {"type": "plain_text", "text": "Please enjoy this photo of a puppy"},
             "block_id": "image4", "image_url": "https://place-puppy.com/500x500",
             "alt_text": "An incredibly cute puppy."}
        ],
        text="An incredibly cute puppy."
    )


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
            view={
                "type": "home",
                "callback_id": "home_view",

                # body of the view
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome to your _App's Home_* :tada:"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "This button won't do much for now but you can set up a "
                                    "listener for it using the `actions()` method and passing its "
                                    "unique `action_id`. See an example in the `examples` folder "
                                    "within your Bolt app. "
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {"type": "plain_text", "text": "Click me!"},
                                "action_id": "home_button",
                            }
                        ]
                    }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("home_button")
def action_home_button_click(body, ack, say):
    # Acknowledge the action - this needs to identify a channel where the
    # message will display
    ack()
    say(channel="CL1PDRL15", text=f"ring ring <@{body['user']['id']}>")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

