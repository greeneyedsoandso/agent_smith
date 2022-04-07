#!/usr/bin/env python3
# JDSmith
"""spams dogs to test incoming webhook"""
import os
import schedule
import time
import requests
import json
import random
# incoming webhook is per channel, set in Slack console. Contains secrets, hence variable.
post_url = os.environ.get("SLACK_WEBHOOK_IGNOREME")


def webhook():
    id_number = random.randint(1, 233)
    link = f"https://placedog.net/800/640?id={str(id_number)}"
    payload = json.dumps({"blocks": [{"type": "image", "title": {"type": "plain_text",
                                                                 "text": "Please enjoy this photo of dogs"},
                                      "image_url": link,
                                      "alt_text": "Doggo"}]})
    return requests.post(post_url, data=payload)


schedule.every(10).seconds.do(webhook)
# this posts every interval UNTIL YOU STOP THE SCRIPT FOR THE LOVE OF GOD STOP THE SCRIPT
while True:
    schedule.run_pending()
    time.sleep(1)
