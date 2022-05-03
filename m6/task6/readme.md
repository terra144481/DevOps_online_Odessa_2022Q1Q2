**Task6**

**A. Create a script that uses the following keys:**
1. When starting without parameters, it will display a list of possible keys and their description.
2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet
3. The --target key displays a list of open system TCP ports.
The code that performs the functionality of each of the subtasks must be placed in a separate function

 **1) Create file first.sh**
``[ec2-user@ip-172-31-26-111 ~]$ nano first.sh``

```
#!/bin/bash
if [ -z $1 ] #значение параметра равно 0
then
        echo "This is scrypt using two keys: --all and --target."
        echo "--all key displays the IP addresses and symbolic names of all hosts in the current subnet"
        echo "--target key displays a list of open system TCP ports"
else

while [ -n "$1" ] #значение параметра больше 0
do
case "$1" in
           --all) echo " Show IP addresses and symbolic names of all hosts in the current subnet :"
#               hostnamectl | grep -i hostname
#               ip addr | grep -i inet
                arp -n;;
        --target) echo "Open system TCP ports:"
                netstat -lt;;
               *) echo "Please choose something key!"
                echo "--all key displays the IP addresses and symbolic names of all hosts in the current subnet"
                echo "--target key displays a list of open system TCP ports";;
esac
shift
done
fi
```
**2) chmod a+x name**
``[ec2-user@ip-172-31-26-111 ~]$ chmod a+x first.sh``  

**3) Run scrypt**
```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh
This is scrypt using two keys: --all and --target.
--all key displays the IP addresses and symbolic names of all hosts in the current subnet
--target key displays a list of open system TCP ports
```

```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh --all
 Show IP addresses and symbolic names of all hosts in the current subnet :
Address                  HWtype  HWaddress           Flags Mask            Iface
172.31.16.1              ether   0a:2d:c6:4b:4c:3d   C                     eth0
```

```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh --target
Open system TCP ports:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
tcp        0      0 localhost:smtp          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:sunrpc          0.0.0.0:*               LISTEN
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN
```

```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh --some
Please choose something key!
--all key displays the IP addresses and symbolic names of all hosts in the current subnet
--target key displays a list of open system TCP ports
```
**B. Using Apache log example create a script to answer the following questions:**
1. From which ip were the most requests?
```
#!/bin/bash
file_out=out_script2
awk '{print $1}' $1 | sort |uniq -c | sort -gr > $file_out
{
read line1
}<$file_out
echo $line1
```
```
[ec2-user@ip-172-31-26-111 ~]$ ./sc1.sh apache_logs.txt
62 157.55.39.250
 ```

   2. What is the most requested page?
```
#!/bin/bash
file_out=out_script2
awk '{print $7}' $1 | sort |uniq -c | sort -gr > $file_out
{
read line1
}<$file_out
echo $line1
```
```
[ec2-user@ip-172-31-26-111 ~]$ ./sc2.sh apache_logs.txt
8 /sitemap1.xml.gz
```
3. How many requests were there from each ip?

4. What non-existent pages were clients referred to?

5. What time did site get the most requests?
```
#!/bin/bash
file_out=out_script2
awk '{print $4}' $1 | sort |uniq -c | sort -gr > $file_out
{
read line1
}<$file_out
echo $line1
```
```
[ec2-user@ip-172-31-26-111 ~]$ ./sc1.sh apache_logs.txt
5 [30/Sep/2015:02:26:55
```

6. What search bots have accessed the site? (UA + IP)

**C. Create a data backup script that takes the following data as parameters:**
1. Path to the syncing directory.
2. The path to the directory where the copies of the files will be stored.
In case of adding new or deleting old files, the script must add a corresponding entry to the log file
indicating the time, type of operation and file name. [The command to run the script must be added to
crontab with a run frequency of one minute]
