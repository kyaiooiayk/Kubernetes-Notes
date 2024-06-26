# Kubernetes
***

## Introduction
- Kubernetes is also known as k8s.
- It's an Infrastructure as a Code (IaaC) framework, which means that everything is an API call whether it’s scaling containers or provisioning a load balancer
- It is meant to run across a cluster environment. 
- Kubernetes is a **container orchestration** platform used to manage containerised applications. 
- It used to automate important parts of the container management process such as container replication, scaling, monitoring and scheduling. It’s an open-source platform written in Google’s Go programming language. 
- How do you coordinate and schedule several containers? How do all of the different containers in your app talk to each other? How do you scale several container instances? This is where Kubernetes can help. 
- It contains all the parts and glue to form a resilient and reliable way of running services, including things like load balancers, resource quotas, scaling policies, traffic management, sharing secrets, and more. 
***

## Kubernetes vs. Docker
 - While Docker provides an open standard (consistent state across different servers or cloud environments) for packaging and distributing containerised apps, the potential complexities can add up fast. 
- Simplistically kubernetes is more extensive than Docker. In another words, kubernetes helps orchastrates several dockers.
***

## Kubernetes vs. on-the-cloud hardwares
- K8s provides the software to deploy your app on cloud services provided such as AWS, Google and Microsoft.
- In paticulat these are k8s services platforms:
  - Elastic Kubernetes Service (EKS) by AWS
  - Azure Kubernetes Service (AKS) by Microsoft
  - Google Kubernetes Engine (GKE) by Google
***

## Use Kubernetes with Docker
In short, use Kubernetes with Docker to:
  - Make your infrastructure more robust and your app more highly available. Your app will remain online, even if some of the nodes go offline.
  - Make your application more scalable. If your app starts to get a lot more load and you need to scale out to be able to provide a better user experience, it’s simple to spin up more containers or add more nodes to your Kubernetes cluster.
***

## Kubernetes nomenclature
Kubernetes calls everything with different names. 

| Without Kubernetes      | With Kubernetes  |
|-------------------------|------------------|
| Containers              | Pod              |
| Internal Load Balancer  | Service          |
| External Load Balancer  | Ingress          |
| Application             | Deployment       |
| Physical Machine        | Node             |
| Cluster of Machines     | Cluster          |
| Virtual Cluster         | Namespace        |
***

## How to emulate a real cluster on your local laptop
- Why woukd you want to do it? Either for testing without paying for expensive on-the-cloud resorces or because your local machine is good enough.
- Keep in mind that deploying the k8s on a local machine will Not ensure that the ML application is accessible to the end-user irrespective of geographic location.  
- Solutions that can be used to run Kubernetes on your local machine (local Kubernetes development environment):
  - [minikube](https://minikube.sigs.k8s.io/docs/)
  - [kind](https://kind.sigs.k8s.io/)
  - [k3s](https://k3s.io/) 
- If you are working in an environment with a tight resource pool or need an even quicker startup time, K3s has the shortest start-up time and smaller memory foot print.
***

## Kubeflow
- Kubeflow is a Kubernetes toolkit developed specifically for machine learning. 
- It provides streamlined access to machine learning pipeline orchestration tools, as well as popular machine learning frameworks and components.
- Its aim is to deliver an E2E platform for the entire machine learning lifecycle. It covers the training, production, and deployment, instead of just one element of the machine learning lifecycle.
- Kubeflow introduces machine learning specific management of the model, framework and storage, whilst Kubernetes deals with the container management.
***

## Kubernetes nomenclature
- **Cluster** is a set of physical machines that contains a central node controlling the Kubernetes API server and many worker nodes.
- **Node** is a single machine (either a physical machine or a virtual machine) within a cluster.
- **Pod** is a group of containers that run together on the same node. Often, a pod only contains a single container.
- **kubelet** is the Kubernetes agent that manages communication with the central node on each worker node.
- **Service** is a group of pods and the policies to access them.
- **Volume** is a storage space shared by all containers in the same pod. 
- `kubectl` is the CLI for Kubernetes.
***

## Available tutorials
- [How to deploy a simple NLP model with Flask, Docker and minikube](https://github.com/kyaiooiayk/Kubernetes-Notes/tree/main/tutorials/NLP_Flask_Docker_minikube)
***

## References
- Pointer, Ian. Programming PyTorch for Deep Learning: Creating and Deploying Deep Learning Applications. " O'Reilly Media, Inc.", 2019.
- https://azure.microsoft.com/en‐gb/topic/kubernetes‐vs‐docker/
- [Deploying ML Models Using Kubernetes on your local machine](https://www.analyticsvidhya.com/blog/2022/01/deploying-ml-models-using-kubernetes/)
- [A Guide to Deploying Machine Learning Models on Kubernetes](https://www.seldon.io/deploying-machine-learning-models-on-kubernetes)
- [Minikube vs. kind vs. k3s - What should I use?](https://shipit.dev/posts/minikube-vs-kind-vs-k3s.html)
- [Introduction to Microservices, Docker, and Kubernetes](https://www.youtube.com/watch?v=1xo-0gCVhTU)
- Hapke, Hannes, and Catherine Nelson. Building machine learning pipelines. O'Reilly Media, 2020.
- [Introduction to Kubernetes with Google Cloud: Deploy your Deep Learning model effortlessly](https://theaisummer.com/kubernetes/)
***
