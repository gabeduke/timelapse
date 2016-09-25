## logWatch ##

*Installation & Execution*

* Make executable `chmod +x ~/logWatch`
* To run as daemon:

```
mkdir & chown to user ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable logWatch.service
systemctl --user start logWatch
```
