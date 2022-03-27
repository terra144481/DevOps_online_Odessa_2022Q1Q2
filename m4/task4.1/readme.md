**task4.1**

**1. Log in to the system as root (or sudo-er).**
```ubuntu@ip-172-31-81-205:~$ sudo su or sudo```

**2. Use the passwd command to change the password. Examine the basic parameters
of the command. What system file does it change ?**
```
root@ip-172-31-81-205:/home/ubuntu# passwd
New password:
Retype new password:
passwd: password updated successfully
root@ip-172-31-81-205:/home/ubuntu# sudo cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
```
/etc/passwd - User account information.
/etc/shadow - Secure user account information.
/etc/pam.d/passwd- PAM configuration for passwd.

**3. Determine the users registered in the system, as well as what commands they
execute. What additional information can be gleaned from the command execution?**
```
ubuntu@ip-172-31-81-205:~$ w
 16:42:55 up 15 min,  1 user,  load average: 0.00, 0.07, 0.04
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
ubuntu   pts/0    78.80.18.26      16:31    0.00s  0.03s  0.00s w
ubuntu@ip-172-31-81-205:~$ who
ubuntu   pts/0        2022-03-27 16:31 (78.80.18.26)
ubuntu@ip-172-31-81-205:~$ whoami
ubuntu
ubuntu@ip-172-31-81-205:~$ id
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev),118(lxd)
ubuntu@ip-172-31-81-205:~$ finger
Login     Name       Tty      Idle  Login Time   Office     Office Phone
ubuntu    Ubuntu     pts/0          Mar 27 16:31 (78.80.18.26)
```
**4. Change personal information about yourself.**
```
root@ip-172-31-81-205:/home/ubuntu# chfn
Changing the user information for root
Enter the new value, or press ENTER for the default
        Full Name [root]: Ivan
        Room Number []: 777
        Work Phone []: 0329-09324423
        Home Phone []: 3249-2349
        Other []:
  ```
  **5. Become familiar with the Linux help system and the man and info commands.**
  ```ubuntu@ip-172-31-81-205:~$ man passwd```
  ```ubuntu@ip-172-31-81-205:~$ info passwd```
Get help on the previously discussed commands, define and describe any two keys
for these commands. Give examples.
```
ubuntu@ip-172-31-81-205:~$ man -w
/usr/local/man:/usr/local/share/man:/usr/share/man
ubuntu@ip-172-31-81-205:~$ man -V
man 2.9.1
```
**6. Explore the more and less commands using the help system. View the contents of
files .bash* using commands.**
```ubuntu@ip-172-31-81-205:~$ more .bash*```
```ubuntu@ip-172-31-81-205:~$ less .bash*```

**7. Describe in plans that you are working on laboratory work 1. Tip: You should
read the documentation for the finger command.**
```
ubuntu@ip-172-31-81-205:~$ finger -l root
Login: root                             Name: Ivan
Directory: /root                        Shell: /bin/bash
Office: 777, 0329-09324423              Home Phone: 3249-2349
Never logged in.
No mail.
No Plan.
ubuntu@ip-172-31-81-205:~$
```

**8. List the contents of the home directory using the ls command, define its files
and directories. Hint: Use the help system to familiarize yourself with the ls
command**
```
ubuntu@ip-172-31-81-205:~$ ls -la
total 36
drwxr-xr-x 4 ubuntu ubuntu 4096 Mar 27 20:34 .
drwxr-xr-x 4 root   root   4096 Mar 27 16:46 ..
-rw------- 1 ubuntu ubuntu  124 Mar 27 20:34 .Xauthority
-rw------- 1 ubuntu ubuntu  560 Mar 27 18:23 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Mar 27 15:47 .cache
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
drwx------ 2 ubuntu ubuntu 4096 Mar 27 15:41 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Mar 27 15:48 .sudo_as_admin_successful
```
