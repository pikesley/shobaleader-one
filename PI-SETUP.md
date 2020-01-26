# From a box-fresh NOOBS 3.2 (on the Pi 4)

* enable ssh
* change hostname

```
sudo apt-get update
sudo apt-get -y upgrade
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
sudo apt-get install -y python3-pip
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
sudo ln -s /home/pi/.poetry/bin/poetry /usr/local/bin/
```

Add ssh key to `.ssh/authorized_keys`

`make push-code` from Docker-side

```
cd shobaleader-one/
make install
make run-api
```
