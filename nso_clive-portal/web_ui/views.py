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
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import traceback
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from web_ui.controllers.nso import NsoController
import web_ui.controllers.webex as webex
import json


# ====================>>>>>>>> Utils <<<<<<<<====================
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# ====================>>>>>>>> Templates <<<<<<<<====================


def index(request):
    return render(request, 'web_app/index.html')


def home(request):
    return render(request, 'web_app/home.html')


def l3vpnList(request):
    return render(request, 'web_app/l3vpnList.html')


def l3vpnDetail(request):
    return render(request, 'web_app/l3vpnDetail.html')


def l3vpnNew(request):
    return render(request, 'web_app/l3vpnNew.html')


# ====================>>>>>>>> APIs <<<<<<<<====================

@csrf_exempt
def apiL3vpn(request, serviceName=""):
    """
       Manages evpn-single-home services in NSO
       POST: Creates a service
       GET: Retrieves the service
       DELETE: Deletes the service
       :param request:
       :return:
    """
    try:
        if request.method == 'GET':
            nsoController = NsoController()
            services = nsoController.getL3VPNServices()
            return JSONResponse(services)
        elif request.method == 'POST':
            # Parse request body to json
            payload = json.loads(request.body)
            nsoController = NsoController()
            nsoController.deployL3vpnService(payload)
            message = """
                      **Nuevo servicio** 
                       <br/> 
                      L3 VPN *""" + payload["name"] + """* ha sido agregado a la red para  
                      *""" + payload["customer"] + """*
                      <br/>
                      """
            webex.sendMessage(message=message)
            return JSONResponse("Ok")
        elif request.method == 'DELETE':
            nsoController = NsoController()
            nsoController.deleteL3vpnService(serviceName)

            webex.sendMessage(message=
                              """
                              **Servicio removido**
                            <br/> 
                            Servicio *""" + serviceName + """* ha sido eliminado de la red""")
            return JSONResponse("Ok")
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)
    except Exception as e:
        print(traceback.print_exc())
        # return the error to web client
        return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)


@csrf_exempt
def apiDevice(request):
    """
       Get devices managed by NSO
       :param request:
       :return:
    """
    try:
        if request.method == 'GET':
            nsoController = NsoController()
            devices = nsoController.getDevices()

            return JSONResponse(devices)
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)
    except Exception as e:
        print(traceback.print_exc())
        # return the error to web client
        return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
