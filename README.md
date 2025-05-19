1. Install k3s (Lightweight Kubernetes)
# Run as root or via sudo
curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="--disable traefik" sh -

# Export kubeconfig for non-root
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

2. Deploy MySQL Cluster (Helm)
   *Create namespace
kubectl create namespace db
***Prepare *mysql-values.****************************yaml**** (already in repo)
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install mysql-cluster bitnami/mysql \
  --namespace db -f mysql-values.yaml
