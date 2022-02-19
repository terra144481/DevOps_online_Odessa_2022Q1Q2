**task2.1**

> Most popular hypervisors for infrastructure virtualization:
- VMware vSphere Hypervisor (VMware vSphere Hypervisor is a free bare-metal hypervisor that virtualizes servers so you can consolidate your applications on less hardware. Use - big company, for administrator, region - North America, Free Trial Unavailable)
- Hyper-V (Microsoft Hyper-V Server 2012 is a stand-alone product providing a simplified, reliable, cost-effective and optimized virtualization solution. Free Trial Unavailable)
- Azure Virtual Machines (Gives you the flexibility of virtualization for a wide range of computing solutions: development and testing, running applications, and extending your datacenter with support for Linux, Windows Server, SQL Server, Oracle, IBM, and SAP. Use- big and mid company, for user, region - North America, Europe )
- WMware ESXi (VMware ESXi is a purpose-built bare-metal hypervisor that installs directly onto a physical server. With direct access to and control of underlying resources, ESXi is more efficient than hosted architectures and can effectively partition hardware to increase consolidation ratios and cut costs for our customers.)



**1. Run VirtualBox and Virtual Machine.**  
Download and install VirtualBox, Ubuntu

**2. Create VM1**  
```c:\Program Files\Oracle\VirtualBox>VBoxManage createvm --name vm1```
Virtual machine 'vm1' is created.  
UUID: c53479f8-ef4c-4725-8ded-aac067f3c3f0

**3. Clone an existing VM1 by creating a VM2.**  
```c:\Program Files\Oracle\VirtualBox>VBoxManage clonevm vm1```  
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%  
Machine has been successfully cloned as "vm1 Clone"

**4. Create a group of two VM: VM1, VM2.**  
![vms group.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/vms%20group.png)

**5. For VM1, changing its state, take several different snapshots**  
```c:\Program Files\Oracle\VirtualBox>VBoxManage snapshot vm1 take mysnappp```  
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Snapshot taken.   UUID: 48bf7677-b112-4dec-b16e-7a47daab3c79  
![state snapshot.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/state%20snapshot.png)

**6. Export, import VM1 to .ova file.**  
![ova file.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/ova%20file.png)

**7. Configuration of virtual machines**  
```C:\Program Files\Oracle>ssh lovkin@localhost -p 2222```  
The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.  
ECDSA key fingerprint is SHA256:CFcM3nmdWOdlsiLg6vHfRZOnqHVGagf6vUQfgC2XrHU.    
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes  
Warning: Permanently added '[localhost]:2222' (ECDSA) to the list of known hosts.  
lovkin@localhost's password:  
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-99-generic x86_64)  

**8. Shared folder to exchange data between the virtual machine**  
![share folder.jpg](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/share%20folder.jpg)  
![share.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/share.png)  

**9. Configure different network modes for VM1, VM2.**  
![nat.jpg](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/nat.jpg)  
![bridge.jpg](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/8d8f839376085f85613bf5514843d290bcd2fb87/m2/task2.1/images/bridge.jpg)  

**10. Work with CLI through VBoxManage**  
list  vms  
```c:\Program Files\Oracle\VirtualBox>VBoxManage list vms```  
"vm1" {2bb4dca8-154b-44f2-82dc-bc1ffacc8b4c}  
"vm2" {0bce1447-5f74-482c-b433-1f85a6ce78c5}  

```C:\Program Files\Oracle\VirtualBox>VBoxManage showvminfo vm1```  
Name:                        vm1  
Groups:                      /vm  
Guest OS:                    Ubuntu (64-bit)  
UUID:                        2bb4dca8-154b-44f2-82dc-bc1ffacc8b4c  

