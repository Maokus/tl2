# TemperatureLogger

This project requires chrome bc im lazy to make it compatible with other browsers.
I am unsure as to whether this project works on windows, if anyone wants to they can pull the code and make it work. 

## Installation
### mac
If chromedriver is not yet installed, go to the selenium chromedriver install page.
https://chromedriver.chromium.org/downloads
Download the chromedriver for the version of chrome you use and move it into `/usr/local/bin` (or anywhere else in your path i dont care)

```
git clone https://github.com/Maokus/TemperatureLogger.git
cd TemperatureLogger
```

## Running
`python3 driver.py`

driver.py is a simple program which checks the time every 2 hours and logs the temperature if the time is between 6 and 9.
