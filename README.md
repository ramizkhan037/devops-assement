1. Install k3s (Lightweight Kubernetes)
   curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="--disable traefik" sh -
# Run as root or via sudo
chmod +x install-k3s.sh
docker pull bitnami/mysql:9.3.0-debian-12-r0  # optional cache
sudo ./install-k3s.sh

# Export kubeconfig for non-root
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
