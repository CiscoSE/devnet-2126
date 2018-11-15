### Step 2 - Starting up NSO

Check to see if NSO is running

```bash
man ncs
```
If you recieve a response "No manual entry for ncs"  Then NSO is not running and we will need to start it.

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
```bash
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
```
At this point, NSO is operational and the packages for IOS-XR NED and L3VPN service have been installed.

[Step 3 - Add devices to NSO]

[Step 3 - Add devices to NSO]: step3.md