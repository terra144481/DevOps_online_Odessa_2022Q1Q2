**task4.2**

**1. Analyze the structure of the /etc/passwd and /etc/group file, what fields are
present in it, what users exist on the system? Specify several pseudo-users, how to
define them?**
In file /etc/passwd are present fields about users OS: name, password incrypt, UID, GID, info about user, home dir, program interpretetor
```
ubuntu@ip-172-31-81-205:~$ cat /etc/passwd
root:x:0:0:Ivan,777,0329-09324423,3249-2349:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```
System is consists: root user(UID=0), local user (UID >= 1000) (ubuntu, user1), pseudo-(1-100) (bin, deamon, etc)

In file /etc/group are present fields about group OS: group name, password incrypt, GID, users groups
```
ubuntu@ip-172-31-81-205:~$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
```
Pseudo-users define them UID (1-100)+nologin (not consists interpratetor)

**2. What are the uid ranges? What is UID? How to define it?**
UID is a number of users (range 0 до 65535). UID 0 - root, от 1 до 999 specify users (daemons, pseudo-users, system and reserved users), 1000+ - local users.
```
ubuntu@ip-172-31-81-205:~$ id root
uid=0(root) gid=0(root) groups=0(root)
```
```
ubuntu@ip-172-31-81-205:~$ cat /etc/passwd
root:x:0:0:Ivan,777,0329-09324423,3249-2349:/root:/bin/bash
user1:x:1001:1001:Test,7,56565655,878985:/home/user1:/bin/bash
or
ubuntu@ip-172-31-81-205:~$ cat /etc/passwd | grep ubuntu
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
```

**3. What is GID? How to define it?**
GID is name group, encripted pass, ID group
```
ubuntu@ip-172-31-81-205:~$ cat /etc/group
root:x:0:
ubuntu:x:1000:
user1:x:1001:
```

**4. How to determine belonging of user to the specific group?**
```
ubuntu@ip-172-31-81-205:~$ id -nG ubuntu
ubuntu adm dialout cdrom floppy sudo audio dip video plugdev netdev lxd
```

**5. What are the commands for adding a user to the system? What are the basic
parameters required to create a user?**
```
sudo adduser testuser
adduser  [options]  [--home  DIR] [--shell SHELL] [--no-create-home] [--uid ID] [--firstuid ID] [--lastuid ID] [--ingroup GROUP | --gid ID] [--disabled-
       password] [--disabled-login] [--gecos GECOS] [--add_extra_groups] [--encrypt-home] user
```

**6. How do I change the name (account name) of an existing user?**
```sudo usermod -l ubuntu1 ubuntu```

**7. What is skell_dir? What is its structure?**
Settings for create new users
```
cat /etc/default/useradd
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/bash
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes
```

**8. How to remove a user from the system (including his mailbox)?**
```ubuntu@ip-172-31-81-205:~$ sudo deluser --remove-all-files user22```

**9. What commands and keys should be used to lock and unlock a user account?**
```
ubuntu@ip-172-31-81-205:~$ sudo passwd --lock testlock
passwd: password expiry information changed.
ubuntu@ip-172-31-81-205:~$ sudo passwd --unlock testlock
passwd: password expiry information changed.
```

**10. How to remove a user's password and provide him with a password-free login
for subsequent password change?**
```
ubuntu@ip-172-31-81-205:~$ sudo passwd -d ubuntu
passwd: password expiry information changed.
ubuntu@ip-172-31-81-205:~$ passwd
New password:
Retype new password:
passwd: password updated successfully
```

**11. Display the extended format of information about the directory, tell about the
information columns displayed on the terminal.**
```
ubuntu@ip-172-31-81-205:~$ ls -la
total 36
drwxr-xr-x 4 ubuntu ubuntu 4096 Mar 29 10:09 .
drwxr-xr-x 5 root   root   4096 Mar 28 22:44 ..
-rw------- 1 ubuntu ubuntu  124 Mar 29 10:09 .Xauthority
-rw------- 1 ubuntu ubuntu 2201 Mar 29 09:58 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Mar 27 15:47 .cache
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
drwx------ 2 ubuntu ubuntu 4096 Mar 27 15:41 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Mar 27 15:48 .sudo_as_admin_successful
```

**12. What access rights exist and for whom (i. e., describe the main roles)? Briefly
describe the acronym for access rights.**
```
-rw-rw-r-- 1 ubuntu ubuntu 20 Mar 29 21:47 role.txt
r - read, w - write, x -execute
```

**13. What is the sequence of defining the relationship between the file and the user?
for files**
1 - owner, 2 - group, 3 - other.

**14. What commands are used to change the owner of a file (directory), as well as
the mode of access to the file? Give examples, demonstrate on the terminal.**
chown - change owner file
chgrp - change group
```
drwxrwxr-x 2 ubuntu ubuntu 4096 Mar 29 22:01 testdir
ubuntu@ip-172-31-81-205:~$ sudo chown root ./testdir
drwxrwxr-x 2 root   ubuntu 4096 Mar 29 22:01 testdir
```

**15. What is an example of octal representation of access rights? Describe the
umask command.**
```
ubuntu@ip-172-31-81-205:~$ umask
0022
ubuntu@ip-172-31-81-205:~$ echo "sometext" > sometextfile
ubuntu@ip-172-31-81-205:~$ ls -l
total 12
-rw-rw-r-- 1 ubuntu ubuntu   20 Mar 29 21:47 role.txt
-rw-r--r-- 1 ubuntu ubuntu    9 Apr  1 17:16 sometextfile
drwxrwxr-x 2 ubuntu ubuntu 4096 Mar 29 22:01 testdir
ubuntu@ip-172-31-81-205:~$ umask 777
ubuntu@ip-172-31-81-205:~$ umask
0777
ubuntu@ip-172-31-81-205:~$ echo "sometext1" > sometextfile1
ubuntu@ip-172-31-81-205:~$ ls -l
total 16
-rw-rw-r-- 1 ubuntu ubuntu   20 Mar 29 21:47 role.txt
-rw-r--r-- 1 ubuntu ubuntu    9 Apr  1 17:16 sometextfile
---------- 1 ubuntu ubuntu   10 Apr  1 17:18 sometextfile1
drwxrwxr-x 2 ubuntu ubuntu 4096 Mar 29 22:01 testdir
```
**16. Give definitions of sticky bits and mechanism of identifier substitution. Give
an example of files and directories with these attributes.**
sticky bits - help protect owner file by remove
```
ubuntu@ip-172-31-81-205:~$ ls -l
total 12
-rw-r--r-- 1 ubuntu ubuntu    1 Apr  1 17:29 next
-rw-rw-r-- 1 ubuntu ubuntu   20 Mar 29 21:47 role.txt
drwxrwxr-x 2 ubuntu ubuntu 4096 Mar 29 22:01 testdir
ubuntu@ip-172-31-81-205:~$ chmod +t next
ubuntu@ip-172-31-81-205:~$ ls -l
total 12
-rw-r--r-T 1 ubuntu ubuntu    1 Apr  1 17:29 next
-rw-rw-r-- 1 ubuntu ubuntu   20 Mar 29 21:47 role.txt
drwxrwxr-x 2 ubuntu ubuntu 4096 Mar 29 22:01 testdir
```

**17. What file attributes should be present in the command script?**  
x -execute atributes
