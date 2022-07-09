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

```
#!/bin/bash
TIME=$(date)
SRC_DIR=$1
DST_DIR=$2
CNTR=0
SRC_FULL_PATH=($1)
DST_FULL_PATH=($2)
touch syncer_log.log
echo "Starting copying data:" > syncer_log.log
echo "Time: '$TIME'" >> syncer_log.log
echo "From: '$SRC_FULL_PATH'" >> syncer_log.log
echo "To: '$DST_FULL_PATH'" >> syncer_log.log
echo "Scanning source folder..." >> syncer_log.log
SRC_FILES=$(ls $SRC_FULL_PATH|sort)
SRC_FILES_AMOUNT=$(ls $SRC_FULL_PATH|sort|wc -w)
echo "Files found: $SRC_FILES_AMOUNT" >> syncer_log.log
for FILE in $SRC_FILES
do
CNTR=$[$CNTR + 1]
echo "$CNTR. $FILE" >> syncer_log.log
done
unset FILE
CNTR=0
echo "Scanning destination folder..." >> syncer_log.log
DST_FILES=$(ls $DST_FULL_PATH|sort)
DST_FILES_AMOUNT=$(ls $DST_FULL_PATH|sort|wc -w)
echo "Files found: $DST_FILES_AMOUNT" >> syncer_log.log
for DFILE in $DST_FILES
do
CNTR=$[$CNTR + 1]
echo "$CNTR. $DFILE" >> syncer_log.log
done
unset DFILE
CNTR=0
echo "Scanning done." >> syncer_log.log
echo "Synchronization of content:" >> syncer_log.log
if [ -z "$DST_FILES" ];
then
echo "$SRC_FULL_PATH and $DST_FULL_PATH"
cp -r $SRC_FULL_PATH/. $DST_FULL_PATH
TIME=$(date)
echo "$TIME -----> $FILE was added to dest. dir." >> syncer_log.log
echo "$TIME -----> All files from source dir. was copied to dst.dir."
elif [ -n "$DST_FILES" ]
then
for FILE in $SRC_FILES
do
for DFILE in $DST_FILES
do
#echo "S:$FILE and D:$DFILE"
if [ "$DFILE" = "$FILE" ];
then
TIME=$(date)
cp -f $SRC_FULL_PATH/$FILE $DST_FULL_PATH/
echo "$TIME -----> $FILE is up to date." >> syncer_log.log
echo "$TIME -----> $FILE is up to date."
SRC_FILES=$(echo '$SRC_FILES' | sort | grep -v "$FILE")
NOT_EXIST=$((0))
break
elif [ "$DFILE" != "$FILE" ]
then
NOT_EXIST=$((1))
fi
done
if [ "$NOT_EXIST" == 1 ];
then
cp -f $SRC_FULL_PATH/$FILE $DST_FULL_PATH/
echo "$TIME -----> $FILE was added to dest. dir." >> syncer_log.log
echo "$TIME -----> $FILE was added to dest. dir."
SRC_FILES=$(echo '$SRC_FILES' | sort | grep -v "$FILE")
NOT_EXIST=$((0))
fi
done
fi
SRC_FILES=$(ls $SRC_FULL_PATH|sort)
DST_FILES=$(ls $DST_FULL_PATH|sort)
if [ -z "$SRC_FILES" ];
then
rm -f $DST_FULL_PATH/*
elif [ -n "$SRC_FILES" ];
then
for DFILE in $DST_FILES
do
for FILE in $SRC_FILES
do
EXIST=$((0))
if [ "$DFILE" == "$FILE" ];
then
EXIST=$((1))
break
elif [ "$DFILE" != "$FILE" ];
then
EXIST=$((0))
fi
done
if [ "$EXIST" == 0 ];
then
TIME=$(date)
rm -f $DST_FULL_PATH/$DFILE
echo "$TIME -----> $DFILE was removed from dest. dir." >> syncer_log.log
echo "$TIME -----> $DFILE was removed from dest. dir."
fi
done
fi
echo "Synchronization done." >> syncer_log.log
```
