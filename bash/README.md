# scripts

## hfedit ##

* this script with take a massive file and extract the lines you would like to edit, on save it will re-insert the lines into the original document

*Installation & Execution*

* Make executable & run:
    ```
    chmod +x hfedit
    sh hfedit yourHugeFile 3 8
    ```
* In that example, vim will open up lines 3 through 8, you can edit them, and when you save and quit, those lines in the hugefile will automatically be overwritten with your saved lines.

## notify-remote ##

* this script will send a notify-send message to a remote x-session

*Installation & Execution*

* to run:
    ```
    chmod +x /usr/local/bin/notify-remote
    notify-remote [message_separated_by_underscore]
    ```

## watchSupervisor ##

* this script is to watch the supervisor service for status changes then calls notify-remote to send a remote x-session message
 
*Installation & Execution*

* make executable and enable cron:
    ````
    sudo chmod +x /usr/local/bin/watchQueue
    crontab -u root -e << */10 * * * * /usr/bin/bash /usr/local/bin/watchQueue
    ````

----