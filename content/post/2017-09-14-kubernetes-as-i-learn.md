---
title: Kubernetes - As I Learn
date: 2017-09-14T00:00:00Z
url: 2017/09/14/Kubernetes_-_As_I_Learn/
categories:
- kubernetes
- infrastructure
- docker
- containers
- cloud
---

I'm currently working on supporting a JupyterHub installation for a series of online courses that we are launching at SAGE. Along the way I've had to get my head around deploying the software using kubernetes. This is a stack that I've been aware of for quite a while, but I've not worked with it before. In order to help with debugging my installation I'm writing up a guide on some of the kubernetes commands that I found useful when deploying a service onto google cloud.

### How do we get our container onto our cluster?

We might visualise it something like this:

1. create a docker container, or docker file describing how to create a docker instance of the software

```
                  "---------------"
  JupyterHub -->  | docker image  |
                  "---------------"
```

2. Create a set of instructions for how to load this using Kubenrentes (this set of instructions is called a chart). The chart will contain a metadata description of the software we want to install as well as configuration options for the cluster.


3. tell helm where this chart is

```
    "---------------"                             //-------//
    | docker image |  <--- (referenced by) ----  // chart //----> (cluster config)
    "--------------"                            //-------//
                                            /
                                           /
    "-------------------"                 /
    | other containers  |  <--- (referenced by)
    "-------------------"

```

4. helm uses the chart to instruct Kubernetes on how to configure the cluster

```
    //-------//
   // chart //  --(helm)--> Kubernetes --> { Cluster }
  //-------//
```

### What is [Kubernetes](http://kubernetes.io/)?

The Kubernetes homepage provides a great definition

>
  Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

It does all of the heavy lifting of deployment, security, networking, monitoring and more. It has some core concepts that are useful to have ready to hand. The three useful to me in getting up to speed were:

- `nodes` - a worker machine, can be physical or virtual. In AWS land this might be an EC2 instance. Some systems call these minions. Where you have a collection of nodes I believe one of them will act as the master node. I'm assuming that in the event of the master node dying, the cluster will re-assign master status to some other node in the cluster, but I'm not sure about this.
- `pods` This is a group of one or more containers. At the simplest level if you are deploying only one container, that will comprise a pod, but you might have an architecture of connected containers and volumes, and these will be abstracted to the pod level in Kubernetes land. Pods are specific, running on nodes, and they can fall over and die. This is where the next level of abstraction comes in
- `services` are abstract descriptions which define sets of pods. Kubernetes should take care to keep your service running but spinning up new pods to provide the work of the service if the existing pod falls over. Other abstractions in the cluster are also described as services, in particular how we manage access in to the cluster via ingress files.

### Creating a cluster

OK, let's have a look at what happens when we create a Kubernetes cluster on google cloud using their command line utilities.

```
$ gcloud container clusters create test-us \
    --num-nodes=2 \
    --machine-type=n1-standard-2 \
    --zone=us-central1-b

...
Creating cluster test-us...done.
Created [url to your gloud cluster dashboard].
kubeconfig entry generated for test-us.
NAME     ZONE           MASTER_VERSION  MASTER_IP        MACHINE_TYPE   NODE_VERSION  NUM_NODES  STATUS
test-us  us-central1-b  1.6.7           104.198.164.219  n1-standard-2  1.6.7         2          RUNNING
```

This will have created your cluster on glcoud, but it also sets a local config file `~/kube/config`. This local config file will be used by helm to figure out where to send your software. It will contain a bunch of useful info about your cluster.

```
$ grep "cluster" .kube/config
clusters:
- cluster:
   cluster: gke_sage-campus-hub_us-central1-b_test-us
```

Let's spin up another cluster in another zone. We can see the list of available zones with the following command

`
  $ gcloud compute zones list
`

Ok, let's spin one up in the EU

