# Kubernetes Roadmap

## Adding And Managing Worker Nodes

# Managing Worker Nodes

Kubernetes runs your workload by placing containers into Pods to run on Nodes. A node may be a virtual or physical machine, depending on the cluster. Each node is managed by the control plane and contains the services necessary to run Pods.

Visit the following resources to learn more:

- [@official@Node Management](https://kubernetes.io/docs/concepts/architecture/nodes/#management)
- [@video@Kubernetes 101: Nodes Tutorial](https://www.youtube.com/watch?v=xhwi3zIVR-8)

## Advanced Topics

# Advanced Kubernetes Topics

Advanced Kubernetes concepts cover production-grade techniques for DevOps, Docker, and backend development. These include GitOps deployments, container optimization, stateful workloads management, secure cloud-native applications and service scalable implementations.

Visit the following resources to learn more:

- [@official@Kubernetes Production Best Practices](https://kubernetes.io/docs/setup/production-environment/)
- [@article@Top Kubernetes design patterns](https://www.wallarm.com/what/top-kubernetes-design-patterns)
- [@article@The Role of Kubernetes in DevOps](https://spacelift.io/blog/kubernetes-devops)
- [@video@Kubernetes for Docker Users](https://www.youtube.com/watch?v=keNQ6V_W4VE&ab_channel=Rancher)

## Assigning Quotas To Namespaces

# Assigning Quotas to Namespaces

Assigning quotas to namespaces is a way to limit resource usage for specific groups of resources in Kubernetes. Quotas can be set for CPU, memory, and other resources, as well as for the number of objects in a namespace. This can help ensure fair resource distribution across different teams or projects within a cluster. Quotas can be applied to individual namespaces or across the entire cluster. Kubernetes allows for both hard quotas, which enforce strict resource limits, and soft quotas, which allow for overages up to a certain point. Quotas can be managed using the Kubernetes API or through YAML configuration files.

Visit the following resources to learn more:

- [@official@Resource Quotas - Documentation](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [@article@Leveraging Namespaces for Cost Optimization with Kubernetes](https://thenewstack.io/leveraging-namespaces-for-cost-optimization-with-kubernetes/)
- [@video@Kubernetes Namespaces Explained in 15 mins](https://www.youtube.com/watch?v=K3jNo4z5Jx8)

## Autoscaling

# Autoscaling

Autoscaling in Kubernetes involves adjusting the resources allocated to a deployment or set of pods based on demand. It includes Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA), which increase or decrease replicas or adjust resource requests and limits, respectively. Autoscaling can be used with Cluster Autoscaling to efficiently allocate resources and ensure application responsiveness. It's useful for handling variable workloads or sudden spikes in traffic.

Visit the following resources to learn more:

- [@official@Autoscaling in Kubernetes](https://kubernetes.io/blog/2016/07/autoscaling-in-kubernetes/)
- [@video@Kubernetes cluster autoscaling for beginners](https://www.youtube.com/watch?v=jM36M39MA3I)

## Basics

# Scheduling Basics

Scheduling involves assigning pods to worker nodes based on criteria such as resource availability, labels, affinity/anti-affinity rules, taints, and tolerations. Pods are the smallest deployable units in k8s, consisting of one or more containers that share the same network namespace. The scheduler is responsible for assigning pods to nodes, while labels are used for matching. Affinity and anti-affinity rules dictate how pods are scheduled based on their relationships with other pods or nodes. QoS is used to prioritize pod scheduling based on their resource requirements.

Visit the following resources to learn more:

- [@official@Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [@video@How Scheduling in Kubernetes Works](https://www.youtube.com/watch?v=0FvQR-0tK54)

## Blue Green Deployments

# Blue Green Deployments

It is a deployment strategy used in Kubernetes for deploying new versions of an application by running two identical production environments, one with the current version (blue) and the other with the new version (green). After the green environment is fully tested, traffic is routed from the blue environment to the green environment, providing a seamless transition for users and avoiding any downtime or disruption. In Kubernetes, Blue-Green Deployments can be implemented using a variety of tools and techniques, including deployment strategies, traffic routing, and load balancing.

Visit the following resources to learn more:

- [@article@Create a Kubernetes Blue Green Deployment](https://developer.harness.io/docs/continuous-delivery/cd-execution/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [@video@Kubernetes - Blue/Green Deployments](https://www.youtube.com/watch?v=jxhpTGQ484Y)

## Canary Deployments

# Canary Deployments

Canary Deployments is a technique used in Kubernetes to gradually roll out new versions of an application by directing a small percentage of users or traffic to the new version while the majority continue using the old version. This approach allows for testing the new version under real-world conditions before fully committing to the update. In Kubernetes, canary deployments can be implemented using tools such as Istio, Linkerd, or Nginx, or by using built-in features like deployment strategies and traffic routing.

Visit the following resources to learn more:

- [@article@Canary deployment for K8s deployments](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml)
- [@video@Kubernetes canary deployments Explained](https://www.youtube.com/watch?v=sCevTD_GtvU)

## Choosing A Managed Provider

# Choosing a Managed Provider

A managed provider is a cloud-based service that provides a managed Kubernetes environment. This means that the provider handles the underlying infrastructure, such as servers, storage, and networking, as well as the installation, configuration, and maintenance of the Kubernetes cluster.

When choosing a managed Kubernetes provider, consider the cloud provider you are using, features and capabilities, pricing and billing, support, security and compliance, and the provider's reputation and reviews. By taking these factors into account, you can select a provider that meets your needs and offers the best value for your organization.

Visit the following resources to learn more:

- [@article@Choosing a Managed Kubernetes Provider](https://containerjournal.com/features/choosing-a-managed-kubernetes-provider/)
- [@article@Amazon Web Services Gears Elastic Kubernetes Service for Batch Work](https://thenewstack.io/amazon-web-services-gears-elastic-kubernetes-service-for-batch-jobs/)
- [@article@How to Build The Right Platform for Kubernetes](https://thenewstack.io/kubernetes/kubernetes-infrastructure-architecture/)

## Ci  Cd Integration

# CI/CD Integration

In CI/CD pattern, the build, test, and deployment of applications to Kubernetes are fully automated. The CI pipeline creates the container image, runs tests, and pushes it to a registry. The CD pipeline then updates Kubernetes manifests or Helm charts and applies them to the cluster using tools like Octopus Deploy, Argo CD, Flux, or kubectl. This makes deployments consistent, repeatable, and fast.

Visit the following resources to learn more:

- [@article@Kubernetes CI/CD Pipelines – 8 Best Practices and Tools](https://spacelift.io/blog/kubernetes-ci-cd)
- [@article@8 Kubernetes CI/CD tools every developer should know](https://octopus.com/devops/kubernetes-deployments/kubernetes-ci-cd-tools-for-developers/)
- [@article@Deploy to Kubernetes with Octopus Deploy](https://octopus.com/use-case/kubernetes?utm_source=roadmap&utm_medium=link&utm_campaign=kubernetes-ci-cd-integration)

## Cluster Autoscaling

# Autoscaling

Autoscaling in Kubernetes involves adjusting the resources allocated to a deployment or set of pods based on demand. It includes Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA), which increase or decrease replicas or adjust resource requests and limits, respectively. Autoscaling can be used with Cluster Autoscaling to efficiently allocate resources and ensure application responsiveness. It's useful for handling variable workloads or sudden spikes in traffic.

Visit the following resources to learn more:

- [@official@Autoscaling in Kubernetes](https://kubernetes.io/blog/2016/07/autoscaling-in-kubernetes/)
- [@video@Kubernetes cluster autoscaling for beginners](https://www.youtube.com/watch?v=jM36M39MA3I)

## Configuration Management

# Secrets

Kubernetes secrets store sensitive data such as passwords, tokens, and API keys in a secure manner. They can be created manually or automatically, and stored in etcd. Secrets can be mounted as files or environment variables in a pod, and access can be managed using Kubernetes RBAC. However, they have some limitations, such as size and the inability to be updated once created. Understanding secrets is important for building secure applications in Kubernetes.

Visit the following resources to learn more:

- [@official@Documentation - Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [@article@Kubernetes Secrets Management: 3 Approaches, 9 Best Practices](https://thenewstack.io/kubernetes-secrets-management-3-approaches-9-best-practices/)
- [@video@Kubernetes Secrets in 5 Minutes!](https://www.youtube.com/watch?v=cQAEK9PBY8U)

## Container And Pod Security

# Container and Pod Security

Kubernetes (k8s) can secure containers and pods through measures like using trusted container images, limiting container privileges, enforcing pod-level security policies, implementing network security measures, using access controls with RBAC, and managing sensitive information with Secrets and ConfigMaps. These practices help organizations reduce the risk of security incidents in their k8s clusters.

Visit the following resources to learn more:

- [@official@Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [@article@Tutorial: Create a Kubernetes Pod Security Policy](https://thenewstack.io/tutorial-create-a-kubernetes-pod-security-policy/)
- [@article@6 Overlooked Yet Important Kubernetes Features to Secure](https://thenewstack.io/6-overlooked-yet-important-kubernetes-features-to-secure/)
- [@video@Kubernetes Security - Security Context for a Pod or Container](https://www.youtube.com/watch?v=i8wfvoVf2xs)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Container And Pod Security

# Container and Pod Security

Kubernetes (k8s) can secure containers and pods through measures like using trusted container images, limiting container privileges, enforcing pod-level security policies, implementing network security measures, using access controls with RBAC, and managing sensitive information with Secrets and ConfigMaps. These practices help organizations reduce the risk of security incidents in their k8s clusters.

Visit the following resources to learn more:

- [@official@Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [@article@Tutorial: Create a Kubernetes Pod Security Policy](https://thenewstack.io/tutorial-create-a-kubernetes-pod-security-policy/)
- [@article@6 Overlooked Yet Important Kubernetes Features to Secure](https://thenewstack.io/6-overlooked-yet-important-kubernetes-features-to-secure/)
- [@video@Kubernetes Security - Security Context for a Pod or Container](https://www.youtube.com/watch?v=i8wfvoVf2xs)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Containers

# Containers

Kubernetes is built on containers, so before learning Kubernetes you should be comfortable running and building containers from scratch.

Visit the following resources to learn more:

- [@article@Official Docker Tutorial](https://www.docker.com/101-tutorial/)
- [@article@Docker Curriculum](https://docker-curriculum.com/)
- [@video@Docker in 100 Seconds (video)](https://www.youtube.com/watch?v=Gjnup-PuquQ)
- [@video@Free 3 Hour Video Course on Docker for Beginners](https://www.youtube.com/watch?v=3c-iBn73dDE)
- [@feed@Explore top posts about Containers](https://app.daily.dev/tags/containers?ref=roadmapsh)

## Creating Custom Controllers

# Custom Controllers

Custom controllers in Kubernetes automate the management of custom resources that are not natively supported by Kubernetes. They are implemented as Kubernetes controllers that watch custom resources and react to changes in their state. Custom resources are created by extending the Kubernetes API with new resource types specific to an organization's needs. Custom controllers can be developed using various programming languages and frameworks, such as the Operator Framework. The Operator Framework provides tools and best practices for developing, testing, and deploying custom controllers.

Visit the following resources to learn more:

- [@official@Custom Controllers](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-controllers)
- [@video@Extending Kubernetes with Custom Controllers](https://www.youtube.com/results?search_query=Custom+controllers+in+k8s)

## Csi Drivers

# CSI drivers

CSI (Container Storage Interface) drivers in Kubernetes provide a standard way for storage providers to integrate with Kubernetes and offer persistent storage for containerized applications. They operate as separate containerized processes and communicate with Kubernetes through a well-defined API. CSI drivers allow Kubernetes to access a wide range of storage systems and provide advanced features like snapshotting and cloning.

Visit the following resources to learn more:

- [@official@Container Storage Interface (CSI) for Kubernetes](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
- [@official@Kubernetes CSI Developer Documentation](https://kubernetes-csi.github.io/docs/)

## Custom Resource Definitions Crds

# Custom Resource Definitions

Custom Resource Definitions (CRDs) in Kubernetes extend the Kubernetes API by defining new resource types specific to an organization's needs. CRDs create custom resources that can manage a wide variety of resources, such as applications, databases, storage, and networking. They are defined using YAML or JSON manifests and can be created and managed using the Kubernetes API server. Once created, custom resources can be managed using Kubernetes controllers and integrated with other Kubernetes components. CRDs are a powerful tool for streamlining operations in Kubernetes and enabling organizations to manage resources in a more efficient and customized way.

Visit the following resources to learn more:

- [@official@Custom Resources - Documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [@video@Custom Resource Definition (CRD) Explained with Demo](https://www.youtube.com/watch?v=u1X5Rf7fWwM)

## Custom Schedulers And Extenders

# Custom Schedulers Extenders

Custom Scheduler Extenders in Kubernetes enhance the scheduling capabilities of Kubernetes by allowing users to define their own scheduling logic based on custom metrics and constraints. They are implemented as custom Kubernetes controllers that run alongside the Kubernetes scheduler. Custom Scheduler Extenders can be used to implement scheduling policies specific to an organization's needs and can be developed using various programming languages. They intercept scheduling requests, add custom scheduling logic based on user-defined rules, and pass requests back to the Kubernetes scheduler.

Visit the following resources to learn more:

- [@article@Create a custom Kubernetes scheduler](https://developer.ibm.com/articles/creating-a-custom-kube-scheduler/)
- [@video@Custom Scheduler Kubernetes | Multiple Schedulers Kubernetes](https://www.youtube.com/watch?v=NiB7sjXmiZc)

## Deploying Your First Application

# Deploying your First Application

To deploy your first application in Kubernetes, you need to create a deployment and service manifest in YAML files, apply the manifests to your Kubernetes cluster using the kubectl apply command, verify that your application's pods are running with kubectl get pods, and test the service with kubectl get services and accessing the service using a web browser or a tool like cURL. There are also various tools and platforms available that can simplify application deployment in Kubernetes, such as Helm charts and Kubernetes operators.

Visit the following resources to learn more:

- [@course@Kubernetes Deployment Hands-on Lab](https://kodekloud.com/studio/labs/kubernetes/deployments-stable)
- [@official@Using kubectl to Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
- [@article@Deploying An Application On Kubernetes From A to Z](https://web.archive.org/web/20230326150953/https://www.weave.works/blog/deploying-an-application-on-kubernetes-from-a-to-z)
- [@article@Kubernetes 101: Deploy Your First Application with MicroK8s](https://thenewstack.io/kubernetes-101-deploy-your-first-application-with-microk8s/)
- [@video@Kubernetes Tutorial | Your First Kubernetes Application](https://www.youtube.com/watch?v=Vj6EFnav5Mg)
- [@video@Kubernetes 101: Deploying Your First Application](https://www.youtube.com/watch?v=XltFOyGanYE)

## Deployment Patterns

# Blue Green Deployments

It is a deployment strategy used in Kubernetes for deploying new versions of an application by running two identical production environments, one with the current version (blue) and the other with the new version (green). After the green environment is fully tested, traffic is routed from the blue environment to the green environment, providing a seamless transition for users and avoiding any downtime or disruption. In Kubernetes, Blue-Green Deployments can be implemented using a variety of tools and techniques, including deployment strategies, traffic routing, and load balancing.

Visit the following resources to learn more:

- [@article@Create a Kubernetes Blue Green Deployment](https://developer.harness.io/docs/continuous-delivery/cd-execution/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [@video@Kubernetes - Blue/Green Deployments](https://www.youtube.com/watch?v=jxhpTGQ484Y)

## Deployments

# Deployments

A Deployment is a resource object for managing Pods and ReplicaSets via a declarative configuration, which define a desired state that describes the application workload life cycle, number of pods, deployment strategies, container images, and more. The Deployment Controller works to ensure the actual state matches desired state, such as by replacing a failed pod. Out of the box, Deployments support several deployment strategies, like "recreate" and "rolling update", however can be customized to support more advanced deployment strategies such as blue/green or canary deployments.

Visit the following resources to learn more:

- [@official@Deployments Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [@article@Kubernetes Deployment: From Basic Strategies to Progressive Delivery
](https://codefresh.io/learn/kubernetes-deployment/)
- [@video@Kubernetes Deployments | Deployment Strategies](https://youtu.be/lxc4EXZOOvE)

## Evictions

# Evictions

Evictions terminate or delete running pods from a node due to reasons like resource constraints or pod failures. They can be initiated by the system or administrators manually through the API. Evictions can be graceful, allowing pods to clean up resources, or forceful, immediately terminating them. Kubernetes provides preemption and pod disruption budgets to handle evictions effectively and minimize service disruptions. Evictions are necessary to manage and maintain Kubernetes clusters, and Kubernetes provides tools to handle them.

Visit the following resources to learn more:

- [@official@Node-pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
- [@official@API-initiated Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/)

## External Access To Services

# External Access to Services

External access to Kubernetes (k8s) Services allows external clients to access pods and services running in the cluster. There are multiple ways to enable external access to Services in k8s, including NodePorts, LoadBalancers, and Ingress. Ingress is a Kubernetes object that provides a flexible way to manage external access, routing traffic to Services based on URL or host. External access is essential to ensure the scalability and reliability of Kubernetes deployments.

Visit the following resources to learn more:

- [@official@Ingress - Documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [@article@Kubernetes Ingress for Beginners](https://thenewstack.io/kubernetes-ingress-for-beginners/)
- [@video@How do I provide external access to Kubernetes services](https://www.youtube.com/watch?v=iBYTFpoXx24)

## Gitops

# GitOps

GitOps is a set of practices for managing infrastructure and applications using Git repositories as the source of truth for declarative configuration. In Kubernetes, GitOps involves using Git as the single source of truth for both the desired and actual state of the system, automating deployment and management tasks, and often using it in conjunction with Continuous Delivery (CD) practices. The result is a more consistent, reliable, and automated approach to managing infrastructure and applications.

Visit the following resources to learn more:

- [@article@Using GitOps with a Kubernetes cluster](https://docs.gitlab.com/ee/user/clusters/agent/gitops.html)
- [@video@DevOps and GitOps for Kubernetes](https://www.youtube.com/watch?v=PFLimPh5-wo)
- [@feed@Explore top posts about GitOps](https://app.daily.dev/tags/gitops?ref=roadmapsh)

## Helm Charts

# Helm Charts

Helm is a Kubernetes package manager that simplifies the deployment and management of complex applications through the use of reusable and versioned Helm charts. These charts are composed of YAML files that describe related sets of Kubernetes resources and can be customized using values files and templating with Go templates. Helm charts can also have dependencies on other charts and be stored in a centralized repository like Helm Hub for easy sharing and access. By utilizing Helm, teams can streamline application management and reduce duplication of effort.

Visit the following resources to learn more:

- [@official@Helm Docs](https://helm.sh/docs/)
- [@video@What is Helm in Kubernetes? Helm and Helm Charts explained](https://www.youtube.com/watch?v=-ykwb1d0DXU)
- [@feed@Explore top posts about Helm](https://app.daily.dev/tags/helm?ref=roadmapsh)

## Horizontal Pod Autoscaler Hpa

# Horizontal Pod Autoscaler

It is a feature in Kubernetes that automatically scales the number of replicas of a pod based on the current demand for the workload it is running. The HPA controller monitors the CPU utilization or other metrics of the pod and adjusts the number of replicas of the pod to meet the specified target. This helps to ensure that the workload can handle increases in traffic and demand without overloading the resources of the cluster.

Visit the following resources to learn more:

- [@official@Horizontal Pod Autoscaling - Documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

## Injecting Pod Config With Configmaps

# ConfigMaps

ConfigMaps are a way to store configuration data that can be used by applications running in the cluster. A Config Map is a key-value store that can hold configuration data such as database URLs, credentials, API keys, or any other application configuration data that can be used by the application.

Visit the following resources to learn more:

- [@official@ConfigMaps Documentation](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [@article@Kubernetes CRDs: What They Are and Why They Are Useful](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/)
- [@video@Tutorial - ConfigMap in Kubernetes](https://www.youtube.com/watch?v=BPrC_lgmcHQ)

## Installing A Local Cluster

# Installing a Local Cluster

To install and configure a Kubernetes cluster on CentOS 7 or Ubuntu, you would need to setup the prerequisites and requirements for setting up a Kubernetes cluster after which you would be installing the Kubernetes components, including Kubeadm, Kubelet, and Kubectl and then you'll need to connect the master and the worker nodes. Once the connection is established you can check it by deploying application on the cluster.

Visit the following resources to learn more:

- [@article@How to Install a Kubernetes Cluster on CentOS 7](https://www.tecmint.com/install-kubernetes-cluster-on-centos-7/)
- [@article@How To Create a Kubernetes Cluster Using on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-cluster-using-kubeadm-on-ubuntu-20-04)
- [@article@Deploy a Kubernetes Cluster on Ubuntu Server with Microk8s](https://thenewstack.io/deploy-a-kubernetes-cluster-on-ubuntu-server-with-microk8s/)

## Installing The Control Plane

# Control Plane Installation

The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment's replicas field is unsatisfied). Control plane components can be run on any machine in the cluster. However, for simplicity, set up scripts typically start all control plane components on the same machine, and do not run user containers on this machine.

Visit the following resources to learn more:

- [@official@Initializing your control-plane node - Documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#initializing-your-control-plane-node)
- [@video@Tutorial - Install Control Plane Components](https://www.youtube.com/watch?v=IUwuyZ5ReF0)

## Introduction

# Kubernetes Introduction

Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides a way to abstract the underlying infrastructure and manage applications at scale, while also offering flexibility, portability, and a rich feature set. Kubernetes has become the de facto standard for container orchestration due to its widespread adoption, active community, and ability to handle complex, multi-tiered applications.

Visit the following resources to learn more:

- [@official@Kubernetes Documentation](https://kubernetes.io/)
- [@article@Introduction of Kubernetes](https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes)
- [@video@Kubernetes Tutorial for Beginners](https://www.youtube.com/watch?v=X48VuDVv0do)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

## Jobs

# Jobs

a Job is a controller that manages the execution of a finite task or batch job. Jobs are used to run short-lived tasks, such as batch processing, data analysis, or backups, that run to completion and then terminate. Jobs create one or more pods to run the task, and they monitor the completion status of each pod. If a pod fails or terminates, the Job automatically creates a replacement pod to ensure that the task is completed successfully. Jobs are defined by a YAML file that includes a pod template, completion criteria, and other settings.

Visit the following resources to learn more:

- [@official@Jobs Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [@article@How Kubernetes Is Transforming into a Universal Scheduler](https://thenewstack.io/how-kubernetes-is-transforming-into-a-universal-scheduler/)
- [@video@Tutorial | Jobs in Kubernetes](https://www.youtube.com/watch?v=j1EnBbxSz64)

## Key Concepts And Terminologies

# Key Concepts Terminologies

Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Here are some important concepts and terminologies in Kubernetes:

*   Cluster Architecture: The architectural concepts behind Kubernetes.
*   Containers: Technology for packaging an application along with its runtime dependencies.
*   Workloads: Understand Pods, the smallest deployable compute object in Kubernetes, and the higher-level abstractions that help you to run them.
*   Services, Load Balancing, and Networking: Concepts and resources behind networking in Kubernetes.
*   Storage: Ways to provide both long-term and temporary storage to Pods in your cluster.
*   Configuration: Resources that Kubernetes provides for configuring Pods.
*   Cluster Administration: Lower-level detail relevant to creating or administering a Kubernetes cluster.

Visit the following resources to learn more:

- [@official@Concepts of Kubernetes](https://kubernetes.io/docs/concepts/)
- [@article@Understand Kubernetes terminology](https://about.gitlab.com/blog/2020/07/30/kubernetes-terminology/)
- [@video@What Is Kubernetes?](https://www.youtube.com/watch?v=QJ4fODH6DXI)
- [@video@Kubernetes Explained by Experts in 2 Minutes](https://youtu.be/XfBrtNZ2OCw)

## Kubernetes Alternatives

# Kubernetes Alternatives

Kubernetes is a popular open-source container orchestration tool that is widely used for managing and deploying containerized applications. While there are other container orchestration tools available, such as Docker Swarm, Mesos, and Nomad, there are some key differences between Kubernetes and these other tools and some of them are mentioned below:

*   Architecture: Kubernetes is designed as a modular system with many components that work together to provide container orchestration, such as the Kubernetes API server, kubelet, kube-proxy, and etcd.
*   Scalability: Kubernetes is designed to handle large-scale deployments and can scale applications up or down based on demand.
*   Flexibility: Kubernetes is highly configurable and can be customized to meet specific requirements, whereas other container orchestration tools may have more limited configuration options.
*   Portability: Kubernetes is designed to be cloud-agnostic and can run on any public or private cloud platform, as well as on-premises.
*   Community: Kubernetes has a large and active community of developers and users who contribute to its development and provide support.

Visit the following resources to learn more:

- [@article@Compare Apache Mesos vs. Kubernetes](https://www.techtarget.com/searchitoperations/tip/Compare-container-orchestrators-Apache-Mesos-vs-Kubernetes)
- [@article@Docker Swarm, a User-Friendly Alternative to Kubernetes](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/)
- [@article@Can You Live without Kubernetes?](https://thenewstack.io/can-you-live-without-kubernetes/)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

## Kubernetes Extensions And Apis

# Kubernetes Extensions and APIs

Kubernetes (k8s) extensions and APIs are used to customize the behavior of Kubernetes and add new capabilities to the system. Kubernetes extensions, including Custom Resource Definitions (CRDs), Custom Controllers, Custom Scheduler Extenders, and Custom Metrics APIs, enhance Kubernetes functionality. Kubernetes APIs are used to manage resources in a Kubernetes cluster and interact with the system. Kubernetes extensions and APIs together provide a powerful toolkit for customizing and extending Kubernetes, enabling users to build custom components and APIs that streamline operations in Kubernetes.

Visit the following resources to learn more:

- [@official@Extensions - Documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/#extensions)
- [@official@The Kubernetes API - Documentation](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

## Load Balancing

# Load Balancing

Load balancing in distributes network traffic across multiple pods or nodes using a Service object. A Service provides a stable network endpoint for a set of pods, allowing other pods or external clients to access them through a single IP address and DNS name. Kubernetes offers three types of load balancing algorithms for Services, which distribute traffic based on round-robin, least connections, or IP hash. Load balancing is an essential part of Kubernetes networking, providing efficient and reliable traffic distribution across a cluster.

Visit the following resources to learn more:

- [@official@Load Balancing - Documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/#load-balancing)
- [@article@Ingress Controllers: The Swiss Army Knife of Kubernetes](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)
- [@video@Tutorial | Load Balancing Service in Kubernetes](https://www.youtube.com/watch?v=xCsz9IOt-fs)

## Logs

# Logs

Logs are generated by containerized applications running on nodes within the cluster. You can access these logs using the kubectl logs command followed by the name of the pod. By default, this command shows the logs from the most recent container in the pod, but you can specify a specific container within the pod by adding the container name to the command. Adding the -f flag to the command allows you to follow the logs in real-time. There are also third-party logging solutions available for Kubernetes, such as the EFK and Prometheus stacks, that provide more advanced logging capabilities and scalability for large-scale applications.

Visit the following resources to learn more:

- [@official@System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
- [@video@Kubernetes: Log collection explained](https://www.youtube.com/watch?v=6kmHvXdAzIM)

## Metrics

# Metrics

Metrics to monitor include CPU usage, memory usage, network usage, disk usage, API server metrics, pod and container metrics, and cluster-level metrics. These metrics provide insights into the performance and health of the cluster, nodes, and applications running on the cluster. Kubernetes provides tools such as Prometheus, Grafana, and Kubernetes Dashboard for collecting and analyzing these metrics. By monitoring these metrics, administrators can identify performance issues and optimize the cluster for better performance and scalability.

Visit the following resources to learn more:

- [@official@Node Metrics Data](https://kubernetes.io/docs/reference/instrumentation/node-metrics/)
- [@video@How to collect metrics in K8s?](https://www.youtube.com/watch?v=JQrk6HwlN78)

## Monitoring  Optimizing Resource Usage

# Monitoring and Optimizing Resource Usage

Monitoring and optimizing resource usage in Kubernetes helps ensure workloads run efficiently while minimizing waste and avoiding performance issues. By observing CPU, memory, and storage consumption at the node, pod, and container levels, teams can identify bottlenecks, detect underutilized resources, and make informed scaling decisions. Optimization techniques include right-sizing resource requests and limits, using autoscaling mechanisms, and continuously analyzing metrics through monitoring tools. Effective monitoring and optimization improve cluster stability, reduce costs, and enhance overall application performance.

Visit the following resources to learn more:

- [@official@Monitoring Resources in Kubernetes](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
- [@official@Metrics Server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-server)
- [@official@Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [@article@Kubernetes Resource Monitoring: Best Practices](https://www.redhat.com/en/blog/kubernetes-resource-monitoring-best-practices)
- [@article@Optimizing Kubernetes Resource Utilization](https://thenewstack.io/optimizing-kubernetes-resource-utilization/)

## Monitoring And Logging

# Observability Engines

Observability in Kubernetes (k8s) refers to the ability to gain insight into the inner workings of your cluster, applications, and services running on top of it. An observability engine in k8s is a tool or platform that facilitates the collection, analysis, and visualization of data from various sources in your k8s environment. Some popular observability engines in k8s include Prometheus, Grafana, Jaeger, and Elastic Stack (ELK).

Visit the following resources to learn more:

- [@opensource@K8sGPT - AI scanner for Kubernetes problems](https://github.com/k8sgpt-ai/k8sgpt)
- [@opensource@HolmesGPT - AIOps Platform for investigating Kubernetes problems and Prometheus alerts](https://github.com/robusta-dev/holmesgpt/)
- [@article@Kubernetes Observability 101: Tools, Best Practices, And More](https://www.cloudzero.com/blog/kubernetes-observability)
- [@article@Kubernetes Observability in KubeSphere](https://kubesphere.io/observability/)
- [@feed@Explore top posts about Observability](https://app.daily.dev/tags/observability?ref=roadmapsh)

## Multi Cluster Management

# Multi Cluster Management

Multi-Cluster Management in Kubernetes (k8s) refers to the ability to manage multiple Kubernetes clusters using a single control plane. This approach allows administrators to centrally manage and orchestrate resources across multiple clusters, regardless of where they are located, without having to switch between multiple management consoles or tools.

Visit the following resources to learn more:

- [@official@Configure Access to Multiple Clusters - Documentation](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
- [@video@Kubernetes Cluster Management Strategies](https://www.youtube.com/watch?v=966TJ6mlOYY)

## Network Security

# Network Security

Network security in Kubernetes involves securing network communication between different components within the cluster and with external networks. This can be achieved through various mechanisms such as Network Policies, Encryption, Authentication, Authorization, and Firewall rules. Network Policies provide fine-grained control over network traffic, while encryption ensures secure communication between pods, nodes, and external systems. Authentication and Authorization mechanisms prevent unauthorized access and provide secure communication between various components. Firewall rules help to protect the cluster against external attacks by limiting access to specific ports and protocols. Overall, network security in Kubernetes is critical to maintaining the confidentiality, integrity, and availability of the cluster.

Visit the following resources to learn more:

- [@official@Network Policies - Documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [@article@6 Kubernetes Security Best Practices](https://thenewstack.io/6-kubernetes-security-best-practices/)
- [@article@The Kubernetes Network Security Effect](https://thenewstack.io/the-kubernetes-network-security-effect/)
- [@article@Kubernetes Security Best Practices to Keep You out of the News](https://thenewstack.io/kubernetes-security-best-practices-to-keep-you-out-of-the-news/)
- [@video@Kubernetes Security Best Practices](https://www.youtube.com/watch?v=oBf5lrmquYI)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Networking  Pod To Pod Communication

# Networking & Pod-to-Pod Communication

Kubernetes networking enables pods to communicate with each other across the cluster, regardless of which node they are running on. Every pod is assigned its own IP address, and Kubernetes follows a flat network model where all pods can directly communicate with each other without Network Address Translation (NAT).

Pod-to-pod communication is implemented by a **Container Network Interface (CNI)** plugin, such as Calico, Flannel, Cilium, or Weave. These plugins are responsible for IP address assignment, routing, and enforcing network policies. By default, all pod traffic is allowed, but **NetworkPolicies** can be used to control and restrict traffic between pods for security and isolation.

Reliable pod-to-pod networking is a core requirement for building distributed and microservices-based applications in Kubernetes.

Visit the following resources to learn more:

- [@official@Cluster Networking - Kubernetes Documentation](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [@official@Network Policies - Kubernetes Documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [@article@Kubernetes Networking Explained](https://www.tigera.io/learn/guides/kubernetes-networking/)
- [@video@Kubernetes Networking Deep Dive](https://www.youtube.com/watch?v=t98ekMiz0hQ)

## Observability Engines

# Observability Engines

Observability in Kubernetes (k8s) refers to the ability to gain insight into the inner workings of your cluster, applications, and services running on top of it. An observability engine in k8s is a tool or platform that facilitates the collection, analysis, and visualization of data from various sources in your k8s environment. Some popular observability engines in k8s include Prometheus, Grafana, Jaeger, and Elastic Stack (ELK).

Visit the following resources to learn more:

- [@opensource@K8sGPT - AI scanner for Kubernetes problems](https://github.com/k8sgpt-ai/k8sgpt)
- [@opensource@HolmesGPT - AIOps Platform for investigating Kubernetes problems and Prometheus alerts](https://github.com/robusta-dev/holmesgpt/)
- [@article@Kubernetes Observability 101: Tools, Best Practices, And More](https://www.cloudzero.com/blog/kubernetes-observability)
- [@article@Kubernetes Observability in KubeSphere](https://kubesphere.io/observability/)
- [@feed@Explore top posts about Observability](https://app.daily.dev/tags/observability?ref=roadmapsh)

## Overview Of Kubernetes

# Kubernetes overview

Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open-sourced the Kubernetes project in 2014. Kubernetes combines over 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community.

Visit the following resources to learn more:

- [@official@Overview of Kubernetes](https://kubernetes.io/docs/concepts/overview/)
- [@article@What is Kubernetes?](https://www.redhat.com/en/topics/containers/what-is-kubernetes)
- [@article@Kubernetes Overview & Essential Reading](https://thenewstack.io/kubernetes/)
- [@video@Tutorial - Kubernetes](https://www.youtube.com/watch?v=VnvRFRk_51k&t=1sn)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

## Pod Priorities

# Pod Priorities

Pod priorities in Kubernetes determine the order in which pods are scheduled on nodes when there are competing demands for resources. Each pod is assigned a numeric priority value, with higher values indicating higher priority. The scheduler maximizes the total priority of scheduled pods while also considering node suitability, taints and tolerations, and affinity and anti-affinity rules. Priorities can be set manually or automatically based on business logic or application requirements. Priorities help ensure that critical workloads receive necessary resources and are scheduled first, while lower priority workloads are scheduled when resources become available.

Visit the following resources to learn more:

- [@official@Pod priority - Documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority)
- [@video@Kubernetes Pod Priority (Examples)](https://www.youtube.com/watch?v=sR_Zmvme3-0)

## Pods

# Pods

In Kubernetes, a pod is the smallest deployable unit that represents a single instance of a running process in a cluster. A pod can contain one or more containers that share the same network namespace and can access the same storage volumes. Pods are created and managed by Kubernetes, and they are scheduled to run on one of the nodes in the cluster. Pods provide a lightweight and flexible abstraction layer that enables Kubernetes to manage the deployment, scaling, and networking of containerized applications. Pods also facilitate the communication and data exchange between containers running in the same pod.

Visit the following resources to learn more:

- [@official@Pods Documentation](https://kubernetes.io/docs/concepts/workloads/pods/)
- [@article@The Kubernetes Way: Pods and Services](https://thenewstack.io/kubernetes-way-part-one/)
- [@article@5 Best Practices for Configuring Kubernetes Pods Running in Production](https://thenewstack.io/5-best-practices-for-configuring-kubernetes-pods-running-in-production/)
- [@video@What is a Pod in kubernetes ? Why do you need it ?](https://www.youtube.com/watch?v=k0fzMZgpp14)

## Replicasets

# ReplicaSets

A ReplicaSet is a controller that ensures a specified number of replicas (identical copies) of a pod are running in a cluster at all times. ReplicaSets help to ensure high availability and scalability by automatically scaling the number of pod replicas up or down in response to changes in demand or hardware failures. They are defined by a YAML file that specifies the desired number of replicas, the pod template to use, and other settings. They are responsible for monitoring the status of pods and creating or deleting replicas as necessary to meet the desired state.

Visit the following resources to learn more:

- [@official@ReplicaSet Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
- [@article@Strategies for Running Stateful Workloads in Kubernetes: Pet Sets](https://thenewstack.io/strategies-running-stateful-applications-kubernetes-pet-sets/)
- [@video@ReplicaSet in Kubernetes](https://www.youtube.com/watch?v=1WM-LsH6tKc)

## Resource Health

# Resource Health

Resource health monitoring in Kubernetes involves monitoring the health and availability of resources such as pods, nodes, and containers. It helps administrators identify and troubleshoot issues that may affect the system's performance and availability using tools such as Kubernetes Dashboard, Prometheus, or Grafana. Resource health monitoring also helps ensure that the system is resilient to failures and can recover quickly from any disruptions. It is an important part of managing a Kubernetes cluster and ensures the reliability, availability, and scalability of the system.

Visit the following resources to learn more:

- [@video@Dashboards with Grafana and Prometheus](https://www.youtube.com/watch?v=fzny5uUaAeY)
- [@video@How to Monitor a Kubernetes Cluster with Prometheus & Grafana](https://www.youtube.com/watch?v=YDtuwlNTzRc)

## Resource Management

# Monitoring and Optimizing Resource Usage

Monitoring and optimizing resource usage in Kubernetes (k8s) is crucial for ensuring efficient and effective use of resources. To monitor resource usage, k8s provides a Metrics Server, and Prometheus can be integrated with k8s. The Container Runtime Interface (CRI) can also be used to monitor container-level resource usage data. To optimize resource usage, setting appropriate requests and limits, using Horizontal Pod Autoscaling (HPA), implementing pod affinity and anti-affinity rules, and controlling node selection can all help reduce resource contention and improve resource utilization. By monitoring and optimizing resource usage, k8s can ensure that applications run efficiently and resources are used effectively.

Visit the following resources to learn more:

- [@official@Tools for Monitoring Resources - Documentation](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
- [@article@Kubernetes Resource Optimization: Just The Basics](https://sequoia.makes.software/kubernetes-resource-optimization-just-the-basics/)
- [@article@How to Choose the Right Kubernetes Monitoring Tool ](https://thenewstack.io/how-to-choose-the-right-kubernetes-monitoring-tool/)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Role Based Access Control Rbac

# Role Based Acccess Control

Role-Based Access Control (RBAC) is a method of controlling access to Kubernetes resources based on the roles assigned to users or groups. RBAC involves creating roles and binding them to users or groups to control access to Kubernetes resources. Roles are defined as a set of rules that determine what actions can be performed on specific resources. By assigning roles to users or groups, access to Kubernetes resources can be restricted or granted based on the permissions defined in the role. RBAC helps ensure the security and integrity of Kubernetes clusters by limiting access to authorized users and groups.

Visit the following resources to learn more:

- [@official@Role Based Access Control Good Practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [@article@A Primer on Kubernetes Access Control](https://thenewstack.io/a-primer-on-kubernetes-access-control/)
- [@article@A Practical Approach to Understanding Kubernetes Authorization](https://thenewstack.io/a-practical-approach-to-understanding-kubernetes-authorization/)
- [@article@3 Realistic Approaches to Kubernetes RBAC](https://thenewstack.io/three-realistic-approaches-to-kubernetes-rbac/)
- [@article@Role-Based Access Control: Five Common Authorization Patterns](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)
- [@article@Securing Kubernetes and Other Resources at Scale Using RBAC](https://thenewstack.io/securing-kubernetes-and-other-resources-at-scale-using-rbac/)
- [@video@Understand Role Based Access Control in Kubernetes](https://www.youtube.com/watch?v=G3R24JSlGjY)

## Rolling Updates  Rollbacks

# Rolling Updates and Rollbacks

Rolling updates and rollbacks are methods for updating applications without downtime. A rolling update gradually replaces old versions of an application with new ones, ensuring that some instances of the application are always available. If problems arise during the update, a rollback allows you to revert to the previous, stable version of the application.

Visit the following resources to learn more:

- [@official@Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
- [@article@How do you rollback deployments in Kubernetes?](https://learnkube.com/kubernetes-rollbacks)
- [@video@Kubernetes Deployments: A Guide to the Rolling Update Deployment Strategy](https://semaphore.io/blog/kubernetes-rolling-update-deployment)
- [@video@Kubernetes Rollbacks Tutorial](https://www.youtube.com/watch?v=9hK11Ov74U4)
- [@video@Kubernetes Deployment strategies | Rolling Update Deployment | Argo rollout | ADAM](https://www.youtube.com/watch?v=cy3KXqgJOrE)

## Running Applications

# Running Applications

Running applications involves deploying and managing software within a Kubernetes cluster. This includes packaging the application, defining its resource requirements (like CPU and memory), specifying how it should be exposed to the outside world, and ensuring it remains healthy and available. It also covers scaling the application to handle varying workloads and updating it without downtime.

Visit the following resources to learn more:

- [@official@Run Applications](https://kubernetes.io/docs/tasks/run-application/)
- [@article@Deploying an Application on Kubernetes: A Complete Guide!](https://dev.to/pavanbelagatti/deploying-an-application-on-kubernetes-a-complete-guide-1cj6)
- [@article@How Do Applications Run on Kubernetes?](https://thenewstack.io/how-do-applications-run-on-kubernetes/)
- [@video@Kubernetes 101: Deploying Your First Application!](https://www.youtube.com/watch?v=XltFOyGanYE)

## Scheduling

# Scheduling

Scheduling in Kubernetes refers to the process of assigning workloads to specific nodes in a cluster. The Kubernetes scheduler makes scheduling decisions based on factors such as resource availability, node suitability, and workload priorities. It balances workloads across the cluster to ensure efficient resource utilization and avoid overloading nodes. Scheduling takes into account factors such as geographic location, hardware requirements, and application-specific needs.

Visit the following resources to learn more:

- [@official@Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [@official@Scheduling Framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)

## Security

# Security Scanners

Kubernetes security scanners help identify vulnerabilities and potential security threats in container images before deployment. Popular options include Aqua Security, Twistlock, Sysdig Secure, Trivy, Anchore Engine, and OpenSCAP. These scanners offer a variety of features such as vulnerability scanning, compliance checks, and runtime protection for Kubernetes environments. By integrating these scanners into their pipelines, organizations can ensure the security and integrity of their Kubernetes deployments and minimize the risk of security breaches and data loss.

Visit the following resources to learn more:

- [@article@8+ open-source Kubernetes vulnerability scanners](https://techbeacon.com/security/8-open-source-kubernetes-vulnerability-scanners-consider)
- [@article@7 Kubernetes Security Scanners](https://thechief.io/c/editorial/7-kubernetes-security-scanners-to-use-in-your-devsecops-pipeline/)
- [@article@Improve Security With Automated Image Scanning Through CI/CD](https://thenewstack.io/improve-security-with-automated-image-scanning-through-ci-cd/)
- [@article@Starboard: Putting all the Kubernetes Security Pieces into One Place](https://thenewstack.io/starboard-putting-all-the-kubernetes-security-pieces-into-one-place/)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Services And Networking

# Networking and Pod to Pod Communication

Networking is crucial for communication between pods and resources in a Kubernetes cluster. Each pod has a unique IP address and can communicate with other pods directly. Container networking interface (CNI) plugins are used to configure pod network interfaces and provide isolation between pods. Kubernetes also provides networking services such as load balancing, service discovery, and ingress, which enable external traffic to access pods and services. These services are implemented using Kubernetes objects such as Services, Ingress, and NetworkPolicies. Networking and pod-to-pod communication are essential for scalability, reliability, and flexibility in Kubernetes clusters.

Visit the following resources to learn more:

- [@official@Cluster Networking - Documentation](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [@official@Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/)
- [@article@How Kubernetes Provides Networking and Storage to Applications](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)
- [@feed@Explore top posts about Networking](https://app.daily.dev/tags/networking?ref=roadmapsh)

## Setting Resource Requests And Limits

# Setting Resource Requests and Limits

Resource requests and limits in Kubernetes specify the minimum and maximum amount of CPU and memory a container requires to run. Resource requests are used for scheduling containers on nodes with sufficient resources, while limits enforce resource quotas and prevent containers from consuming too much. These settings can be configured at the pod or container level using the resources field in YAML. It's important to set resource requests and limits correctly to ensure optimal resource utilization in your Kubernetes cluster.

Visit the following resources to learn more:

- [@official@Requests and limits - Documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
- [@official@Motivation for default memory limits and requests](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/#motivation-for-default-memory-limits-and-requests)
- [@article@Understanding Kubernetes Resource Types](https://thenewstack.io/understanding-kubernetes-resource-types/)
- [@article@Kubernetes Requests and Limits Demystified ](https://thenewstack.io/kubernetes-requests-and-limits-demystified/)

## Setting Up Kubernetes

# Deploying your First Application

To deploy your first application in Kubernetes, you need to create a deployment and service manifest in YAML files, apply the manifests to your Kubernetes cluster using the kubectl apply command, verify that your application's pods are running with kubectl get pods, and test the service with kubectl get services and accessing the service using a web browser or a tool like cURL. There are also various tools and platforms available that can simplify application deployment in Kubernetes, such as Helm charts and Kubernetes operators.

Visit the following resources to learn more:

- [@official@Using kubectl to Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
- [@article@Deploying An Application On Kubernetes From A to Z](https://web.archive.org/web/20230326150953/https://www.weave.works/blog/deploying-an-application-on-kubernetes-from-a-to-z)
- [@article@Kubernetes 101: Deploy Your First Application with MicroK8s](https://thenewstack.io/kubernetes-101-deploy-your-first-application-with-microk8s/)
- [@video@Kubernetes Tutorial | Your First Kubernetes Application](https://www.youtube.com/watch?v=Vj6EFnav5Mg)
- [@video@Kubernetes 101: Deploying Your First Application](https://www.youtube.com/watch?v=XltFOyGanYE)

## Should You Manage Your Own Cluster

# Own Cluster

To create your own Kubernetes cluster, you need to choose a cloud provider or set up your own infrastructure, install Kubernetes on your infrastructure, configure your cluster by setting up networking, storage, and security, deploy your applications using Kubernetes manifests, and monitor and manage your cluster using tools like Kubernetes Dashboard, kubectl, and Prometheus. This process can be complex and time-consuming, but it gives you complete control over your infrastructure and allows for customization to meet your specific needs.

Visit the following resources to learn more:

- [@official@Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [@video@KUBERNETES | Install Kubernetes Cluster](https://www.youtube.com/watch?v=Ro2qeYeisZQ)

## Stateful Applications

# Stateful Applications

In Kubernetes, storage is a key component for stateful applications, as these applications require persistent data storage that is available across multiple replicas of the application. Kubernetes provides several options for storage, including volumes, persistent volumes, and storage classes.

Volumes are the basic building blocks of storage in Kubernetes. A volume is a directory that is accessible to the container running the application, and it can be backed by different types of storage, such as a host directory, a cloud provider disk, or a network storage system. Volumes are created and managed by Kubernetes, and they can be mounted into containers as part of a pod definition.

Visit the following resources to learn more:

- [@official@Stateful Applications](https://kubernetes.io/docs/tutorials/stateful-application/)
- [@video@The basics of stateful applications in Kubernetes](https://www.youtube.com/watch?v=GieXzb91I40)

## Statefulsets

# StatefulSets

It is a controller that manages the deployment and scaling of a set of stateful pods that require stable network identities and stable storage volumes. StatefulSets are used to run stateful applications such as databases, where the order and uniqueness of each pod is important. StatefulSets provide unique stable network identities and stable storage volumes for each pod, which allows stateful applications to maintain data consistency even when they are scaled up or down, or when nodes fail or are replaced. StatefulSets are defined by a YAML file that includes a pod template, a service to access the pods, and other settings.

Visit the following resources to learn more:

- [@official@StatefulSets Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [@article@Different Approaches for Building Stateful Kubernetes Applications](https://thenewstack.io/different-approaches-for-building-stateful-kubernetes-applications/)
- [@video@Kubernetes StatefulSet | Tutorial](https://www.youtube.com/watch?v=pPQKAR1pA9U)

## Storage And Volumes

# CSI drivers

CSI (Container Storage Interface) drivers in Kubernetes provide a standard way for storage providers to integrate with Kubernetes and offer persistent storage for containerized applications. They operate as separate containerized processes and communicate with Kubernetes through a well-defined API. CSI drivers allow Kubernetes to access a wide range of storage systems and provide advanced features like snapshotting and cloning.

Visit the following resources to learn more:

- [@official@Container Storage Interface (CSI) for Kubernetes](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
- [@video@CSI in Kubernetes](https://www.youtube.com/watch?v=brXPQ1Qwjl4)

## Taints And Tolerations

# Taints and Tolerations

Taints and tolerations are used in Kubernetes to restrict or allow pods to be scheduled on certain nodes based on labels. A taint is a label that is applied to a node to indicate certain limitations or requirements. A toleration is a label applied to a pod to indicate that it can tolerate certain taints. When a node has a taint, only pods with the corresponding tolerations can be scheduled on that node. This feature is useful for various purposes, such as ensuring separation of critical and non-critical workloads, reserving nodes for certain tasks, and protecting nodes from overloading.

Visit the following resources to learn more:

- [@official@Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [@video@Kubernetes For Beginners: Taints & Tolerations](https://www.youtube.com/watch?v=mo2UrkjA7FE)

## Topology Spread Constraints

# Topology Spread Constraints

Topology spread constraints ensure even distribution of pods across a cluster's topology. Constraints define rules for the number of pods of a certain type that can run on a given level, such as nodes, zones, or racks. These constraints can be customized to fit specific needs, such as ensuring that critical workloads are spread across multiple zones. They help prevent single points of failure and improve application resilience by preventing resource overloading and promoting balanced distribution of workloads. Constraints can be added using the Kubernetes API or command line interface.

Visit the following resources to learn more:

- [@official@Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- [@video@Kubernetes | Topology Spread Constraints](https://www.youtube.com/watch?v=joRrWJ6bwvE)

## Traces

# Traces

Tracing in Kubernetes involves monitoring the flow of requests through different components of the system, using tools such as Jaeger or Zipkin. OpenTracing and OpenCensus provide a consistent way of capturing traces across different components and applications running on the cluster. Tracing helps identify performance bottlenecks, debug issues, and optimize the system for better performance and scalability. By monitoring traces in Kubernetes, administrators can identify issues and take corrective actions to ensure efficient system performance.

Visit the following resources to learn more:

- [@official@Traces For Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/)
- [@video@Introduction to Tracing](https://www.youtube.com/watch?v=idDu_jXqf4E)

## Using Secrets For Sensitive Data

# Secrets

Kubernetes secrets store sensitive data such as passwords, tokens, and API keys in a secure manner. They can be created manually or automatically, and stored in etcd. Secrets can be mounted as files or environment variables in a pod, and access can be managed using Kubernetes RBAC. However, they have some limitations, such as size and the inability to be updated once created. Understanding secrets is important for building secure applications in Kubernetes.

Visit the following resources to learn more:

- [@official@Documentation - Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [@article@Kubernetes Secrets Management: 3 Approaches, 9 Best Practices](https://thenewstack.io/kubernetes-secrets-management-3-approaches-9-best-practices/)
- [@video@Kubernetes Secrets in 5 Minutes!](https://www.youtube.com/watch?v=cQAEK9PBY8U)

## Vertical Pod Autoscaler Vpa

# Vertical Pod Autoscaler

Vertical Pod Autoscaler (VPA) is a Kubernetes feature that automates the process of adjusting resource limits for containers in pods. Unlike Horizontal Pod Autoscaler (HPA), which scales the number of replicas of a pod, VPA scales the resources allocated to a pod's containers. It adjusts the resource requests and limits for each container based on its actual usage.

Visit the following resources to learn more:

- [@article@What is Kubernetes VPA?](https://www.kubecost.com/kubernetes-autoscaling/kubernetes-vpa/)
- [@video@Vertical Pod Autoscaling: Example](https://www.youtube.com/watch?v=3h-vDDTZrm8)

## Why Use Kubernetes

# Why Kubernetes

Kubernetes (k8s) is needed because it provides a powerful and flexible platform for deploying and managing containerized applications at scale. It allows for easy scalability, high resilience, application portability, automation of many tasks, and standardization of the container platform. k8s also helps reduce complexity and workload for operations teams, enabling them to focus on more strategic initiatives.

Visit the following resources to learn more:

- [@official@Why you need Kubernetes and what it can do](https://kubernetes.io/docs/concepts/overview/#why-you-need-kubernetes-and-what-can-it-do)
- [@article@Primer: How Kubernetes Came to Be, What It Is, and Why You Should Care](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)
