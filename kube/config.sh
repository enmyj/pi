## Install k3s
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --disable servicelb" sh -

# copy the k3s config file so I don't hav to sudo kubectl
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown imyjer:imyjer ~/.kube/config
chmod 600 ~/.kube/config
echo 'export KUBECONFIG=~/.kube/config' >> ~/.bashrc
source ~/.bashrc


## install Helm
# https://helm.sh/docs/intro/install/#from-apt-debianubuntu

## Setup cloudflare tunnel
# https://developers.cloudflare.com/cloudflare-one/tutorials/many-cfd-one-tunnel/
cloudflared tunnel create raspberrypi
kubectl create secret generic tunnel-credentials \
    --from-file=credentials.json=/path/to-credentials-file.json
cloudflared tunnel route dns raspberrypi dev.ianmyjer.com


# install metallb
# also enable "promiscious" mode on wifi interface
# https://metallb.universe.tf/troubleshooting/#using-wifi-and-cant-reach-the-service
helm repo add metallb https://metallb.github.io/metallb
helm install metallb metallb/metallb -n metallb-system --create-namespace
kubectl apply -f metal.yaml


## install traefik with helm
# https://github.com/traefik/traefik-helm-chart/tree/master?tab=readme-ov-file
# might be nice to use this instead:
# https://docs.k3s.io/helm#using-the-helm-controller
# If not installed via helm, need to install Traefik CRDs
# https://doc.traefik.io/traefik/user-guides/crd-acme/#ingressroute-definition
helm repo add traefik https://traefik.github.io/charts
helm install traefik traefik/traefik


## hellpot
docker build XXX
docker save -o hellpot-latest.tar hellpot:latest
sudo k3s ctr images import hellpot-latest.tar
sudo k3s ctr images ls | grep hellpot


## Pihole
helm repo add mojo2600 https://mojo2600.github.io/pihole-kubernetes/
helm repo update
kubectl create secret generic pihole-admin-secret --from-literal=password='your_password_here'
helm install pihole-2.26.1 mojo2600/pihole -f kube/charts/pihole-values.yaml