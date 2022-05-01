**Task6**

**A. Create a script that uses the following keys:**  
1. When starting without parameters, it will display a list of possible keys and their description.
2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet
3. The --target key displays a list of open system TCP ports.
The code that performs the functionality of each of the subtasks must be placed in a separate function

```
#!/bin/bash
echo "This is scrypt using two keys: --all and --target."
echo " Please using it.--all key displays the IP addresses and symbolic names of all hosts in the current subnet"
echo " --target key displays a list of open system TCP ports"

while [ -n "$1" ]
do
case "$1" in
           --all) echo "Name of host and IP addresses :"
                hostnamectl | grep -i hostname
                ip addr | grep -i inet;;
        --target) echo "Open system TCP ports:"
                netstat -lt;;
               *) echo "Enter somting key!"
                echo "--all key displays the IP addresses and symbolic names of all hosts in the current subnet"
                echo "--target key displays a list of open system TCP ports";;
esac
shift
done
```

```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh
This is scrypt using two keys: --all and --target.
 Please using it.--all key displays the IP addresses and symbolic names of all hosts in the current subnet
 --target key displays a list of open system TCP ports
```

```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh --all
This is scrypt using two keys: --all and --target.
 Please using it.--all key displays the IP addresses and symbolic names of all hosts in the current subnet
 --target key displays a list of open system TCP ports
Name of host and IP addresses :
   Static hostname: ip-172-31-26-111.ec2.internal
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
    inet 172.31.26.111/20 brd 172.31.31.255 scope global dynamic eth0
    inet6 fe80::819:e7ff:fe16:b45b/64 scope link
```
```
[ec2-user@ip-172-31-26-111 ~]$ ./first.sh --target
This is scrypt using two keys: --all and --target.
 Please using it.--all key displays the IP addresses and symbolic names of all hosts in the current subnet
 --target key displays a list of open system TCP ports
Open system TCP ports:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 localhost:smtp          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:sunrpc          0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
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
