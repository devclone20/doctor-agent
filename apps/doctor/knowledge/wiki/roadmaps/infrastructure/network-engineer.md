# Network Engineer Roadmap

## Access Points  Controllers

# Access Points & Controllers

Wireless access points (APs) are devices that broadcast Wi-Fi signals and connect wireless clients to a wired network. In larger deployments, multiple access points are managed by a wireless controller, which centralizes configuration, monitoring, and roaming policies across all APs. This controller-based architecture simplifies management and ensures consistent performance and security across the entire wireless network.

Visit the following resources to learn more:

- [@article@What Is Access Point Controller and How to Use?](https://www.qsfptek.com/qt-news/what-is-access-point-controller-and-how-to-use.html?srsltid=AfmBOopKCqq5gmcPlfeBDm4CFpiZhpfyx38GQ0Ec33h9U_W3Hl6j3W7A)
- [@video@Wireless Access Points Explained - Home Networking For Beginners](https://www.youtube.com/watch?v=bRjbil52Qm4)

## Access Points

# Access Points

A wireless access point (AP) is a device that creates a wireless local area network, typically in an office or large building, by connecting to a wired router or switch and broadcasting a Wi-Fi signal. Multiple access points can be deployed across a large area to extend wireless coverage and allow devices to roam seamlessly. Access points are distinct from routers —they extend the network wirelessly but do not typically perform routing functions on their own.

Visit the following resources to learn more:

- [@article@What is a wireless access point?](https://www.cisco.com/site/us/en/learn/topics/small-business/what-is-an-access-point.html)
- [@video@Wireless Access Point vs Wi-Fi Router](https://www.youtube.com/watch?v=OxiY4yf6GGg)

## Acls

# ACLs

ACLs, or Access Control Lists, are ordered sets of rules applied to a router or switch interface that permit or deny traffic based on criteria such as source IP address, destination IP address, protocol, and port number. They are one of the most fundamental tools for controlling traffic flow and enforcing security policies on a network. ACLs can be applied inbound or outbound on an interface and are evaluated sequentially, with the first matching rule determining the action taken on the packet.

Visit the following resources to learn more:

- [@article@What Is A Network Access Control List (ACL)?](https://www.fortinet.com/resources/cyberglossary/network-access-control-list)
- [@video@What Are Access Lists? -- Access Control Lists (ACLs) -- Part 1 of 8](https://www.youtube.com/watch?v=0gGhuYOh-54&list=PLIFyRwBY_4bRkAk_BkWL3ea6lRvOn8AKs)

## Ansible

# Ansible

Ansible is an open-source automation tool that uses simple, human-readable YAML files called playbooks to automate the configuration and management of servers, network devices, and cloud infrastructure. Unlike some automation tools, Ansible is agentless — it communicates with devices directly over SSH or APIs without requiring any software to be installed on the target device first. For network engineers, Ansible is particularly valuable for pushing configuration changes to many routers and switches simultaneously, ensuring consistency across the network and eliminating the need to log into each device manually.

Visit the following resources to learn more:

- [@official@Ansible for Network Automation](https://docs.ansible.com/projects/ansible/latest/network/index.html)
- [@official@Ansible Docs](https://docs.ansible.com/)
- [@video@Introduction to Ansible - Automating Network Configuration](https://www.youtube.com/watch?v=il5IjFehoMA)

## Apis For Networking

# APIs

An API, or Application Programming Interface, is a standardized interface that allows software applications and automation tools to communicate with network devices and services programmatically, without a human typing commands manually into a CLI. In networking, APIs are the foundation of modern automation: when a Python script configures a switch, when Ansible pushes a change to a router, or when Terraform creates a cloud network, they are all talking to devices and platforms through an API under the hood.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated API Design Roadmap](https://roadmap.sh/api-design)
- [@article@What Is a Network API?](https://www.vonage.com/resources/articles/what-is-a-network-api/)
- [@video@Full HTTP Networking Course – Fetch and REST APIs in JavaScript](https://www.youtube.com/watch?v=2JYT5f2isg4)

## Application

# Application

The Application layer is the seventh and topmost layer of the OSI model, where end-user software interacts with the network. It provides network services directly to applications, enabling functions like web browsing, email, file transfer, and domain name resolution. Protocols such as HTTP, FTP, SMTP, and DNS all operate at this layer.

Visit the following resources to learn more:

- [@article@What is layer 7? | How layer 7 of the Internet works](https://www.cloudflare.com/en-gb/learning/ddos/what-is-layer-7/)
- [@video@OSI Model Layer 7 - Application](https://www.youtube.com/watch?v=L_wLexApMkA)

## Application

# Application

The Application layer of the TCP/IP model is the topmost layer and encompasses all the protocols that applications use to communicate over the network. It combines the functions of the OSI Session, Presentation, and Application layers into one. Protocols like HTTP, DNS, SMTP, FTP, and SSH all operate here, directly serving user-facing applications.

## Arp

# ARP

ARP, or Address Resolution Protocol, is used to map an IP address to a physical MAC address on a local network. When a device wants to communicate with another device on the same network, it uses ARP to discover which MAC address corresponds to a known IP address. The result is stored temporarily in an ARP cache to speed up future lookups.

Visit the following resources to learn more:

- [@article@Address Resolution Protocol (ARP): Resolving Network Address Conflicts](https://www.fortinet.com/resources/cyberglossary/what-is-arp)
- [@video@ARP Explained - Address Resolution Protocol](https://www.youtube.com/watch?v=cn8Zxh9bPio)

## Aws

# AWS

AWS (Amazon Web Services) offers a comprehensive set of networking services that allow engineers to build and manage network infrastructure entirely in the cloud. Core networking components include VPC (Virtual Private Cloud) for creating isolated virtual networks, subnets for segmenting those networks, Security Groups and Network ACLs for controlling traffic, Route Tables for directing traffic between subnets and to the Internet, and Internet Gateways for enabling public connectivity. For connecting cloud and on-premises environments, AWS provides services like Direct Connect for dedicated private connections, AWS VPN for encrypted tunnels, Transit Gateway for connecting multiple VPCs and on-premises networks at scale, and Elastic Load Balancing for distributing traffic across resources.

Visit the following resources to learn more:

- [@course@AWS Networking Basics](https://skillbuilder.aws/learn/S1VYRYHD8V/aws-networking-basics/SKP7248UVF)
- [@video@AWS Networking Basics For Programmers | Hands On](https://www.youtube.com/watch?v=2doSoMN2xvI)
- [@video@Introduction to AWS Networking](https://www.youtube.com/watch?v=XZbvQWkpJTI)

## Azure

# Azure

Microsoft Azure provides a full suite of networking services built around the concept of Virtual Networks (VNets), which are the foundational isolated network environments where Azure resources are deployed. Key networking services include VNet Peering for connecting virtual networks together, Azure VPN Gateway for site-to-site and point-to-site VPN connections, ExpressRoute for dedicated private connectivity between on-premises networks and Azure, Azure Firewall for centralized network security, Network Security Groups (NSGs) for controlling inbound and outbound traffic, and Azure Load Balancer and Application Gateway for distributing traffic across services. Azure also offers Azure Virtual WAN for large-scale branch connectivity and Azure DNS for managing domain name resolution within and across cloud environments.

Visit the following resources to learn more:

- [@official@Networking on Azure](https://azure.microsoft.com/en-us/products/category/networking)
- [@article@Cloud Networking Basics with Azure](https://medium.com/@AlexanderObregon/cloud-networking-basics-with-azure-16509a99aca6)
- [@video@Azure Master Class v3 - Part 6 - Networking](https://www.youtube.com/watch?v=nDtCSQyG_I8)

## Bandwidth

# Bandwidth

Bandwidth refers to the maximum amount of data that can be transmitted over a network connection in a given amount of time, typically measured in bits per second (bps). Higher bandwidth means more data can flow simultaneously, which generally results in faster network performance. It is often compared to the width of a pipe: the wider the pipe, the more water (data) can flow through it at once.

Visit the following resources to learn more:

- [@article@What is Network Bandwidth?](https://www.solarwinds.com/resources/it-glossary/network-bandwidth)
- [@video@Internet Bandwidth (speed) Explained](https://www.youtube.com/watch?v=DHa9gxRfAmM)

## Bgp

# BGP

BGP, or Border Gateway Protocol, is the routing protocol that powers the Internet by exchanging routing information between autonomous systems, i.e., the large networks operated by ISPs, corporations, and other organizations. It is a path-vector protocol that makes routing decisions based on network policies, path attributes, and rules rather than simply the shortest path. BGP is responsible for ensuring that traffic can reach any two points on the global Internet.

Visit the following resources to learn more:

- [@article@What is BGP? | BGP routing explained](https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-bgp/)
- [@video@MicroNugget: What is BGP and BGP Configuration Explained](https://www.youtube.com/watch?v=z8INzy9E628)

## Bluetooth Basics

# Bluetooth Basics

Bluetooth is a short-range wireless communication standard used to connect devices over distances typically up to 10 meters. It operates in the 2.4 GHz frequency band and is designed for low-power, point-to-point or small-group connections between devices like phones, headsets, keyboards, and IoT sensors. Bluetooth is not a replacement for Wi-Fi, but complements it for personal area networking and device pairing scenarios.

Visit the following resources to learn more:

- [@article@What is Bluetooth and how does it work?](https://theconversation.com/what-is-bluetooth-and-how-does-it-work-242892)
- [@video@How Does Bluetooth Technology Work?](https://www.youtube.com/watch?v=ObcBJyVS10E)

## Ccna

# CCNA

The Cisco Certified Network Associate (CCNA) certification is an entry-level certification for IT professionals who want to specialize in networking, specifically within the realm of Cisco products. This certification validates an individual's ability to install, configure, operate, and troubleshoot medium-sized routed and switched networks. It also covers the essentials of network security and management.

Visit the following resources to learn more:

- [@official@CCNA Certification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html)
- [@video@Network Chuck Free CCNA Course](https://www.youtube.com/playlist?list=PLIhvC56v63IJVXv0GJcl9vO5Z6znCVb1P)
- [@video@Jeremy's IT Lab](https://www.youtube.com/@JeremysITLab)

## Ccnp

# CCNP

CCNP (Cisco Certified Network Professional) is an intermediate-level professional certification that validates a candidate's ability to plan, implement, verify, and troubleshoot local and wide-area enterprise networks. It focuses on advanced core technologies, including routing, switching, security, automation, and programmable network solutions. Earning this credential requires passing a core exam followed by a concentration exam, demonstrating that an individual possesses the deep technical expertise necessary to manage complex network infrastructures in large-scale environments.

Visit the following resources to learn more:

- [@official@CCNP Certification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccnp-enterprise/exams-and-training.html)
- [@video@CCNP  Course Introduction](https://www.youtube.com/watch?v=0iBRK8GRTrI&list=PLxbwE86jKRgOb2uny1CYEzyRy_mc-lE39)

## Cidr

# CIDR

CIDR, or Classless Inter-Domain Routing, is a method of allocating IP addresses and routing that replaced the older class-based system. Instead of fixed classes (A, B, C), CIDR uses a slash notation (e.g., 192.168.1.0/24) to indicate how many bits are used for the network portion of the address. This allows for more flexible and efficient use of IP address space and is the standard method used in modern networking.

Visit the following resources to learn more:

- [@article@What is CIDR?](https://aws.amazon.com/what-is/cidr/)
- [@video@What is CIDR (Classless Inter Domain Routing)?](https://www.youtube.com/watch?v=KiWXRL-2TnY)
- [@video@What is network CIDR notation?](https://www.youtube.com/watch?v=tpa9QSiiiUo)

## Circuit Level Gateway

# Circuit Level Gateway

A circuit-level gateway is a type of firewall that operates at the session layer and monitors TCP handshakes to verify that a connection is legitimate before allowing data to flow. Unlike application-layer proxies, it does not inspect the content of the data itself — only the connection establishment. Once a session is deemed valid, traffic passes through without further inspection, making it faster but less thorough than application-layer firewalls.

Visit the following resources to learn more:

- [@article@What Is a Circuit Level Gateway?](https://www.paloaltonetworks.com/cyberpedia/what-is-a-circuit-level-gateway)
- [@article@What is a circuit level firewall?](https://nordlayer.com/learn/firewall/circuit-level/)

## Cisco Packet Tracer

# Cisco Packet Tracer

Cisco Packet Tracer is a visual simulation and modeling tool that allows users to design, configure, and troubleshoot network topologies without the need for physical hardware. It provides a drag-and-drop interface where you can place virtual routers, switches, and end devices, and then execute Cisco IOS commands to test network connectivity and protocols. It is widely used to practice networking concepts, build simulated lab environments, and prepare for certification exams in a safe, risk-free virtual space.

Visit the following resources to learn more:

- [@article@Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
- [@article@What is Cisco Packet Tracer? | Free Training and Download](https://www.netcomlearning.com/blog/what-is-cisco-packet-tracer)

## Client Server Network

# Client-Server Network

A client-server network is a model where one or more central servers provide resources or services, and multiple client devices request and consume those resources. The server manages shared resources such as files, databases, or applications, while clients interact with them through the network. This model is widely used in enterprise environments because it centralizes management, improves security, and makes it easier to scale.

Visit the following resources to learn more:

- [@article@A Guide to Understanding Client-Server Network](https://www.fs.com/blog/a-guide-to-understanding-clientserver-network-6976.html)
- [@video@The Client Server Model | Clients and Servers](https://www.youtube.com/watch?v=L5BlpPU_muY)

## Client

# Client

A client is any device or software application that sends requests to a server to access resources or services. In everyday terms, your web browser acts as a client when it asks a web server to load a page. Clients initiate communication in the client-server model and rely on servers to respond with the requested data or functionality.

Visit the following resources to learn more:

- [@article@What is a client?](https://www.techtarget.com/searchenterprisedesktop/definition/client)

## Cloud Certifications

# Cloud Certifications

Cloud certifications are professional credentials that validate an individual's ability to design, deploy, and manage scalable infrastructure and services on platforms like AWS, Microsoft Azure, and Google Cloud. These programs cover essential technical competencies, including virtual networking, identity and access management, storage solutions, and security configurations within public and hybrid cloud environments. Earning these certifications demonstrates proficiency in transitioning traditional on-premises network architectures to cloud-native models while ensuring connectivity, performance, and reliability.

Visit the following resources to learn more:

- [@official@AWS Certified Advanced Networking - Specialty](https://aws.amazon.com/certification/certified-advanced-networking-specialty/)
- [@official@Google Professional Cloud Network Engineer](https://cloud.google.com/learn/certification/cloud-network-engineer)
- [@official@Azure Network Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-network-engineer-associate/)

## Cloud Network Types

# Cloud Network Types

Cloud providers offer several types of virtual network constructs that mirror traditional networking concepts but operate in software. The most fundamental is the Virtual Private Cloud (VPC), a logically isolated section of the cloud where resources are deployed. Within a VPC, public subnets host resources accessible from the Internet, while private subnets contain resources with no direct public exposure. Cloud environments also support concepts like peering connections between VPCs, transit networks for hub-and-spoke architectures, and overlay networks for connecting cloud resources across regions or providers.

Visit the following resources to learn more:

- [@article@What are the different types of cloud computing?](https://cloud.google.com/discover/types-of-cloud-computing?hl=en)
- [@video@Types Of Cloud Computing](https://www.youtube.com/watch?v=1BMO7YkwR6Y)

## Cloud Networking Basics

# Cloud Networking Basics

Cloud networking refers to the networking infrastructure and services delivered through cloud platforms, allowing organizations to build, connect, and secure their resources in the cloud using virtual equivalents of traditional network components. Instead of physical routers, switches, and firewalls, cloud networking uses software-defined resources that can be provisioned, configured, and scaled through APIs and web consoles. Understanding cloud networking is increasingly essential for network engineers as more infrastructure moves away from on-premises data centers and into cloud environments.

Visit the following resources to learn more:

- [@article@What is cloud networking? - Cloudflare](https://www.cloudflare.com/en-gb/learning/cloud/what-is-cloud-networking/)
- [@article@What is cloud networking? - Cisco](https://www.cisco.com/site/us/en/learn/topics/cloud-networking/what-is-cloud-networking.html)
- [@video@Cloud Networking Explained](https://www.youtube.com/playlist?list=PLOspHqNVtKAA_5N3pI49wkH4WsTkeZ_iQ)

## Cloud Routing

# Cloud Routing

Cloud routing refers to how traffic is directed between subnets, virtual networks, on-premises environments, and the Internet within a cloud platform. Each cloud provider uses route tables (collections of rules that determine where traffic destined for specific IP ranges should be sent) to control the flow of packets through the virtual network. Cloud routing also involves dynamic routing protocols through services like AWS Transit Gateway, Azure Route Server, or GCP Cloud Router, which use BGP to exchange routes automatically between cloud and on-premises environments, making large hybrid network architectures manageable without manual route configuration.

Visit the following resources to learn more:

- [@video@Amazon Virtual Private Cloud (VPC) Routing Deep Dive](https://www.youtube.com/watch?v=LJNNMTicv1c)
- [@video@Azure Routing](https://www.youtube.com/watch?v=BUH9kVTrM-8&t=22s)
- [@video@02- Google Cloud Routing: A Complete Guide with Real-World Examples](https://www.youtube.com/watch?v=fby0PSTH3AY)

## Cloud Vpn

# Cloud VPN

A Cloud VPN is a managed service offered by cloud providers that creates encrypted IPSec tunnels between a cloud virtual network and an on-premises network or another cloud environment over the public Internet. It allows organizations to securely extend their private network into the cloud without needing a dedicated physical connection, making it a cost-effective option for hybrid connectivity. Cloud VPNs are suitable for moderate traffic volumes and scenarios where the latency and variability of the public Internet are acceptable, as opposed to dedicated interconnect services that provide more consistent, higher-bandwidth private connections.

Visit the following resources to learn more:

- [@article@Cloud VPN: Secure Remote Access For Modern Workforces](https://www.fortinet.com/resources/cyberglossary/cloud-vpn)
- [@article@What Is a Cloud VPN? | Cloud-Based Remote Access VPNs Explained](https://www.paloaltonetworks.com/cyberpedia/what-is-a-cloud-vpn)

## Cloud

# Cloud

In networking, the cloud refers to a model of delivering computing resources, such as servers, storage, databases, and networking, over the Internet on a pay-as-you-go basis. Rather than owning and maintaining physical infrastructure, organizations can provision and scale resources through cloud providers like AWS, Azure, or Google Cloud. This shifts network design considerations to include connectivity to cloud environments, hybrid architectures, and cloud-native security.

Visit the following resources to learn more:

- [@article@What is Cloud Networking?](https://aws.amazon.com/what-is/cloud-networking/)
- [@article@What is cloud networking?](https://www.cloudflare.com/en-gb/learning/cloud/what-is-cloud-networking/)

## Cloudflare

# Cloudflare

Cloudflare's DNS resolver, known by its address 1.1.1.1, is a public DNS service focused on speed and privacy. It is consistently ranked among the fastest DNS resolvers in the world and does not log user queries for advertising purposes. Cloudflare also supports DNS over HTTPS (DoH) and DNS over TLS (DoT) to encrypt DNS queries and prevent snooping.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Cloudflare Roadcamp](https://roadmap.sh/cloudflare)
- [@official@Cloudflare](https://www.cloudflare.com/en-gb/)

## Common Networks Issues

# Common Network Issues

Common network issues are recurring problems that network engineers encounter regularly across different environments and infrastructures. These include IP address conflicts where two devices share the same address, DNS resolution failures where domain names cannot be translated to IP addresses, default gateway misconfigurations that prevent traffic from leaving the local network, duplex and speed mismatches between connected devices causing performance degradation, VLAN misconfigurations that isolate devices unintentionally, routing loops where packets cycle endlessly between routers, and high latency or packet loss caused by congestion, faulty hardware, or misconfigured QoS policies.

Visit the following resources to learn more:

- [@article@7 Common Network Issues and How to Resolve Them Fast](http://cbtnuggets.com/blog/technology/networking/7-common-network-issues-and-how-to-resolve-them-fast)
- [@article@9 common network issues and how to fix them](https://www.techtarget.com/searchnetworking/answer/What-are-the-3-most-common-network-issues-to-troubleshoot)
- [@video@Network Troubleshooting for Beginners: Fix Your Internet Step-by-Step](https://www.youtube.com/watch?v=czXiP1mYtPE)

## Comptia Network

# CompTIA Network+

The CompTIA Network+ is a highly sought-after certification for IT professionals who aim to build a solid foundation in networking concepts and practices. This certification is vendor-neutral, meaning that it covers a broad range of knowledge that can be applied to various network technologies, products, and solutions. The Network+ certification is designed for beginners in the world of IT networking, and it is recommended that you first obtain the CompTIA A+ certification before moving on to Network+.

Visit the following resources to learn more:

- [@official@CompTIA Network+](https://www.comptia.org/certifications/network)
- [@video@CompTIA Network+ Course](https://www.youtube.com/watch?v=xmpYfyNmWbw)

## Comptia Security

# CompTIA Security+

CompTIA Security+ is a global certification that establishes the baseline knowledge required to perform core security functions and pursue an IT security career. It covers foundational principles of network security, including threat identification, risk management, cryptography, and identity and access management. Earning this credential validates an individual's ability to secure devices, applications, and networks against common vulnerabilities and cyberattacks.

Visit the following resources to learn more:

- [@official@CompTIA Security+ Website](https://www.comptia.org/certifications/security)
- [@video@CompTIA SY0-701 Security+ Exam Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv)
- [@video@CompTIA Security+ Course](https://www.youtube.com/watch?v=yLf2jRY39Rc&list=PLIhvC56v63IIyU0aBUed4qwP0nSCORAdB)

## Data Link

# Data Link

The Data Link layer is the second layer of the OSI model, responsible for node-to-node data transfer and error detection within a single network segment. It organizes raw bits from the Physical layer into frames and uses MAC addresses to identify devices on the local network. This layer is divided into two sublayers: the Logical Link Control (LLC) and the Media Access Control (MAC).

Visit the following resources to learn more:

- [@article@Understanding Layers 2 and 3 of the OSI Model](https://www.comptia.org/en-us/blog/layers-2-and-3-osi-model/)
- [@video@Networking Fundamentals: OSI 7 - Layer 2 - the data link layer - Part 1](https://www.youtube.com/watch?v=c5lV995dSAA)
- [@video@Networking Fundamentals: OSI 7 - Layer 2 - the data link layer - Part 2](https://www.youtube.com/watch?v=Q_55Lryu9zc)

## Datadog

# Datadog

Datadog is a cloud-based observability platform that provides monitoring, logging, and security capabilities across infrastructure, applications, and networks in a single unified interface. It collects metrics, traces, and logs from servers, containers, cloud services, and network devices, correlating them to give a complete picture of system health. For network engineers, Datadog offers network performance monitoring (NPM) features that provide visibility into traffic flows, latency between services, and the health of network paths across on-premises and cloud environments.

Visit the following resources to learn more:

- [@official@Datadog](https://www.datadoghq.com/)
- [@official@Datadog Docs](https://docs.datadoghq.com/)

## Default Gateway

# Default Gateway

A default gateway is the IP address of the router that a device uses to send traffic destined for networks outside its own local subnet. When a device does not have a specific route for a destination, it forwards the packet to the default gateway, which then handles the routing decision. In most home and office networks, the default gateway is the IP address of the local router.

Visit the following resources to learn more:

- [@article@What is a default gateway, and how can you find its address?](https://nordvpn.com/blog/what-is-a-default-gateway/?srsltid=AfmBOop1EOdHkR__w-7OxSPfTRdWONwCm-BmXoLZ5tadeiF4o5ZASfa-)
- [@article@What is Default Gateway?](https://www.cbtnuggets.com/blog/technology/networking/what-is-default-gateway)
- [@video@Default Gateway Explained](https://www.youtube.com/watch?v=pCcJFdYNamc)

## Dhcp

# DHCP

DHCP, or Dynamic Host Configuration Protocol, is a network management protocol that automatically assigns IP addresses and other network configuration parameters to devices when they join a network. Without DHCP, administrators would need to manually configure the IP address, subnet mask, gateway, and DNS settings on every device. DHCP simplifies network management by handling these assignments dynamically from a central server or router.

Visit the following resources to learn more:

- [@article@What is DHCP? and Why is it important?](https://efficientip.com/glossary/what-is-dhcp-and-why-is-it-important/)
- [@video@DHCP Explained - Dynamic Host Configuration Protocol](https://www.youtube.com/watch?v=e6-TaH5bkjo)

## Dns

# DNS

DNS, or Domain Name System, is the system that translates human-readable domain names like [www.example.com](http://www.example.com) into IP addresses that computers use to identify each other on the network. Without DNS, users would need to memorize IP addresses to visit websites or access online services. DNS operates as a distributed, hierarchical database spread across many servers around the world.

Visit the following resources to learn more:

- [@article@What is DNS? | How DNS works](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [@video@How a DNS Server (Domain Name System) works.](https://www.youtube.com/watch?v=mpQZVYPuDGU)

## Dos  Ddos

# DoS & DDoS

A DoS (Denial of Service) attack is an attempt to make a network resource or service unavailable by overwhelming it with a flood of illegitimate traffic or requests. A DDoS (Distributed Denial of Service) attack is the same concept but launched from many different sources simultaneously — often thousands of compromised machines in a botnet — making it much harder to block. These attacks do not typically steal data but can cause significant downtime and financial damage to the targeted organization.

Visit the following resources to learn more:

- [@article@DoS Attack vs DDoS Attack](https://www.fortinet.com/resources/cyberglossary/dos-vs-ddos)
- [@video@DoS vs DDoS Attacks: What's the Difference? | Animated](https://www.youtube.com/watch?v=nw2SBTgLLwc)

## Dynatrace

# Dynatrace

Dynatrace is an AI-powered observability platform that automatically discovers, maps, and monitors the full technology stack, from infrastructure and networks to applications and user experience. Its standout feature is the Davis AI engine, which automatically detects anomalies, determines root causes, and reduces alert noise by correlating data across the entire environment. While primarily used by application and platform teams, network engineers in large enterprises use Dynatrace to gain visibility into how network performance impacts application behavior and end-user experience.

## Eigrp

# EIGRP

EIGRP, or Enhanced Interior Gateway Routing Protocol, is an advanced distance-vector routing protocol developed by Cisco that combines features of both distance-vector and link-state protocols. It uses a composite metric based on bandwidth, delay, load, and reliability to calculate the best route and converges faster than traditional distance-vector protocols. EIGRP is efficient in terms of bandwidth usage and CPU load, making it popular in Cisco-based enterprise networks.

Visit the following resources to learn more:

- [@article@Introduction to EIGRP](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/13669-1.html)
- [@article@What is EIGRP (Enhanced Interior Gateway Routing Protocol)?](https://www.cbtnuggets.com/blog/technology/networking/what-is-eigrp)
- [@video@EIGRP Explained | Step by Step](https://www.youtube.com/watch?v=QyymlFWDEgM)

## Encryption Basics

# Encryption Basics

Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) using an algorithm and a key, so that only authorized parties with the correct key can decrypt and read it. It is the foundation of data security in networking, protecting information in transit and at rest from unauthorized access. The two main types are symmetric encryption, where the same key is used to encrypt and decrypt, and asymmetric encryption, which uses a pair of public and private keys.

Visit the following resources to learn more:

- [@course@Encryption Course](https://www.internetsociety.org/learning/encryption/)
- [@article@What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)
- [@video@Cryptography Full Course Part 1](https://www.youtube.com/watch?v=j_8PLI_wCVU)
- [@video@Cryptography Full Course Part 2](https://www.youtube.com/watch?v=s5yza-s0bhM)

## Eve Ng

# EVE-NG

EVE-NG (Emulated Virtual Environment - Next Generation) is a multi-vendor network emulation platform that allows users to create virtual network topologies. It runs as a virtual machine on a server, enabling engineers to drag and drop various virtual appliances, such as routers, switches, and firewalls, into a workspace to simulate complex enterprise environments. It provides a functional environment to test configurations, troubleshoot connectivity, and practice new protocols without the need for physical hardware.

Visit the following resources to learn more:

- [@official@EVE-NG](https://www.eve-ng.net/)
- [@video@EVE NG Installation](https://www.youtube.com/watch?v=FDbgTlr-tnw)

## Failover

# Failover

Failover is the process by which a system automatically switches to a backup server, network path, or resource when the primary one becomes unavailable due to failure or maintenance. The goal is to minimize downtime and ensure continuity of service without requiring manual intervention. Failover configurations can be active-passive, where the backup sits idle until needed, or active-active, where multiple systems share the load and take over seamlessly if one fails.

Visit the following resources to learn more:

- [@article@Load Balancing vs Failover: An Overview](https://www.parallels.com/blogs/ras/load-balancing-vs-failover/?srsltid=AfmBOoqc5D3jnDadoZi4MfxBshZhvanecpzP_nXz_PbIt6NpAfEYs4pN)
- [@video@Fail-over and High-Availability (Explained by Example)](https://www.youtube.com/watch?v=Zgy1miPsTNs)

## Firewalls

# Firewalls

A firewall is a network security device or software that monitors and controls incoming and outgoing network traffic based on predefined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, blocking traffic that does not meet the specified criteria. Firewalls are a foundational component of network security and can be implemented in hardware, software, or as a cloud-based service.

Visit the following resources to learn more:

- [@article@What is a firewall?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)
- [@article@What is a firewall? How network firewalls work](https://www.cloudflare.com/en-gb/learning/security/what-is-a-firewall/)
- [@video@What is a Firewall?](http://youtube.com/watch?v=kDEX1HXybrU)

## Frame

# Frame

A frame is a unit of data transmission at the Data Link layer of the OSI model. It wraps raw bits into a structured format that includes source and destination MAC addresses, the data payload, and error-checking information. Frames are used to move data between devices on the same local network segment.

Visit the following resources to learn more:

- [@article@Frames and Packets in Computer Networks ✉️📦📮](https://www.patreon.com/posts/frames-and-in-101725193)
- [@video@Packets and Frames — The containers of networking](https://www.youtube.com/watch?v=-hkF4OyxzNQ)

## Ftp  Sftp

# FTP / SFTP

FTP (File Transfer Protocol) is a standard protocol used to transfer files between a client and a server over a network. It operates over two channels (one for commands and one for data), but transmits information in plain text, making it insecure. SFTP (SSH File Transfer Protocol) is a secure alternative that encrypts both commands and data using SSH, making it the preferred choice for transferring sensitive files.

Visit the following resources to learn more:

- [@article@FTP vs SFTP: What’s the Difference? Which One Should You Use?](https://kinsta.com/blog/ftp-vs-sftp/)
- [@video@FTP (File Transfer Protocol), SFTP, TFTP Explained.](https://www.youtube.com/watch?v=tOj8MSEIbfA)

## Gcp

# GCP

Google Cloud Platform (GCP) takes a unique approach to networking with its globally distributed Virtual Private Cloud (VPC), which, unlike AWS and Azure, operates as a single global resource rather than being tied to a specific region. Key networking services include Cloud Router for dynamic routing between on-premises and GCP networks using BGP, Cloud VPN and Cloud Interconnect for hybrid connectivity, Cloud Load Balancing for distributing traffic globally across regions, Firewall Rules for controlling traffic at the network level, and Cloud DNS for scalable domain name resolution. GCP's network is built on the same private global fiber infrastructure that powers Google's own services, giving it a performance advantage for traffic that can be routed through Google's backbone rather than the public Internet.

Visit the following resources to learn more:

- [@course@Networking in Google Cloud: Fundamentals](https://www.skills.google/course_templates/35)
- [@video@Cloud OnAir: Google Cloud Networking 101](https://www.youtube.com/watch?v=0hN-dyOV10c&t=146s)
- [@video@Networking End to End](https://www.youtube.com/playlist?list=PLIivdWyY5sqJ0oXcnZYqOnuNRsLF9H48u)

## Glbp

# GLBP

GLBP, or Gateway Load Balancing Protocol, is a Cisco proprietary protocol that goes beyond simple redundancy by also distributing traffic across multiple routers simultaneously. Unlike HSRP and VRRP, where only one router actively handles traffic at a time, GLBP allows all routers in the group to forward traffic, improving both availability and bandwidth utilization. Each router in the group shares the same virtual IP address but is assigned a different virtual MAC address, allowing traffic to be load-balanced across all active gateways.

Visit the following resources to learn more:

- [@article@GLBP - Gateway Load Balancing Protocol](https://www.cisco.com/en/US/docs/ios/12_2t/12_2t15/feature/guide/ft_glbp.html)
- [@article@Gateway Load Balancing Protocol (GLBP)](https://www.networkacademy.io/ccna/network-services/gateway-load-balancing-protocol-glbp)
- [@video@GLBP Operation (Cisco SWITCH (300-115) Complete Video Course)](https://www.youtube.com/watch?v=ujApoqozzsE)

## Gns3

# GNS3

GNS3 is a graphical network simulation software that allows users to design, configure, and test complex network topologies in a virtual environment. It works by combining real Cisco IOS images or open-source network operating systems with virtual machines to emulate hardware behavior, enabling engineers to build lab environments without the need for physical equipment. It uses a drag-and-drop interface that facilitates the creation and troubleshooting of routed and switched networks, making it a standard tool for study, certification preparation, and proof-of-concept testing.

Visit the following resources to learn more:

- [@official@GNS3](https://www.gns3.com/)
- [@opensource@gns3](https://github.com/GNS3/gns3-gui)
- [@video@GNS3 Installation](https://www.youtube.com/watch?v=Ibe3hgP8gCA&list=PLhfrWIlLOoKNFP_e5xcx5e2GDJIgk3ep6)

## Google

# Google Public DNS

Google Public DNS is a global Domain Name System (DNS) resolution service that translates human-readable domain names into numerical IP addresses. It functions as a recursive name server, allowing users and network devices to perform lookups more efficiently by leveraging Google's massive infrastructure for faster responses and enhanced security. By utilizing Anycast routing, it directs DNS queries to the nearest data center, minimizing latency and providing a highly available, reliable alternative to standard ISP-provided DNS resolvers.

Visit the following resources to learn more:

- [@official@Google  Coud DNS](https://cloud.google.com/dns)

## Grafana

# Grafana

Grafana is an open-source data visualization and dashboarding platform that connects to a wide range of data sources, including Prometheus, InfluxDB, Elasticsearch, and SNMP collectors, and displays the data in customizable, real-time dashboards. In network engineering, it is commonly used to visualize metrics like interface traffic, packet loss, latency, and device health collected from monitoring tools. Grafana does not collect data itself but excels at making complex time-series data understandable through graphs, gauges, and alerts.

Visit the following resources to learn more:

- [@official@Grafana](https://grafana.com/)
- [@official@Grafana Webinars and Videos](https://grafana.com/videos/)
- [@video@Server Monitoring // Prometheus and Grafana Tutorial](https://www.youtube.com/watch?v=9TJx7QTrTyo)

## Greipsec Tunnels

# GRE / IPSec Tunnels

GRE, or Generic Routing Encapsulation, is a tunneling protocol that wraps packets from one protocol inside packets of another, allowing traffic to be carried across networks that would not normally support it. On its own, GRE provides no encryption, so it is commonly combined with IPSec, which adds authentication and encryption to secure the tunnel. Together, GRE over IPSec is widely used to create flexible, secure connections between sites while supporting routing protocols and multicast traffic that plain IPSec tunnels cannot carry on their own.

Visit the following resources to learn more:

- [@article@Encrypted GRE Tunnel with IPSEC](https://networklessons.com/vpn/encrypted-gre-tunnel-with-ipsec)
- [@video@Net Talk - GRE over IPsec](https://www.youtube.com/watch?v=anm84IVNBZU)

## High Availability

# High Availability

High Availability refers to systems and network configurations designed to ensure continuous operational uptime by minimizing service disruptions caused by hardware failures, software errors, or maintenance. It is typically achieved through redundancy, where backup components or secondary paths are ready to take over automatically if the primary system fails.

## Host

# Host

A host is any device connected to a network that has an IP address and can send or receive data. This includes computers, servers, printers, smartphones, and any other networked device. The term is used broadly to refer to any endpoint that participates in network communication.

Visit the following resources to learn more:

- [@article@What is a Host: How It Works in Networking](https://www.temok.com/blog/what-is-a-host)
- [@video@What is Web Hosting and How Does It Work?](https://www.youtube.com/watch?v=H8oAvyqQwew)

## Hotspot And Tethering

# Hotspot and Tethering

A hotspot is a physical location or device that provides wireless Internet access to other devices, typically by sharing a cellular data connection. Tethering is the act of connecting a device, such as a laptop, to a smartphone's mobile data connection via Wi-Fi, USB, or Bluetooth to access the Internet. Both concepts are relevant for network engineers when designing mobile connectivity solutions or troubleshooting remote access scenarios.

Visit the following resources to learn more:

- [@article@Tethering vs. a hotspot: What’s the difference?](https://saily.com/blog/tethering-vs-hotspot/)
- [@video@What is a Hotspot?](https://www.youtube.com/watch?v=ktxC3vDukbc)
- [@video@Tethering and Personal Hotspots](https://www.youtube.com/watch?v=07r7nPeNDm0)

## How Does The Internet Work

# How does the Internet Work?

The Internet is a massive global network of interconnected computers and devices that communicate by sending data to each other using a shared set of rules. When you visit a website, your device sends a request that travels through multiple routers and networks until it reaches the server hosting that site, which then sends the data back to your screen. This exchange happens through a system of protocols —most notably TCP/IP— that break data into small packets, route them across the network, and reassemble them at the destination.

Visit the following resources to learn more:

- [@article@How does the internet work?](https://roadmap.sh/guides/what-is-internet)
- [@article@How does the Internet work? | Cloudflare](https://www.cloudflare.com/en-gb/learning/network-layer/how-does-the-internet-work/)
- [@article@How does the Internet work? - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work)

## Hsrp

# HSRP

HSRP, or Hot Standby Router Protocol, is a Cisco proprietary protocol that provides gateway redundancy by allowing two or more routers to work together as a single virtual router. One router acts as the active gateway handling all traffic, while one or more standby routers monitor it and take over automatically if the active router fails. End devices are configured to use the shared virtual IP address as their default gateway, so they experience no disruption when a failover occurs.

Visit the following resources to learn more:

- [@article@Hot Standby Router Protocol (HSRP)](http://networklessons.com/ip-services/hot-standby-router-protocol-hsrp)
- [@video@Understanding (and Configuring) HSRP](https://www.youtube.com/watch?v=-IaUa4-6ZeI&pp=ygUESFNSUA%3D%3D)

## Http  Https

# HTTP / HTTPS

HTTP (HyperText Transfer Protocol) is the foundation of data communication on the web, defining how messages are formatted and transmitted between browsers and servers. HTTPS is the secure version of HTTP, adding an SSL/TLS encryption layer to protect data from being intercepted during transmission. Most modern websites use HTTPS to ensure privacy and data integrity for their users.

Visit the following resources to learn more:

- [@article@What’s the Difference Between HTTP and HTTPS?](https://aws.amazon.com/compare/the-difference-between-https-and-http/)
- [@video@SSL, TLS, HTTP, HTTPS Explained](https://www.youtube.com/watch?v=hExRDVZHhig)

## Hub

# Hub

A hub is a basic network device that connects multiple devices in a LAN and broadcasts incoming data to all connected ports, regardless of the intended recipient. This makes hubs simple but inefficient, as all devices receive all traffic, even if it is not meant for them. Hubs have largely been replaced by switches, which are smarter and handle traffic more efficiently.

Visit the following resources to learn more:

- [@article@What is a hub?](https://www.lenovo.com/us/en/glossary/what-is-a-hub/?orgRef=https%253A%252F%252Fwww.google.com%252F&srsltid=AfmBOorUVQYz_rnn0AMWBhjhWbGypNf7SE3oHeDSXPYS3hsKpIKEFZGD)
- [@video@Hub, Switch, & Router Explained - What's the difference?](https://www.youtube.com/watch?v=1z0ULvg_pW8&t=20s)

## Ids  Ips

# IDS / IPS

An IDS (Intrusion Detection System) monitors network traffic for suspicious patterns and known attack signatures, alerting administrators when potential threats are detected without taking direct action. An IPS (Intrusion Prevention System) goes a step further by automatically blocking or dropping malicious traffic in real time based on the same detection mechanisms. Together, they provide visibility into network threats and an active layer of defense against intrusions.

Visit the following resources to learn more:

- [@article@Intrusion Detection and Prevention Systems (IDS/IPS)](https://www.group-ib.com/resources/knowledge-hub/ids/)
- [@video@IDS vs IPS: Which to Use and When](https://www.youtube.com/watch?v=wQSd_piqxQo)

## Infrastructure As Code

# Infrastructure as Code

Infrastructure as Code (IaC) is the practice of managing and provisioning infrastructure — including networks, servers, and cloud resources — through machine-readable configuration files rather than manual processes or interactive tools. Instead of clicking through a web console or typing commands into a CLI to set up a network, IaC lets you write code that describes exactly what the infrastructure should look like, check that code into version control, and apply it automatically and repeatably. This brings software development practices like version control, code review, and automated testing to infrastructure management, making changes more reliable, auditable, and consistent across environments

Visit the following resources to learn more:

- [@article@What Is Infrastructure as Code?](https://www.cisco.com/site/us/en/learn/topics/computing/what-is-iac.html)
- [@article@Infrastructure-as-Code (IaC): Benefits And Best Practices](https://www.fortinet.com/resources/cyberglossary/infrastructure-as-code)
- [@video@What is Infrastructure as Code?](https://www.youtube.com/watch?v=zWw2wuiKd5o)

## Internet

# Internet

The Internet layer of the TCP/IP model corresponds to the Network layer of the OSI model and is responsible for logical addressing and routing packets across networks. The primary protocol at this layer is IP (Internet Protocol), which assigns addresses to packets and determines how they are routed toward their destination. ICMP and ARP also operate at this layer.

## Introduction

# Introduction

A network engineer is a technology professional responsible for designing, building, and maintaining the communication infrastructure that allows computers and devices to exchange data. This includes planning how networks are structured, selecting and configuring hardware like routers and switches, troubleshooting connectivity issues, and ensuring the network remains secure and reliable. Network engineers work across a wide range of environments and must understand both the theoretical principles behind how data travels and the practical skills needed to implement and manage real-world systems.

Visit the following resources to learn more:

- [@article@Network Engineer - Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/tech-roles/network-engineer.html)
- [@article@What Is a Network Engineer?](https://www.indeed.com/career-advice/finding-a-job/what-is-a-network-engineer)
- [@video@What Does A Network Engineer Actually Do](https://www.youtube.com/watch?v=JpiCwQKb0PM)

## Ip Address

# IP Address

An IP address is a numerical label assigned to each device on a network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host and providing its location in the network for routing purposes. IP addresses come in two versions: IPv4, which uses a 32-bit format, and IPv6, which uses a 128-bit format to accommodate a much larger number of devices.

Visit the following resources to learn more:

- [@article@What Is an IP Address?](https://www.coursera.org/articles/ip-address)
- [@video@what is an IP Address?](https://www.youtube.com/watch?v=5WfiTHiU4x8)

## Ip Addressing

# IP Addressing

IP addressing is the system used to assign unique numerical identifiers to devices on a network so they can communicate with each other. Every device connected to a network needs an IP address, which tells other devices where to send data. IP addresses come in two versions — IPv4 and IPv6 — and can be assigned statically by an administrator or dynamically by a DHCP server.

Visit the following resources to learn more:

- [@article@IP Addressing And Its Classification In Computer Networks](https://medium.com/@mustafa.bohra20/ip-addressing-and-its-classification-in-computer-networks-6b7112439a87)
- [@article@IP address - Wikipedia](https://en.wikipedia.org/wiki/IP_address)
- [@video@what is an IP Address?](https://www.youtube.com/watch?v=5WfiTHiU4x8)

## Ip Vs Mac Vs Arp

# IP vs MAC vs ARP

An IP address is a logical address used to identify a device across networks and is assigned by software, while a MAC address is a physical address burned into the network interface hardware, used for communication within a local network segment. ARP (Address Resolution Protocol) bridges the two by resolving a known IP address to its corresponding MAC address so that data can be delivered on the local network. Together, these three concepts work in layers: IP handles routing across networks, MAC handles delivery within a network, and ARP connects them.

Visit the following resources to learn more:

- [@article@ARP – Associating IP with MAC addresses](https://www.homenethowto.com/switching/arp-mac-ip/)
- [@article@Understanding MAC Addresses & ARP](https://www.youtube.com/watch?v=R41uQv_Ap0s)
- [@article@How does ARP work with IP and MAC addresses](https://www.youtube.com/watch?v=TOYgyYpOK4I)

## Ipconfig  Ifconfig

# ipconfig / ifconfig

ipconfig (on Windows) and ifconfig (on Linux and macOS) are command-line tools used to view and manage the network configuration of a device's interfaces. They display information such as the assigned IP address, subnet mask, default gateway, and MAC address for each network adapter. They are among the first tools used when troubleshooting a connectivity issue at the device level, confirming whether the device has a valid network configuration.

Visit the following resources to learn more:

- [@article@Ipconfig – network ad­min­is­tra­tion via the command line](https://www.ionos.com/digitalguide/server/configuration/ipconfig/)
- [@video@IPCONFIG Explained - Flush DNS Cache](https://www.youtube.com/watch?v=ZKhorleA5aA)

## Ipsec Vs Ssl Vpn

# IPSec vs SSL VPN

IPSec (Internet Protocol Security) VPNs operate at the network layer, encrypting all IP traffic between two endpoints and are commonly used for site-to-site connections between networks. SSL/TLS VPNs operate at the application layer, typically accessible through a web browser or lightweight client, and are better suited for remote individual user access. The choice between the two depends on the use case: IPSec is generally preferred for permanent network-to-network tunnels, while SSL VPNs offer more flexibility for end-user remote access.

Visit the following resources to learn more:

- [@article@VPN IPsec vs. VPN SSL](https://www.cloudflare.com/es-es/learning/network-layer/ipsec-vs-ssl-vpn/)
- [@video@What Are the Differences Between SSL VPN and IPsec VPN?](https://www.youtube.com/watch?v=At44WU9EKjQ)

## Ipv4 Vs Ipv6

# IPv4 vs IPv6

IPv4 is the original version of the Internet Protocol, using 32-bit addresses written in dotted decimal notation (e.g., 192.168.1.1), allowing for about 4.3 billion unique addresses. IPv6 was introduced to solve the problem of IPv4 address exhaustion, using 128-bit addresses written in hexadecimal (e.g., 2001:0db8::1), providing an astronomically larger address space. Beyond address size, IPv6 also introduces improvements in routing efficiency, auto-configuration, and built-in security features.

Visit the following resources to learn more:

- [@article@What’s the Difference Between IPv4 and IPv6?](https://aws.amazon.com/compare/the-difference-between-ipv4-and-ipv6/)
- [@article@IPv4 vs IPv6: What’s The Difference Between the Two Protocols?](https://kinsta.com/blog/ipv4-vs-ipv6/)
- [@video@Internet Protocol - IPv4 vs IPv6 as Fast As Possible](https://www.youtube.com/watch?v=aor29pGhlFE)

## Lan

# LAN

A LAN, or Local Area Network, is a network that connects devices within a limited geographic area, such as a home, office, or building. LANs typically use Ethernet cables or Wi-Fi to link computers, printers, and other devices, allowing them to share files and resources at high speeds. Because all devices are physically close together, LANs offer low latency and high bandwidth compared to larger networks.

Visit the following resources to learn more:

- [@article@What Is a LAN?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-lan-local-area-network.html)
- [@video@LAN, WAN, SUBNET - EXPLAINED](https://www.youtube.com/watch?v=NyZWSvSj8ek&t=40s)
- [@video@LAN vs. WAN: What's the Difference? | Network Essentials](https://www.youtube.com/watch?v=5OoX_cRLaNM)

## Latency

# Latency

Latency is the time it takes for a data packet to travel from its source to its destination, usually measured in milliseconds. Low latency means data arrives quickly, which is critical for real-time applications like video calls and online gaming. Latency is influenced by factors such as physical distance, network congestion, and the number of hops between devices.

Visit the following resources to learn more:

- [@article@What is Network Latency?](https://aws.amazon.com/what-is/latency/)
- [@video@What is Latency? (In about a minute)](https://www.youtube.com/watch?v=S0NKk86HRdg&pp=ygUZd2hhdCBpcyBhIGxhdGVuY3kgbmV0b3drcg%3D%3D)

## Least Connections

# Least Connections

The Least Connections algorithm is a load-balancing method that routes each new request to the server with the fewest active connections at that moment. This approach is more adaptive than Round Robin because it accounts for varying request durations and server load. It is particularly useful when requests have significantly different processing times, ensuring that no single server gets backed up while others are idle.

Visit the following resources to learn more:

- [@article@Types of load balancing algorithms](https://www.cloudflare.com/en-gb/learning/performance/types-of-load-balancing-algorithms/)
- [@video@LTM Load Balancing Algorithms: Least Connections Types](https://www.youtube.com/watch?v=tAAmZ3bz8AA)

## Link Aggregation

# Link Aggregation

Link aggregation is a technique that combines multiple physical network connections between two devices into a single logical link, increasing bandwidth and providing redundancy. If one physical link fails, the others continue to carry traffic without interruption. It is standardized under IEEE 802.3ad (LACP) and is commonly used between switches, servers, and storage devices to improve both performance and reliability.

Visit the following resources to learn more:

- [@article@Essential FAQs about Link Aggregation, LAG, and LACP](https://www.fs.com/blog/understanding-link-aggregation-and-lacp-faqs-1262.html)
- [@video@Cisco CCNA - What is LACP In Networking?](https://www.youtube.com/watch?v=z6hStQ3g4ck)
- [@video@What is LACP (Link Aggregation Control Protocol)?](https://www.youtube.com/watch?v=gtDkqhP6Gvc)

## Linux For Networking

# Linux for Networking

Linux is the operating system that powers the majority of the world's network infrastructure, from routers and firewalls to servers and cloud platforms. Network engineers working with Linux need to understand how to configure network interfaces, manage routing tables, control firewall rules, monitor traffic, and automate tasks through the command line. Unlike GUI-based systems, Linux gives engineers direct, low-level control over every aspect of network behavior, making it an essential skill for anyone working in modern networking environments.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Linux Roadmap](https://roadmap.sh/linux)
- [@course@Linux Networking - Basics and Beyond Specialization](https://www.coursera.org/specializations/pearson-linux-networking-basics-and-beyond)
- [@article@Linux for Network Engineers – Lesson 1: Getting Started](https://richardkilleen.co.uk/blog/linux/linux-for-network-engineers-lesson-1-getting-started/)
- [@video@Linux For Network Engineers - INTRO](https://www.youtube.com/watch?v=Wz9eAdNMVUs&list=PLhHT1w6sU7CMj-NKi-wQrC0DM0WadS4Bq)

## Load Balancer

# Load Balancer

A load balancer is a device or software that distributes incoming network traffic across multiple servers to prevent any single server from becoming overwhelmed. By spreading the workload, load balancers improve application availability, responsiveness, and fault tolerance. They can operate at Layer 4 (based on IP and TCP/UDP) or Layer 7 (based on application-level data like HTTP headers and URLs).

Visit the following resources to learn more:

- [@article@What is Network Load Balancing? Understanding Traffic Distribution](https://www.digitalocean.com/resources/articles/network-load-balancing)
- [@video@Load Balancer Explained](https://www.youtube.com/watch?v=1fN2UDbtGDQ)

## Load Balancing

# Load Balancing

Cloud load balancing distributes incoming network traffic across multiple backend resources, such as virtual machines, containers, or serverless functions, to ensure no single resource is overwhelmed and that applications remain available even if individual components fail. Unlike hardware load balancers in traditional data centers, cloud load balancers are fully managed services that scale automatically with traffic and require no physical maintenance. Cloud providers offer multiple types, including application load balancers that operate at Layer 7 and make routing decisions based on HTTP content, and network load balancers that operate at Layer 4 for high-performance, low-latency traffic distribution.

Visit the following resources to learn more:

- [@article@What is cloud load balancing? | LBaaS](https://www.cloudflare.com/en-gb/learning/performance/cloud-load-balancing-lbaas/)
- [@video@Cloud Load Balancing](https://www.youtube.com/watch?v=egkxWAmw4BQ)

## Mac Address Tables

# MAC Address Tables

A MAC address table, also called a CAM (Content Addressable Memory) table, is a database maintained by a network switch that maps MAC addresses to the specific ports those devices are connected to. When a frame arrives, the switch looks up the destination MAC address in this table to determine which port to forward the frame to. If the address is not found, the switch floods the frame to all ports until it learns the correct mapping.

Visit the following resources to learn more:

- [@article@What Is a MAC Address Table?](https://jumpcloud.com/it-index/what-is-a-mac-address-table)
- [@video@How a Switch Forwards and Builds the MAC Address Table](https://www.youtube.com/watch?v=sdYDLip2ANI)
- [@video@MAC Address Explained](https://www.youtube.com/watch?v=TIiQiw7fpsU)

## Mac Address

# Mac Address

A MAC address, or Media Access Control address, is a unique hardware identifier assigned to a network interface card (NIC) by its manufacturer. It operates at the Data Link layer and is used to identify devices within the same local network segment. Unlike IP addresses, MAC addresses are typically fixed and do not change as a device moves between networks.

Visit the following resources to learn more:

- [@article@Mac Address: Explained](https://licensespring.com/blog/glossary/mac-address)
- [@video@MAC Address Explained](https://www.youtube.com/watch?v=TIiQiw7fpsU)

## Man

# MAN

A MAN, or Metropolitan Area Network, is a network that covers a geographic area roughly the size of a city or a large campus. It is larger than a LAN but smaller than a WAN, often used by organizations or service providers to connect multiple buildings or locations within the same metropolitan region. MANs typically use fiber optic cables or wireless links to achieve high-speed connectivity across the area.

Visit the following resources to learn more:

- [@article@What is a metropolitan area network (MAN)?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-metropolitan-area-network/)
- [@video@Network Types: LAN, WAN, PAN, CAN, MAN, SAN, WLAN](https://www.youtube.com/watch?v=4_zSIXb7tLQ)

## Methdologies

# Troubleshooting Methodologies

A troubleshooting methodology is a structured approach to diagnosing network problems that prevents guesswork and reduces time to resolution. The most common approaches are bottom-up (starting at the Physical layer and working up through the OSI model), top-down (starting at the Application layer and working down), and divide and conquer (starting at a middle layer based on available evidence). Most methodologies follow a general cycle: identify the problem, establish a theory of probable cause, test the theory, create a plan of action, implement the fix, verify full functionality, and document the outcome.

Visit the following resources to learn more:

- [@article@Network Troubleshooting Methodology and Techniques](https://study-ccna.com/network-troubleshooting-methodology-techniques/)
- [@article@Most Common Network Troubleshooting Steps, Techniques and Best Practices](https://www.dnsstuff.com/network-troubleshooting-steps)

## Mlps Vpn

# MPLS VPN

MPLS VPN is a technique that uses Multiprotocol Label Switching to create private, isolated network connections over a shared provider backbone. Service providers use it to offer private WAN connectivity to enterprise customers, where each customer's traffic is logically separated from others, even though it travels across the same physical infrastructure. MPLS VPNs are highly scalable and offer predictable performance, making them a popular choice for connecting multiple branch offices across a wide area network.

Visit the following resources to learn more:

- [@article@MPLS VPN services, types, and benefits](https://nordvpn.com/blog/mpls-vpn)
- [@article@MPLS](https://networklessons.com/mpls)
- [@video@Understanding L2 VPNs in MPLS](https://www.youtube.com/watch?v=PErdlfW-wkQ)

## Mobile Networks

# Mobile Networks

Mobile networks are wireless communication systems that provide connectivity to devices over large geographic areas through a network of cell towers and base stations. They have evolved through generations, from 2G and 3G through 4G to 5G, each offering faster speeds, lower latency, and greater capacity. Understanding mobile network architecture is increasingly important as more devices rely on cellular connectivity and as 5G enables new enterprise and IoT use cases.

Visit the following resources to learn more:

- [@article@What is 5G?](https://aws.amazon.com/what-is/5g/)
- [@video@Every Mobile Network Explained in 8 Minutes](https://www.youtube.com/watch?v=4BZg9YQy5WY)
- [@video@Cellular Mobile Communication (2G,3G,4G,5G) - A Crash Course](https://www.youtube.com/watch?v=m1dTsqElxS0&list=PL-XjHn7CHrmTjCaAVPTYQ1iMGEfq3x7j2)

## Modems

# Modems

A modem (modulator-demodulator) is a device that converts digital data from a computer into a format suitable for transmission over a communication medium such as telephone lines or cable, and vice versa. It serves as the bridge between your local network and your Internet Service Provider's infrastructure. Modern modems often include router functionality built in, combining both devices into a single unit.

Visit the following resources to learn more:

- [@article@What is a modem?](https://www.lenovo.com/us/en/glossary/what-is-modem/?orgRef=https%253A%252F%252Fwww.google.com%252F&srsltid=AfmBOopdszN4vAUvKQcsMrDdyHVGiqrtTRETbQeOZD8-jopF4wZoIdEH)
- [@video@Modem vs Router - What's the difference?](https://www.youtube.com/watch?v=Mad4kQ5835Y)

## Mpls

# MPLS

MPLS, or Multiprotocol Label Switching, is a technique for speeding up network traffic by using short labels to direct packets along predetermined paths rather than making complex routing decisions at each hop. When a packet enters an MPLS network, it is assigned a label, and subsequent routers forward it based on that label without needing to inspect the IP header. Service providers widely use MPLS to manage traffic efficiently and deliver services such as VPNs and quality-of-service guarantees.

Visit the following resources to learn more:

- [@article@What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-mpls/)
- [@video@What is MPLS and How Does it Work?](https://www.youtube.com/watch?v=E5Ud1m9h0yc)

## Nat Vs Pat

# NAT / PAT

NAT, or Network Address Translation, is a method used by routers to map private IP addresses on a local network to a single public IP address before traffic leaves for the Internet. This allows many devices to share one public IP, which helps conserve the limited pool of available IPv4 addresses. PAT, or Port Address Translation, is an extension of NAT that also maps different port numbers to each internal device, allowing multiple simultaneous connections to be tracked and distinguished even when they all share the same public IP.

## Netflow  Sflow

# NetFlow / sFlow

NetFlow is a Cisco-developed protocol that collects and exports metadata about IP traffic flows passing through a network device, providing visibility into who is communicating with whom, how much data is being exchanged, and what protocols are in use. sFlow is a similar, vendor-neutral sampling-based protocol that works across a broader range of hardware. Both are used for traffic analysis, capacity planning, anomaly detection, and security monitoring without requiring full packet capture.

Visit the following resources to learn more:

- [@official@sflow](https://sflow.org/)
- [@article@What is NetFlow?](https://www.ibm.com/think/topics/netflow)
- [@video@MicroNugget: What is Netflow?](https://www.youtube.com/watch?v=aqTpUmUibB8)
- [@video@Network Flow Monitoring Explained | Concepts and protocols](http://youtube.com/watch?v=5i9sgB7CprM&t=182s)

## Netstat

# netstat

netstat, short for network statistics, is a command-line tool that displays active network connections, listening ports, routing tables, and network interface statistics on a device. It is useful for identifying which services are listening on which ports, spotting unexpected or unauthorized connections, and understanding the current state of network activity on a machine. Although largely replaced by the newer `ss` command on Linux systems, netstat remains widely used and available across Windows, macOS, and Linux.

Visit the following resources to learn more:

- [@article@What is the netstat Command?](https://www.cbtnuggets.com/blog/technology/networking/netstat-command)
- [@video@NETSTAT Command Explained](https://www.youtube.com/watch?v=8UZFpCQeXnM)

## Network Access

# Network Access

The Network Access layer is the lowest layer of the TCP/IP model, combining the functions of the OSI Physical and Data Link layers. It handles how data is physically transmitted over the network medium, including framing, MAC addressing, and hardware-level error detection. Ethernet and Wi-Fi protocols operate at this layer.

## Network Attacks

# Network Attacks

Network attacks are deliberate actions taken by malicious actors to disrupt, intercept, or gain unauthorized access to network resources and data. They can target vulnerabilities in protocols, devices, software, or human behavior to compromise the confidentiality, integrity, or availability of a network. Understanding the types of attacks that exist is the first step in designing defenses and responding effectively when incidents occur.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Cybersecurity Roadmap](https://roadmap.sh/cyber-security)
- [@article@What Is a Network Attack?](https://www.cynet.com/security-foundations/attack-techniques/network-attacks-and-network-security-threats/)
- [@article@10 Types of Network Attacks: Common Threats and How to Prevent Them](https://cymulate.com/blog/types-of-network-attacks/)

## Network Automation

# Network Automation

Network automation is the process of using software, scripts, and tools to automatically configure, manage, monitor, and operate network devices and infrastructure instead of performing these tasks manually. Traditionally, network engineers would log into each device individually and type commands one at a time — a process that is slow, error-prone, and impossible to scale across hundreds or thousands of devices. Automation replaces repetitive manual work with code that can apply consistent configurations across the entire network in seconds, respond to events without human intervention, and make infrastructure changes as reliable and repeatable as software deployments.

Visit the following resources to learn more:

- [@article@What is network automation?](https://www.ibm.com/think/topics/network-automation)
- [@video@Fundamentals of Network Automation](https://www.youtube.com/watch?v=K8ptdi-z7ls)

## Network Devices

# Network Devices

Network devices are the physical hardware components that make up a network and enable communication between connected devices. Each type of device serves a specific function, such as directing traffic, amplifying signals, or connecting different network segments. Understanding what each device does and how they interact is fundamental to designing and troubleshooting any network.

Visit the following resources to learn more:

- [@article@A Guide to Network Devices](https://sciencelogic.com/articles/a-guide-to-network-devices)
- [@video@Network Devices Explained | Hub, Bridge, Router, Switch](https://www.youtube.com/watch?v=eMamgWllRFY)

## Network Simulators

# Network Simulators

Network simulators are software applications that allow engineers to create, configure, and test virtual network topologies without needing physical hardware. By modeling the behavior of devices like routers, switches, and firewalls, these tools enable the practice of complex configurations, troubleshooting scenarios, and protocol analysis in a safe, controlled environment. They serve as a practical platform for verifying network designs and preparing for certification exams by emulating various operating systems and network conditions.

Visit the following resources to learn more:

- [@article@Top 10 Most Popular Network Simulation Tools](https://www.pynetlabs.com/top-most-popular-network-simulation-tools/)

## Network

# Network

The Network layer is the third layer of the OSI model, responsible for logical addressing and routing data packets between devices across different networks. It uses IP addresses to determine the best path for data to travel from source to destination. Routers operate at this layer, making forwarding decisions based on routing tables and protocols.

Visit the following resources to learn more:

- [@article@Understanding Layer 3: The Network Layer of the OSI Model](https://jumpcloud.com/it-index/understanding-layer-3-the-network-layer-of-the-osi-model)
- [@video@Networking Fundamentals: OSI 7 - Layer 3 - the network layer - Part 1](https://www.youtube.com/watch?v=WAZxo2ObFIw)
- [@video@Networking Fundamentals: OSI 7 - Layer 3 - the network layer - Part 2](https://www.youtube.com/watch?v=2MpRlYIYxz4)

## Next Generation

# Next-Generation

A Next-Generation Firewall (NGFW) is an advanced firewall that goes beyond traditional packet filtering and stateful inspection to include deep packet inspection, application awareness, intrusion prevention, and user identity tracking. NGFWs can identify and control traffic based on the specific application being used, regardless of port or protocol, and can detect and block sophisticated threats in real time. They represent the current standard for enterprise perimeter security.

Visit the following resources to learn more:

- [@article@What is a next-generation firewall (NGFW)?](https://www.cloudflare.com/en-gb/learning/security/what-is-next-generation-firewall-ngfw/)
- [@video@What is Next Generation Firewalls? | Next Gen Firewalls Explained | NGFWS](https://www.youtube.com/watch?v=KsELeMSYZN0)

## Nmap

# Nmap

Nmap (Network Mapper) is a free, open-source tool used to discover hosts and services on a network by sending packets and analyzing the responses. It can identify active devices, open ports, running services, operating systems, and potential vulnerabilities across a network. Nmap is widely used by network engineers and security professionals for network inventory, auditing, and reconnaissance.

Visit the following resources to learn more:

- [@official@Nmap](https://nmap.org/)
- [@opensource@nmap](https://github.com/nmap/nmap)
- [@video@Nmap for beginners](https://www.youtube.com/watch?v=5MTZdN9TEO4&list=PLBf0hzazHTGM8V_3OEKhvCM9Xah3qDdIx)

## Nslookup

# nslookup

nslookup is a command-line tool used to query DNS servers and retrieve information about domain name resolution. It allows a network engineer to check what IP address a domain resolves to, which DNS server is being used, and whether DNS records such as A, MX, or CNAME entries are correctly configured. It is an essential tool for diagnosing DNS-related issues, such as a website being unreachable due to a missing or incorrect DNS record.

Visit the following resources to learn more:

- [@official@What Is nslookup and How Does It Work?](https://www.networksolutions.com/blog/what-is-nslookup/)
- [@video@What is Nslookup?](https://www.youtube.com/watch?v=n6pT8lbyhog)

## Ntp

# NTP

NTP, or Network Time Protocol, is used to synchronize the clocks of computers and network devices over a network. Accurate timekeeping is essential for logging events, coordinating distributed systems, and ensuring security certificates work correctly. NTP works by having devices query time servers and adjust their local clocks to match, accounting for network delay in the process.

Visit the following resources to learn more:

- [@article@Network Time Protocol (NTP)](https://www.mobatime.com/technology/ntp-network-time-protocol/)
- [@video@Network Time Protocol (NTP)](https://www.youtube.com/watch?v=BAo5C2qbLq8)

## Observability

# Observability

Network observability refers to the ability to understand the internal state and behavior of a network by collecting and analyzing data from its components, including logs, metrics, traces, and flow records. It goes beyond basic monitoring by providing deep insight into why things are happening, not just what is happening. Good observability enables network engineers to detect issues early, troubleshoot faster, and optimize performance across complex, distributed environments.

Visit the following resources to learn more:

- [@article@What is network observability?](https://www.ibm.com/think/topics/network-observability)
- [@video@Observability vs. APM vs. Monitoring](https://www.youtube.com/watch?v=CAQ_a2-9UOI)

## Opendns

# OpenDNS

OpenDNS is a cloud-based DNS service operated by Cisco that provides fast DNS resolution along with additional security and filtering features. It can block access to malicious websites, phishing domains, and unwanted content categories before a connection is ever established. OpenDNS is commonly used by organizations and families to add a layer of protection at the DNS level without requiring software on individual devices.

Visit the following resources to learn more:

- [@official@OpenDNS](https://www.opendns.com/)
- [@video@OpenDNS vs Google DNS (2026) - Which One Is BETTER?](https://www.youtube.com/watch?v=b3fYQ77VOrk)

## Osi Model

# OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a network into seven distinct layers, from physical transmission up to application-level communication. It was developed to help different systems and vendors communicate using common standards, making troubleshooting and network design more systematic. Each layer has a specific role and interacts only with the layers directly above and below it.

Visit the following resources to learn more:

- [@article@What is the OSI Model?](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [@article@OSI Model](https://www.imperva.com/learn/application-security/osi-model/)
- [@video@What is OSI Model?](https://www.youtube.com/watch?v=Ilk7UXzV_Qc)

## Ospf

# OSPF

OSPF, or Open Shortest Path First, is a link-state interior gateway routing protocol used within a single autonomous system or organization. It works by having each router build a complete map of the network topology and then calculate the shortest path to every destination using Dijkstra's algorithm. OSPF converges quickly after network changes and is widely used in medium to large enterprise networks.

Visit the following resources to learn more:

- [@article@What is OSPF?](https://www.networkacademy.io/ccna/ospf/what-is-ospf)
- [@video@What is OSPF and How Does It Work?](https://www.youtube.com/watch?v=Xb3CbIDMDRk&t=74s)

## Package

# Package

In networking, a package (or packet) is a small chunk of data broken off from a larger message for transmission across a network. Each packet travels independently through the network and is reassembled at the destination. Packets contain both the payload data and header information, such as source and destination addresses, needed to route them correctly.

Visit the following resources to learn more:

- [@article@What is a packet? | Network packet definition](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-packet/)
- [@video@How Does the Internet Work? | Data Packets](https://www.youtube.com/watch?v=KjD3KANH-xc)

## Packet Analysis

# Packet Analysis

Packet analysis is the process of capturing and inspecting the raw data packets traveling across a network to understand exactly what is happening at a detailed level. By examining individual packets, network engineers can diagnose connectivity issues, identify security threats, verify that protocols are behaving correctly, and understand the root cause of performance problems. Tools like Wireshark and tcpdump are the primary instruments used for packet analysis, allowing engineers to filter, decode, and interpret traffic at every layer of the OSI model.

Visit the following resources to learn more:

- [@article@What Is Network Packet Analysis and Why Does It Matter?](https://www.networkcritical.com/blogs/what-is-network-packet-analysis)
- [@video@Hands-On Packet Analysis : The Course Overview](https://www.youtube.com/watch?v=1b54-GSYqDc&list=PLTgRMOcmRb3PFf5ZBQbM1OJUcs4SQjggv)
- [@video@Wireshark Tutorial for Beginners | Network Scanning Made Easy](https://www.youtube.com/watch?v=qTaOZrDnMzQ)

## Packet Filtering

# Packet Filtering

Packet filtering is the most basic type of firewall technique, where each packet is inspected individually against a set of rules based on attributes like source IP, destination IP, port numbers, and protocol. If a packet matches an allow rule, it passes through; if it matches a deny rule or no rule at all, it is dropped. Packet filtering is fast and lightweight, but provides limited protection since it does not consider the state of the connection or the content of the data.

Visit the following resources to learn more:

- [@article@What Is a Packet Filtering Firewall?](https://www.paloaltonetworks.com/cyberpedia/what-is-a-packet-filtering-firewall)
- [@video@Firewalls: Packet-Filtering/Stateless Firewalls](https://www.youtube.com/watch?v=jkYVRtiUmJ0)

## Packet Prioritization

# Packet prioritization

Packet prioritization is the process of classifying network traffic and assigning different levels of importance to different types of packets so that critical traffic is processed and delivered first. Real-time traffic, like VoIP and video conferencing, is given higher priority than background activities like file downloads or software updates. This ensures that time-sensitive applications remain functional even when the network is under heavy load.

Visit the following resources to learn more:

- [@article@Implementing Quality of Service for Prioritizing Network Traffic](https://www.etherwan.com/support/featured-articles/implementing-quality-service-prioritizing-network-traffic)
- [@video@QoS Explained | How to Prioritize Voice, Video & Data on Your Network](https://www.youtube.com/watch?v=FFL8Uql1m_4)

## Pan

# PAN

A PAN, or Personal Area Network, is a small network designed for communication between devices in proximity to a single person, typically within a range of a few meters. Examples include connecting a smartphone to wireless earbuds via Bluetooth or linking a laptop to a smartwatch. PANs can be wired (such as USB) or wireless (such as Bluetooth or infrared).

Visit the following resources to learn more:

- [@article@What is a personal area network (PAN)?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-personal-area-network/)
- [@video@What is a Personal Area Network (PAN)? (Animation)](https://www.youtube.com/watch?v=AYq-sqSzHKs)

## Peer To Peer Network

# Peer-to-Peer Network

A peer-to-peer (P2P) network is one where each device, or peer, can act as both a client and a server, sharing resources directly with other devices without a central server. This model is simpler and cheaper to set up than a client-server network, making it common in small home networks or applications like file sharing. However, P2P networks can be harder to manage and secure as they grow in size.

Visit the following resources to learn more:

- [@article@What Is a Peer-to-Peer Network?](https://www.coursera.org/articles/peer-to-peer)
- [@video@What is a Peer to Peer Network? Blockchain P2P Networks Explained](https://www.youtube.com/watch?v=ie-qRQIQT4I)

## Physical

# Physical

The Physical layer is the first and lowest layer of the OSI model, responsible for the actual transmission of raw bits over a physical medium such as copper cables, fiber optics, or radio waves. It defines the electrical, mechanical, and timing specifications for hardware components like network cables, connectors, and network interface cards. Everything at this layer deals with the physical delivery of signals, not their meaning.

Visit the following resources to learn more:

- [@article@What Is the Physical Layer: A Beginner’s Guide](https://www.coursera.org/articles/physical-layer)
- [@video@Networking Fundamentals: OSI 7 - Layer 1 - the physical layer](http://youtube.com/watch?v=a5SMTyhn0U8)

## Ping

# ping

ping is one of the most basic and widely used network diagnostic tools, sending ICMP Echo Request packets to a target host and measuring whether a response is received and how long it takes. It is typically the first tool used when troubleshooting connectivity, quickly confirming whether a device is reachable on the network. The results show round-trip time and packet loss, giving an immediate indication of whether a path exists between two devices and how stable it is.

Visit the following resources to learn more:

- [@article@Understanding Ping](https://www.zscaler.com/es/blogs/product-insights/understanding-ping-network-troubleshooting-and-beyond)
- [@video@PING Command - Troubleshooting Networks](https://www.youtube.com/watch?v=IIicPE38O-s)
- [@video@What Is Ping and What Does Its Output Tell Me?](https://www.youtube.com/watch?v=ZCMMyzBv354)

## Port

# Port

A port is a numerical identifier used to direct network traffic to a specific application or service running on a device. While an IP address identifies the device, the port number identifies which program on that device should handle the incoming data. For example, web traffic typically uses port 80 for HTTP and port 443 for HTTPS.

Visit the following resources to learn more:

- [@article@What is a computer port?](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)
- [@video@Network Ports Explained](https://www.youtube.com/watch?v=g2fT-g9PX9o)

## Presentation

# Presentation

The Presentation layer is the sixth layer of the OSI model, responsible for translating data between the format used by the application and the format used for network transmission. It handles tasks such as data encryption and decryption, compression, and character encoding. This layer ensures that data sent from one system can be read by another, regardless of differences in internal data representation.

Visit the following resources to learn more:

- [@article@Understanding Layer 6: The Presentation Layer of the OSI Model](https://jumpcloud.com/it-index/understanding-layer-6-the-presentation-layer-of-the-osi-model)
- [@video@Layer 6 (Presentation Layer)](https://www.youtube.com/watch?v=AtITX-U2mL4)

## Prometheus

# Prometheus

Prometheus is an open-source monitoring and alerting toolkit originally built at SoundCloud and now widely adopted across the industry. It collects metrics by scraping data from configured targets at regular intervals, stores them in a time-series database, and provides a powerful query language called PromQL to analyze and visualize the data. While not network-specific, Prometheus is commonly used in modern infrastructure to monitor network devices, services, and applications, often paired with Grafana for visualization and alerting.

Visit the following resources to learn more:

- [@article@Prometheus](https://prometheus.io/)
- [@video@Introduction to the Prometheus Monitoring System | Key Concepts and Features](https://www.youtube.com/watch?v=STVMGrYIlfg)

## Protocol

# Protocol

A protocol is a set of rules that defines how data is formatted, transmitted, and received between devices on a network. Protocols ensure that different systems, regardless of manufacturer or operating system, can predictably communicate with each other. Examples include TCP, IP, HTTP, and DNS, each governing a specific aspect of how network communication works.

Visit the following resources to learn more:

- [@article@What is a protocol?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-protocol/)
- [@video@Network Protocols Explained: Networking Basics](https://www.youtube.com/watch?v=1zVZ9cWFnCc)

## Proxy

# Proxy

A proxy firewall operates at the application layer and acts as an intermediary between internal clients and external servers, inspecting the full content of network requests and responses. Instead of allowing direct connections, all traffic is routed through the proxy, which can apply content filtering, authentication, and logging. Because it terminates and re-establishes each connection, a proxy firewall provides deep inspection but can introduce latency.

Visit the following resources to learn more:

- [@article@What Is A Proxy Firewall?](https://www.fortinet.com/resources/cyberglossary/proxy-firewall)
- [@video@Types of Firewalls Explained](https://www.youtube.com/watch?v=IbimC-tx7XI)
- [@video@What is a Proxy Server?](https://www.youtube.com/watch?v=5cPIukqXe5w)

## Public Vs Private Addresses

# Public vs Private Addresses

Public IP addresses are globally unique addresses assigned by Internet Service Providers and are reachable over the Internet. Private IP addresses are reserved for use within local networks and are not routable on the public Internet (ranges like 192.168.x.x, 10.x.x.x, and 172.16.x.x are commonly used internally). Devices with private addresses access the Internet through a process called NAT (Network Address Translation), which maps multiple private addresses to a single public one.

Visit the following resources to learn more:

- [@article@Public vs. Private IP Addresses: What’s the Difference?](https://www.avast.com/c-ip-address-public-vs-private)
- [@video@Public vs Private IP Address](https://www.youtube.com/watch?v=po8ZFG0Xc4Q)

## Qos Quality Of Service

# QoS (Quality of Service)

QoS, or Quality of Service, refers to a set of techniques used to manage network traffic and ensure that critical applications receive the bandwidth, low latency, and reliability they need. Without QoS, all traffic is treated equally, which can cause voice calls to break up or video to buffer when the network is congested. QoS works by classifying, prioritizing, and managing packets so that high-priority traffic is delivered first.

Visit the following resources to learn more:

- [@article@What Is Quality Of Service (QoS) In Networking?](https://www.fortinet.com/resources/cyberglossary/qos-quality-of-service)
- [@article@What is Quality of Service?](https://www.paloaltonetworks.com/cyberpedia/what-is-quality-of-service-qos)
- [@video@Communication Networks Quality Of Service (QOS).](https://www.youtube.com/watch?v=-cGMmSx9Ag0)

## Quad9

# Quad9

Quad9 is a free, public DNS resolver that focuses on security by blocking access to known malicious domains at the DNS level. It uses threat intelligence from multiple cybersecurity partners to identify and block harmful websites before a connection is made, without logging personally identifiable information. Quad9 is operated by a non-profit organization and is accessible at the address 9.9.9.9.

Visit the following resources to learn more:

- [@official@Quad9](https://quad9.net/)

## Rip

# RIP

RIP, or Routing Information Protocol, is one of the oldest dynamic routing protocols, using a distance-vector algorithm to determine the best path based on hop count —the number of routers a packet must pass through to reach its destination. It has a maximum hop count of 15, making it unsuitable for large networks. RIP is simple to configure but has largely been replaced by more efficient protocols like OSPF and EIGRP in modern networks.

Visit the following resources to learn more:

- [@article@Routing Information Protocol:](https://www.cloudns.net/blog/routing-information-protocol-explaining-one-of-the-oldest-routing-protocols/)
- [@video@Networking Basics - How RIP Works](https://www.youtube.com/watch?v=tZWlRq-iunI&t=59s)

## Round Robin

# Round Robin

Round Robin is one of the simplest load balancing algorithms, where incoming requests are distributed sequentially to each server in the pool, one after another, cycling back to the first when the end is reached. It assumes all servers have roughly equal capacity and is easy to implement. Round Robin works well when the servers are similar in performance and the requests are similar in complexity.

Visit the following resources to learn more:

- [@article@Round Robin Load Balancing Definition](https://www.vmware.com/topics/round-robin-load-balancing)
- [@video@Top 6 Load Balancing Algorithms Every Developer Should Know](https://www.youtube.com/watch?v=dBmxNsS3BGE)

## Routers

# Routers

A router is a network device that forwards data packets between different networks, directing traffic based on IP addresses. It determines the best path for data to travel from source to destination, making routing decisions using routing tables and protocols. Routers are what connect your home or office network to the Internet and are essential for communication between separate networks.

Visit the following resources to learn more:

- [@article@What is a router?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-router/)
- [@video@Modem vs Router - What's the difference?](https://www.youtube.com/watch?v=Mad4kQ5835Y)

## Routing

# Routing

Routing is the process of selecting a path for traffic to travel across one or more networks from source to destination. Routers perform this function by examining the destination IP address of each packet and consulting a routing table to determine where to forward it next. Routing can be done statically, where paths are manually configured, or dynamically, where routers automatically discover and update paths using routing protocols.

Visit the following resources to learn more:

- [@article@What is routing? | IP routing](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-routing/)
- [@video@Understanding Routing! | ICT#8](https://www.youtube.com/watch?v=gQtgtKtvRdo&t=77s)
- [@video@What is a ROUTER?](https://www.youtube.com/watch?v=p9ScLm9S3B4)

## San

# SAN

A SAN, or Storage Area Network, is a specialized high-speed network that provides block-level access to shared storage devices such as disk arrays and tape libraries. Unlike a regular network where files are shared, a SAN makes storage appear as locally attached to the servers that use it, enabling fast and reliable data access. SANs are commonly used in enterprise environments to support databases, virtualization, and backup systems.

Visit the following resources to learn more:

- [@article@What is a storage area network (SAN)?](https://www.ibm.com/think/topics/storage-area-network)
- [@video@NAS vs SAN - Network Attached Storage vs Storage Area Network](https://www.youtube.com/watch?v=3yZDDr0JKVc)
- [@video@Ultimate Beginners Guide to Storage Area Network / SAN](https://www.youtube.com/watch?v=1PIxEpQDRqc)

## Sd Wan

# SD-WAN

SD-WAN, or Software-Defined Wide Area Network, is a technology that uses software to centrally manage and optimize how traffic is routed across multiple WAN connections, such as MPLS, broadband Internet, and 4G/5G links, based on real-time conditions and application requirements. Instead of rigidly sending all traffic through a single expensive MPLS circuit, SD-WAN can intelligently distribute traffic across the best available link at any given moment, improving performance and reducing costs. It is managed through a centralized controller that gives network engineers visibility and control over the entire WAN from a single interface, without needing to manually configure each individual device at every site.

Visit the following resources to learn more:

- [@article@What is SD-WAN? Software-Defined WAN (SDWAN)](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-sd-wan.html)
- [@article@What Is SD-WAN](https://www.fortinet.com/resources/cyberglossary/sd-wan-explained)
- [@video@Fundamentals of SD-WAN](https://www.youtube.com/watch?v=cos4ujj80iI)

## Security Groups

# Security Groups

Security groups are virtual firewalls applied at the resource level in cloud environments, controlling which traffic is allowed to reach individual instances, containers, or services based on rules that specify protocol, port range, and source or destination IP address. Unlike traditional network firewalls that sit at the perimeter, security groups travel with the resource and enforce rules wherever that resource is deployed within the cloud. Most cloud providers implement security groups as stateful, meaning if an inbound connection is allowed, the corresponding outbound response is automatically permitted without needing an explicit outbound rule.

Visit the following resources to learn more:

- [@video@AWS Security Groups Simply Explained: A Step-by-Step Tutorial for Beginners](https://www.youtube.com/watch?v=uYDT2SsHImQ)
- [@video@AZ-900 Episode 21 | Azure Security Groups](https://www.youtube.com/watch?v=w8H5fWBHddA&pp=ygUbY2xvdWQgc2VjdXJpdHkgZ3JvdXBzIGF6dXJl)

## Server

# Server

A server is a computer or software system that listens for requests from clients and responds by providing resources, data, or services. Servers can host websites, store files, manage emails, or run applications that many users access simultaneously. They are typically designed to be always available, handling multiple client connections at the same time.

Visit the following resources to learn more:

- [@article@What Are Servers? A Practical Guide](https://www.splunk.com/en_us/blog/learn/computer-servers.html)
- [@video@Networking Basics: What is a Server?](https://www.youtube.com/watch?v=SpcGyrhJUJk)

## Session

# Session

The Session layer is the fifth layer of the OSI model, responsible for establishing, managing, and terminating communication sessions between applications. It handles synchronization and dialog control, ensuring that data exchanges are organized and that sessions can be paused and resumed if needed. Examples of protocols operating at this layer include NetBIOS and RPC.

Visit the following resources to learn more:

- [@article@Understanding Layer 5: The Session Layer of the OSI Model](https://jumpcloud.com/it-index/understanding-layer-5-the-session-layer-of-the-osi-model)
- [@video@Networking Fundamentals: OSI 7 - Layer 4&5 - Transport & Session Layers - Part 1](https://www.youtube.com/watch?v=MBLecyQuNqk)
- [@video@Networking Fundamentals: OSI 7 - Layer 4&5 - Transport & Session Layers - Part 2](https://www.youtube.com/watch?v=drvbm6R0ONY)

## Shell  Scripting

# Shell & Scripting

The shell is the command-line interface used to interact with a Linux system, while scripting is the practice of combining shell commands into reusable files called scripts. For network engineers, shell scripting helps automate repetitive tasks such as backing up device configurations, parsing log files, running diagnostic checks across multiple devices, and generating reports. Bash is the most common shell used in networking environments, and even basic scripting knowledge can significantly reduce manual work and human error. Python is equally important and has become the dominant programming language in network engineering. Compared to Bash, Python is better suited for complex automation tasks and serves as the foundation for many modern network automation tools and frameworks, including Ansible and API-based network management.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Shell/Bash Roadmap](https://roadmap.sh/shell-bash)
- [@roadmap@Visit the Dedicated Python Roadmap](https://roadmap.sh/python)
- [@video@Shell Scripting Tutorial for Beginners 1 - Introduction](https://www.youtube.com/watch?v=cQepf9fY6cE&list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_)

## Site To Site Vs Remote Access

# Site-to-Site vs Remote Access

Site-to-site VPNs connect two entire networks together — such as a branch office to a headquarters — over an encrypted tunnel, allowing devices on both networks to communicate as if they were on the same LAN. Remote access VPNs allow individual users to securely connect to a corporate network from any location, typically using a VPN client on their device. Both serve different purposes and are often deployed together in enterprise environments to address different connectivity needs.

Visit the following resources to learn more:

- [@article@Site-to-site VPN vs remote access VPN: Which is better?](https://nordvpn.com/blog/site-to-site-vpn-vs-remote-access-vpn/?srsltid=AfmBOoq_TRsDLA4LQ2Rxo_jdvPWQNjKg85L1eBDf8zlgodcp9QFvqx7V)
- [@video@VPNs Explained | Site-to-Site + Remote Access](https://www.youtube.com/watch?v=CWy3x3Wux6o)

## Smtp  Imap

# SMTP / IMAP

SMTP (Simple Mail Transfer Protocol) is the protocol used to send emails from a client to a server or between mail servers. IMAP (Internet Message Access Protocol) is used by email clients to retrieve and manage messages stored on a mail server, allowing access from multiple devices while keeping messages synchronized. Together, these protocols handle the sending and receiving sides of email communication.

Visit the following resources to learn more:

- [@article@What are Email Protocols](https://www.siteground.com/tutorials/email/protocols-pop3-smtp-imap/)
- [@video@SMTP vs IMAP vs POP3 Explained - Tutorial by Mailtrap](https://www.youtube.com/watch?v=IMLFrYqI-oQ)

## Snmp

# SNMP

SNMP, or Simple Network Management Protocol, is a widely used protocol for monitoring and managing network devices such as routers, switches, servers, and printers. It allows a central management system to query devices for performance data — like CPU usage, interface statistics, and error counts — and can also receive unsolicited alerts called traps when certain conditions occur. SNMP is a foundational tool in network operations centers (NOCs) for maintaining visibility across large infrastructure.

Visit the following resources to learn more:

- [@article@What Is SNMP?](https://www.fortinet.com/uk/resources/cyberglossary/simple-network-management-protocol)
- [@video@How SNMP Works - a quick guide](https://www.youtube.com/watch?v=2IXP0TkwNJU)

## Sntp

# SNTP

SNTP, or Simple Network Time Protocol, is a simplified version of NTP used to synchronize device clocks over a network. It is less precise than full NTP but requires fewer resources, making it suitable for devices that do not need highly accurate timekeeping. SNTP is commonly used in embedded systems, IoT devices, and environments where simplicity is prioritized over precision.

Visit the following resources to learn more:

- [@article@Simple network time protocol (SNTP)](https://www.ionos.com/digitalguide/server/know-how/sntp-simple-network-time-protocol/)
- [@video@SNTP explained](https://www.youtube.com/watch?v=eGMZ5Eobx7c)

## Socket

# Socket

A socket is the combination of an IP address and a port number, forming a unique endpoint for network communication. When two devices establish a connection, each end uses a socket to send and receive data, creating a two-way communication channel. Sockets are the fundamental abstraction used by applications to interact with the network.

Visit the following resources to learn more:

- [@article@Networking 101: What are sockets?](https://medium.com/@ahnafzamil/networking-101-what-are-sockets-7e2d274e153)
- [@video@What is a Socket?](https://www.youtube.com/watch?v=Gr2ROxZXuvQ)

## Speedtest

# speedtest

A speedtest is a diagnostic tool that measures the actual throughput of a network connection by downloading and uploading data to a remote server and reporting the results in megabits per second. It is used to verify that a connection is delivering the bandwidth expected from an ISP or internal network link, and to identify discrepancies between advertised and real-world speeds. Speedtest tools like [Speedtest.net](http://Speedtest.net) or iPerf (used internally between two endpoints) are common first steps when users report slow Internet or network performance.

Visit the following resources to learn more:

- [@article@speedtest](https://www.speedtest.net/)
- [@article@Google Fiber Internet Speed Test](https://www.speedtest.net/)

## Ssh

# SSH

SSH, or Secure Shell, is a network protocol that provides a secure, encrypted channel for remotely accessing and managing devices over an unsecured network. It replaces older, insecure protocols like Telnet by encrypting all communication between the client and the server. Network engineers use SSH extensively to configure routers, switches, and servers from a remote location.

Visit the following resources to learn more:

- [@article@What is SSH? | Secure Shell (SSH) protocol](https://www.cloudflare.com/en-gb/learning/access-management/what-is-ssh/)
- [@video@SSH explained in 2 minutes!](https://www.youtube.com/watch?v=P0Fk-K2eZF8)

## Ssl  Tls

# SSL / TLS

SSL (Secure Sockets Layer) and its successor TLS (Transport Layer Security) are cryptographic protocols designed to provide secure communication over a network. They work by encrypting the data exchanged between a client and a server, verifying the identity of the parties involved through digital certificates. TLS is the modern standard and is used to secure HTTPS connections, email, and many other internet services.

Visit the following resources to learn more:

- [@article@What's the difference between SSL and TLS?](https://aws.amazon.com/compare/the-difference-between-ssl-and-tls/)
- [@video@SSL, TLS, HTTPS Explained](https://www.youtube.com/watch?v=j9QmMEWmcfo)

## Stateful Inspection

# Stateful Inspection

Stateful inspection, also known as dynamic packet filtering, is a firewall technique that tracks the state of active network connections and makes filtering decisions based on context, not just individual packets. By maintaining a state table of established connections, a stateful firewall can allow response packets that belong to a legitimate session while blocking unsolicited incoming traffic. This provides significantly better security than simple packet filtering without sacrificing too much performance.

Visit the following resources to learn more:

- [@article@What Is a Stateful Firewall?](https://www.paloaltonetworks.com/cyberpedia/what-is-a-stateful-firewall)
- [@video@Stateful Inspection Firewall](https://www.youtube.com/watch?v=rC37jKY3ono)

## Static Vs Dynamic Routing

# Static vs Dynamic Routing

Static routing involves manually configuring fixed routes in a router's routing table, which do not change unless an administrator updates them. It is simple and predictable, but does not adapt automatically to network changes or failures. Dynamic routing uses routing protocols that allow routers to automatically discover routes, share information with neighboring routers, and adapt to topology changes in real time.

Visit the following resources to learn more:

- [@article@Static vs Dynamic Routing: What's the Difference?](https://www.ioriver.io/blog/static-dynamic-routing)
- [@video@Understanding Routing!](https://www.youtube.com/watch?v=gQtgtKtvRdo&t=77s)

## Stp

# STP

STP, or Spanning Tree Protocol, is a network protocol that prevents loops in Ethernet networks by creating a logical tree topology from a physically redundant network. Without STP, multiple paths between switches could cause broadcast storms that would bring a network down. STP works by electing a root bridge and blocking redundant paths, re-enabling them only if the primary path fails.

Visit the following resources to learn more:

- [@article@Introduction to Spanning Tree](https://networklessons.com/spanning-tree/introduction-to-spanning-tree)
- [@video@Spanning Tree Protocol | CCNA - Explained](https://www.youtube.com/watch?v=6MW5P6Ci7lw)

## Subnet Masks

# Subnet Masks

A subnet mask is a 32-bit number used alongside an IP address to determine which portion of the address identifies the network and which portion identifies the individual host. It works by applying a bitwise AND operation with the IP address to extract the network address. For example, a subnet mask of 255.255.255.0 means the first three octets represent the network and the last octet identifies hosts within that network.

Visit the following resources to learn more:

- [@article@What Is a Subnet Mask?](https://www.coursera.org/articles/subnet-mask)
- [@video@Subnet Mask - Explained](https://www.youtube.com/watch?v=s_Ntt6eTn94)

## Subnetting

# Subnetting

Subnetting is the process of dividing a large network into smaller, more manageable sub-networks called subnets. It helps improve network performance by reducing broadcast traffic and allows organizations to organize their network logically, such as separating departments or locations. Subnetting works by borrowing bits from the host portion of an IP address to create a subnet identifier, controlled by the subnet mask.

Visit the following resources to learn more:

- [@article@What is a subnet? | How subnetting works](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-subnet/)
- [@video@Subnetting Explained: Networking Basics](https://www.youtube.com/watch?v=hbdT_Q9DM8w)

## Supernetting

# Supernetting

Supernetting, also known as route aggregation or summarization, is the process of combining multiple smaller network routes into a single, larger route advertisement. This reduces the size of routing tables and simplifies routing by representing several contiguous subnets as one summary route. It is commonly used in large-scale networks and by ISPs to keep routing tables manageable.

Visit the following resources to learn more:

- [@article@Ultimate Guide to Supernetting](https://www.dnsstuff.com/supernetting)
- [@video@Supernetting, IP Aggregation, and IP Summarization](https://www.youtube.com/watch?v=Q4MArJTbUwk)

## Switches

# Switches

A switch is a network device that connects multiple devices within the same local network and forwards data based on MAC addresses. Unlike a hub, a switch sends data only to the specific device it is intended for, making communication more efficient and reducing unnecessary network traffic. Managed switches offer additional features like VLANs, port security, and traffic monitoring.

Visit the following resources to learn more:

- [@article@What is a network switch? | Switch vs. router](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-network-switch/)
- [@video@What is a Network Switch?](https://www.youtube.com/watch?v=OvEu4owdjcg)

## Switching

# Switching

Switching is the process of forwarding data frames within a local network based on MAC addresses. A network switch receives incoming frames and sends them only to the port connected to the intended destination device, unlike a hub, which broadcasts to all ports. Switching forms the foundation of modern LAN design and can be enhanced with features like VLANs, STP, and link aggregation.

Visit the following resources to learn more:

- [@article@What Is Network Switching?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-switching.html)
- [@video@What is a SWITCH?](https://www.youtube.com/watch?v=9eH16Fxeb9o)
- [@video@Circuit Switching vs Packet Switching](https://www.youtube.com/watch?v=G7n8thqwO2c)

## Tcpip Model

# TCP/IP Model

The TCP/IP model is a practical, four-layer framework that describes how data is transmitted over the Internet and most modern networks. It was developed by the U.S. Department of Defense and serves as the foundation for Internet communication. Unlike the OSI model's seven layers, the TCP/IP model consolidates functions into four layers: Network Access, Internet, Transport, and Application.

Visit the following resources to learn more:

- [@article@Internet protocol suite - Wikipedia](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [@article@What Are the 4 Layers of the TCP/IP Model?](https://thepower.education/en/blog/what-are-the-four-layers-that-make-up-tcp-ip)
- [@video@What is TCP/IP?](https://www.youtube.com/watch?v=PpsEaqJV_A0)

## Terraform

# Terraform

Terraform is an open-source Infrastructure as Code tool developed by HashiCorp that allows engineers to define and provision infrastructure — including network resources — using a declarative configuration language called HCL (HashiCorp Configuration Language). Instead of manually creating networks, subnets, firewall rules, and load balancers through a cloud console, Terraform lets you describe the desired state of your infrastructure in code and then automatically creates or modifies resources to match that state. It supports all major cloud providers and many network vendors, making it a popular choice for managing cloud networking infrastructure consistently and repeatably.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Terraform Roadmap](https://roadmap.sh/terraform)
- [@official@Terraform Docs](https://developer.hashicorp.com/terraform/docs)
- [@video@Terraform explained in 15 mins | Terraform Tutorial for Beginners](https://www.youtube.com/watch?v=l5k1ai_GBDE)

## Throughput

# Throughput

Throughput is the actual amount of data successfully transferred over a network in a given period of time, as opposed to the theoretical maximum that bandwidth represents. While bandwidth is the capacity of a network link, throughput reflects real-world performance after accounting for packet loss, latency, and protocol overhead. It is also measured in bits per second.

Visit the following resources to learn more:

- [@article@What’s the Difference Between Throughput and Latency?](https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/)
- [@video@Inside Wireless: Network Throughput](https://www.youtube.com/watch?v=l23baEHJ9YQ)

## Traceroute  Tracert

# traceroute / tracert

traceroute (on Linux and macOS) and tracert (on Windows) are diagnostic tools that map the path packets take from a source device to a destination, showing each hop along the route and the latency at each one. By sending packets with incrementally increasing TTL (Time to Live) values, they reveal every router the traffic passes through on its way to the target. This makes them invaluable for identifying where in the network a problem is occurring — whether a packet is being dropped, a specific hop has high latency, or traffic is taking an unexpected route.

Visit the following resources to learn more:

- [@article@What is Traceroute? How It Works and How to Read Results](https://www.varonis.com/blog/what-is-traceroute)
- [@video@Traceroute (tracert) Explained - Network Troubleshooting](https://www.youtube.com/watch?v=up3bcBLZS74)

## Traffic Management

# Traffic Management

Traffic management refers to the set of techniques and tools used to control how network traffic flows, ensuring efficient use of available bandwidth and reliable delivery of data. It covers everything from prioritizing critical applications over less important ones, to shaping traffic to prevent congestion, to distributing load across multiple servers or links. Effective traffic management ensures that the network performs well under normal conditions and degrades gracefully under heavy load.

## Traffic Shaping

# Traffic shaping

Traffic shaping is a QoS technique used to control the rate at which data is transmitted on a network, smoothing out bursts and enforcing bandwidth limits for specific types of traffic. By delaying or queuing packets that exceed a defined rate, traffic shaping ensures that no single application or user monopolizes network resources. It is commonly used by ISPs and enterprises to manage congestion and maintain consistent performance across the network.

Visit the following resources to learn more:

- [@article@QoS Traffic Shaping Explained](https://networklessons.com/quality-of-service/qos-traffic-shaping-explained)
- [@video@What is Traffic Shaping and Policing?](https://www.youtube.com/watch?v=khS8c1WrWfU)

## Transmission Media Types

# Transmission Media Types

Transmission media refers to the physical or wireless channels through which data travels between devices. Wired media includes twisted pair cables (like Ethernet), coaxial cables, and fiber optic cables, each with different speeds, ranges, and interference characteristics. Wireless media uses radio waves, microwaves, or infrared signals to transmit data without physical connections.

Visit the following resources to learn more:

- [@article@Transmission Media and Its Types in Computer Networks](https://www.uninets.com/blog/transmission-media-in-computer-networks)
- [@video@Guided Vs Unguided Transmission Media | Differences & Comparison | Types of Transmission Media](https://www.youtube.com/watch?v=vUDtFjiNib4)
- [@video@CN 5 : Transmission Media | Guided & Unguided Media with Examples](https://www.youtube.com/watch?v=HryzQDpKvwA)

## Transport

# Transport

The Transport layer is the fourth layer of the OSI model, responsible for end-to-end communication, data flow control, and error recovery between applications on different hosts. It breaks data into segments, ensures they are delivered reliably and in order, and manages retransmission if packets are lost. The two main protocols at this layer are TCP, which provides reliable delivery, and UDP, which prioritizes speed over reliability.

Visit the following resources to learn more:

- [@article@Understanding Layer 4: The Transport Layer of the OSI Model](https://jumpcloud.com/it-index/understanding-layer-4-the-transport-layer-of-the-osi-model)
- [@video@Networking Fundamentals: OSI 7 - Layer 4&5 - Transport & Session Layers - Part 1](https://www.youtube.com/watch?v=MBLecyQuNqk)
- [@video@Networking Fundamentals: OSI 7 - Layer 4&5 - Transport & Session Layers - Part 2](https://www.youtube.com/watch?v=drvbm6R0ONY)

## Transport

# Transport

The Transport layer of the TCP/IP model is responsible for end-to-end communication between applications on different hosts. It uses TCP for reliable, ordered delivery and UDP for faster, connectionless communication where some data loss is acceptable. This layer manages segmentation, flow control, and error handling to ensure data reaches the correct application.

## Troubleshooting

# Troubleshooting

Network troubleshooting is the process of identifying, diagnosing, and resolving problems that affect network connectivity, performance, or reliability. It requires a combination of systematic methodology, knowledge of networking concepts, and familiarity with diagnostic tools. Good troubleshooting is not about randomly trying fixes, it is about gathering evidence, forming a hypothesis, testing it, and working through the problem layer by layer until the root cause is found and resolved.

Visit the following resources to learn more:

- [@article@What Is Network Troubleshooting?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-troubleshooting.html)
- [@video@Steps for Network Troubleshooting](https://www.youtube.com/watch?v=1i3XdhC2ZAs)

## Tunneling  Vpns

# VPNs

A VPN, or Virtual Private Network, is a technology that creates an encrypted, secure tunnel between a device and a remote network or server over the public Internet. It allows users to access private network resources securely from remote locations and hides their traffic from potential eavesdroppers. VPNs are used by organizations for secure remote access and site-to-site connectivity, as well as by individuals for privacy and anonymity online.

Visit the following resources to learn more:

- [@article@What is a VPN? Meaning and what it’s used for](https://nordvpn.com/what-is-a-vpn/?srsltid=AfmBOoqW3KGxs9k--CDwPvajgU48eeQJe8bhKdb-eBRd8qojyH-wvyrH)
- [@video@https://www.youtube.com/watch?v=R-JUOpCgTZc](https://www.youtube.com/watch?v=R-JUOpCgTZc)

## Virtual Networks

# Virtual Networks

A virtual network in cloud computing is a software-defined network that replicates the functionality of a physical network entirely in software, allowing cloud resources to communicate with each other, with on-premises systems, and with the Internet. Virtual networks are defined through configuration rather than physical cabling, making them fast to create, easy to modify, and infinitely scalable. Each cloud provider has its own implementation —AWS calls it a VPC, Azure calls it a VNet, and GCP also uses the VPC model— but all share the same core concept of providing isolated, configurable network environments for cloud resources.

Visit the following resources to learn more:

- [@article@What is a Virtual Network? How it Works and Its Types?](https://www.pynetlabs.com/what-is-a-virtual-network/)
- [@video@Virtual Networking Explained](https://www.youtube.com/watch?v=u0TgGIn2LIM)
- [@video@Virtual Private Cloud (VPC) Explained](https://www.youtube.com/watch?v=2fPgKvDBfbs)

## Vlans

# VLANs

A VLAN, or Virtual Local Area Network, is a logical subdivision of a physical network that groups devices together regardless of their physical location. VLANs allow network administrators to segment traffic, improve security, and reduce broadcast domains without needing separate physical switches. Devices in different VLANs cannot communicate directly without going through a router or a Layer 3 switch.

Visit the following resources to learn more:

- [@article@Guide to VLANs](https://www.cbtnuggets.com/blog/technology/networking/what-is-a-vlan-and-how-they-work)
- [@video@VLAN Explained](https://www.youtube.com/watch?v=jC6MJTh9fRE)

## Vlsm

# VLSM

VLSM, or Variable Length Subnet Masking, is a technique that allows a network to be divided into subnets of different sizes by using different subnet masks within the same network. Unlike fixed-length subnetting, where all subnets are the same size, VLSM lets you allocate address space more efficiently based on the actual needs of each subnet. This is especially useful for conserving IP addresses in complex network designs with varying host requirements.

Visit the following resources to learn more:

- [@article@What Is VLSM Variable Length Subnet Masking?](https://jumpcloud.com/it-index/what-is-vlsm-variable-length-subnet-masking)
- [@video@VLSM Subnetting - subnetting a subnet](https://www.youtube.com/watch?v=RLCd5u0sjoU)

## Vpn

# VPN

A VPN, or Virtual Private Network, creates an encrypted tunnel between a device and a remote network over the public Internet, allowing secure communication as if the device were directly connected to that network. Organizations use VPNs to let remote employees securely access internal resources, while individuals use them for privacy and to bypass geographic content restrictions. VPNs mask the user's IP address and encrypt all traffic passing through the tunnel.

Visit the following resources to learn more:

- [@article@What is a VPN (virtual private network)?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn)
- [@video@VPN (Virtual Private Network) Explained](https://www.youtube.com/watch?v=R-JUOpCgTZc)

## Vpns

# VPNs

A VPN, or Virtual Private Network, is a technology that creates an encrypted, secure tunnel between a device and a remote network or server over the public Internet. It allows users to access private network resources securely from remote locations and hides their traffic from potential eavesdroppers. VPNs are used by organizations for secure remote access and site-to-site connectivity, as well as by individuals for privacy and anonymity online.

Visit the following resources to learn more:

- [@article@What is a VPN? Meaning and what it’s used for](https://nordvpn.com/what-is-a-vpn/?srsltid=AfmBOoqW3KGxs9k--CDwPvajgU48eeQJe8bhKdb-eBRd8qojyH-wvyrH)
- [@video@https://www.youtube.com/watch?v=R-JUOpCgTZc](https://www.youtube.com/watch?v=R-JUOpCgTZc)

## Vrfs

# VRFs

VRF, or Virtual Routing and Forwarding, is a technology that allows a single physical router to run multiple independent routing tables at the same time. Each VRF acts like a completely separate virtual router, meaning traffic in one VRF is fully isolated from traffic in another, even if they share the same physical hardware. This is commonly used by service providers to keep customer traffic separate on shared infrastructure, and by enterprises to isolate different departments or network segments on the same device.

Visit the following resources to learn more:

- [@article@What is Cisco VRF (Virtual Routing and Forwarding)?](https://www.cbtnuggets.com/blog/technology/networking/what-is-cisco-vrf-virtual-routing-forwarding)
- [@video@What is Cisco VRF (Virtual Routing and Forwarding)?](https://www.youtube.com/watch?v=JIEwTTZuNHI)

## Vrrp

# VRRP

VRRP, or Virtual Router Redundancy Protocol, is an open standard protocol that provides the same gateway redundancy function as HSRP but works across equipment from any vendor. A group of routers share a virtual IP address, with one elected as the master and the others as backups ready to take over if the master becomes unavailable. Because it is vendor-neutral, VRRP is the preferred choice in multi-vendor network environments.

Visit the following resources to learn more:

- [@article@Virtual Router Redundancy Protocol (VRRP)](https://www.networkacademy.io/ccna/network-services/virtual-router-redundancy-protocol-vrrp)
- [@video@What is VRRP? Virtual Router Redundancy Protocol](https://www.youtube.com/watch?v=GyQrgfrKJ38)

## Vxlan

# VXLAN

VXLAN, or Virtual Extensible LAN, is a network virtualization technology that extends Layer 2 networks over a Layer 3 infrastructure by encapsulating Ethernet frames inside UDP packets. It was created to overcome the scalability limitations of traditional VLANs, which support a maximum of 4,096 network segments, by supporting up to 16 million virtual network identifiers. VXLAN is widely used in data centers and cloud environments where large numbers of isolated virtual networks need to coexist on shared physical infrastructure.

Visit the following resources to learn more:

- [@article@What is VXLAN?](https://www.hpe.com/emea_europe/en/what-is/vxlan.html)
- [@video@VXLAN - What is VXLAN?](https://www.youtube.com/watch?v=Jv0IqaM9KOs)

## Wan

# WAN

A WAN, or Wide Area Network, is a network that spans a large geographic area, often connecting multiple LANs across cities, countries, or continents. The Internet itself is the largest example of a WAN. Organizations use WANs to connect their branch offices and data centers, often leasing connections from telecommunications providers.

Visit the following resources to learn more:

- [@article@What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-wan/)
- [@video@LAN, WAN, SUBNET - EXPLAINED](https://www.youtube.com/watch?v=NyZWSvSj8ek)

## Web Application

# Web Application

A Web Application Firewall (WAF) is a specialized security tool designed to filter, monitor, and block HTTP/HTTPS traffic to and from web applications. It protects against common web-based attacks such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF) by inspecting application-layer traffic against a set of rules or policies. WAFs can be deployed as hardware, software, or cloud services and are an essential layer of defense for any publicly accessible web application.

Visit the following resources to learn more:

- [@article@What is a WAF?](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)
- [@video@What is a Web Application Firewall (WAF)?](https://www.youtube.com/watch?v=p8CQcF_9280)

## What Are Networks

# What are Networks?

A network is a collection of two or more devices connected to share resources and communicate. Networks can be as small as two computers linked in a home office or as large as the global infrastructure of the Internet. They form the backbone of modern digital communication, enabling everything from file sharing and printing to video streaming and cloud computing.

Visit the following resources to learn more:

- [@article@What is computer networking?](https://www.ibm.com/think/topics/networking)
- [@video@Computer Networks: Crash Course Computer Science #28](https://www.youtube.com/watch?v=3QhU9jd03a0)
- [@video@Every Networking Concept Explained In 20 Minutes](https://www.youtube.com/watch?v=xj_GjnD4uyI)

## Wifi Standards

# WiFi Standards

Wi-Fi standards are a series of specifications developed by the IEEE under the 802.11 family that define how wireless networks operate. Each generation, from 802.11b and 802.11g through to 802.11ac (Wi-Fi 5) and 802.11ax (Wi-Fi 6), brings improvements in speed, range, efficiency, and the ability to handle more simultaneous connections. Understanding the differences between standards helps in selecting the right hardware for a given environment.

Visit the following resources to learn more:

- [@article@WiFi Standards Explained: Compare 802.11be, 802.11ac, 802.11ax and More](https://www.fs.com/blog/80211-wireless-standards-explained-35.html)
- [@video@WIFI (wireless) Standards and Generations Explained](https://www.youtube.com/watch?v=hhks5xSpM-0&list=PL7zRJGi6nMRyB2f3BHfecjyd7_nuO63P0&index=1)

## Wireless Networking

# Wireless Networking

Wireless networking refers to the technology that allows devices to connect to a network and communicate without physical cables, using radio frequency signals instead. It encompasses standards like Wi-Fi, Bluetooth, and cellular networks, each suited to different ranges and use cases. Wireless networks introduce unique considerations around signal strength, interference, frequency bands, and security that wired networks do not face.

Visit the following resources to learn more:

- [@article@What Is A Wireless Network? Types Of Wireless Networks](https://www.fortinet.com/resources/cyberglossary/wireless-network)
- [@video@Wireless Networking Technology](https://www.youtube.com/watch?v=hhks5xSpM-0&list=PL7zRJGi6nMRyB2f3BHfecjyd7_nuO63P0)

## Wireless Security

# Wireless Security

Wireless security refers to the measures taken to protect wireless networks from unauthorized access, eavesdropping, and attacks. Because wireless signals travel through the air and can be intercepted by anyone within range, securing Wi-Fi networks requires encryption, strong authentication, and proper configuration. Key considerations include choosing strong encryption protocols, using strong passwords, and monitoring for rogue access points.

Visit the following resources to learn more:

- [@article@Wireless Security Fundamentals](https://www.networkacademy.io/ccna/wireless/wireless-security-fundamentals)
- [@article@What is Wi-Fi security?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wi-fi-security.html)
- [@video@Free CCNA | Wireless Security](https://www.youtube.com/watch?v=wHXKo9So5y8)

## Wireshark

# Wireshark

Wireshark is an open-source network protocol analyzer that captures and displays the data traveling across a network in real time. Engineers use it to inspect individual packets, decode protocols, diagnose connectivity problems, and investigate security incidents at a granular level. It supports hundreds of protocols and is one of the most widely used tools for deep network troubleshooting and analysis.

Visit the following resources to learn more:

- [@official@Wireshark](https://www.wireshark.org/)
- [@opensource@wireshark](https://github.com/wireshark/wireshark)
- [@video@ES  Skip navigation Search    Create   Avatar image Wireshark Full Course 🦈| Wireshark Tutorial Beginner to Advance](https://www.youtube.com/watch?v=n4muxtqLhN4)

## Wlan

# WLAN

A WLAN, or Wireless Local Area Network, is a type of LAN that uses wireless radio signals instead of cables to connect devices. It is the technology behind Wi-Fi networks found in homes, offices, and public spaces. WLANs offer the convenience of mobility within the coverage area, though they can be more susceptible to interference and security risks than wired networks.

Visit the following resources to learn more:

- [@article@What is a wireless LAN?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-wireless-lan.html)
- [@video@WLAN vs. Wi-Fi: What's the Difference?](https://www.youtube.com/watch?v=xt0YqqbvSFQ)

## Wpa Vs Wps

# WPA vs WPS

WPA (Wi-Fi Protected Access) is a security protocol designed to protect wireless networks through encryption and authentication, with WPA2 and WPA3 being the current standards offering strong AES-based encryption. WPS (Wi-Fi Protected Setup) is a feature designed to simplify the process of connecting devices to a Wi-Fi network, typically using a PIN or button press. However, WPS has well-known security vulnerabilities (particularly the PIN method) and is generally recommended to be disabled on network equipment.

Visit the following resources to learn more:

- [@article@Wi-Fi Security Comparisons](https://www.avast.com/c-wep-vs-wpa-or-wpa2)
- [@video@WiFi (Wireless) Password Security](https://www.youtube.com/watch?v=WZaIfyvERcA)

## Zero Trust Architecture

# Zero Trust Architecture

Zero Trust is a security model based on the principle of "never trust, always verify" — meaning no user, device, or network segment is trusted by default, even if they are inside the corporate network. Every access request must be authenticated, authorized, and continuously validated regardless of where it originates. Zero Trust architecture replaces the traditional perimeter-based security model and is increasingly adopted as networks become more distributed and cloud-based.

Visit the following resources to learn more:

- [@article@What is zero trust?](https://www.ibm.com/think/topics/zero-trust)
- [@video@Cybersecurity and Zero Trust](https://www.youtube.com/watch?v=FMMWSLIcaME)