**11. Run the powershell. vagrant create vm**  
```PS C:\> mkdir test```  
```PS C:\> cd ./test/```  
```PS C:\test> vagrant init ubuntu/jammy64```  
```PS C:\test> vagrant up```  
```PS C:\test> vagrant ssh```  
Welcome to Ubuntu Jammy Jellyfish (development branch) (GNU/Linux 5.15.0-18-generic x86_64)Welcome to Ubuntu Jammy  
```vagrant@ubuntu-jammy:~ date```  
Thu Feb 10 09:07:33 UTC 2022  
```vagrant@ubuntu-jammy:~/.ssh$ exit```  
logout  
```PS C:\test> vagrant halt```  
```PS C:\test> vagrant destroy```

**12. Create a test environment from a few servers. Servers' parameters are chosen independently by the student.**  
link to vagrantfile  
```PS C:\test> vagrant up```  
Bringing machine 'vm1' up with 'virtualbox' provider...  
Bringing machine 'vm2' up with 'virtualbox' provider...  
==> vm1: Clearing any previously set forwarded ports...  
==> vm1: Clearing any previously set network interfaces...  
==> vm1: Preparing network interfaces based on configuration...  
    vm1: Adapter 1: nat  
    vm1: Adapter 2: bridged  
==> vm1: Forwarding ports...  
    vm1: 22 (guest) => 2222 (host) (adapter 1)  
==> vm1: Running 'pre-boot' VM customizations...  
==> vm1: Booting VM...  
==> vm1: Waiting for machine to boot. This may take a few minutes...  
    vm1: SSH address: 127.0.0.1:2222  
    vm1: SSH username: vagrant  
    vm1: SSH auth method: private key  
    vm1: Warning: Connection aborted. Retrying...  
    vm1: Warning: Connection reset. Retrying...  
==> vm1: Machine booted and ready!  
==> vm1: Checking for guest additions in VM...  
    vm1: The guest additions on this VM do not match the installed version of  
    vm1: VirtualBox! In most cases this is fine, but in rare cases it can  
    vm1: prevent things such as shared folders from working properly. If you see  
    vm1: shared folder errors, please make sure the guest additions within the  
    vm1: virtual machine match the version of VirtualBox you have installed on  
    vm1: your host and reload your VM.  
    vm1:  
    vm1: Guest Additions Version: 5.2.42  
    vm1: VirtualBox Version: 6.1  
==> vm1: Setting hostname...  
==> vm1: Configuring and enabling network interfaces...  
==> vm1: Mounting shared folders...  
    vm1: /vagrant => C:/test  
==> vm1: Machine already provisioned. Run `vagrant provision` or use the `--provision`  
==> vm1: flag to force provisioning. Provisioners marked to run always will still run.  
==> vm2: Clearing any previously set forwarded ports...  
==> vm2: Fixed port collision for 22 => 2222. Now on port 2200.  
==> vm2: Clearing any previously set network interfaces...  
==> vm2: Preparing network interfaces based on configuration...  
    vm2: Adapter 1: nat  
    vm2: Adapter 2: bridged  
==> vm2: Forwarding ports...  
    vm2: 22 (guest) => 2200 (host) (adapter 1)  
==> vm2: Running 'pre-boot' VM customizations...  
==> vm2: Booting VM...  
==> vm2: Waiting for machine to boot. This may take a few minutes...  
    vm2: SSH address: 127.0.0.1:2200  
    vm2: SSH username: vagrant  
    vm2: SSH auth method: private key  
    vm2: Warning: Connection aborted. Retrying...  
==> vm2: Machine booted and ready!  
==> vm2: Checking for guest additions in VM...  
    vm2: The guest additions on this VM do not match the installed version of  
    vm2: VirtualBox! In most cases this is fine, but in rare cases it can  
    vm2: prevent things such as shared folders from working properly. If you see
    vm2: shared folder errors, please make sure the guest additions within the  
    vm2: virtual machine match the version of VirtualBox you have installed on  
    vm2: your host and reload your VM.  
    vm2:  
    vm2: Guest Additions Version: 5.2.42  
    vm2: VirtualBox Version: 6.1  
