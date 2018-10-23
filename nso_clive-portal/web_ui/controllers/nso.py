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
from web_ui.envs import *

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))
# Disable warnings
requests.packages.urllib3.disable_warnings()


class NsoController:
    # TODO: These are sandbox credentials and are hardcoded for simplicity.
    # TODO: By any means include blank password in your source code.
    credentials = get_nso_credentials()
    url = get_nso_url()

    def makeCall(self, p_url, method, data="", headers={}):
        """
        Basic method to make a call. Please this one to all the calls that you want to make
        :param p_url: APIC URL
        :param method: POST/GET/DELETE
        :param data: Payload to send
        :param headers: Headers to send
        :return:
        """
        # Debug
        print("Sending " + method + " request to NSO: " + p_url)
        print(data)
        headers["Authorization"] = "Basic " + self.credentials
        if method == "POST":
            response = requests.post(self.url + p_url, data=data, headers=headers, verify=False)
        elif method == "GET":
            response = requests.get(self.url + p_url, headers=headers, verify=False)
        elif method == "DELETE":
            response = requests.delete(self.url + p_url, headers=headers, verify=False, data="")
        else:
            raise Exception("Method not supported")
        if 199 < response.status_code < 300:
            return response
        else:
            raise Exception(response.text)

    def getL3VPNServices(self):
        """
        Queries all EVPN Single Home services in NSO
        :return:
        """
        p_url = "api/running/services/l3vpn-test1/"
        headers = {"Content-Type": "application/vnd.yang.collection+json",
                   "Accept": "application/vnd.yang.collection+json"}
        l3vpnServices = []
        method = "GET"
        httpResponse = self.makeCall(p_url=p_url, headers=headers, method=method)
        if httpResponse.text == "":
            return []
        response = httpResponse.json()
        for service in response["collection"]["l3vpn-test1:l3vpn-test1"]:
            p_url = "api/running/services/l3vpn-test1/" + service["name"] + "/devices"
            httpResponse = self.makeCall(p_url=p_url, headers=headers, method=method)
            if httpResponse.text != "":
                serviceDevices = httpResponse.json()
                service["devices"] = serviceDevices["collection"]["l3vpn-test1:devices"]
            l3vpnServices.append(service)
        return l3vpnServices

    def syncFromDevices(self):
        """
        Sync database from all devices
        :return:
        """
        p_url = "api/running/devices/_operations/sync-from/"
        method = "POST"
        headers = {
            'content-type': "application/vnd.yang.operation+json"
        }
        self.makeCall(p_url=p_url, headers=headers, method=method)
        # Create a new request with the given parameters

    def deployL3vpnService(self, data):
        """
        Deploy an L3 VPN service in NSO
        :param data: Service parameters
        :return: None
        """
        p_url = "api/running/services/"
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "POST"
        template = JSON_TEMPLATES.get_template('l3vpn.j2.json')
        self.syncFromDevices()
        payload = template.render(data).replace("\n", "")
        self.makeCall(p_url=p_url, headers=headers, method=method, data=payload)

    def deleteL3vpnService(self, serviceName):
        """
        Deletes an EVPN Single Home services in NSO
        :param customerName:
        :return: None
        """
        p_url = "api/running/services/l3vpn-test1/" + serviceName
        method = "DELETE"
        headers = {"Content-Type": "application/vnd.yang.data+json",
                   "Accept": "application/vnd.yang.data+json"}
        self.syncFromDevices()
        self.makeCall(p_url=p_url, headers=headers, method=method)

    def getDevices(self):
        """
        Return all devices managed by NSO
        :return:
        """
        p_url = "api/running/devices/device"
        method = "GET"
        headers = {"Content-Type": "application/vnd.yang.data+json",
                   "Accept": "application/vnd.yang.collection+json"}
        response = self.makeCall(p_url=p_url, headers=headers, method=method).json()['collection']['tailf-ncs:device']

        return response

    def getRollbackConfig(self, rollbackId):
        """
        Return configuration done on an specific rollback
        :return:
        """
        p_url = "api/rollbacks/" + str(rollbackId)
        method = "GET"
        headers = {}
        response = self.makeCall(p_url=p_url, headers=headers, method=method)

        return response.text
