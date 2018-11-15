# Devnet-2126 Workshop CL Cancun 2018 - Automate service deployment in your network
This lab will provide you with a guide to utilizing NSO to create a simple service deployment in your network.  

Contacts:
* Jason Mah - jamah@cisco.com
* Santiago Flores Kanter - sfloresk@cisco.com

In this lab we will only setup the PE routers for a simple L3VPN use case.  Typically, you would also need the associate CE routers to complete the service.  However, we will demostrate NSO's capabilities to create, update and remove the service with this example. 

## Setup

A vagrant script will bring up two IOS-XRv instances that will be networked together through gig0/0/0/2 (IP:10.1.1.1 and 10.1.1.2).  The vagrant script will also spin up an ubuntu instance which will be used for a custom web portal.  

![devnet_2126_lab](/lab/images/devnet_2126_lab.png)

In this lab we will start NSO and onboard the two IOS-XRv instances.  Once we establish a connection with the two devices, we will configure the L3VPN service on the routers using the NSO command line interface and a custom web portal.


## NSO

Cisco® Network Services Orchestrator (NSO) enabled by Tail-f® is an industry-leading orchestration platform for hybrid networks. It provides comprehensive lifecycle service automation to enable you to design and deliver high-quality services faster and more easily.

Network Services Orchestrator helps customers to achieve important business objectives:

●   Faster development and deployment of new revenue-generating services
●   Better quality of services, with fewer human errors and less repetitive manual work
●   Vendor independence

NSO is now free to download for non-production use!!
https://developer.cisco.com/site/nso/


[Let's Get Started]

[Let's Get Started]: lab/step1.md

