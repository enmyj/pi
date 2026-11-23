#!/usr/bin/env bash
set -euo pipefail

# Generates a least-privilege base64-encoded kubeconfig for GitHub Actions
# (ServiceAccount default/imdc-deployer) targeting this Pi over Tailscale.

TS_IP="$(tailscale ip -4 | head -n1)"
CA_B64="$(kubectl -n default get secret imdc-deployer-token -o jsonpath='{.data.ca\.crt}')"
TOKEN="$(kubectl -n default get secret imdc-deployer-token -o jsonpath='{.data.token}' | base64 -d)"

cat <<EOF | base64 -w 0
apiVersion: v1
kind: Config
clusters:
- name: pi
  cluster:
    certificate-authority-data: ${CA_B64}
    server: https://${TS_IP}:6443
    tls-server-name: raspberrypi
contexts:
- name: deploy
  context:
    cluster: pi
    namespace: default
    user: imdc-deployer
current-context: deploy
users:
- name: imdc-deployer
  user:
    token: ${TOKEN}
EOF
echo
