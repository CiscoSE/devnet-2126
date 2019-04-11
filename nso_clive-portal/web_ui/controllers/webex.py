"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import requests

BOT_TOKEN = ""  #add token
ROOM_ID = "" #add room_id
URL = "https://api.ciscospark.com/"

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))


def makeCall(p_url, method, data=""):
    """
    All APIs call single point of execution
    :return:
    """
    # Debug
    print("Sending " + method + " request to Webex Team: " + p_url)
    print(data)
    headers = {
        "Content-type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + BOT_TOKEN
    }
    if method == "POST":
        response = requests.post(URL + p_url, data=data, headers=headers)
    else:
        raise Exception("Method not supported")
    if 199 < response.status_code < 300:
        return response
    else:
        raise Exception(response.text)


def sendMessage(message):
    """
    Send a message to a configured ROOM_ID using a bot account token
    :param message:
    :return:
    """
    template = JSON_TEMPLATES.get_template('send_webex_message.j2.json')
    payload = template.render(room_id=ROOM_ID, message=message).replace("\n", "")
    p_url = "v1/messages"
    method = "POST"
    makeCall(p_url=p_url, method=method, data=payload)
