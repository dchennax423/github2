Two ways to clone the repo
First way:
Go to https://github.com/ --> click on profile icon ---> go to settings--> go to drop down

Click on developer settings--> click on personal access tokens-- Generate new token --> give name , expiration date, click checkbox on repos , write packages--> click on generate token

Save the token in the notepad/sticky notes

Click on configure SSO -- authenticate to inter inner source

Open the repo url for eg: https://github.com/intel-innersource/firmware.storage.optane.ise.jenkins-utils

Click on code--> copy the https url
Create local folder on desktop--> right click on that folder --> click gitbash here--> 
Git clone paste the <url link>
Ask for authentication-- give username: dprudhix
password : paste the token value

Throws any error like this follow the below steps:


Open windows powershell--> Run as administrator--> give the particular command <git config --system core.longpaths true>


Clone the repo successfully 


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



Second Way: Clone via dt setup

Go to https://1source.intel.com/onboard

Download devtool from the above link
Once downloaded --> open the command prompt -- execute the command <.\Downloads\dt.exe install> ---> close the command prompt

Open a new command prompt--> execute the command<dt setup>

Microsoft Windows [Version 10.0.19044.2006]
(c) Microsoft Corporation. All rights reserved.

C:\Users\dprudhix>dt setup
 ====> Git Proxy configuration
? Allow devtool to manage your github proxy settings in the .gitconfig file? Yes
? Your Intel email: [? for help] (devisrix.prudhive@intel.com)

? Your Intel email: devisrix.prudhive@intel.com
Checking GitHub account status...
Your GitHub account is properly configured
Git already installed - skipping
git proxy setting for github.com updated to http://proxy-iind.intel.com:912
 ====> Git Configuration
? Your full name: [? for help] (dprudhix)

? Your full name: dprudhix
Your email address: devisrix.prudhive@intel.com
Git settings successfully configured
 ====> Github token creation
? Choose a Git token storage type: netrc

The next step will create an authentication token for GitHub and
store it in C:\Users\dprudhix\_netrc.

Before proceeding, please open the browser of your laptop to
https://github.com and login with your GitHub account that you
wish to use for Intel development. Make sure to use incognito
tab if this is generic account

Once you have successfully logged in to your GitHub account,
press <Enter> to continue:

Using the same browser from the previous step, please visit the
following URL and enter the one-time security code:

    URL: https://github.com/login/device
    One-time code: 01D4-17D1

Waiting for you to complete the authorization on the website above...
Successfully configured Github oauth token

Checking workstation configuration...
Version: 2.0.460 (538d272)
Latest version: 2.0.460
Build Time: Wed, 21 Sep 2022 17:15:35 -0700
Compiled for: windows
USERPROFILE directory: C:\Users\dprudhix
devtool path: C:\Users\dprudhix\bin\dt.exe
IP Address: 10.253.157.51
Operating system: Windows 10 Enterprise
Log: C:\Users\dprudhix\.config\dt\dt.log
Config: C:\Users\dprudhix\.config\dt\config.toml
User Extensions: C:\Users\dprudhix\.config\dt\extensions
System Extensions: C:\Users\dprudhix\bin\.dt-extensions
Migrations: C:\Users\dprudhix\.config\dt\migrations
Intel email: devisrix.prudhive@intel.com
GitHub onboard completed: yes
====== Checking tools ======
Git installed: yes
Git version: 2.14.3.windows.1
====== Git configuration ======
Git user.name: dprudhix
Git user.email: devisrix.prudhive@intel.com
====== Proxy configuration ======
Autoproxy feature enabled: yes
On Intel network: yes
Current autoproxy value: http://proxy-iind.intel.com:912
Manage .gitconfig github proxies: yes
====== Proxy environment variables ======
HTTPS_PROXY:
NO_PROXY:
HTTPS_PROXY env has not been configured yet
====== Proxy Git configuration ======
github.com proxy value: http://proxy-iind.intel.com:912
lfs.github.com proxy value: http://proxy-iind.intel.com:912
github-cloud.s3.amazonaws.com proxy value: http://proxy-iind.intel.com:912
github-cloud.githubusercontent.com proxy value: http://proxy-iind.intel.com:912
You have http.proxy=https://proxy-dmz.intel.com:912 configured in file:C:/Users/dprudhix/.gitconfig which may lead to unexpected behaviour
====== Github authentication ======
Github token storage type: netrc
Github oauth token configured: yes
Github oauth token uses new GitHub format: yes
Github authentication: successful
Github username: dprudhix
====== Checking GitHub Innersource Access ======
Employee Type: green-badge
Contingent worker (GB) access is based on a need-to-know basis.
Visit https://1source.intel.com/inventory/explore to see the AGS entitlements for repos you need access to

C:\Users\dprudhix>



above log will come --> verify the details and click enter--> open the url <URL: https://github.com/login/device> authenticate the login 


Now clone the repo it will not ask for any authentication it will clone the repo successfully



