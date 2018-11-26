### Step 7 - Create L3VPN service with custom portal

We will next log into Ubuntu instance which will host the custom web portal

```
cd $HOME/devnet-2126/xrv-vagrant
vagrant ssh devbox -- -R 12345:localhost:8080
```

The prompt should change now to vagrant@ubuntu-bionic:~$, this means you have ssh into the ubuntu VM
```
cd devnet-2126/nso_clive-portal/
python3 manage.py runserver 0.0.0.0:8080
```

Now open your browser to http://0.0.0.0:2200

From here we can create a new service just like we did from the NSO CLI.  

Please see a sample of the dashboard below:

![Portal](/lab/images/nso_portal.png)

#### End of the Lab - Congrats!!
