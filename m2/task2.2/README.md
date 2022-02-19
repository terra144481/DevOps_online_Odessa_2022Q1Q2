**task2.2**
1. Create ec2 instance.

2. Create a snapshot of instance.

3. Create and attach a Disk_D (EBS). Mount Disk_D and create file "newfile".
```
[ec2-user@ip-172-31-92-116 ~]$ sudo blkid /dev/xvdf
/dev/xvdf: UUID="b269188c-376d-4594-91fd-bdd2744e104b" TYPE="ext4"
[ec2-user@ip-172-31-92-116 ~]$ mkdir disk
[ec2-user@ip-172-31-92-116 ~]$ sudo mount -t ext4 /dev/xvdf disk
[ec2-user@ip-172-31-92-116 ~]$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        475M     0  475M   0% /dev
tmpfs           483M     0  483M   0% /dev/shm
tmpfs           483M  496K  483M   1% /run
tmpfs           483M     0  483M   0% /sys/fs/cgroup
/dev/xvda1      8.0G  1.6G  6.5G  19% /
tmpfs            97M     0   97M   0% /run/user/1000
tmpfs            97M     0   97M   0% /run/user/0
/dev/xvdf       976M  2.6M  907M   1% /home/ec2-user/disk
[ec2-user@ip-172-31-92-116 ~]$ cd ./disk/
[ec2-user@ip-172-31-92-116 disk]$ sudo vi newfile
[ec2-user@ip-172-31-92-116 disk]$ ls
lost+found  newfile
[ec2-user@ip-172-31-92-116 disk]$ cd ..
[ec2-user@ip-172-31-92-116 ~]$ ls
disk
[ec2-user@ip-172-31-92-116 ~]$ cat ./disk/newfile
hello world
```

4. Launch the second instance from backup.

5. Detach Disk_D from the 1st instance and attach disk_D to the new instance.  
```
[ec2-user@ip-172-31-82-52 ~]$ lsblk -f  
NAME    FSTYPE LABEL UUID                                 MOUNTPOINT
xvda
└─xvda1 xfs    /     1aadf926-2d49-4c16-a47e-9aa2e0f50dc0 /
xvdf    ext4         b269188c-376d-4594-91fd-bdd2744e104b
[ec2-user@ip-172-31-82-52 ~]$ sudo mkdir diskd
[ec2-user@ip-172-31-82-52 ~]$ sudo mount /dev/xvdf diskd
[ec2-user@ip-172-31-82-52 ~]$ cd ./diskd/
[ec2-user@ip-172-31-82-52 diskd]$ ls
lost+found  newfile
```

6. register the domain name lovkin.pp.ua,change DNS A to static IP AWS WP (http://18.235.43.255/).

7. Configure a WordPress instance with Amazon Lightsail

8. Create bucket and upload file.

10. Create a user AWS IAM, configure CLI AWS and upload any files to S3

```
C:\Users\Home>aws configure
AWS Access Key ID [None]: AKIAVVR75ZTXHG4YR***
AWS Secret Access Key [None]: cmvNWDeTQt4tvsb3H/YHE4MURAdu43eiWUQ8w***
Default region name [None]: us-east-1
Default output format [None]: json

C:\Users\Home>aws s3 mb s3://mybucket144481144481
make_bucket: mybucket144481144481

C:\Users\Home>aws s3 cp "C:/Users/Home/Downloads/20220210_101324.jpg" s3://mybucket144481144481
upload: Downloads\20220210_101324.jpg to s3://mybucket144481144481/20220210_101324.jpg

C:\Users\Home>aws s3 cp s3://mybucket144481144481/20220210_101324.jpg ./
download: s3://mybucket144481144481/20220210_101324.jpg to .\20220210_101324.jpg

C:\Users\Home>aws s3 rm s3://mybucket144481144481/20220210_101324.jpg
delete: s3://mybucket144481144481/20220210_101324.jpg

C:\Users\Home>aws s3 rb s3://mybucket144481144481 --force
remove_bucket: mybucket144481144481
```
11. Create a cluster at Docker Containers on Amazon Elastic Container, and run the online demo application.  
command history ec2 machine:
```
    1  sudo yum update
    2  sudo amazon-linux-extras install docker
    3  sudo service docker start
    4  sudo systemctl enable docker
    5  sudo usermod -a -G docker ec2-user
    6  exit
    7  sudo docker info
    8  touch Dockerfile
    9*
   10  nano Dockerfile
   12  docker build -t hello-world .
   13  docker images --filter reference=hello-world
   14  docker run -t -i -p 80:80 hello-world
   16  curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
   17  unzip awscliv2.zip
   18  sudo ./aws/install
   27  aws --version
   28  aws configure
   34  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 389902355694.dkr.ecr.us-east-1.amazonaws.com
   35  docker build -t testapp .
   36  docker tag testapp:latest 389902355694.dkr.ecr.us-east-1.amazonaws.com/testapp:latest
   37  docker push 389902355694.dkr.ecr.us-east-1.amazonaws.com/testapp:latest
```
results:
```
aws --version
aws-cli/2.4.19 Python/3.8.8 Linux/5.10.96-90.460.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off
[ec2-user@ip-172-31-24-184 ~]$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 389902355694.dkr.ecr.us-east-1.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
Login Succeeded
[ec2-user@ip-172-31-24-184 ~]$ docker build -t testapp .
Sending build context to Docker daemon    248MB
Step 1/6 : FROM ubuntu:18.04
 ---> dcf4d4bef137
Step 2/6 : RUN apt-get update &&  apt-get -y install apache2
 ---> Using cache
 ---> d5cad079f156
Step 3/6 : RUN echo 'Hello World!' > /var/www/html/index.html
 ---> Using cache
 ---> 4f744f246f88
Step 4/6 : RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh &&  echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh &&  echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh &&  echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh &&  chmod 755 /root/run_apache.sh
 ---> Using cache
 ---> 0ac248d0b1cd
Step 5/6 : EXPOSE 80
 ---> Using cache
 ---> 19ee942712af
Step 6/6 : CMD /root/run_apache.sh
 ---> Using cache
 ---> 2daf69ba8252
Successfully built 2daf69ba8252
Successfully tagged testapp:latest
[ec2-user@ip-172-31-24-184 ~]$ docker tag testapp:latest 389902355694.dkr.ecr.us-east-1.amazonaws.com/testapp:latest
[ec2-user@ip-172-31-24-184 ~]$ docker push 389902355694.dkr.ecr.us-east-1.amazonaws.com/testapp:latest
The push refers to repository [389902355694.dkr.ecr.us-east-1.amazonaws.com/testapp]
4c4d153f6607: Pushed
9ab884869b1b: Pushed
f8988637651f: Pushed
1dc52a6b4de8: Pushed
latest: digest: sha256:d14781f711c81e012b68e0066e130d919ba16927efae6e128e7ea53d088e3960 size: 1155
```

12. Create a serverless "Hello, World!" with AWS Lambda.  

13. Сreate a static website on Amazon S3.  
http://devopsonline2022.s3-website-us-east-1.amazonaws.com/  
http://lovkin.pp.ua/  
