# linux stuff
sudo apt-get update && apt-get install -y \
    git \
    curl \
    htop \
    vim \
    jq \
    ufw \
    fail2ban

### install docker
# https://docs.docker.com/engine/install/debian/
# https://docs.docker.com/engine/install/linux-postinstall/

### install tailscale
# setup server: https://tailscale.com/kb/1245/set-up-servers
# setup firewall: https://tailscale.com/kb/1077/secure-server-ubuntu
# tailcale up <flags>

### security
sudo bash -c 'cat << EOF > /etc/ssh/sshd_config.d/custom.conf
PermitRootLogin no
PasswordAuthentication no
Port 2222
AllowUsers imyjer
EOF'
sudo systemctl restart ssh

# ufw config
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 2222/tcp

# fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo touch /var/log/auth.log

# edit the sshd part of /etc/fail2ban/jail.local
# [sshd]
# enabled = true
# port = 2222
# maxretry = 3
# bantime = 600
# findtime = 600
# logpath = /var/log/auth.log
# backend = %(sshd_backend)s
sudo systemctl start fail2ban
sudo systemctl enable fail2ban

# install cloudflared
https://pimylifeup.com/raspberry-pi-cloudflare-tunnel/
