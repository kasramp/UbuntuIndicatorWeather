---
title: How to install Simple Weather Indicator
feature_text: |
  ## Simple Weather Indicator Installation
feature_image: "https://unsplash.it/1300/400?image=970"
image: "https://unsplash.it/1300/400?image=970"
---
There are three installation methods exist which are:
- Via PPA
- Via Debian package file
- Via AUR (Arch Linux)
- Via source code

### Via PPA (Ubuntu only version 0.7 and onwards)
You can add PPA repository for easy installation and be notified on updates. Add the following repository to your machine like this:

`$ sudo add-apt-repository ppa:kasra-mp/ubuntu-indicator-weather`

`$ sudo apt-get update`

To install the weather indicator run:

`$ sudo apt-get install indicator-weather`

Keep in mind that the described method is only valid for Ubuntu distribution and it is only supported for version 0.7 of the indicator and later. If you want to decide older version please refer to the next section.

#### Supported Ubuntu versions
- Zesty Zapus 17.04
- Yakkety Yak 16.10
- Xenial Xerus 16.04 LTS
- Wily Werewolf 15.10 (Until version 0.8.2)
- Vivid Vervet 15.04
- Trusty Tahr 14.04 LT

#### Supported architectures
- i386
- X64

### Via Debian package file
If you are using any Debian based distribution except Ubuntu, you can download `.deb` file from releases link and install it via this command:

`$ sudo dpkg -i indicator-weather_Version_all.deb`

### Via AUR (Arch Linux)
For Arch Linux, Simple Weather Indicator is available on the Arch User Repository, under the package name ubuntu-indicator-weather via this link:
[https://aur.archlinux.org/packages/ubuntu-indicator-weather/](https://aur.archlinux.org/packages/ubuntu-indicator-weather/)

### Via source code
At the moment other Linux distributions users have to rely on source code to use this indicator. To do that, download `.tar.gz` package of your desired version from releases section and uncompress it to any desire location. 

Before proceeding to the next step make sure that you have the following packages installed on your system.
- Python >= 2.7
- Python gtk library
- Gir1.2-appindicator3-0.1
- Python urllib
- Python json library

After that run the installation script with root permission,

`sudo ./install.sh`

The last step is to run the indicator using the following command,

`indicator-weather`

To make the indicator to start automatically on system startup, depends on your desktop/window manager, you need to add `indicator-weather` file to the startup script.
