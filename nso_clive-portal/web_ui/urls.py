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
"""
URL mapping of the application
"""

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index),

    # Angular mappings
    url(r'^home/?$', views.index),
    url(r'^l3vpn/?$', views.index),
    url(r'^l3vpn-detail/?$', views.index),
    url(r'^l3vpn-new/?$', views.index),
    url(r'^l3vpn-list/?$', views.index),

    url(r'^ng/home/?$', views.home),
    url(r'^ng/l3vpn-list/?$', views.l3vpnList),
    url(r'^ng/l3vpn-detail/?$', views.l3vpnDetail),
    url(r'^ng/l3vpn-new/?$', views.l3vpnNew),

    # APIs Mappings

    # Maps the URL web/api/pod to the method api_pod inside views.py
    url(r'^api/services/l3vpn/(?P<serviceName>.*)/?$', views.apiL3vpn),
    url(r'^api/services/l3vpn/?$', views.apiL3vpn),
    url(r'^api/device/?$', views.apiDevice),

]
