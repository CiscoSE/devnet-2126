# Devnet-2126 Workshop CL Cancun 2018 - Automate service deployment in your network
This lab will provide you with a guide to utilizing NSO to create a simple service deployment in your network.  

Contacts:
* Jason Mah - jamah@cisco.com

In this lab we will only setup the PE routers for a simple L3VPN use case.  Typically, you would also need the associate CE routers to complete the service.  However, we will demostrate NSO's capabilities to create, update and remove the service.  

## Setup

A vagrant script will bring up a two IOS-XR instances that will be networked together through gig0/0/0/2 (IP:10.1.1.1 and 10.1.1.2).  The vagrant script will also spin up an ubuntu instance which will be used for a custom web portal.  


At the end of the lab, 
## NSO

Service Model

Device Model

NED - Cisco-IOS-XR


### Step 1 - Starting up Vagrant

To get started, open a terminal :computer: and start up vagrant file:

```bash
cd $HOME/devnet-2126/xrv-vagrant
vagrant up
```

From the Applications folder, open PyCharm. This is a useful integrated development environment 
(IDE) that we will be used to edit different files. 
 
Click on "open" and then choose the directory created before (devnet-2126 - inside the home directory)

Within the solution, there are four directories that you should be aware:

1. **l3vpn-test1** contains the nso yang and xml templates for simple l3vpn
2. **nso_clive-portal:** contains the Django custom web portal
3. **xrv-vagrant:** contains the files for vagrant to create the IOS-XRv and ubuntu instances and day0 configuration files.


### Step 2 - 

Check to see if NSO is running

```bash
man ncs
```
If you a response "No manual entry for ncs"  Then NSO is not running and we will need to start it.

```bash
source $HOME/ncs-4.7/ncsrc
```

Copy the L3vpn package to the running NSO directory. 
```bash
cp -r $HOME/devnet-2126/l3vpn-test1 $HOME/ncs-4.7-run/packages
```

Change directory to l3vpn NSO package and compile the model
```bash
cd $HOME/ncs-4.7-run/packages/l3vpn-test1/src
make all
```

Start NSO
```bash
cd $HOME/ncs-4.7-run
ncs
```

To open a NSO cli client
```bash
ncs_cli -u admin -C
```

Install NSO packages - check that the result for each package is true
```bash
packages reload
```

admin@ncs# packages reload
reload-result {
    package cisco-iosxr
    result true
}
reload-result {
    package l3vpn-test1
    result true
}
admin@ncs#

### Step 3 - Add devices to NSO

####Create an Authgroup

We will need to create an authentication group to specify the credentials for NSO to use when connecting to the devices:

```bash
ncs_cli -u admin -C

config
devices authgroups group vagrant default-map remote-name vagrant remote-password vagrant remote-secondary-password vagrant
commit
end
```

admin@ncs# config
Entering configuration mode terminal
admin@ncs(config)# devices authgroups group vagrant default-map remote-name vagrant remote-password vagrant remote-secondary-password vagrant
admin@ncs(config-group-vagrant)# commit
Commit complete.
admin@ncs(config-group-vagrant)# end
admin@ncs# show running-config devices authgroups group vagrant
devices authgroups group vagrant
 default-map remote-name   vagrant
 default-map remote-password $8$D7LrdZEDGb0bTCDZhFmNr8gEFUa9Fig0q5azBsm9oOo=
 default-map remote-secondary-password $8$SDK0GokN/RZGI59CqCwzp7H4M29Qdk4FAOdskgzB0HA=
 umap vagrant
  remote-name     vagrant
  remote-password $8$3yiuHKomFWF0U+0rmt7U2+nw+HLjGldWwNQkooyyKv0=
 !
!
admin@ncs#


####Add the first IOS-XR vagrant device


```bash
config t
devices device PE1
address 127.0.0.1 port 2322
device-type cli ned-id cisco-ios-xr protocol ssh
authgroup vagrant
state admin-state unlocked
commit
end
device fetch-ssh-host-keys devices PE1
```

admin@ncs# config t
Entering configuration mode terminal
admin@ncs(config)# devices device PE1
admin@ncs(config-device-PE1)# address 127.0.0.1 port 2322
admin@ncs(config-device-PE1)# device-type cli ned-id cisco-ios-xr protocol ssh
admin@ncs(config-device-PE1)# authgroup vagrant
admin@ncs(config-device-PE1)# state admin-state unlocked
admin@ncs(config-device-PE1)# commit
Commit complete.
admin@ncs(config-device-PE1)# end
admin@ncs# devices fetch-ssh-host-keys device PE1
fetch-result {
    device PE1
    result updated
    fingerprint {
        algorithm ssh-rsa
        value 2a:84:97:b7:2f:de:28:bf:98:ea:68:c4:26:8e:37:c3
    }
}
admin@ncs#

```bash
config t
devices device PE2
address 127.0.0.1 port 2422
device-type cli ned-id cisco-ios-xr protocol ssh
authgroup vagrant
state admin-state unlocked
commit
end
device fetch-ssh-host-keys devices PE2
```

admin@ncs# config t
Entering configuration mode terminal
admin@ncs(config)# devices device PE2
admin@ncs(config-device-PE2)# address 127.0.0.1 port 2422
admin@ncs(config-device-PE2)# device-type cli ned-id cisco-ios-xr protocol ssh
admin@ncs(config-device-PE2)# authgroup vagrant
admin@ncs(config-device-PE2)# state admin-state unlocked
admin@ncs(config-device-PE2)# commit
Commit complete.
admin@ncs(config-device-PE2)# end
admin@ncs# devices fetch-ssh-host-keys device PE2
fetch-result {
    device PE2
    result updated
    fingerprint {
        algorithm ssh-rsa
        value 2a:84:97:b7:2f:de:28:bf:98:ea:68:c4:26:8e:37:c3
    }
}
admin@ncs#


