### install k3s
# https://docs.k3s.io/installation/configuration
# add some junk to the boot file thing: https://docs.k3s.io/installation/requirements?os=pi
# add ufw rules for k3s

# install without traefik (so I can bring my own)
curl -sfL https://get.k3s.io | sh -s - --disable traefik


### MetalLB
# consider trying to use this instead of ServiceLB
# https://metallb.universe.tf/configuration/


### install Traefik CRDs
# https://doc.traefik.io/traefik/user-guides/crd-acme/#ingressroute-definition


### hellpot
docker save -o hellpot-latest.tar hellpot:latest
sudo k3s ctr images import hellpot-latest.tar
sudo k3s ctr images ls | grep hellpot
