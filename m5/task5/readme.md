**task5**

**1. На Server_1 налаштувати статичні адреси на всіх інтерфейсах
Server_1 – ОС Linux Ubuntu 20.**
net1 - 192.168.0.1/24 (enp0s3) режим «Мережевий міст» Int1 -192.168.0.103
net2 - 10.84.16.1/24 (enp0s8) режим «Внутрішня мережа» Int2
net3 - 10.10.84.1/24 (enp0s9) режим «Внутрішня мережа» Int3

Client1:
net2 - 10.84.16.2/24 (enp0s3) Int1 режим «Внутрішня мережа»
net4 - 172.16.10.1/24 (enp0s8) Int2  режим «Внутрішня мережа»

Client2:
net3 - 10.10.84.0/24 (enp0s3) Int1 режим «Внутрішня мережа»
net4 - 172.16.10.2/24 (enp0s8) Int2  режим «Внутрішня мережа»
```
testpc@server1:~$ ls /sys/class/net
enp0s3  enp0s8  enp0s9  lo
```
``testpc@server1:~$ sudo nano /etc/netplan/00-installer-config.yaml``
```
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      addresses: [192.168.0.103/24]
      gateway4: 192.168.0.1
      dhcp4: no
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
    enp0s8:
      addresses: [10.84.16.1/24]
    enp0s9:
      addresses: [10.10.84.1/24]
  version: 2

testpc@server1:~$ sudo netplan generate
testpc@server1:~$ sudo netplan --debug generate
testpc@server1:~$ sudo netplan apply
```
```
testpc@server1:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group defaul                                                                                    t qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP gr                                                                                    oup default qlen 1000
    link/ether 08:00:27:ec:8e:74 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.103/24 brd 192.168.0.255 scope global enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:feec:8e74/64 scope link
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP gr                                                                                    oup default qlen 1000
    link/ether 08:00:27:5a:dc:de brd ff:ff:ff:ff:ff:ff
    inet 10.84.16.1/24 brd 10.84.16.255 scope global enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe5a:dcde/64 scope link
       valid_lft forever preferred_lft forever
4: enp0s9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP gr                                                                                    oup default qlen 1000
    link/ether 08:00:27:03:e6:3b brd ff:ff:ff:ff:ff:ff
    inet 10.10.84.1/24 brd 10.10.84.255 scope global enp0s9
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe03:e63b/64 scope link
       valid_lft forever preferred_lft forever
```

**2. На Server_1 налаштувати DHCP сервіс, який буде конфігурувати адреси Int1
Client_1 та Client_2**

``testpc@server1:~$ sudo apt install isc-dhcp-server``
```
testpc@server1:~$ sudo nano /etc/dhcp/dhcpd.conf

default-lease-time 600;
max-lease-time 7200;
authoritative;
subnet 10.84.16.0 netmask 255.255.255.0 {
range 10.84.16.2 10.84.16.50;
option routers 10.84.16.254;
option domain-name-servers 10.84.16.1, 8.8.8.8, 8.8.4.4;
picture 1
```
``nano /etc/default/isc-dhcp-server `` добавить физические интерфейсы
``sudo systemctl restart isc-dhcp-server``

``sudo systemctl status isc-dhcp-server``
![pic 2]()

``sudo systemctl start isc-dhcp-server``

``sudo systemctl stop isc-dhcp-server``

**4. На віртуальному інтерфейсу lo Client_1 призначити дві ІР адреси за таким
правилом: 172.17.26.1/24 та 172.17.36.1/24. Налаштувати маршрутизацію
таким чином, щоб трафік з Client_2 до 172.17.26.1 проходив через Server_1, а до
172.17.36.1 через Net4. Для перевірки використати traceroute**

![2_VirtualBox_client1_15_04_2022_19_17_37_add lo]

![5 VirtualBox_client1_16_04_2022_01_15_41add route]

![6 VirtualBox_client1_16_04_2022_01_29_11 addrout]

**5. Розрахувати спільну адресу та маску (summarizing) адрес 172.17.26.1 та
172.17.36.1, при чому маска має бути максимально можливою.
Видалити
маршрути, встановлені на попередньому кроці та замінити їх об’єднаним
маршрутом, якій має проходити через Server_1
172.17.0.1/18**

10101100.00010001.00011010.00000001 172.17.26.1
10101100.00010001.00100100.00000001 172.17.36.1
10101100.00010001.00111110.00000001 172.17.0.1/18

![7 VirtualBox_client1_17_04_2022_12_15_51_add_172_17_0_0_18]()

**6. Налаштувати SSH сервіс таким чином, щоб Client_1 та Client_2 могли
підключатись до Server_1 та один до одного.**

![8 VirtualBox_client1_17_04_2022_12_23_08_ssh192_168_0_103]
![9]()
![10 VirtualBox_client1_17_04_2022_12_23_08_ssh172_16_10_2]()

**7. Налаштуйте на Server_1 firewall таким чином:
• Дозволено підключатись через SSH з Client_1 та заборонено з Client_2
• З Client_2 на 172.17.26.1 ping проходив, а на 172.17.36.1 не проходив**
```
sudo apt install ufw
sudo ufw allow in on enp0s8 to any port 22
sudo ufw dany in on enp0s9 to any port 80
sudo ufw enable
```
**8. Якщо в п.3 була налаштована маршрутизація для доступу Client_1 та Client_2 до
мережі Інтернет – видалити відповідні записи. На Server_1 налаштувати NAT
сервіс таким чином, щоб з Client_1 та Client_2 проходив ping в мережу Інтернет**
```
testpc@server1:~$ sysctl net.ipv4.conf.all.forwarding
net.ipv4.conf.all.forwarding = 0
testpc@server1:~$ cat /proc/sys/net/ipv4/ip_forward
0
testpc@server1:~$ sysctl net.ipv4.conf.all.forwarding=1
sysctl: permission denied on key "net.ipv4.conf.all.forwarding", ignoring
testpc@server1:~$ sudo !!
sudo sysctl net.ipv4.conf.all.forwarding=1
net.ipv4.conf.all.forwarding = 1
testpc@server1:~$ nano /etc/sysctl.conf
testpc@server1:~$ sudo !!
sudo nano /etc/sysctl.conf
net.ipv4.conf.all.forwarding=1
testpc@server1:~$ sudo iptables -t nat -A POSTROUTING -s 10.84.16.0/24 -j SNAT --to-source 192.168.0.103
testpc@server1:~$ sudo iptables -t nat -A POSTROUTING -s 10.10.84.0/24 -j SNAT --to-source 192.168.0.103

testpc@server1:~$ sudo iptables -t nat -L
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination

Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination
SNAT       all  --  10.84.16.0/24        anywhere             to:192.168.0.103
SNAT       all  --  10.10.84.0/24        anywhere             to:192.168.0.103
```
![12 VirtualBox_client1_18_04_2022_15_38_36_inet]()