==> vm2: Setting hostname...  
==> vm2: Configuring and enabling network interfaces...  
==> vm2: Mounting shared folders...  
    vm2: /vagrant => C:/test  

```PS C:\test> vagrand ssh vm1```   
vagrand ssh vm1  
    CategoryInfo          : ObjectNotFound: (vagrand:String) [], CommandNotFoundException  
    FullyQualifiedErrorId : CommandNotFoundException  

```PS C:\test> vagrant ssh vm1```  
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-167-generic x86_64)  
 * Documentation:  https://help.ubuntu.com  
 * Management:     https://landscape.canonical.com  
 * Support:        https://ubuntu.com/advantage  
  System information as of Thu Feb 10 11:51:57 UTC 2022  
  System load:  0.16              Processes:             99  
  Usage of /:   2.7% of 38.71GB   Users logged in:       0  
  Memory usage: 25%               IP address for enp0s3: 10.0.2.15  
  Swap usage:   0%                IP address for enp0s8: 192.168.1.160  

0 updates can be applied immediately.  

New release '20.04.3 LTS' available.  
Run 'do-release-upgrade' to upgrade to it.  


Last login: Thu Feb 10 11:47:20 2022 from 10.0.2.2  
```vagrant@vm1:~ ip a```  
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000  
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00  
    inet 127.0.0.1/8 scope host lo  
       valid_lft forever preferred_lft forever  
    inet6 ::1/128 scope host  
       valid_lft forever preferred_lft forever  
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel   state UP group default qlen 1000  
    link/ether 02:e8:64:37:14:18 brd ff:ff:ff:ff:ff:ff  
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3  
       valid_lft 86318sec preferred_lft 86318sec  
    inet6 fe80::e8:64ff:fe37:1418/64 scope link  
       valid_lft forever preferred_lft forever  
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel   state UP group default qlen 1000  
    link/ether 08:00:27:5c:b3:30 brd ff:ff:ff:ff:ff:ff  
    inet 192.168.1.160/24 brd 192.168.1.255 scope global enp0s8  
       valid_lft forever preferred_lft forever  
    inet6 fe80::a00:27ff:fe5c:b330/64 scope link  
       valid_lft forever preferred_lft forever  
```vagrant@vm1:~ ping 192.168.1.161```  
PING 192.168.1.161 (192.168.1.161) 56(84) bytes of data.  
64 bytes from 192.168.1.161: icmp_seq=1 ttl=64 time=0.743 ms  
64 bytes from 192.168.1.161: icmp_seq=2 ttl=64 time=0.292 ms  
64 bytes from 192.168.1.161: icmp_seq=3 ttl=64 time=0.327 ms  
64 bytes from 192.168.1.161: icmp_seq=4 ttl=64 time=0.292 ms  
64 bytes from 192.168.1.161: icmp_seq=5 ttl=64 time=0.316 ms  
64 bytes from 192.168.1.161: icmp_seq=6 ttl=64 time=0.507 ms  
64 bytes from 192.168.1.161: icmp_seq=7 ttl=64 time=0.266 ms  
64 bytes from 192.168.1.161: icmp_seq=8 ttl=64 time=0.336 ms  
^Z
[1]+  Stopped                 ping 192.168.1.161  
```vagrant@vm1:~ exit```  
logout  
There are stopped jobs.  
vagrant@vm1:~ exit  
logout  
Connection to 127.0.0.1 closed.  
```PS C:\test> vagrant halt```  
==> vm2: Attempting graceful shutdown of VM...  
==> vm1: Attempting graceful shutdown of VM...  
```PS C:\test> vagrant destroy```  
    vm2: Are you sure you want to destroy the 'vm2' VM? [y/N] y  
==> vm2: Destroying VM and associated drives...  
    vm1: Are you sure you want to destroy the 'vm1' VM? [y/N] y  
==> vm1: Destroying VM and associated drives..  
