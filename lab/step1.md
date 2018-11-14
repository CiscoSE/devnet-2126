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

[Step 2 - Starting up NSO]

[Step 2 - Starting up NSO]: step2.md