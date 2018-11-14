### Step 3 - Add devices to NSO

#### Create an Authgroup

We will need to create an authentication group to specify the credentials for NSO to use when connecting to the devices:

```bash
ncs_cli -u admin -C

config
devices authgroups group vagrant default-map remote-name vagrant remote-password vagrant remote-secondary-password vagrant
commit
end
```
```bash
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
```

#### Add the first IOS-XR vagrant device


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
```bash
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
```

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
``` bash
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
```

#### Get initial configuration from device

```bash
devices sync-from
```
```bash
admin@ncs# devices sync-from
sync-result {
    device PE1
    result true
}
sync-result {
    device PE2
    result true
}
```
To display the devices and the configuration saved by NSO

```bash
show devices brief

show devices device PE1 | display xml
```

[Step 4 - Review XML L3VPN Template]

[Step 4 - Review XML L3VPN Template]: step4.md