### Step 6 - Create L3VPN service in NSO CLI

Let's create a L3VPN service using the NSO CLI.  

```bash
config
services l3vpn-test1 coke customer coke vrf-name coke devices PE1 interface-id 0/0/0/2 ip-address 5.5.5.1 netmask 255.255.255.252 router-id 1.1.1.1
devices PE2 interface-id 0/0/0/2 ip-address 6.6.6.1 netmask 255.255.255.252 router-id 2.2.2.2
commit dry-run outformat cli
commit
```
```bash
admin@ncs# config
Entering configuration mode terminal
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
admin@ncs(config-devices-PE2)#commit
Commit complete.
admin@ncs(config-devices-PE2)#
```

[Step 7 - Create L3VPN service with custom portal]

[Step 7 - Create L3VPN service with custom portal]: step7.md
