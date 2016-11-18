INTRODUCTION
------------

wioLeet gathers sensor data from any wioLinks or wioNodes and exports the data to ThingSpeak and Initial State


REQUIREMENTS
------------

This module requires the following modules:

 * Python version: 2.7
 * Python packages: enum, ISStreamer, smtplib
 

INSTALLATION
------------
 
 * in root dir run `python setup.py install`

 * run `python configure.py` to set run params
 
 * run `python app/run.py` to run the service
 
 * Setup cron: 
```bash
crontab -u [user] -e << '* * * * * [user] /usr/bin/python /pathToApp/run.py >> /var/log/wioLeet.log
sudo chown /var/log/wioLeet.log
```


PACKAGING
---------
 
 * in root dir run `python setup.py sdist`