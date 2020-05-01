# i-watch-these-vods
Want to complete any "Watch x Videos for rewards" Mission without actually watching anything? Look no further!

This script uses Selenium to automatically navigate your browser to the next VOD and therefore requires either Firefox _(preferred)_ or Chrome to be installed. It should run on all systems and uses Python 3.

## Setup

1. Download and Unzip this repo

2. **Install [Python 3](https://www.python.org/downloads/)** and install the `pip` package `selenium`

3. **Download a matching WebDriver**

   for Firefox: [geckodriver](https://github.com/mozilla/geckodriver/releases), for Chrome: [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), they are OS specific!
   
   unzip it and put it into the `driver` folder

## Usage

  - Set up the VODs by pasting the Links, each one line, into the `data/sources_vods` file. (Optional, I have already pasted enough for all *Watch & Earn Missions* in Spring 2020)
  - Double Click the Script to run it
  - After starting the script, Log in with your Riot Account to get watch rewards, then go back to the Script Window and press `Enter`
  - It will work for every other "Watch VODs" Mission Type
