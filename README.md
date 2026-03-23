# rtk-gps
Repo to explore RTK GPS



## Host setup
### venv
```bash
sudo apt install python3-venv
```



## TCP Server
### ser2net
```bash
sudo apt install ser2net
sudo nano /etc/ser2net.yaml
```
Comment everything in /etc/ser2net.yaml and add the following:
```yaml
connection: &ublox-x20p
    accepter: tcp,2000
    connector: serialdev,
              /dev/ttyACM0,
              38400n81,local,nobreak
```

```bash
sudo systemctl restart ser2net.service
```
This service fails to autostart probably because the device is not yet available...

## Extra USB UART issues on linux 
https://github.com/aussierobots/ublox_dgnss/issues/48

https://github.com/phkehl/ubloxcfg/blob/main/tools/99-ftdi-ublox.rules

U-Blox EVK kit use two ftdi chips with ublox vendor IDs

Temporary fix:
```bash
echo 1546 050c > /sys/bus/usb-serial/drivers/ftdi_sio/new_id
echo 1546 050d > /sys/bus/usb-serial/drivers/ftdi_sio/new_id
```
Permanent fix:
```bash
sudo cp 99-ublox-ftdi.rules /etc/udev/rules.d/
```


## RTK Corrections
http://rtk2go.com:2101/SNIP::MOUNTPT?baseName=Bobcat58504&tk=q7dc88eev2qzmSSkuMb6


## Minicom
```bash
minicom -b 38400 -D /dev/ttyUSB0 -C minicom-log
```


## X20P Messages
### GGA
**Quality**

The `$GNGGA` quality field is the 6th comma-delimited value.

| Value | Description |
|-------|-------------|
| 1 | Standalone |
| 4 | Fixed |
| 5 | Float |