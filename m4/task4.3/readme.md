**task4.3**

**1. Part1**
**1. How many states could has a process in Linux?**
 - Running or Runnable (R)
 - Uninterruptible Sleep (D)
 - Interruptable Sleep (S)
 - Stopped (T)
 - Zombie (Z)

**2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current
process.**
```ubuntu@ip-172-31-81-205:~$ pstree -ha```
```
systemd
  ├─accounts-daemon
  │   └─2*[{accounts-daemon}]
  ├─acpid
  ├─agetty -o -p -- \\u --keep-baud 115200,38400,9600 ttyS0 vt220
  ├─agetty -o -p -- \\u --noclear tty1 linux
  ├─amazon-ssm-agen
  │   ├─ssm-agent-worke
  │   │   └─6*[{ssm-agent-worke}]
  │   └─7*[{amazon-ssm-agen}]
....
```
**3. What is a proc file system?**
Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down. It contains useful information about the processes that are currently running, it is regarded as control and information center for kernel.
folder /proc
**4. Print information about the processor (its type, supported technologies, etc.).**

```ubuntu@ip-172-31-81-205:~$ less /proc/cpuinfo```
```
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 63
model name      : Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
stepping        : 2
microcode       : 0x46
cpu MHz         : 2400.041
cache size      : 30720 KB
...
```
**5. Use the ps command to get information about the process. The information should be as
follows: the owner of the process, the arguments with which the process was launched for
execution, the group owner of this process, etc.**

```ubuntu@ip-172-31-81-205:~$ ps -eo pid,ppid,fgroup,ni,lstart,etime,user```
```
     PID    PPID FGROUP    NI STARTED     ELAPSED USER
      1       0 root       0 Thu Apr  7 13:52:05 2022       43:26 root
      2       0 root       0 Thu Apr  7 13:52:05 2022       43:26 root
      3       2 root     -20 Thu Apr  7 13:52:05 2022       43:26 root
      4       2 root     -20 Thu Apr  7 13:52:05 2022       43:26 root
```
**6. How to define kernel processes and user processes?**
kernel process [...]. They are starts with OS.

**7. Print the list of processes to the terminal. Briefly describe the statuses of the processes.
What condition are they in, or can they be arriving in?**
```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.2 102948 12272 ?        Ss   11:47   0:03 /sbin/init
root           2  0.0  0.0      0     0 ?        S    11:47   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   11:47   0:00 [rcu_gp]
```
stat - S, R, I

**8. Display only the processes of a specific user.**
```
ubuntu@ip-172-31-81-205:~$ ps -u ubuntu

    PID TTY          TIME CMD
   1163 ?        00:00:00 systemd
   1164 ?        00:00:00 (sd-pam)
   1266 ?        00:00:00 sshd
   1270 pts/0    00:00:00 bash
   2236 pts/0    00:00:00 ps
   ```

**9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?**
 pgrep, pstree, top, htop

**10. What information does top command display?**
Dinamic information about process.
PID, User, CPu, Mem, etc.