```
$ gcloud container clusters create test-eu \
                             --num-nodes=2 \
                             --machine-type=n1-standard-2 \
                             --zone=europe-west2-a
Creating cluster test-eu...done.
Created [url to cluster].
kubeconfig entry generated for test-eu.
NAME     ZONE            MASTER_VERSION  MASTER_IP       MACHINE_TYPE   NODE_VERSION  NUM_NODES  STATUS
test-eu  europe-west2-a  1.6.7           35.197.192.188  n1-standard-2  1.6.7         2          RUNNING

```

Now let's check that config kube file again.

```
$ grep "cluster" .kube/config
clusters:
- cluster:
- cluster:
    cluster: gke_sage-campus-hub_us-central1-b_test-us
    cluster: gke_sage-campus-hub_europe-west2-a_test-eu
```

and we see it now contains info about the two clusters that we have spun up.

### Checking in on your clusters

You can explore the status of a cluster in three ways:

- via the gloud console
- via the `kubectl` command line utility
- via the kubernetes dashboard

##### Using the google cloud dashboard

I've chosen to do this tutorial through google cloud mostly as this is the service that is described in the zero to hub tutorial. You should equally be able to use helm and Kubernetes to deploy into other platforms too, but as we are using google's cloud platform we can also look at some status about our cluster through their online dashboard.

https://console.cloud.google.com/compute/instances will show you your VM instances. These are the nodes in the cluster.

Your platform account comes with some quotas. I ran into an issue with Kubernetes failing to deploy a cluster once as I'd run out of quota on memory. You can check on your quotas from this page:

https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com

We have deployed two kuberentes clusters, and the cluster level can be seen from this page: https://console.cloud.google.com/kubernetes/list. You can drill down from here to look at details of a given cluster, or look at the workloads you have deployed across you cluster, amongst other aspects of the cluster, such as config and storage options.

##### Using the command line

The go to way of checking on your cluster is the `[kubectl](https://kubernetes.io/docs/user-guide/kubectl-overview/)` command line utility.

```
$ kubectl get nodes                                         10:15:18
NAME                                     STATUS    AGE       VERSION
gke-test-eu-default-pool-a3ebba15-38l0   Ready     17h       v1.6.7
gke-test-eu-default-pool-a3ebba15-mch6   Ready     17h       v1.6.7
```
This pulled up the nodes from the last cluster that we configured. To see the nodes from the first cluster we need to switch the context that `kubectl` is working under. We saw the cluster names earlier, and we can use those to change the context.

```
$ kubectl config use-context gke_sage-campus-hub_us-central1-b_test-us
$ kubectl  get nodes
NAME                                     STATUS    AGE       VERSION
gke-test-us-default-pool-1ee9e215-g8dm   Ready     18h       v1.6.7
gke-test-us-default-pool-1ee9e215-xtx2   Ready     18h       v1.6.7
```

Great!

Now let's look at the pods that are running on this cluster.

```
$ kubectl --namespace=test-us get pods
No resources found.
```

So, we have no actually deployed any software yet to this cluster. Let's deploy some software. For this we will use `helm`

# What is Helm?

As mentioned before helm is the package manager for kubernetes. It uses collections of instructions called charts to coordinate finding or configuring docker containers, along with all of the other cluster config options, such as load balancing and storage options.

We need to init for each cluster, so we need to

```
helm init                                                                               10:41:22
$HELM_HOME has been configured at /Users/ianm/.helm.

Tiller (the helm server side component) has been installed into your Kubernetes Cluster.
Happy Helming!
```

Helm uses the kubeconfig context to decide where to install Tiller.

