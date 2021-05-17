# k8s-devs-and-ops
Repository for `k8s for developers and operators` workshop in GKE. 

Below are some of the various `gcloud` commands that are required throughout the workshop.

### Create GKE Cluster
```
gcloud beta container clusters create "lab" \
  --zone "us-central1-a" \
  --machine-type "n1-standard-1" \
  --num-nodes "3" \
  --enable-autoprovisioning --min-cpu 1 --max-cpu 15 \
  --min-memory 1 --max-memory 100
```

### Add a GKE Node Pool
```
$ gcloud beta container node-pools create "pool-2" \
  --cluster "lab" \
  --zone "us-central1-a" \
  --machine-type "n1-standard-1" \
  --num-nodes "1" \
  --enable-autoscaling --min-nodes 1 --max-nodes 3 \
  --node-labels node-preference=preferred
```
### Add a GKE Maintenance Exclusion

```
$ export MAINTENANCE_EXCLUSION_START=$(date)
```
```
$ gcloud container clusters update "lab" \
  --zone "us-central1-a" \
  --add-maintenance-exclusion-name "maintenance-exclusion-demo" \
  --add-maintenance-exclusion-start "$MAINTENANCE_EXCLUSION_START" \
  --add-maintenance-exclusion-end "+pt5m"
```
### Configure GKE Surge Upgrades
```
$ gcloud beta container node-pools update "default-pool" \
  --cluster="lab" \
  --max-surge-upgrade=2 --max-unavailable-upgrade=2
```
### Cleanup GKE Cluster
```
$ gcloud container clusters delete "lab" \
  --zone "us-central1-a"
```
### Create GKE Autopilot Cluster
```
$ gcloud container clusters create-auto "lab-autopilot" \
    --region us-west1 \
```

