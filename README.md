1. Install k3s (Lightweight Kubernetes)
# Run as root or via sudo
curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="--disable traefik" sh -

# Export kubeconfig for non-root
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# Create the database namespace
kubectl create namespace db

# Add Bitnami Helm repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Install MySQL using Helm
helm install mysql-cluster bitnami/mysql \
  --namespace db -f mysql-values.yaml

# Verify the deployment
kubectl -n db get pods
kubectl -n db get pvc

# Check replication status
kubectl exec -n db mysql-cluster-secondary-0 -- \
  mysql -uroot -pmy-secret-root-pw -e "SHOW SLAVE STATUS\G"
# Log in to Docker Hub
docker login

# Build and push the Docker image
cd api
docker build -t <your-dockerhub-username>/ip-logger:latest .
docker push <your-dockerhub-username>/ip-logger:latest

# Deploy to Kubernetes
cd ../k8s-manifests/web
kubectl create namespace web
kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml# Send a POST request to the API
curl -X POST http://<EC2_PUBLIC_IP>:30080/log-ip

# Expected response
{"status":"ok","ip":"<YOUR_IP>"}

# Verify the deployment
kubectl -n web get pods,svc
# Send a POST request to the API
curl -X POST http://<EC2_PUBLIC_IP>:30080/log-ip

# Expected response
{"status":"ok","ip":"<YOUR_IP>"}