There are  a bunch of stable chart files for deploying a range of software available at [this repo](https://github.com/kubernetes/charts/tree/master/stable).

Let's install redis!

```
$ helm install stable/redis
```

And we can now have a look at our pods via

```
$ kubectl get pods
NAME                                         READY     STATUS    RESTARTS   AGE
jumpy-shrimp-redis-2361047644-9f5xv          1/1       Running   0          1m
jumpy-shrimp-redis-client-2779061195-xjww7   1/1       Running   0          41s
```

There are some other `kubectl` commands that will come in handy at this point.

`
$ kubectl describe --all-namespaces=true pvc
`

`
$ kubectl describe pod jumpy-shrimp-redis-client-2779061195-xjww7
`

There are a lot of other commands for interrogating the status of the cluster, pods and services.


##### Using the Kubernetes dashboard

Kuberetes probably comes with a dashboard installed, out of the box.

So far we have been looking at the pods related to redis, but there are a bunch of other pods that get installed by default. You can have a look at them with:

```
$ kubectl get pods --all-namespaces
NAMESPACE     NAME                                                READY     STATUS    RESTARTS   AGE
default       jumpy-shrimp-redis-2361047644-9f5xv                 1/1       Running   0          10m
default       jumpy-shrimp-redis-client-2779061195-xjww7          1/1       Running   0          9m
kube-system   fluentd-gcp-v2.0-40712                              2/2       Running   0          18h
kube-system   fluentd-gcp-v2.0-7zb2z                              2/2       Running   0          18h
kube-system   heapster-v1.3.0-4004699650-z3bpj                    2/2       Running   0          18h
kube-system   kube-dns-3664836949-lrhnv                           3/3       Running   0          18h
kube-system   kube-dns-3664836949-nqp86                           3/3       Running   0          18h
kube-system   kube-dns-autoscaler-2667913178-v20s6                1/1       Running   0          18h
kube-system   kube-proxy-gke-test-us-default-pool-1ee9e215-g8dm   1/1       Running   0          18h
kube-system   kube-proxy-gke-test-us-default-pool-1ee9e215-xtx2   1/1       Running   0          18h
kube-system   kubernetes-dashboard-2917854236-q874c               1/1       Running   0          18h
kube-system   l7-default-backend-1044750973-wt3xn                 1/1       Running   0          18h
kube-system   tiller-deploy-3703072393-2f90d                      1/1       Running   0          13m
```

We can access the dashboard via

```
$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```

Navigate to [http://127.0.0.1:8001/ui]() and you will see a nice dashboard with info on the cluster.

### Tearing down what we have built.

OK, let's get rid of the cluster that is running redis.

```
gcloud container clusters delete test-eu --zone=europe-west2-a                   11:08:35
The following clusters will be deleted.
 - [test-eu] in [europe-west2-a]

Do you want to continue (Y/n)?  Y
```


### How do we deploy our own local software?

So far in this guide we have looked at deploying a docker conatiner for redis that is alredy in the helm registry. How do you deploy your own software that you have built locally? You need to dockerise it. There is a tool called Draft that lets you get started with that, but I've not tried it out. You can have a look at a guide here:

[http://blog.kubernetes.io/2017/05/draft-kubernetes-container-development.html]()

### Cheatsheet

There is a nice cheat sheet here:
https://kubernetes.io/docs/user-guide/kubectl-cheatsheet/

### Other commands I have found useful

There are a bunch of other commands that I found useful, but didn't get the time to writeup here.

```bash
kubectl config current-context  
kubectl describe --namespace=hub-no-auth pod hub-deployment-3311999561-w53zz  
kubectl --namespace=jupyterhub-noauth get svc proxy-public  
kubectl get nodes --show-labels  
kubectl --namespace=jupyterhub-test edit deployment  
kubectl --namespace=jupyterhub-test describe all  
kubectl --namespace=jupyterhub-test describe  
kubectl --namespace=jupyterhub-test get values  
kubectl get pods -l purpose=demonstrate-envars  
kubectl get pods -l  
kubectl --namespace=testhub exec -it hub-deployment-1369850868-c4bv6  /bin/bash  
kubectl --namespace=testhub get pod -o yaml | grep "image"  
kubectl --namespace=testhub delete deployment hub-deployment
helm list  
kubectl --namespace=testhub get pod -o yaml | grep "hub"
```  
