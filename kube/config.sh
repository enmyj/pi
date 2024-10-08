# install Traefik CRDs
# https://doc.traefik.io/traefik/user-guides/crd-acme/#ingressroute-definition

# hellpot
docker save -o hellpot-latest.tar hellpot:latest
sudo k3s ctr images import hellpot-latest.tar
sudo k3s ctr images ls | grep hellpot