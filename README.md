# UbuntuIndicatorWeather ![Tag](https://img.shields.io/github/tag/kasramp/UbuntuIndicatorWeather.svg)
## Description
UbuntuIndicatorWeather is a very simple weather indicator for Ubuntu unity and Gnome 3. It is developed with Python and uses two web service calls [Ip-api.com](http://ip-api.com/), [Weather-api.madadipouya.com](http://weather-api.madadipouya.com/) (based on [Open Weather Map](http://api.openweathermap.org/)) to detect user's location and temperature respectively. 

## Dependencies
The indicator has dependencies for Python >= 2.7 and requires some Python libraries which are listed below
* Python >= 2.7
* Python gtk library
* Gir1.2-appindicator3-0.1
* Gir1.2-notify-0.7
* Python urllib
* Python json library
* Python retry library

## How to install
### Via PPA (Ubuntu only version 0.7 and onwards)
You can add PPA repository for easy installation and be notified on updates. Add the following repository to your machine like this:

`$ sudo add-apt-repository ppa:kasra-mp/ubuntu-indicator-weather`

`$ sudo apt-get update`


To install the weather indicator run:

`$ sudo apt-get install indicator-weather`

#### Supported Ubuntu versions
* Bionic Beaver 18.04 LTS
* ~~Zesty Zapus 17.04 (Until version 1.0)~~
* ~~Yakkety Yak 16.10 (Until version 0.9.0)~~
* Xenial Xerus 16.04 LTS
* ~~Wily Werewolf 15.10 (Until version 0.8.2)~~
* ~~Vivid Vervet 15.04 (Until version 0.9.0)~~
* Trusty Tahr 14.04 LTS

#### Supported architectures
* i386
* X64

### Via .deb file
If you want to use older versions (< 0.7) of the indicator or install it on other Debian based distributions, you can download .deb package(s) from release section ([link](https://github.com/kasramp/UbuntuIndicatorWeather/releases)).

### Via AUR (Arch Linux)
For Arch Linux, UbuntuIndicatorWeather is available on the Arch User Repository, under the package name ubuntu-indicator-weather  ([link](https://aur.archlinux.org/packages/ubuntu-indicator-weather/))

### Via .tar.gz file
For non-debian based distributions you can download .tar.gz files which consist of the source code of the indicator from release section ([link](https://github.com/kasramp/UbuntuIndicatorWeather/releases)). 

Extract the content of the compressed file and run installation file with root permission.

`$ sudo ./install.sh`

## Website
For more information please refer to [Simple Weather Indicator](http://simpleweatherindicator.madadipouya.com/) website.

## Screenshot
<p align="center">
<img src="http://blog.madadipouya.com/wp-content/uploads/2014/07/Screenshot-from-2015-12-25-14-08-10.png" alt="Simple Weather Indicator" height="26" width="148"/>
</p>

## Donate
You can always support, show appreciation by buying a cup of coffee :-)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=C68PYFWLT332S)

## Contact
* kasra@madadipouya.com
* kasra_mp@live.com
	
## License
<p>
<img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="License"/>
</p>

Indicator Weather is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3
as published by the Free Software Foundation.

Indicator Weather is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.  <http://www.gnu.org/licenses/>

Author(s):

© 2015-2018 Kasra Madadipouya <kasra@madadipouya.com>

