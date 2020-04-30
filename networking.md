
# Dynamic DNS
Apparently my router's public IP address can change anytime so I'm using DuckDNS.org cuz it's free and hilariously simple
Google also offers dynamic DNS it turns out lol

How to resolve dynamic DNS from with home: https://raspberrypi.stackexchange.com/questions/13757/problems-with-dynamic-dns-and-raspberry-pi

# Static IP (aka internal IP address)
I was able to set this on my router directly. Otherwise these instructions seem solid even though they didn't work for me: https://pimylifeup.com/raspberry-pi-static-ip-address/

# PI DNS settings (somehow this got borked at one point)
https://pimylifeup.com/raspberry-pi-dns-settings/

# Port Forwarding
I set this up through router directly. I'm forwarding 22 for ssh, 80 for web, and 1194 for VPN

# VPN

Raspberry Pi has an ARM CPU, so I used this: https://github.com/giggio/docker-openvpn-arm. Very simple to setup, although having a VPN at my house seems useless.

# PiHole

Got this running using `docker`. Stupid router won't let me change this either. 

This looks solid: https://demyx.sh/tutorial/how-to-run-openvpn-and-pi-hole-using-docker-in-a-vps/

# Host website with Traefik (all examples are for Traefik v1.7)

https://beenje.github.io/blog/posts/running-your-application-over-https-with-traefik/
https://docs.traefik.io/v1.7/user-guide/docker-and-lets-encrypt/
https://docs.traefik.io/v2.0/https/acme/#httpchallenge
https://www.reddit.com/r/pihole/comments/fy8zmu/pihole_traefik_dnsovertls/


# Ubuntu local DNS
the current bane of my existence

https://archive.fosdem.org/2019/schedule/event/dns_systemd_resolved/

```
symlink /etc/resolv.conf to...
   /run/systemd/resolve/stub-resolv.conf
   /usr/lib/systemd/resolv.conf
   /run/systemd/resolve/resolv.conf
   

systemd-resolve
sudo resolvectl dns wlp2s0 10.0.0.200  # works but not after restart
```