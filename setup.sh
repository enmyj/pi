# starting with raspian lite image
sudo useradd imyjer 
sudo usermod -aG sudo imyjer
exit

### as imyjer ###
mkdir ~/.ssh  # add public keys to ~/.ssh/authorized_keys

# remove pi user
sudo userdel pi
sudo rm -rf /home/pi

# linux stuff
sudo apt-get update && apt-get install -y \
    git \
    vim \
    htop \
    fish \
    sl \
    cowsay \
    python3-venv \
    python3-pip \
    nginx

# install docker
# https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# python stuff
sudo python3 -m pip3 install \
    docker-compose \
    flake8 \
    flask \
    gunicorn \
    keyring \
    numpy \
    pandas \
    pytest \
    scikit-learn \
    sqlalchemy \
    uvicorn \
    virtualenv

# docker stuff
docker pull python
docker pull jwilder/nginx-proxy
docker pull jrcs/letsencrypt-nginx-proxy-companion

# switch to fish shell as default
# and install oh my fish
sudo echo $(which fish) >> /etc/shells
sudo chsh --shell `which fish` $USER
curl -L https://get.oh-my.fish | fish

# disable wifi
# https://raspberrypi.stackexchange.com/questions/100543/how-to-disable-wifi-in-raspberry-pi-4/100549#comment166502_100549