####Get initial configuration from device

```bash
devices sync-from
```

admin@ncs# devices sync-from
sync-result {
    device PE1
    result true
}
sync-result {
    device PE2
    result true
}

To display the devices and the configuration saved by NSO

```bash
show devices brief

show devices device PE1 | display xml
```


### Step 4 - Review XML L3VPN Template

The XML L3VPN template can be found in the following directory.

```bash
cd $HOME/ncs-4.7-run/packages/l3vpn-test1/templates/
more l3vpn-test1-template.xml
```

Open the folder on PyCharm - add picture


### Step 5 - Review Yang data model L3VPN

The Yang data model can be found in the following directory.

```bash
cd $HOME/ncs-4.7-run/packages/l3vpn-test1/packages/l3vpn-test1/src/yang
more l3vpn-test1.yang
```

Open the folder on PyCharm - add picture


### Step 6 - Create L3VPN service in NSO CLI

admin@ncs# config
Entering configuration mode terminal
admin@ncs(config)# services l3vpn-test1 ?
Possible completions:
  <name:string>  range
admin@ncs(config)# services l3vpn-test1 coke ?
Possible completions:
  check-sync           Check if device config is according to the service
  commit-queue
  customer
  deep-check-sync      Check if device config is according to the service
  devices
  get-modifications    Get the data this service created
  log
  re-deploy            Run/Dry-run the service logic again
  reactive-re-deploy   Reactive redeploy of service logic
  touch                Touch a service
  un-deploy            Undo the effects of this service
  vrf-name
  <cr>
admin@ncs(config)# services l3vpn-test1 coke customer coke ?
Possible completions:
  devices  vrf-name  <cr>
admin@ncs(config)# services l3vpn-test1 coke customer coke vrf-name coke ?
Possible completions:
  devices  <cr>
admin@ncs(config)# services l3vpn-test1 coke customer coke vrf-name coke devices PE1 ?
Possible completions:
  interface-id  ip-address  netmask  router-id  <cr>
admin@ncs(config)# services l3vpn-test1 coke customer coke vrf-name coke devices PE1 interface-id 0/0/0/2 ip-address 5.5.5.1 netmask 255.255.255.252 router-id 1.1.1.1
admin@ncs(config-devices-PE1)# devices PE2 interface-id 0/0/0/2 ip-address 6.6.6.1 netmask 255.255.255.252 router-id 2.2.2.2

admin@ncs(config-devices-PE2)# commit dry-run outformat cli
cli {
    local-node {
        data  devices {
                  device PE1 {
                      config {
                          cisco-ios-xr:vrf {
             +                vrf-list coke {
             +                    address-family {
             +                        ipv4 {
             +                            unicast {
             +                                import {
             +                                    route-target {
             +                                        address-list 1:1;
             +                                    }
             +                                }
             +                                export {
             +                                    route-target {
             +                                        address-list 1:1;
             +                                    }
             +                                }
             +                            }
             +                        }
             +                    }
             +                }
                          }
                          cisco-ios-xr:interface {
                              GigabitEthernet 0/0/0/2 {
             +                    description "interface to coke";
             +                    vrf coke;
                                  ipv4 {
                                      address {
             -                            ip 10.1.1.1;
             +                            ip 5.5.5.1;
             -                            mask 255.255.255.0;
             +                            mask 255.255.255.252;
                                      }
                                  }
                              }
                          }
                          cisco-ios-xr:router {
                              bgp {
                                  bgp-no-instance 1 {
             +                        vrf coke {
             +                            rd 1:1;
             +                            address-family {
             +                                ipv4 {
             +                                    unicast {
             +                                    }
             +                                }
             +                            }
             +                        }
                                  }
                              }
                          }
                      }
                  }
                  device PE2 {
                      config {
                          cisco-ios-xr:vrf {
             +                vrf-list coke {
             +                    address-family {
             +                        ipv4 {
             +                            unicast {
             +                                import {
             +                                    route-target {
             +                                        address-list 1:1;
             +                                    }
             +                                }
             +                                export {
             +                                    route-target {
             +                                        address-list 1:1;
             +                                    }
             +                                }
             +                            }
             +                        }
             +                    }
             +                }
                          }
                          cisco-ios-xr:interface {
                              GigabitEthernet 0/0/0/2 {
             +                    description "interface to coke";
             +                    vrf coke;
                                  ipv4 {
                                      address {
             -                            ip 10.1.1.2;
             +                            ip 6.6.6.1;
             -                            mask 255.255.255.0;
             +                            mask 255.255.255.252;
                                      }
                                  }
                              }
                          }
                          cisco-ios-xr:router {
                              bgp {
                                  bgp-no-instance 1 {
             +                        vrf coke {
             +                            rd 1:1;
             +                            address-family {
             +                                ipv4 {
             +                                    unicast {
             +                                    }
             +                                }
             +                            }
             +                        }
                                  }
                              }
                          }
                      }
                  }
              }
              services {
             +    l3vpn-test1 coke {
             +        vrf-name coke;
             +        customer coke;
             +        devices PE1 {
             +            interface-id 0/0/0/2;
             +            ip-address 5.5.5.1;
             +            netmask 255.255.255.252;
             +            router-id 1.1.1.1;
             +        }
             +        devices PE2 {
             +            interface-id 0/0/0/2;
             +            ip-address 6.6.6.1;
             +            netmask 255.255.255.252;
             +            router-id 2.2.2.2;
             +        }
             +    }
              }
    }
}
admin@ncs(config-devices-PE2)#

### Step 7 - Create L3VPN service with custom portal


