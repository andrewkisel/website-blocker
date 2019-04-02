# Website Blocker

Helps to block some websites during working hours.

## Getting Started

Schedule this script to run at the startup/login and it is going to forward websites you want to block to localhost.

### Prerequisites

Modify TO_BLOCK list to reflect websites you would like to block. REDIRECT_IP sets which IP to redirect websites you included in the list above. START_TIME and END_TIME variables can be adjusted to reflect your working hours. The app will block websites only from Monday to Friday.

### Installing

Set the script to run at the startup depending on your operating system. launchd is recommended for OSX, Windows Task Scheduler for Windows.

## Authors

* **Andrew Kisel** - *Initial work* - [AndrewKisel](https://github.com/andrewkisel)
