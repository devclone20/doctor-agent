# Linux Roadmap

## Adding Disks

# Adding Disks

Adding disks in Linux involves partitioning, creating filesystems, and mounting. Use `lsblk` to list devices, `fdisk /dev/sdX` to create partitions, `mkfs.ext4 /dev/sdX1` to create filesystems, and `mount /dev/sdX1 /mount/point` to mount. This process prepares new storage devices for seamless integration into the Linux filesystem hierarchy.

Visit the following resources to learn more:

- [@article@How to Add a New Disk](https://linuxconfig.org/how-to-add-new-disk-to-existing-linux-system)
- [@article@How to Add a New Disk to an Existing Linux Server](https://www.tecmint.com/add-new-disk-to-an-existing-linux/)

## Archiving And Compressing

# Archiving

Linux offers powerful utilities for archiving, where multiple files and directories are combined into a single file, primarily for backup and simplification of distribution. The main tools used for this purpose are `tar`, `gzip`, and `bzip2`.

The `tar` command, originally for tape archiving, is a versatile tool that can manage and organize files into one archive. Meanwhile, `gzip` and `bzip2` are used for file compression, reducing the file size and making data transmission easier.

Take a look at the following commands in use:

    # To create a tar archive:
    tar cvf archive_name.tar directory_to_archive/
    
    # To extract a tar archive:
    tar xvf archive_name.tar
    
    # To create a gzip compressed tar archive:
    tar cvzf archive_name.tar.gz directory_to_archive/
    
    #To create a bzip2 compressed tar archive:
    tar cvjf archive_name.tar.bz2 directory_to_archive/
    

Remember, in Linux, archiving and compression are separate processes, hence `tar` to archive and `gzip`/`bzip2` to compress. Although they're commonly used together, they can very much be used separately as per the requirements.

Visit the following resources to learn more:

- [@article@Linux File Packaging and Compression](https://labex.io/tutorials/linux-file-packaging-and-compression-385413)

## Authentication Logs

# Authentication Logs

Authentication logs in Linux record all auth-related events like logins, password changes, and sudo commands. Located at `/var/log/auth.log` (Debian) or `/var/log/secure` (RHEL/CentOS), these logs help detect brute force attacks and unauthorized access attempts. Use `tail /var/log/auth.log` to view recent entries. Regular log analysis is essential for server security monitoring.

Here is an example of how you can use the `tail` command to view the last few entries of the authentication log:

    tail /var/log/auth.log

Visit the following resources to learn more:

- [@article@Monitoring Linux Authentication Logs](https://betterstack.com/community/guides/logging/monitoring-linux-auth-logs/)
- [@article@How to Check Linux Login History - Linux Handbook](https://linuxhandbook.com/linux-login-history/)

## Available Memory  Disk

# Available Memory and Disk

Linux provides tools like `free`, `vmstat`, and `top` to monitor system memory usage and performance. The `free -h` command shows total, used, free, shared, buffer/cache, and available memory in human-readable format. Regular memory monitoring helps maintain optimal server performance, prevent overload, and troubleshoot resource issues effectively.

Visit the following resources to learn more:

- [@article@5 Best Ways To Check Available Memory In Linux](https://itslinuxfoss.com/5-ways-check-available-memory-linux/)
- [@article@Free vs. Available Memory in Linux](https://linuxblog.io/free-vs-available-memory-in-linux/)

## Awk

# AWK

AWK is a powerful text-processing language for Unix-like systems, named after its creators Aho, Weinberger, and Kernighan. It reads files line by line, identifies patterns, and executes actions on matches. Commonly used in bash scripts for sorting, filtering, and report generation.

Example: `awk '{print $1,$2}' filename` prints first two fields of each line.

Visit the following resources to learn more:

- [@article@IBM.com: Awk by Example](https://developer.ibm.com/tutorials/l-awk1/)
- [@article@AWK Tutorial](https://linuxhandbook.com/awk-command-tutorial/)
- [@article@Linux awk Command: Text Processing](https://labex.io/tutorials/linux-linux-awk-command-text-processing-388493)
- [@video@Learning Awk Is Essential For Linux Users](https://www.youtube.com/watch?v=9YOZmI-zWok)
- [@feed@Explore top posts about Bash](https://app.daily.dev/tags/bash?ref=roadmapsh)

## Background  Foreground Processes

# Background and Foreground Processes

Linux processes run in foreground (taking direct user input) or background (running independently). Send processes to background with `&` or `bg` command. Bring to foreground with `fg`. Use Ctrl+Z to pause, then `bg` to resume in background. Part of job control for managing multiple tasks simultaneously from single terminal.

Visit the following resources to learn more:

- [@article@Understanding Foreground and Background Processes](https://linuxconfig.org/understanding-foreground-and-background-linux-processes)
- [@article@Running Linux Commands in Background and Foreground](https://linuxhandbook.com/run-process-background/)
- [@article@Foreground and Background Processes - LinuxOPsys](https://linuxopsys.com/foreground-and-background-processes-co11/)

## Basic Commands

# Linux Navigation Basics: Basic Commands

Linux Navigation Basics is about using simple commands to move around and manage files on your computer. For example, `cd` lets you go into different folders, `ls` shows you what files and folders are inside, and `pwd` tells you where you are currently. These commands help you easily find and organize your files.

Visit the following resources to learn more:

- [@article@Linux Filesystem Navigation Basics](https://linuxconfig.org/filesystem-basics)
- [@article@Linux Navigation and File Management](https://www.digitalocean.com/community/tutorials/basic-linux-navigation-and-file-management)
- [@article@Basic Navigation Commands: cd, ls, and pwd ](https://www.linuxbash.sh/post/basic-navigation-commands-cd-ls-and-pwd)

## Boot Loaders

# Boot Loaders

Boot loaders load the OS kernel into memory when systems start. Common Linux boot loaders include GRUB (modern, feature-rich with graphical interface) and LILO (older, broader hardware support). Boot loaders initialize hardware, load drivers, start schedulers, and execute init processes. Use `sudo update-grub` to update GRUB configuration. Enable multi-OS booting on single machines.

Visit the following resources to learn more:

- [@official@The GNU GRUB](https://www.gnu.org/software/grub/)
- [@article@Bootloader - Archlinux wiki](https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader)
- [@article@Most Popular Linux Boot Loaders](https://thelinuxcode.com/what-is-a-boot-loader/)
- [@article@GRUB Bootloader in Linux](https://phoenixnap.com/kb/what-is-grub)

## Booting Linux

# Booting Linux

Linux booting involves several stages: POST, MBR, GRUB, Kernel, Init, and GUI/CLI. The bootloader loads the kernel into memory, which detects hardware, loads drivers, mounts filesystems, starts system processes, and presents login prompts. GRUB configuration is managed through `/etc/default/grub` with settings like timeout and default boot options.

Visit the following resources to learn more:

- [@official@The GNU GRUB](https://www.gnu.org/software/grub/)
- [@article@Booting process of Linux - Wikipedia](https://en.wikipedia.org/wiki/Booting_process_of_Linux)
- [@article@The Linux Booting Process](https://thelinuxcode.com/the-linux-booting-process-6-steps-described-in-detail/)

## Cgroups

# Cgroups

Cgroups (control groups) are a Linux kernel feature that organizes processes into hierarchical groups and limits their resource usage (CPU, memory, disk I/O). Essential for containerization, cgroups prevent containers from monopolizing host resources, ensuring system stability and performance. Use `cgcreate` to create groups, assign processes, and set resource limits effectively.

Visit the following resources to learn more:

- [@official@Control Groups — The Linux Kernel](https://docs.kernel.org/admin-guide/cgroup-v1/)
- [@article@cgroups — Linux manual page](https://www.man7.org/linux/man-pages/man7/cgroups.7.html)
- [@article@Introduction to Control Groups (Cgroups)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/resource_management_guide/chap-introduction_to_control_groups)

## Checking Service Logs

# Checking Service Logs

Systemd captures output from all managed services and stores it in the journal, a binary log managed by journald. You can view logs for a specific service using journalctl -u service-name. Useful flags include -f to follow logs in real time, --since and --until to filter by time range, and -n to limit the number of lines shown. Logs include both stdout/stderr from the process and systemd lifecycle events.

Visit the following resources to learn more:

- [@article@Journalctl Explained: How To View And Analyze Systemd Logs.](https://uptimerobot.com/knowledge-hub/logging/journalctl-explained-how-to-view-and-analyze-systemd-logs/)
- [@article@How To Use journalctl to View and Manipulate systemd Logs on Linux](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)

## Checking Service Status

# Checking Service Status

systemctl status service-name gives a real-time snapshot of a service: whether it's active, inactive, or failed; its process ID; recent log lines; and any error messages from the last run. For a quick boolean check, systemctl is-active and systemctl is-enabled return simple values suitable for use in scripts. The enabled/disabled state indicates whether the service is configured to start automatically at boot, separate from whether it's currently running.

Visit the following resources to learn more:

- [@article@Checking the Status of a Service Without Having an Exact Name](https://www.baeldung.com/linux/initialization-managers-service-status)

## Command Help

# Command Help

Linux command help provides documentation and usage information for shell commands. Use `man command` for detailed manuals, `help command` for shell built-ins, `command --help` for quick options, and `tldr command` for practical examples. Essential for learning command syntax, parameters, and functionality in Linux terminal environments.

Visit the following resources to learn more:

- [@opensource@tldr-pages/tldr](https://github.com/tldr-pages/tldr)
- [@article@Using the Help Command in Linux](https://linuxhandbook.com/help-command/)
- [@article@Chapter 10: Getting Help in Linux Terminal](https://itsfoss.com/linux-command-help/)
- [@article@Get Help on Linux Commands](https://labex.io/tutorials/linux-get-help-on-linux-commands-18000)

## Command Path

# Command Path in Shell

The command path is a variable that is used by the shell to determine where to look for the executable files to run. Linux commands are nothing but programs residing in particular directories. But, one does not have to navigate to these directories every time to run these programs. The command path comes to the rescue!

Usually, when you type a command in the terminal, the shell needs to know the absolute path of the command's executable to run it. Instead of typing the full path each time, command paths allow the shell to automatically search the indicated directories in the correct order. These paths are stored in the $PATH environment variable.

Visit the following resources to learn more:

- [@article@Linux path environment variable](https://linuxconfig.org/linux-path-environment-variable)
- [@article@How to find a path of a Linux command like a pro](https://www.cyberciti.biz/howto/finding-a-path-of-a-linux-command-like-a-pro/)

## Conditionals

# Conditionals

Shell conditionals allow scripts to make decisions based on conditions using `if`, `elif`, and `else` statements. These control process flow by evaluating string variables, arithmetic tests, or process status. Conditions are checked sequentially - if true, the corresponding code block executes; otherwise, it moves to the next condition until finding a match or reaching `else`.

Visit the following resources to learn more:

- [@article@Bash Scripting: Conditionals](https://linuxconfig.org/bash-scripting-conditionals)
- [@article@Using If Else in Bash Scripts [Examples] - Linux Handbook](https://linuxhandbook.com/if-else-bash/)

## Container Runtime

# Container Runtime

Container runtime is software responsible for running containers in Linux, providing image transport, storage, execution, and network interactions. Popular options include Docker (comprehensive ecosystem), Containerd (lightweight standalone), and CRI-O (Kubernetes-optimized). Each runtime offers specific features and benefits for different use cases in containerized application deployment and management.

Visit the following resources to learn more:

- [@article@Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
- [@article@What are Container Runtimes? Types and Popular Runtime](https://www.wiz.io/academy/container-runtimes)
- [@article@What are container runtimes?](https://opensource.com/article/21/9/container-runtimes)

## Containerization

# Containerization

Containerization is a virtualization method that encapsulates applications in containers with isolated operating environments, enabling reliable deployment across computing environments. Unlike VMs requiring full operating systems, containers share the host system's user space, making them lightweight and faster. Docker is a popular Linux containerization tool for managing complex applications.

Visit the following resources to learn more:

- [@official@Docker](https://docker.com)
- [@official@Kubernetes](https://kubernetes.io)
- [@article@What is Containerization? - Containerization Explained - AWS](https://aws.amazon.com/what-is/containerization/)
- [@article@What is Containerization? - DigitalOcean](https://www.digitalocean.com/resources/articles/what-is-containerization)

## Copying And Renaming

# Copying and Renaming Files

Essential Linux file operations use `cp` to copy files and `mv` to move/rename them. The `cp` command copies files from source to destination, while `mv` moves or renames files/directories. Both commands use the syntax `command source destination`. These case-sensitive commands are fundamental for daily file management tasks in Linux systems.

Visit the following resources to learn more:

- [@article@mv and cp - Linux.org](https://www.linux.org/threads/mv-and-cp.54793/)
- [@article@Mastering cp and mv Commands in Linux](https://dev.to/ldwit/mastering-cp-and-mv-commands-in-linux-plus-related-cmds-5cc9)
- [@article@Linux cp Command: File Copying](https://labex.io/tutorials/linux-linux-cp-command-file-copying-209744)
- [@article@Linux mv Command: File Moving and Renaming](https://labex.io/tutorials/linux-linux-mv-command-file-moving-and-renaming-209743)

## Create  Delete  Update

# Create, Update, and Delete Users

Linux user management involves creating, updating, and deleting user accounts for system security and resource utilization. Key commands: `useradd`/`adduser` (create users), `usermod` (update user details like home directory/shell), `userdel` (delete users). Essential for maintaining secure, organized multi-user system environments and efficient resource allocation.

Visit the following resources to learn more:

- [@article@Creating, Modifying, and Deleting User Accounts](https://serveracademy.com/courses/linux-server-administration/creating-modifying-and-deleting-user-accounts/)
- [@article@How to create, update, and delete users account on Linux](https://linuxconfig.org/how-to-create-modify-and-delete-users-account-on-linux)
- [@article@User Management in Linux: A Beginner's Guide](https://dev.to/austinozor/user-management-in-linux-a-beginners-guide-to-creating-modifying-and-deleting-users-fhf)

## Creating  Deleting Files  Dirs

# Creating Files

Linux file creation uses `touch` for empty files, `echo "text" > filename` for text files, or `cat > filename` for interactive input. Commands like `mkdir` create directories. File creation is immediate and permanent. Essential for organizing data, scripts, and configuration files in Linux systems.

Visit the following resources to learn more:

- [@article@What is the Difference Between Cat and Touch Command](https://linuxways.net/centos/what-is-the-difference-between-cat-and-touch-command/)
- [@article@Creating and Deleting Files / Directories in Linux](https://useful.codes/creating-and-deleting-files-directories-in-linux/)
- [@article@Creating, Moving, and Deleting Files and Folders](https://dev.to/alkesh009/linux-basics-part-4-creating-moving-and-deleting-files-and-folders-5hip)

## Creating New Services

# Creating Services

Creating Linux services involves setting up background applications using systemd service files. Services run continuously performing essential tasks like web servers, databases, and mail servers. Create `.service` files in `/etc/systemd/system/` with Unit, Service, and Install sections. Control services using `systemctl` commands. Best practice: avoid running services as root for security.

Visit the following resources to learn more:

- [@article@How to Create a systemd Service in Linux](https://linuxhandbook.com/create-systemd-services/)
- [@article@A Beginner's Guide to Creating Linux Services](https://www.fosslinux.com/111815/a-guide-to-creating-linux-services-with-systemd.htm)

## Cut

# Cut Command

The `cut` command is a text processing utility that allows you to cut out sections of each line from a file or output, and display it on the standard output (usually, the terminal). It's commonly used in scripts and pipelines, especially for file operations and text manipulation.

Visit the following resources to learn more:

- [@article@Cut Command in Linux | Linuxize](https://linuxize.com/post/linux-cut-command/)
- [@article@Linux cut Command: Text Cutting](https://labex.io/tutorials/linux-linux-cut-command-text-cutting-219187)

## Debugging

# Debugging

Shell script debugging in Linux uses tools like bash's `-x` option for execution traces, `trap`, `set` commands, and external tools like `shellcheck`. Use `#!/bin/bash -x` in scripts or `bash -x script.sh` from command line for tracing. These debugging options help detect, trace, and fix errors to make scripts more efficient and error-proof.

Visit the following resources to learn more:

- [@article@How To Debug a Bash Shell Script Under Linux or UNIX](https://www.cyberciti.biz/tips/debugging-shell-script.html)
- [@article@How to Debug a Bash Shell Script in Linux](https://www.linuxtechi.com/debugging-shell-scripts-in-linux/)
- [@article@How to Debug Bash Scripts](https://thelinuxcode.com/debug-bash-script/)

## Dhcp

# DHCP

DHCP (Dynamic Host Configuration Protocol) automatically allocates IP addresses and network configuration to clients, ensuring unique addresses for each machine. In Linux, install with `sudo apt-get install isc-dhcp-server` and configure via `/etc/dhcp/dhcpd.conf`. DHCP servers require static IPs for effective management and can handle DNS and network data. The DHCP server effectively manages the IP addresses and information related to them, making sure that each client machine gets a unique IP and all the correct network information.

Visit the following resources to learn more:

- [@article@Dynamic Host Configuration Protocol - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
- [@article@DHCP Protocol: How Dynamic Host Configuration Protocol Works](https://network-guides.com/dhcp-protocol/)

## Directory Hierarchy Overview

# Understanding Directory Hierarchy

In Linux, understanding the directory hierarchy is crucial for efficient navigation and file management. A Linux system's directory structure, also known as the Filesystem Hierarchy Standard (FHS), is a defined tree structure that helps to prevent files from being scattered all over the system and instead organise them in a logical and easy-to-navigate manner.

*   `/`: Root directory, the top level of the file system.
*   `/home`: User home directories.
*   `/bin`: Essential binary executables.
*   `/sbin`: System administration binaries.
*   `/etc`: Configuration files.
*   `/var`: Variable data (logs, spool files).
*   `/usr`: User programs and data.
*   `/lib`: Shared libraries.
*   `/tmp`: Temporary files.
*   `/opt`: Third-party applications.

Visit the following resources to learn more:

- [@article@Linux Directory Structure Explained for Beginners](https://linuxhandbook.com/linux-directory-structure/)
- [@article@Overview of File System Hierarchy Standard (FHS)](https://access.redhat.com/documentation/ru-ru/red_hat_enterprise_linux/4/html/reference_guide/s1-filesystem-fhs#s3-filesystem-usr)
- [@video@The Linux File System Explained in 1,233 Seconds](https://youtu.be/A3G-3hp88mo?si=sTJTSzubdb0Vizjr)

## Disks And Filesystems

# Disks and Filesystems

Linux uses various filesystems to organize, store, and retrieve data from storage devices. Popular filesystems include EXT4 (robust for Linux volumes), FAT32 (compatible with all OS for removable media), NTFS, and Btrfs. Each has specific advantages and use cases. Use `df -T` command to display filesystem types, disk space usage, and mounted device information.

Visit the following resources to learn more:

- [@official@Filesystems in the Linux Kernel](https://www.kernel.org/doc/html/v6.16-rc2/filesystems/index.html)
- [@article@Partitions And Filesystems In Linux - Introduction](https://www.linuxfordevices.com/tutorials/linux/partitions-and-filesystems)
- [@article@Overview of File System Hierarchy Standard (FHS)](https://access.redhat.com/documentation/ru-ru/red_hat_enterprise_linux/4/html/reference_guide/s1-filesystem-fhs#s3-filesystem-usr)
- [@article@Understanding Linux Filesystems: Inodes, Block Sizes, and Data](https://www.linuxjournal.com/content/understanding-linux-filesystems-inodes-block-sizes-and-data-structures)

## Dns Resolution

# DNS Resolution

DNS (Domain Name System) converts hostnames to IP addresses, enabling users to access websites without remembering numeric addresses. Linux systems use `/etc/resolv.conf` to configure DNS resolution. Applications consult the DNS resolver, which communicates with DNS servers for address translation. Use `nslookup` or `dig` commands to query DNS and troubleshoot network connectivity issues.

Visit the following resources to learn more:

- [@article@Setup DNS Resolution With "resolv.conf" in Examples](https://www.shellhacks.com/setup-dns-resolution-resolvconf-example/)
- [@article@DNS Resolution](https://wiki.archlinux.org/title/Domain_name_resolution)
- [@article@nslookup command](https://linuxconfig.org/nslookup-linux-command)
- [@article@dig command](https://linuxhandbook.com/dig-command/)

## Docker

# Docker

Docker is an open-source containerization platform that uses OS-level virtualization to package applications with dependencies into lightweight containers. In Linux, Docker containers share the kernel and use features like namespaces and cgroups for isolation. This provides less overhead than traditional VMs while enabling consistent deployment across environments.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Docker](https://docker.com)
- [@official@Docker Documentation](https://docs.docker.com/)
- [@article@How To Install and Use Docker on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

## Editing Files

# Editing Files

Linux, like other operating systems, allows file editing for numerous purposes, whether you need to configure some system functionality or writing scripts. There's a variety of text editors available in Linux by default, these include: `nano`, `vi/vim`, `emacs`, and `gedit`. Each of these has its own learning curve and set of commands.

Visit the following resources to learn more:

- [@article@Editing Files in Linux Command Line](https://itsfoss.com/edit-files-linux/)
- [@article@The Complete Guide to Text Editing in Linux with Nano and Vim](https://thelinuxcode.com/how-to-edit-file-in-linux/)
- [@article@Vim Tutorial for Beginners](https://linuxconfig.org/vim-tutorial)

## Environment Variables

# Environment Variables

Environment variables are dynamic named values that can affect the behavior of running processes in a shell. They exist in every shell session. A shell session's environment includes, but is not limited to, the user's home directory, command search path, terminal type, and program preferences.

Environment variables help to contribute to the fantastic and customizable flexibility you see in Unix systems. They provide a simple way to share configuration settings between multiple applications and processes in Linux.

Visit the following resources to learn more:

- [@article@Environment Variables in Linux](https://labex.io/tutorials/linux-environment-variables-in-linux-385274)
- [@article@Linux Environment Variables List, Set, Create & Remove](https://www.computernetworkingnotes.com/linux-tutorials/linux-environment-variables-list-set-create-remove.html)
- [@article@How to Set and List Environment Variables in Linux](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)

## Ethernet  Arprarp

# Ethernet, ARP and RARP

Three crucial Linux networking components: Ethernet enables LAN device communication, ARP (Address Resolution Protocol) translates IP addresses to MAC addresses for direct network communication, and RARP (Reverse ARP) converts MAC addresses to IP addresses when devices know their MAC but need their IP. Essential for diagnosing and managing Linux networking issues.

Visit the following resources to learn more:

- [@article@A Comprehensive guide to Linux Networking](https://centlinux.com/linux-networking/)
- [@article@A Beginner's Guide to Linux Networking Fundamentals](https://dev.to/iaadidev/a-beginners-guide-to-linux-networking-fundamentals-dev-ops-prerequisite-7-434o)
- [@video@ARP Explained - Address Resolution Protocol](https://www.youtube.com/watch?v=cn8Zxh9bPio)
- [@video@What is Ethernet?](https://www.youtube.com/watch?v=HLziLmaYsO0)

## Expand

# Expand

The `expand` command converts tabs to spaces in text files, useful for consistent formatting across different systems and editors. Default conversion is 8 spaces per tab. Use `expand filename` for basic conversion or `expand -t 4 filename` to specify 4 spaces per tab. Essential for maintaining code readability and consistent indentation in shell scripts.

Visit the following resources to learn more:

- [@article@expand — Linux manual page](https://www.man7.org/linux/man-pages/man1/expand.1.html)
- [@article@How to Use the 'expand' Command (with examples)](https://commandmasters.com/commands/expand-common/)

## File Permissions

# Linux File Permissions

In Linux systems, rights and privileges are assigned to files and directories in the form of permissions. These permissions indicate who can read, write, or execute (run) them. In Linux, there are three types of users: owners, groups, and others who can have a different set of permissions.

In fact, permissions on the system are there for a reason: to prevent unprivileged users from making changes on the system that would ultimately affect other users. With inadequate permissions, unprivileged users are able to make changes that would be beneficial or harmless to the Linux system.

Let's have a look at an example:

    -rwxr--r-- 1 root root 4096 Jan 1 12:00 filename
    

From the above example, the first character `-` indicates if it is a regular file(`-`) or directory(`d`). The following group of three characters(`rwx`) represents the permissions for the file owner. The next three characters(`r--`) represent permissions for the group and the last set of three characters(`r--`) represents permissions for others.

The `r` indicates that the file can be read, `w` indicates that the file can be written to, and `x` indicates that the file can be executed.

The permissions can be changed using the `chmod`, `chown`, and `chgrp` commands.

Visit the following resources to learn more:

- [@article@Linux File Permissions](https://linuxhandbook.com/linux-file-permissions/)
- [@article@Linux Permissions of Files](https://labex.io/tutorials/linux-permissions-of-files-270252)
- [@video@Linux File Permissions in 5 Minutes](https://www.youtube.com/watch?v=LnKoncbQBsM)

## File Transfer

# File Transfer

Linux file transfer involves copying or moving files between systems over networks. Command-line tools support protocols like FTP, HTTP, SCP, SFTP, and NFS. Common commands include `scp`, `rsync`, and `wget`. Example: `scp /local/file username@remote:/destination` copies files to remote systems. These tools make network file sharing streamlined, easier, and more secure.

Visit the following resources to learn more:

- [@article@How to Use Linux FTP Command to Transfer Files](https://linuxize.com/post/how-to-use-linux-ftp-command-to-transfer-files/)
- [@article@Rsync Command in Linux with Examples](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
- [@article@Using scp Command in Linux](https://linuxhandbook.com/scp-command/)
- [@article@Wget Command in Linux with Examples](https://linuxize.com/post/wget-command-examples/)

## Filesystems

# Filesystems

Filesystems define how files are stored and organized on Linux storage disks, ensuring data integrity, reliability, and efficient access. Linux supports various types like EXT4, XFS, BTRFS with different performance and recovery capabilities. All files start from root directory '/'. Use `df -T` to display filesystem types and disk usage status. Essential for Linux administration tasks.

Visit the following resources to learn more:

- [@official@Filesystems in the Linux Kernel](https://www.kernel.org/doc/html/v6.16-rc2/filesystems/index.html)
- [@article@df command in Linux (Check Disk Space)](https://linuxize.com/post/how-to-check-disk-space-in-linux-using-the-df-command/)
- [@article@Partitions And Filesystems In Linux - Introduction](https://www.linuxfordevices.com/tutorials/linux/partitions-and-filesystems)

## Finding  Installing Packages

# Finding and Installing Packages

Linux package managers like `apt`, `yum`, and `dnf` automate software installation, upgrading, configuring, and removal. Debian-based systems: `sudo apt-get update && sudo apt-get install package-name`. Fedora/CentOS: `sudo dnf update && sudo dnf install package-name`. Package management eliminates manual compilation from source code. Root permissions required for installation.

Visit the following resources to learn more:

- [@official@APT Package Manager](https://www.debian.org/doc/manuals/apt-guide/index.en.html)
- [@official@Yum Package Manager](http://yum.baseurl.org/)
- [@official@Using the DNF Software Package Manager](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)
- [@article@Linux Package Manager Explained](https://geekflare.com/dev/linux-package-manager-explained/)
- [@article@8 Best Package Manager for Linux](https://linuxsimply.com/linux-basics/package-management/best-package-manager/)

## Grep

# GREP

GREP (Global Regular Expression Print) is a powerful text search utility that finds and filters text matching specific patterns in files. It searches line by line and prints matching lines to the screen. Essential for shell scripts and command-line operations. Example: `grep "pattern" fileName` searches for specified patterns. Alternative: `ripgrep` offers enhanced performance and features.

Visit the following resources to learn more:

- [@opensource@Ripgrep: GitHub Repository](https://github.com/BurntSushi/ripgrep)
- [@article@Grep and Regular Expressions for Beginners](https://ryanstutorials.net/linuxtutorial/grep.php)
- [@article@bgsu.edu: Advanced Grep Topics](https://caspar.bgsu.edu/~courses/Stats/Labs/Handouts/grepadvanced.htm)
- [@article@Linux grep Command: Pattern Searching](https://labex.io/tutorials/linux-linux-grep-command-pattern-searching-219192)

## Head

# Head Command

The `head` command in Linux is a text processing utility that allows a user to output the first part (or the "head") of files. It is commonly used for previewing the start of a file without loading the entire document into memory, which can act as an efficient way of quickly examining the data in very large files. By default, the `head` command prints the first 10 lines of each file to standard output, which is the terminal in most systems.

Visit the following resources to learn more:

- [@article@Head Command in Linux - 5 Essential Examples](https://linuxhandbook.com/head-command/)
- [@article@Linux head Command: File Beginning Display](https://labex.io/tutorials/linux-linux-head-command-file-beginning-display-214302)

## Icmp

# ICMP

Internet Control Message Protocol (ICMP) is a supportive protocol used by network devices to communicate error messages and operational information. Essential for Linux network troubleshooting, ICMP enables tools like `ping` and `traceroute` to diagnose network connectivity and routing issues. Use `ping www.google.com` to send ICMP echo requests and test network reachability effectively.

Visit the following resources to learn more:

- [@article@icmp(7) — Linux manual page](https://www.man7.org/linux/man-pages/man7/icmp.7.html)
- [@article@Understanding ICMP Packets with Examples](https://www.howtouselinux.com/post/icmp-packets)

## Inodes

# Inodes

An inode (index node) is a data structure in Linux filesystems that stores metadata about files and directories except their names and actual data. Contains file size, owner, permissions, timestamps, and more. Each file has a unique inode number for identification. Understanding inodes helps with advanced operations like linking and file recovery. Use `ls -i filename` to view inode numbers.

Visit the following resources to learn more:

- [@article@Introduction to Inodes](https://linuxjourney.com/lesson/inodes)
- [@article@Index Nodes — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/ext4/inodes.html?highlight=inode)

## Install  Remove  Upgrade Packages

# Install, Remove, and Upgrade Packages

Linux package management handles installing, removing, and upgrading pre-compiled software modules. Different distributions use specific package managers: `apt` (Debian/Ubuntu), `yum`/`dnf` (Fedora/RHEL/CentOS), `zypper` (SUSE). Example installation: `sudo apt-get install packagename`. Each manager has specific commands for removal and upgrades. Critical skill for effective Linux system administration.

## Ip Routing

# IP Routing

IP routing in Linux involves configuring routing tables and network routes for packet forwarding across networks. The kernel handles route selection to send packets to their destinations. Use the `ip` command (replacing deprecated `ifconfig`) for network configuration. Example: `ip route show` displays all kernel-known routes for network troubleshooting and management.

Visit the following resources to learn more:

- [@article@Linux Set Up Routing with ip Command](https://www.cyberciti.biz/faq/howto-linux-configuring-default-route-with-ipcommand/)
- [@article@Linux Networking: A Simplified Guide to IP Addresses](https://www.linuxjournal.com/content/linux-networking-simplified-guide-ip-addresses-and-routing)

## Join

# join Command

`join` is a powerful text processing command in Linux. It lets you combine lines of two files on a common field, which works similar to the 'Join' operation in SQL. It's particularly useful when you're dealing with large volumes of data. Specifically, `join` uses the lines from two files to form lines that contain pairs of lines related in a meaningful way.

Visit the following resources to learn more:

- [@article@join(1) — Linux manual page](https://www.man7.org/linux/man-pages/man1/join.1.html)
- [@article@join command in Linux with examples](https://linuxconfig.org/join)
- [@article@Linux join Command: File Joining](https://labex.io/tutorials/linux-linux-join-command-file-joining-219193)

## Killing Processes

# Kill Processes

The `kill` command terminates processes manually by sending specific signals to Process IDs (PIDs). Used when processes behave unexpectedly due to system bugs or accidental initiation. Syntax: `kill [signal or option] PID(s)`. Essential for Linux process management, allowing administrators to stop, pause, or terminate problematic processes and maintain system stability.

Visit the following resources to learn more:

- [@article@Using Kill Command in Linux](https://linuxhandbook.com/kill-command/)
- [@article@Kill Command in Linux](https://linuxize.com/post/kill-command-in-linux/)

## Listing  Finding Processes

# Listing and Finding Processes

Linux processes can be monitored using the `proc` virtual filesystem and commands like `ps`, `top`, and `htop`. Use `ps -ef` for process snapshots, `top`/`htop` for real-time views. The `/proc` directory contains detailed process information. View specific process details with `cat /proc/{PID}/status`. Essential for system performance monitoring and troubleshooting.

Visit the following resources to learn more:

- [@article@The /proc File System](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- [@article@What is a Process in Linux/Unix?](https://www.scaler.com/topics/linux-process/)
- [@article@Exploring the Linux /proc Filesystem](https://www.redhat.com/en/blog/linux-proc-filesystem)

## Listing Installed Packages

# Listing Installed Packages

Linux distributions use different package managers: `apt` (Debian-based), `dnf` (Fedora), `zypper` (OpenSUSE), `pacman` (Arch). Listing installed packages helps with auditing software and deployment automation. Commands: `sudo apt list --installed` for apt systems, `dnf list installed` for dnf systems. Each distribution has its own syntax for this command.

Visit the following resources to learn more:

- [@official@APT Package Manager](https://www.debian.org/doc/manuals/apt-guide/index.en.html)
- [@article@5 ways to list installed packages in Linux](https://www.howtouselinux.com/post/list-installed-packages-in-linux)
- [@article@Linux Package Manager Explained](https://geekflare.com/dev/linux-package-manager-explained/)

## Literals

# Literals

Shell literals are fixed values in source code including string literals (enclosed in quotes), numeric literals (sequences of digits), and boolean literals (1=true, 0=false). String examples: 'Hello, world!' or "Hello, world!". Numeric examples: 25, 100, 1234. Understanding literals is fundamental for shell scripting readability and functionality in Linux programming.

Visit the following resources to learn more:

- [@article@Bash Tutorial - Quoting literal text](https://riptutorial.com/bash/example/2465/quoting-literal-text)
- [@article@Handling Special Characters in Shell Scripts](https://www.baeldung.com/linux/special-characters-in-shell-scripts)

## Logs

# System Logs

Linux maintains logs documenting system activities, errors, and kernel messages. Boot logs record all operations during system startup for troubleshooting. Use `dmesg` to view kernel ring buffer messages in real-time, or access logs in `/var/log`. Systemd uses `journalctl` for logging. Log levels range from emergency (system unusable) to debug messages.

Visit the following resources to learn more:

- [@article@How to Use journalctl Command to Analyze Logs in Linux](https://linuxhandbook.com/journalctl-command/)
- [@article@How to Check System Logs on Linux](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm)
- [@article@What is dmesg in Linux, And How Do I Use It?](https://linuxconfig.org/what-is-dmesg-and-how-do-i-use-it)

## Loops

# Loops

Shell loops automate repetitive tasks with three types: `for` (iterates over lists), `while` (executes while condition true), `until` (runs until condition true). Example: `for i in 1 2 3; do echo "$i"; done` outputs each number. Essential for script efficiency, automation, and effective Linux shell programming.

Visit the following resources to learn more:

- [@article@Using For, While and Until Loops in Bash](https://linuxhandbook.com/bash-loops/)
- [@article@Bash Loops with examples](https://linuxconfig.org/bash-loops-with-examples)

## Lvm

# LVM (Logical Volume Manager)

LVM provides logical volume management through device mapper framework, offering flexible disk management with resizing, mirroring, and moving capabilities. Three levels: Physical Volumes (PVs - actual disks), Volume Groups (VGs - storage pools), and Logical Volumes (LVs - carved portions). Create with `pvcreate`, `vgcreate`, and `lvcreate` commands. Essential for enterprise storage systems.

Visit the following resources to learn more:

- [@article@The Complete Beginner's Guide to LVM in Linux](https://linuxhandbook.com/lvm-guide/)
- [@article@A Beginner's Guide to LVM in Linux - It's FOSS](https://itsfoss.com/lvm-guide/)

## Managing Permissions

# Permissions

Linux permissions control file and directory access for users, groups, and others with read, write, and execute types. Commands include `chmod` (change permissions), `chown` (change owner), and `chgrp` (change group). Proper permission management is crucial for system security and organization. Essential for maintaining controlled access to system resources.

Visit the following resources to learn more:

- [@article@Understanding Linux File Permissions](https://linuxize.com/post/understanding-linux-file-permissions/)
- [@article@Linux File Permissions](https://linuxhandbook.com/linux-file-permissions/)
- [@article@Linux Permissions of Files](https://labex.io/tutorials/linux-permissions-of-files-270252)
- [@video@Linux File Permissions in 5 Minutes](https://www.youtube.com/watch?v=LnKoncbQBsM)

## Mounts

# Mounts

Mounting in Linux attaches filesystems to specific directories (mount points) in the directory tree, allowing the OS to access data on storage devices. The `mount` command performs this operation. Example: `mount /dev/sdb1 /mnt` mounts second partition to `/mnt` directory. The `/mnt` directory is conventionally used for temporary mounting operations. Essential for Linux disk and filesystem management.

Visit the following resources to learn more:

- [@official@The mount command manual page](https://man7.org/linux/man-pages/man8/mount.8.html)
- [@article@Mounting, unmounting and the /mnt directory - The Linux Documentation Project](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/mnt.html)
- [@article@Linux mount command with Examples](https://phoenixnap.com/kb/linux-mount-command)

## Moving Files  Directories

# Moving Files

In Linux, moving files is an essential task that you will need to perform quite frequently. The `mv` command, short for move, is used to move files and directories from one location to another. The `mv` command can also be used for renaming files in Linux.

Visit the following resources to learn more:

- [@article@mv command](https://linuxhandbook.com/mv-command/)
- [@article@mv Cheat Sheet](https://www.commandinline.com/cheat-sheet/mv/)
- [@article@Linux mv Command: File Moving and Renaming](https://labex.io/tutorials/linux-linux-mv-command-file-moving-and-renaming-209743)

## Nano

# Nano: A File Editing Tool

Nano is a popular, user-friendly text editor used for creating and editing files directly within the Linux command line interface (CLI). It is an alternative to editors like `Vi` and `Emacs` and is considered more straightforward for beginners due to its simple and intuitive interface.

Visit the following resources to learn more:

- [@official@nano - Text editor](https://www.nano-editor.org/)
- [@article@Editing Files With Nano in Linux](https://itsfoss.com/nano-editor-guide/)
- [@article@Nano in Linux](https://ioflood.com/blog/nano-linux-command/)
- [@video@Nano editor fundamentals](https://www.youtube.com/watch?v=gyKiDczLIZ4&ab_channel=HackerSploit)

## Navigation Basics

# Navigation Basics

In Linux, navigation between directories and files is a fundamental, yet essential function that allows you to exploit the power of the command-line interface (CLI). Mastering the basic Linux navigation commands such as `cd`, `pwd`, `ls`, and `tree` enables you to flawlessly move from one point to another within the filesystem, display the list of files & directories, and understand your position relative to other system components.

Visit the following resources to learn more:

- [@course@Linux for Noobs (Hands-on)](https://labex.io/courses/linux-for-noobs)
- [@article@Linux Filesystem Navigation Basics](https://linuxconfig.org/filesystem-basics)
- [@article@Basic Navigation Commands: cd, ls, and pwd](https://www.linuxbash.sh/post/basic-navigation-commands-cd-ls-and-pwd)
- [@article@Practice on Linux Fundamentals](https://linuxjourney.com/)
- [@video@Linux fundamentals](https://www.youtube.com/watch?v=kPylihJRG70&t=1381s&ab_channel=TryHackMe)

## Netfilter

# Netfilter

Netfilter is a Linux kernel framework for manipulating and filtering network packets with hooks at various stages (pre-routing, input, forward, output, post-routing). Used for firewalls and NAT management with iptables configuration. Essential for traffic control, packet modification, logging, and intrusion detection in Linux networking systems.

Visit the following resources to learn more:

- [@official@netfilter/iptables project homepage](https://netfilter.org/)
- [@article@Packet filtering in Linux - iptables, nftables and firewalld](https://wyssmann.com/blog/2021/07/packet-filtering-in-linux-iptables-nftables-and-firewalld/)

## Netstat

# Netstat

Netstat is a command-line tool for network troubleshooting and performance measurement in Linux. It provides network statistics, open ports, routing table information, and protocol details. Use options like `-n` for numerical addresses, `-c` for continuous monitoring, and `-t`/`-u` for specific protocols. Example: `netstat -n` lists all connections with numerical values.

Visit the following resources to learn more:

- [@article@Netstat Command in Linux](https://linuxhandbook.com/netstat-command/)
- [@article@How to Use netstat on Linux](https://www.howtogeek.com/513003/how-to-use-netstat-on-linux/)

## Networking

# Networking

Linux networking enables system connections and resource sharing across platforms with robust management tools. Network configurations stored in `/etc/network/interfaces`. Key commands include `ifconfig` (deprecated) and `ip` for interface management. Supports various protocols with excellent scalability. Essential for system connectivity and network troubleshooting. Linux adopts a file-based approach for network configuration, storing network-related settings and configurations in standard files, such as `/etc/network/interfaces` or `/etc/sysconfig/network-scripts/`, depending on the Linux distribution.

Visit the following resources to learn more:

- [@article@A Comprehensive Guide to Linux Networking](https://centlinux.com/linux-networking/)
- [@article@A Beginner's Guide to Linux Networking Fundamentals](https://dev.to/iaadidev/a-beginners-guide-to-linux-networking-fundamentals-dev-ops-prerequisite-7-434o)
- [@article@Practice on Networking Fundamentals](https://linuxjourney.com/lesson/network-basics)

## Nl

# NL (Number Lines)

The `nl` command numbers lines in text files, providing an overview of line locations. By default, it numbers only non-empty lines, but this behavior can be modified. Syntax: `nl [options] [file_name]`. If no file is specified, nl reads from stdin. Valuable for text processing when line numbers are needed for reference or debugging purposes.

Visit the following resources to learn more:

- [@article@nl command](https://www.computerhope.com/unix/nl.htm)
- [@article@Linux nl Command: Line Numbering](https://labex.io/tutorials/linux-linux-nl-command-line-numbering-210988)
- [@article@Master the Linux 'nl' Command: A Comprehensive Guide](https://hopeness.medium.com/master-the-linux-nl-command-a-comprehensive-guide-79c6adf50fa9)

## Package Management

# Package Management

Package management handles software installation, updates, configuration, and removal in Linux. It manages collections of files and tracks software prerequisites automatically. Common package managers include `apt` (Debian-based), `yum`/`dnf` (Red Hat-based), and `pacman` (Arch). Example: `sudo apt install <package-name>` installs packages. Essential for efficient application management.

Visit the following resources to learn more:

- [@official@APT Package Manager](https://www.debian.org/doc/manuals/apt-guide/index.en.html)
- [@official@Yum Package Manager](http://yum.baseurl.org/)
- [@official@Using the DNF Software Package Manager](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)
- [@article@Linux Package Manager Explained](https://geekflare.com/dev/linux-package-manager-explained/)
- [@article@8 Best Package Manager for Linux](https://linuxsimply.com/linux-basics/package-management/best-package-manager/)
- [@article@Software Installation on Linux](https://labex.io/tutorials/linux-software-installation-on-linux-18005)

## Package Repositories

# Repositories

Repositories are storage locations containing collections of software packages for Linux distributions. They store thousands of compiled packages specific to each distribution (.deb for Debian/Ubuntu, .rpm for Fedora/CentOS). Repositories ensure secure, tested software with proper dependencies. Update commands: `sudo apt update` (Ubuntu), `sudo yum update` (CentOS/Fedora). Essential for secure software management.

Visit the following resources to learn more:

- [@official@APT Package Manager](https://www.debian.org/doc/manuals/apt-guide/index.en.html)
- [@article@What is Repository in Linux?](https://linuxsimply.com/what-is-repository-in-linux/)
- [@article@Official Repositories - ArchWiki](https://wiki.archlinux.org/title/Official_repositories)
- [@article@Understanding Linux Repositories](https://blogs.maalavs.com/linux/understanding-linux-repositories/)

## Packet Analysis

# Packet Analysis

Packet analysis is a key Linux network troubleshooting skill involving capturing and analyzing network traffic to identify performance issues, connectivity problems, and security vulnerabilities. Tools like tcpdump and Wireshark provide packet-level details for network diagnostics. Use `sudo tcpdump -i eth0` to capture packets on the eth0 interface for debugging network protocols.

Visit the following resources to learn more:

- [@article@How to Capture and Analyze Packets with tcpdump](https://www.debian.org/doc/manuals/apt-guide/index.en.html)
- [@article@Mastering Network Traffic Analysis in Linux](https://en.ittrip.xyz/linux/linux-network-analysis)
- [@article@16 Best Free and Open Source Network Analyzers](https://www.linuxlinks.com/best-free-open-source-network-analyzers/)

## Paste

# Paste

In Linux, paste is a powerful text processing utility that is primarily used for merging lines from multiple files. It allows users to combine data by columns rather than rows, adding immense flexibility to textual data manipulation. Users can choose a specific delimiter for separating columns, providing a range of ways to format the output. You may use `paste` command like `$ paste file1.txt file2.txt > combined.txt`.

Visit the following resources to learn more:

- [@article@Paste Command in Linux (Merge Lines)](https://linuxize.com/post/paste-command-in-linux/)
- [@article@7 Practical Usage of Paste Command in Linux](https://linuxhandbook.com/paste-command/)

## Ping

# Ping

The `ping` command is essential for Linux network troubleshooting, checking connectivity between your host and target machines. It sends ICMP ECHO\_REQUEST packets and listens for ECHO\_RESPONSE returns, providing insights into connection health and speed. Use `ping <target IP or hostname>` to diagnose network connectivity issues and identify reachability problems efficiently.

Visit the following resources to learn more:

- [@article@Ping Command in Linux](https://linuxize.com/post/linux-ping-command/)
- [@article@Ping Command Examples in Linux - It's FOSS](https://itsfoss.com/ping-command/)

## Pipe

# Pipe Commands

The pipe (`|`) is a powerful feature in Linux used to connect two or more commands together. This mechanism allows output of one command to be "piped" as input to another. With regards to text processing, using pipe is especially helpful since it allows you to manipulate, analyze, and transform text data without the need to create intermediary files or programs.

Here is a simple example of piping two commands, `ls` and `grep`, to list all the text files in the current directory:

    ls | grep '\.txt$'
    

In this example, `ls` lists the files in the current directory and `grep '\.txt$'` filters out any files that don't end with `.txt`. The pipe command, `|`, takes the output from `ls` and uses it as the input to `grep '\.txt$'`. The output of the entire command is the list of text files in the current directory.

Visit the following resources to learn more:

- [@article@An In-Depth Guide to Pipes in Linux - TheLinuxCode](https://thelinuxcode.com/linux-pipe-command-examples/)
- [@article@Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php#piping)
- [@article@What is Piping in Linux?](https://linuxsimply.com/what-is-piping-in-linux/)

## Process Forking

# Process Forking

Process forking uses the `fork()` system call to create child processes from parent processes, enabling concurrent execution. Child processes are nearly perfect copies of parents with different PIDs. Changes in child processes don't affect parents. Essential for understanding Linux process creation and control in multi-processing environments.

Visit the following resources to learn more:

- [@article@fork — Linux manual page](https://www.man7.org/linux/man-pages/man2/fork.2.html)
- [@article@Understanding the fork() System Call in Linux](https://thelinuxcode.com/fork-system-call-linux/)
- [@article@Linux Process calls: Creating process using fork](https://medium.com/@joshuaudayagiri/linux-process-calls-creating-process-using-fork-52a1eac7de8b)

## Process Management

# Process Management

Linux treats every running program as a process. Process management commands help view, control, and manipulate these processes. Key commands: `ps aux` shows running processes, `top` provides live system view, `kill -SIGTERM pid` gracefully stops processes, `kill -SIGKILL pid` forcefully terminates processes. Essential for understanding and controlling Linux system operations effectively.

Visit the following resources to learn more:

- [@article@The Complete Guide to Process Management Commands](https://thelinuxcode.com/process-management-commands-linux/)
- [@article@Commands for Process Management in Linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)

## Process Priorities

# Process Priorities

Linux assigns priority levels to processes for efficient resource utilization and execution timing. Priority values ("nice" values) range from -20 (highest) to +19 (lowest priority). View priorities with `ps -eo pid,pri,user,comm`. Change priorities using `renice -5 -p [PID]`. Essential for system performance optimization and CPU resource management.

Visit the following resources to learn more:

- [@article@Understanding Process Thread Priorities in Linux](https://blogs.oracle.com/linux/post/task-priority)
- [@article@How To Manipulate Process Priority In Linux](https://www.itsmarttricks.com/how-to-manipulate-process-priority-in-linux-using-nice-and-renice-commands/)

## Process Signals

# Process Signals

Process signals are communication mechanisms in Linux that notify processes of synchronous or asynchronous events. Common signals include SIGINT, SIGSTOP, SIGKILL for interrupting, pausing, or terminating processes. Example: `kill -SIGSTOP 12345` suspends process with PID 12345 until `SIGCONT` is received. Essential for comprehensive process management and resource allocation.

Visit the following resources to learn more:

- [@article@Understanding Linux Process Signals](https://www.ceos3c.com/linux/understanding-linux-process-signals-a-complete/)
- [@article@Linux Process Signals and their meaning](https://linux-audit.com/processes/linux-process-signals/)

## Redirects

# Redirects

The shell in Linux provides a robust way of managing input and output streams of a command or program, this mechanism is known as Redirection. Linux being a multi-user and multi-tasking operating system, every process typically has 3 streams opened:

*   Standard Input (stdin) - This is where the process reads its input from. The default is the keyboard.
*   Standard Output (stdout) - The process writes its output to stdout. By default, this means the terminal.
*   Standard Error (stderr) - The process writes error messages to stderr. This also goes to the terminal by default.

Visit the following resources to learn more:

- [@article@Input Output & Error Redirection in Linux](https://linuxhandbook.com/redirection-linux/)
- [@article@Redirections (Bash Reference Manual)](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- [@article@Redirections in Linux with Examples](https://linuxopsys.com/redirections-in-linux-with-examples)

## Server Review

# Server Review

Server review in Linux involves assessing performance, security, and configuration to identify improvements and issues. Check security enhancements, log files, user accounts, network configuration, and software versions. Common commands: `free -m` for memory, `df -h` for disk usage, `uptime` for CPU load. Critical task for system administrators and DevOps professionals to ensure optimal performance, security, and reliability.

Visit the following resources to learn more:

- [@article@Linux Server Management Essentials](https://www.ictbroadcast.com/linux-server-management-essentials-administration-monitoring-and-maintenance-guidelines-for-success/)
- [@article@Essential Linux Server Maintenance Checklist](https://tecadmin.net/linux-server-maintenance-checklist/)
- [@article@Optimizing Linux Server Performance](https://www.linuxjournal.com/content/optimizing-linux-server-performance-benchmarking-and-advanced-techniques)

## Service Management Systemd

# Service Management

Service management controls Linux services (daemons) during boot and shutdown processes. Common systemctl commands include start, stop, restart, reload, status, enable/disable. Modern Linux uses systemd while older systems use SystemV or Upstart. Example: `sudo systemctl start sshd` starts SSH service. Essential skill for Linux system administration and maintaining secure, stable systems.

Visit the following resources to learn more:

- [@article@How to Master Linux Service Management with Systemctl](https://labex.io/tutorials/linux-how-to-master-linux-service-management-with-systemctl-392864)
- [@article@Service Management in Linux: A Comprehensive Guide](https://medium.com/@thesureshvadde/service-management-in-linux-a-comprehensive-guide-cb4c7e81dfa9)
- [@article@How to Manage Services in Linux: systemd and SysVinit](https://dev.to/iaadidev/how-to-manage-services-in-linux-systemd-and-sysvinit-essentials-devops-prerequisite-8-1jop)

## Services Running

# Running Services

Linux servers run various services including web, database, DNS, and mail servers. System administrators use tools like `systemctl`, `service`, `netstat`, `ss`, and `lsof` to manage and monitor services. Use `systemctl --type=service` to list all active services with their status. Essential for server management, resource monitoring, and troubleshooting.

Visit the following resources to learn more:

- [@article@How to List Linux Services With systemctl](https://www.howtogeek.com/839285/how-to-list-linux-services-with-systemctl/)
- [@article@Service Management in Linux: A Comprehensive Guide](https://medium.com/@thesureshvadde/service-management-in-linux-a-comprehensive-guide-cb4c7e81dfa9)
- [@article@How to Manage Services in Linux: systemd and SysVinit](https://dev.to/iaadidev/how-to-manage-services-in-linux-systemd-and-sysvinit-essentials-devops-prerequisite-8-1jop)

## Shell And Other Basics

# Shell Basics

The Linux shell is a command-line interface that acts as an intermediary between users and the system kernel. Common shells include Bash, sh, and csh. Basic operations involve navigating directories, creating/deleting files, and executing commands. Shell knowledge is fundamental for Linux administration, scripting, and automation tasks.

Visit the following resources to learn more:

- [@article@Learning The Shell](https://www.linuxcommand.org/lc3_lts0010.php)
- [@article@What is a Shell in Linux](https://linuxsimply.com/what-is-a-shell-linux/)
- [@article@Learn Linux Easily](https://linuxjourney.com)

## Shell Programming

# Shell Programming

Shell programming (scripting) automates administrative tasks, repetitive operations, and system monitoring in Linux. Bash is the default shell and scripting language in most distributions. Scripts are text files executed by the shell, excellent for system automation. Example: `#!/bin/bash echo "Hello, World!"` creates a simple script that prints output to terminal.

Visit the following resources to learn more:

- [@article@Learn Shell - Free Interactive Shell Tutorial](https://www.learnshell.org/)
- [@article@Bash Scripting Tutorial Series for Beginners](https://linuxhandbook.com/bash/)
- [@article@Linux Bash Shell Scripting Tutorial Wiki](https://bash.cyberciti.biz/guide/Main_Page)
- [@video@Bash Scripting on Linux - YT Playlist](https://youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&si=MSehStqnhSqgoMSj)

## Snap

# Snap

Snap is a modern Linux package management system by Canonical providing self-contained packages with all dependencies included. Snaps run consistently across different Linux distributions, install from Snapcraft store, and update automatically. Updates are transactional with automatic rollback on failure. Install packages using `sudo snap install [package-name]` command.

Visit the following resources to learn more:

- [@article@The "snap" Command in Linux](https://linuxsimply.com/snap-command-in-linux/)
- [@article@How to Install and Use Snap in Various Linux Distributions](https://itsfoss.com/install-snap-linux/)

## Soft Links  Hard Links

# Soft and Hard Links

Linux supports two types of file links. Hard links share the same inode and data as the original file - if the original is deleted, data remains accessible. Soft links (symbolic links) are shortcuts pointing to the original file path - they break if the original is removed. Create with `ln` for hard links and `ln -s` for soft links.

Visit the following resources to learn more:

- [@article@Hard links and Soft links in Linux Explained](https://www.redhat.com/en/blog/linking-linux-explained)
- [@article@Difference between hard link and soft link](https://kerneltalks.com/commands/difference-between-hard-link-and-soft-link/)
- [@article@How to Understand the Difference between Hard and Symbolic Links in Linux](https://labex.io/tutorials/linux-how-to-understand-the-difference-between-hard-and-symbolic-links-in-linux-409929)

## Sort

# Sort

Linux provides a variety of tools for processing and manipulating text files, one of which is the sort command. The `sort` command in Linux is used to sort the contents of a text file, line by line. The command uses ASCII values to sort files. You can use this command to sort the data in a file in a number of different ways such as alphabetically, numerically, reverse order, or even monthly. The sort command takes a file as input and prints the sorted content on the standard output (screen).

Visit the following resources to learn more:

- [@article@Sort Command in Linux - 10 Useful Examples](https://linuxhandbook.com/sort-command/)
- [@article@Sort Command in Linux with Practical Examples](https://tecadmin.net/linux-sort-command/)
- [@article@Linux sort Command: Text Sorting](https://labex.io/tutorials/linux-linux-sort-command-text-sorting-219196)

## Split

# Split Command

Linux provides an extensive set of tools for manipulating text data. One of such utilities is the `split` command that is used, as the name suggests, to split large files into smaller files. The `split` command in Linux divides a file into multiple equal parts, based on the lines or bytes specified by the user.

Visit the following resources to learn more:

- [@article@Split Command in Linux: 9 Useful Examples](https://linuxhandbook.com/split-command/)
- [@article@Split Command in Linux: Usage Guide with Examples](https://ioflood.com/blog/split-linux-command/)

## Ssh

# SSH

SSH (Secure Shell) is a cryptographic network protocol providing secure remote access, command execution, and data communication between networked computers. Replaces insecure protocols like Telnet with confidentiality, integrity, and security. Use `ssh username@server_ip_address` to connect to remote Linux servers. Essential for secure system administration and remote management.

Visit the following resources to learn more:

- [@article@Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)
- [@article@Mastering SSH - A Complete Guide to Secure Shell Protocol](https://www.socketxp.com/iot/ssh-secure-shell/)
- [@article@What is SSH? | Secure Shell (SSH) Protocol - Cloudflare](https://www.cloudflare.com/learning/access-management/what-is-ssh/)

## Starting  Stopping Services

# Starting / Stopping Services

Linux service management controls system services like firewall, network, and database using `systemctl` commands. Basic operations: `sudo systemctl start service_name` (start), `sudo systemctl stop service_name` (stop), `sudo systemctl restart service_name` (restart). Root permissions required. Essential for system administrators managing updates and configuration changes.

Visit the following resources to learn more:

- [@article@Service Management in Linux: A Comprehensive Guide](https://medium.com/@thesureshvadde/service-management-in-linux-a-comprehensive-guide-cb4c7e81dfa9)
- [@article@How to Master Linux Service Management with Systemctl](https://labex.io/tutorials/linux-how-to-master-linux-service-management-with-systemctl-392864)
- [@article@How to Manage Services in Linux: systemd and SysVinit](https://dev.to/iaadidev/how-to-manage-services-in-linux-systemd-and-sysvinit-essentials-devops-prerequisite-8-1jop)

## Stdout  Stdin  Stderr

# Stdout, Stdin, and Stderr

Linux processes use three standard data streams: STDIN (input), STDOUT (output), and STDERR (error messages). STDOUT handles normal command output while STDERR specifically handles error messages. You can redirect these streams using operators like `>` for stdout and `2>` for stderr, allowing separate handling of normal output and errors for better scripting and debugging.

Visit the following resources to learn more:

- [@article@Linux Fundamentals - I/O, Standard Streams, and Redirection](https://www.putorius.net/linux-io-file-descriptors-and-redirection.html)
- [@article@Understanding 'stdin', 'stdout' and 'stderr' in Linux](https://www.slingacademy.com/article/understanding-stdin-stdout-and-stderr-in-linux/)
- [@article@Working with data streams on the Linux command line](https://opensource.com/article/18/10/linux-data-streams)

## Subnetting

# Subnetting

Subnetting divides networks into smaller subnets to improve performance and security in Linux networking. It organizes IP addresses within IP addressing schemes, preventing conflicts and efficiently utilizing address ranges. Use `route -n` to view routing tables and `route add -net xxx.xxx.xxx.x/xx gw yyy.yyy.yyy.y` to add subnets. Essential for complex networking environments.

Visit the following resources to learn more:

- [@article@Understanding IP Addressing and Subnetting in Linux](https://useful.codes/understanding-ip-addressing-and-subnetting-in-linux/)
- [@article@The Basics of IP Subnetting | Linux Journal](https://www.linuxjournal.com/article/6287)
- [@article@How to Find Subnet Mask in Linux](https://www.howtouselinux.com/post/find-subnet-mask-on-linux)

## Super User

# Super User

The Super User, also known as "root user", represents a user account in Linux with extensive powers, privileges, and capabilities. This user has complete control over the system and can access any data stored on it. This includes the ability to modify system configurations, change other user's passwords, install software, and perform more administrative tasks in the shell environment.

The usage of super user is critical to operating a Linux system properly and safely as it can potentially cause serious damage. The super user can be accessed through the `sudo` or `su` commands.

Visit the following resources to learn more:

- [@article@Linux Superuser Access, Explained](https://www.redhat.com/en/blog/linux-superuser-access/)
- [@article@Difference between the root user and super (sudo) user](https://www.computernetworkingnotes.com/linux-tutorials/difference-between-the-root-user-and-super-sudo-user.html)
- [@article@What is Superuser Access in Linux?](https://www.scaler.com/topics/super-user-in-linux/)

## Swap

# Swap Space

Swap space extends physical memory by using disk storage when RAM is full. Inactive memory pages move to swap, freeing RAM but with performance impact due to slower disk access. Swap can exist as dedicated partitions or regular files. Create with `fallocate`, `mkswap`, and `swapon` commands. Critical for memory management and system stability optimization.

Visit the following resources to learn more:

- [@article@Swap - Arch Wiki](https://wiki.archlinux.org/title/Swap)
- [@article@How to Increase Swap Space on Linux](https://linuxconfig.org/how-to-increase-swap-space-on-linux)

## Tail

# Tail Command

The `tail` command in Linux is a utility used in text processing. Fundamentally, it's used to output the last part of the files. The command reads data from standard input or from a file and outputs the last `N` bytes, lines, blocks, characters or words to the standard output (or a different file). By default, `tail` returns the last 10 lines of each file to the standard output. This command is common in situations where the user is interested in the most recent entries in a text file, such as log files.

Visit the following resources to learn more:

- [@article@5 Practical Examples of Tail Command in Linux](https://linuxhandbook.com/tail-command/)
- [@article@Linux Tail Command | Linuxize](https://linuxize.com/post/linux-tail-command/)
- [@article@Linux tail Command: File End Display](https://labex.io/tutorials/linux-linux-tail-command-file-end-display-214303)

## Tcpip Stack

# TCP/IP

TCP/IP (Transmission Control Protocol/Internet Protocol) forms the backbone of internet communication, allowing computers to connect and transfer data. It comprises four layers: Network Interface, Internet, Transport, and Application. Essential for Linux networking, enabling hosts to interact across networks. Use `netstat -at` to view active TCP/IP connections. Crucial for network management and troubleshooting.

Visit the following resources to learn more:

- [@article@TCP/IP Commands for Linux](https://whatismyipaddress.com/tcp-ip-commands-linux)
- [@article@Netstat Command in Linux](https://phoenixnap.com/kb/netstat-command)
- [@article@Netstat Command in Linux: 13 Practical Examples](https://linuxhandbook.com/netstat-command/)

## Tee

# Tee

The `tee` command reads from standard input and writes to both standard output and files simultaneously, like a T-splitter in plumbing. It enables users to view results in the terminal while saving output to files concurrently. Syntax: `command | tee file`. Extremely useful for documenting terminal activities and preserving command outputs for later analysis.

Visit the following resources to learn more:

- [@article@Tee Command in Linux Explained with Examples](https://linuxhandbook.com/tee-command/)
- [@article@Linux Tee Command](https://linuxize.com/post/linux-tee-command/)

## Text Processing

# Text Processing

Linux offers robust text processing capabilities essential for system administrators and developers. Users can leverage command-line tools like `awk`, `sed`, `grep`, and `cut` for tasks such as filtering, substitution, and regular expression handling. Scripting languages like Python and Perl further enhance text processing. While primarily command-line based, Linux also provides GUI text editors such as `gedit`, `nano`, and `vim`. Proficiency in these tools is vital for automating tasks, parsing files, and efficient data mining.

Visit the following resources to learn more:

- [@article@Common Linux Text Processing Commands](https://www.commandinline.com/linux/common-linux-text-processing-commands/)
- [@article@Linux Filters](https://ryanstutorials.net/linuxtutorial/filters.php)
- [@article@Linux Text Processing Command](https://earthly.dev/blog/linux-text-processing-commands/)
- [@article@Master Linux Text Processing Commands](https://everythingdevops.dev/linux-text-processing-commands/)

## Tr

# Tr-Command

The `tr` command in Linux is a command-line utility that translates or substitutes characters. It reads from the standard input and writes to the standard output. Although commonly used for translation applications, `tr` has versatile functionality in the text processing aspect of Linux. Ranging from replacing a list of characters, to deleting or squeezing character repetitions, `tr` presents a robust tool for stream-based text manipulations.

Visit the following resources to learn more:

- [@article@tr Command in Linux: 6 Useful Examples](https://linuxhandbook.com/tr-command/)
- [@article@Linux tr Command with Practical Examples](https://labex.io/tutorials/linux-linux-tr-command-with-practical-examples-422963)

## Traceroute

# Traceroute

Traceroute is a Linux network diagnostic tool that displays the path packets take from your system to a destination. It identifies routing problems, measures latency, and reveals network structure as packets traverse the internet. Each hop is tested multiple times with round-trip times displayed. Use `traceroute www.example.com` to discover packet routes and diagnose failures.

Visit the following resources to learn more:

- [@article@traceroute Command Examples in Linux](https://linuxhandbook.com/traceroute/)
- [@article@How to Use the traceroute Command on Linux](https://www.howtogeek.com/657780/how-to-use-the-traceroute-command-on-linux/)

## Troubleshooting

# Troubleshooting

Linux troubleshooting involves identifying and resolving system errors, hardware/software issues, network problems, and resource management challenges. Key skills include using command-line tools, inspecting log files, understanding processes, and interpreting error messages. Tools like `top` provide real-time process monitoring to identify resource-heavy processes causing performance issues efficiently.

Visit the following resources to learn more:

- [@article@Troubleshooting Linux Problems: A Beginner's Guide](https://learn.redhat.com/t5/Platform-Linux/Troubleshooting-Linux-Problems-A-Beginner-s-Guide/td-p/36236)
- [@article@Linux Top 20 Important Commands for Monitoring and Troubleshooting](https://medium.com/@stepstodevops/linux-top-20-important-commands-for-monitoring-and-troubleshooting-a-comprehensive-guide-for-cd5aaa37da17)
- [@article@10 Linux Troubleshooting Tips - dummies](https://www.dummies.com/article/technology/computers/operating-systems/linux/10-linux-troubleshooting-tips-274301/)

## Ulimits

# Ulimits

Ulimits (user limits) are Linux kernel features that restrict resources like file handles and memory that processes can consume. In containerization, ulimits prevent rogue processes from exhausting server resources and creating denial-of-service situations. Use `ulimit -a` to view current limits and `ulimit -n 1024` to set specific limits for optimal container performance and security.

Visit the following resources to learn more:

- [@article@Check and set user limits with ulimit Linux command](https://linuxconfig.org/limit-user-environment-with-ulimit-linux-command)
- [@article@How to Use Ulimit Command in Linux](https://linuxhandbook.com/ulimit-command/)
- [@article@10 Linux Troubleshooting Tips](https://www.dummies.com/article/technology/computers/operating-systems/linux/10-linux-troubleshooting-tips-274301/)

## Unexpand

# Unexpand

The `unexpand` command converts spaces to tabs in text files, making documents more coherent and neat. Commonly used in programming scripts where tab indentation is preferred. Use `unexpand -t 4 file.txt` to replace every four spaces with a tab. Opposite of `expand` command, useful for standardizing indentation formatting in code files.

Visit the following resources to learn more:

- [@article@unexpand Cheat Sheet](https://www.commandinline.com/cheat-sheet/unexpand/)
- [@article@Master the Linux 'unexpand' Command: A Comprehensive Guide](https://hopeness.medium.com/master-the-linux-unexpand-command-a-comprehensive-guide-6966c1f90acb)
- [@article@Linux unexpand Command with Practical Examples](https://labex.io/tutorials/linux-linux-unexpand-command-with-practical-examples-422975)

## Uniq

# Uniq

`uniq` is an extremely useful command-line program for text processing. It aids in the examination and manipulation of text files by comparing or filtering out repeated lines that are adjacent. Whether you're dealing with a list of data or a large text document, the `uniq` command allows you to find and filter out duplicate lines, or even provide a count of each unique line in a file. It's important to remember that `uniq` only removes duplicates that are next to each other, so to get the most out of this command, data is often sorted using the `sort` command first.

Visit the following resources to learn more:

- [@article@Uniq Command in Unix and Linux: 7 Essential Examples](https://linuxhandbook.com/uniq-command/)
- [@article@Linux uniq Command: Duplicate Filtering](https://labex.io/tutorials/linux-linux-uniq-command-duplicate-filtering-219199)
- [@article@How to Use the Uniq Command to Process Lists in Linux](https://www.redhat.com/en/blog/uniq-command-lists)

## Uptime And Load

# Uptime and Load

The `uptime` command shows system running time and load averages for 1, 5, and 15-minute intervals. Load average indicates computational work and processes waiting for CPU time. High load suggests insufficient resources or misconfigurations. Example: `uptime` shows "2 days, 20 min" uptime and "0.00, 0.01, 0.05" load averages. Essential for performance monitoring and capacity planning.

Visit the following resources to learn more:

- [@article@Linux Uptime Command With Usage Examples](https://www.tecmint.com/linux-uptime-command-examples/)
- [@article@How to Check Uptime in Linux Command Line](https://linuxhandbook.com/uptime-command/)
- [@article@Linux Load Average: What is Load Average in Linux?](https://www.digitalocean.com/community/tutorials/load-average-in-linux)

## User Management

# User Management

Linux user management allows multiple users to interact with the system in isolation. Includes creating, deleting, modifying users and groups, assigning permissions and ownership. Key commands: `adduser`/`useradd` creates users, `deluser`/`userdel` removes users, `passwd` manages passwords, `su` switches users. Essential for providing proper accessibility and maintaining Linux system security.

Visit the following resources to learn more:

- [@article@User Account Management](https://labex.io/tutorials/linux-user-account-management-49)
- [@article@Creating, Modifying, and Deleting User Accounts](https://serveracademy.com/courses/linux-server-administration/creating-modifying-and-deleting-user-accounts/)
- [@article@User Management in Linux: A Beginner's Guide](https://dev.to/austinozor/user-management-in-linux-a-beginners-guide-to-creating-modifying-and-deleting-users-fhf)

## Users And Groups

# Users and Groups

Linux user groups simplify system administration by managing collections of users with shared access rights to files and directories. Each user belongs to one or more groups, enabling privilege management without full superuser access. Management commands: `groupadd`, `groupdel`, `groupmod`, `usermod`, `gpasswd`. Essential for secure and organized system environments.

Visit the following resources to learn more:

- [@article@How to create, delete, and modify groups in Linux](https://www.redhat.com/sysadmin/linux-groups)
- [@article@How to manage groups on Linux](https://linuxconfig.org/how-to-manage-groups-on-linux)
- [@article@Creating, Modifying, and Deleting User Accounts](https://serveracademy.com/courses/linux-server-administration/creating-modifying-and-deleting-user-accounts/)
- [@article@User Management in Linux: A Beginner's Guide](https://dev.to/austinozor/user-management-in-linux-a-beginners-guide-to-creating-modifying-and-deleting-users-fhf)

## Variables

# Variables

Shell variables store system or user-defined data that can change during script execution. Two categories exist: System Variables (PATH, HOME, PWD) created by Linux, and User-Defined Variables created by users. Define variables with `=` operator and retrieve values with `$` prefix. Example: `MY_VARIABLE="Hello World"` then `echo $MY_VARIABLE` prints the value.

Visit the following resources to learn more:

- [@article@Learning The Shell](https://www.linuxcommand.org/lc3_lts0010.php)
- [@article@How to Use Variables in Bash Shell Scripts](https://linuxhandbook.com/bash-variables/)
- [@article@How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux)

## Vim

# Vim: An Essential Tool for Editing Files

Vim (Vi Improved) is a powerful and flexible text editor used in Unix-like systems. It builds on the original Vi editor with additional features and improvements, including multi-level undo, syntax highlighting, and an extensive set of commands for text manipulation.

Vim operates primarily in three modes:

*   Normal (for navigation and manipulation).
*   Insert (for editing text).
*   Command (for executing commands).

Visit the following resources to learn more:

- [@course@Learn Vimscript The Hard Way](https://learnvimscriptthehardway.stevelosh.com/)
- [@article@Vim Cheat Sheet](https://vim.rtorr.com/)
- [@article@Learn Vim Progressively](https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)
- [@article@Platform to practice Vim](https://vim-adventures.com/)
- [@video@Vim Basics](https://www.youtube.com/watch?v=wACD8WEnImo&list=PLT98CRl2KxKHy4A5N70jMRYAROzzC2a6x&ab_channel=LearnLinuxTV)

## Wc

# WC - Text Processing

The `wc` command is a commonly used tool in Unix or Linux that allows users to count the number of bytes, characters, words, and lines in a file or in data piped from standard input. The name `wc` stands for 'word count', but it can do much more than just count words. Common usage of `wc` includes tracking program output, counting code lines, and more. It's an invaluable tool for analyzing text at both granular and larger scales.

Visit the following resources to learn more:

- [@article@Wc Command in Linux (Count Number of Lines, Words, and Characters)](https://linuxize.com/post/linux-wc-command/)
- [@article@wc Command Examples - Linux Handbook](https://linuxhandbook.com/wc-command/)
- [@article@Linux wc Command: Text Counting](https://labex.io/tutorials/linux-linux-wc-command-text-counting-219200)

## Working With Files

# Working with Files

Working with files is an essential part of Linux and it's a skill every Linux user must have. In Linux, everything is considered a file: texts, images, systems, devices, and directories. Linux provides multiple command-line utilities to create, view, move or search files. Some of the basic commands for file handling in Linux terminal include `touch` for creating files, `mv` for moving files, `cp` for copying files, `rm` for removing files, and `ls` for listing files and directories.

Visit the following resources to learn more:

- [@article@Editing Files in Linux Command Line](https://itsfoss.com/edit-files-linux/)
- [@article@Mastering cp and mv Commands in Linux](https://dev.to/ldwit/mastering-cp-and-mv-commands-in-linux-plus-related-cmds-5cc9)
- [@article@Vim Tutorial for Beginners](https://linuxconfig.org/vim-tutorial)
- [@article@Linux Basic Files Operations](https://labex.io/tutorials/linux-basic-files-operations-270248)
- [@article@What is the Difference Between Cat and Touch Command](https://linuxways.net/centos/what-is-the-difference-between-cat-and-touch-command/)