**11. Display the processes of the specific user using the top command.**
```ubuntu@ip-172-31-81-205:~$ top -u ubuntu```
```
top - 15:24:11 up  3:36,  1 user,  load average: 0.00, 0.00, 0.00
Tasks: 104 total,   1 running, 103 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :    967.9 total,    191.0 free,    154.7 used,    622.2 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.    651.9 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   1163 ubuntu    20   0   18228   9476   8132 S   0.0   1.0   0:00.03 systemd
   1164 ubuntu    20   0  104164   4368      4 S   0.0   0.4   0:00.00 (sd-pam)
   1266 ubuntu    20   0   14064   6528   4796 S   0.0   0.7   0:01.53 sshd
   1270 ubuntu    20   0   10040   5048   3344 S   0.0   0.5   0:00.11 bash
   2299 ubuntu    20   0   11020   3912   3332 R   0.0   0.4   0:00.04 top
```
**12. What interactive commands can be used to control the top command? Give a couple of
examples.**
  k,r       Manipulate tasks: 'k' kill; 'r' renice
 u,U,o,O . Filter by: 'u'/'U' effective/any user; 'o'/'O' other criteria
 **13. Sort the contents of the processes window using various parameters (for example, the
amount of processor time taken up, etc.)**
y <>
**14. Concept of priority, what commands are used to set priority?**
nice, renice
**15. Can I change the priority of a process using the top command? If so, how?**
top r nice, renice
**16. Examine the kill command. How to send with the kill command process control signal? Give
an example of commonly used signals.**
 ```
PID to signal/kill [default pid = 3975] 4069
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   3975 ubuntu    20   0   13940   5288   3832 S   0.0   0.5   0:00.00 sshd
   4069 ubuntu    20   0   11020   3860   3184 R   0.0   0.4   0:00.30 top
```
**17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to
demonstrate the process control mechanism with fg, bg.**
``sleep 5 - stop ps 5 sec``
```
[1]+  Exit 127                $ nice gzip < /dev/zero > /dev/null
ubuntu@ip-172-31-81-205:~$ nice bzip2 < /dev/zero > /dev/null &
[1] 2853
ubuntu@ip-172-31-81-205:~$ nice gzip < /dev/zero > /dev/null &
[2] 2857
ubuntu@ip-172-31-81-205:~$ nice xz < /dev/zero > /dev/null &
[3] 2858
ubuntu@ip-172-31-81-205:~$ jobs
[1]   Running                 nice bzip2 < /dev/zero > /dev/null &
[2]-  Running                 nice gzip < /dev/zero > /dev/null &
[3]+  Running                 nice xz < /dev/zero > /dev/null &
ubuntu@ip-172-31-81-205:~$ jobs -l
[1]   2853 Running                 nice bzip2 < /dev/zero > /dev/null &
[2]-  2857 Running                 nice gzip < /dev/zero > /dev/null &
[3]+  2858 Running                 nice xz < /dev/zero > /dev/null &
ubuntu@ip-172-31-81-205:~$ fg
nice xz < /dev/zero > /dev/null
^Z
[3]+  Stopped                 nice xz < /dev/zero > /dev/null
ubuntu@ip-172-31-81-205:~$ jobs -l
[1]   2853 Running                 nice bzip2 < /dev/zero > /dev/null &
[2]-  2857 Running                 nice gzip < /dev/zero > /dev/null &
[3]+  2858 Stopped                 nice xz < /dev/zero > /dev/null
ubuntu@ip-172-31-81-205:~$ bg
[3]+ nice xz < /dev/zero > /dev/null &
ubuntu@ip-172-31-81-205:~$ jobs -l
[1]   2853 Running                 nice bzip2 < /dev/zero > /dev/null &
[2]-  2857 Running                 nice gzip < /dev/zero > /dev/null &
[3]+  2858 Running                 nice xz < /dev/zero > /dev/null &

ubuntu@ip-172-31-81-205:~$ fg 1
nice bzip2 < /dev/zero > /dev/null
^C
ubuntu@ip-172-31-81-205:~$ jobs -l
[2]-  2857 Running                 nice gzip < /dev/zero > /dev/null &
[3]+  2858 Running                 nice xz < /dev/zero > /dev/null &
```

**Part2**
**1. Check the implementability of the most frequently used OPENSSH commands in the MS
Windows operating system. (Description of the expected result of the commands +screenshots:
command – result should be presented)**
a) ssh-copy-id username@remote_host
```
 ssh-keygen
 ssh testpc@192.168.0.110
 ssh-copy-id testpc@192.168.0.110
 exit
 ssh testpc@192.168.0.110
```


b) ``cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"``
```
mkdir ~/.ssh
chmod 0700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 0644 ~/.ssh/authorized_keys
cat > .ssh/authorized_keys
past id_rsa.pub ctrl+D
```
c) ```ssh-copy-id -i ~/.ssh/id_rsa.pub user@host```

**2. Implement basic SSH settings to increase the security of the client-server connection (at
least)**
edit sshd_config, del pass auth.
change ssh port on file 22 > 2233
```testpc@ubuntu-VirtualBox:~$ sudo nano /etc/ssh/sshd_config```

```testpc@ubuntu-VirtualBox:~/.ssh$ ssh -p2233 testpc@192.168.0.109```

**3. List the options for choosing keys for encryption in SSH. Implement 3 of them.**
```
ssh-keygen [-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]

testpc@ubuntu-VirtualBox:~/.ssh$ ssh-keygen -t ecdsa
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBab56dEbWiA8tRA ...

testpc@ubuntu-VirtualBox:~/.ssh$ ssh-keygen -t ed25519
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIxYvuv67SybDVLiWjs53yI2Afhh1w82RlBurzhphvOa testpc@ubuntu-VirtualBox

testpc@ubuntu-VirtualBox:~/.ssh$ ssh-keygen -t rsa
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCyuuKV....
```
**4. Implement port forwarding for the SSH client from the host machine to the guest Linux
virtual machine behind NAT.**
```
C:\Users\User>ssh -p 2222 testpc@127.0.0.1
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ECDSA key fingerprint is SHA256:aGaFjZNqMhO9WEb35efCTbEdM5HcDTYOMoEmWxYThQE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ECDSA) to the list of known hosts.
testpc@127.0.0.1's password:
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-39-generic x86_64)
```
**images link**

**5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the
server using ssh, telnet, rlogin. Analyze the result.**
For SSH I used command:
sudo tcpdump -vv -i any -nn port 22 -w   dump_ssh.pcap

For Telnet I used command:
sudo tcpdump -vv -i any -nn port 23 -w    dump_telnet.pcap
