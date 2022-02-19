**task3.1**  
**1. Create 3 LANs:**

![image 1](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/751317483b92f6762c4f64bf42f7be743395a5b8/m3/task3.1/images/main3.1.png)  

- LAN "Enterprise" 10.84.16.0/24 includs:  
        PC "Client 1" IP 10.84.16.10  
        PC "Client 2" IP 10.84.16.20  
        DHCP server 10.84.16.100  
        switch 2960  
- LAN "Data Center" 10.16.84.0/24 includs:  
        "Web Server 1" IP 10.16.84.50  
        "Web Server 2" IP 10.16.84.100  
        "DNS Server" IP 10.16.84.150  
- LAN "Home Office"  
        "Home Router" IP 192.168.0.1  
        "Client 3" IP 192.168.0.26  


**2. LAN Enterprise. Co to command line Client 1**  
 - ```C:\>ping 10.84.16.20```  

Pinging 10.84.16.20 with 32 bytes of data:  

Reply from 10.84.16.20: bytes=32 time=23ms TTL=128  
Reply from 10.84.16.20: bytes=32 time=3ms TTL=128  
Reply from 10.84.16.20: bytes=32 time=3ms TTL=128  
Reply from 10.84.16.20: bytes=32 time<1ms TTL=128  

Ping statistics for 10.84.16.20:  
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
Approximate round trip times in milli-seconds:  
    Minimum = 0ms, Maximum = 23ms, Average = 7ms  

- ```C:\>ping 10.84.16.100```  

Pinging 10.84.16.100 with 32 bytes of data:  

Reply from 10.84.16.100: bytes=32 time<1ms TTL=128  
Reply from 10.84.16.100: bytes=32 time<1ms TTL=128  
Reply from 10.84.16.100: bytes=32 time<1ms TTL=128  
Reply from 10.84.16.100: bytes=32 time<1ms TTL=128  

Ping statistics for 10.84.16.100:  
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
Approximate round trip times in milli-seconds:  
    Minimum = 0ms, Maximum = 0ms, Average = 0ms  
![image 2](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/751317483b92f6762c4f64bf42f7be743395a5b8/m3/task3.1/images/client1%20cmd.png)

**3. LAN Data Center. Go to command line Web Server 1**  
- ```C:\>ping 10.16.84.150```  

Pinging 10.16.84.150 with 32 bytes of data:  

Reply from 10.16.84.150: bytes=32 time=1ms TTL=128  
Reply from 10.16.84.150: bytes=32 time=1ms TTL=128  
Reply from 10.16.84.150: bytes=32 time<1ms TTL=128  
Reply from 10.16.84.150: bytes=32 time=3ms TTL=128  

Ping statistics for 10.16.84.150:  
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
Approximate round trip times in milli-seconds:  
    Minimum = 0ms, Maximum = 3ms, Average = 1ms  

- ```C:\>ping 10.16.84.100```  

Pinging 10.16.84.100 with 32 bytes of data:  

Reply from 10.16.84.100: bytes=32 time=1ms TTL=128  
Reply from 10.16.84.100: bytes=32 time=3ms TTL=128  
Reply from 10.16.84.100: bytes=32 time<1ms TTL=128  
Reply from 10.16.84.100: bytes=32 time=5ms TTL=128  

Ping statistics for 10.16.84.100:  
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
Approximate round trip times in milli-seconds:  
    Minimum = 0ms, Maximum = 5ms, Average = 2ms  

![image 3](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/751317483b92f6762c4f64bf42f7be743395a5b8/m3/task3.1/images/webserver1%20cmd.png)

**4. LAN "Home Office" Go to command line "Client 3"**  
- ```C:\>ping 192.168.0.1```  

Pinging 192.168.0.1 with 32 bytes of data:  

Reply from 192.168.0.1: bytes=32 time=8ms TTL=255  
Reply from 192.168.0.1: bytes=32 time=32ms TTL=255  
Reply from 192.168.0.1: bytes=32 time=47ms TTL=255  
Reply from 192.168.0.1: bytes=32 time=6ms TTL=255  

Ping statistics for 192.168.0.1:  
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),  
Approximate round trip times in milli-seconds:  
    Minimum = 6ms, Maximum = 47ms, Average = 23ms    

![image 4](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/751317483b92f6762c4f64bf42f7be743395a5b8/m3/task3.1/images/client3%20cmd.png)  
