**task3.2**

1. **ІР-адреси інтерфейсів маршрутизаторів:**  

Router ISP1 GE0/0 - 10.84.16.1/24;  
Router ISP1 GE1/0 - 26.10.84.126/26  
Router ISP1 GE2/0 - 26.10.84.129/26  

Router ISP2 GE0/0 - 26.10.84.1/26  
Router ISP2 GE1/0 - 26.10.84.65/26  
Router ISP2 GE3/0 - 26.10.84.254/26  

Router ISP3 GE0/0 - 10.16.84.1/24;  
Router ISP3 GE2/0 - 26.10.84.190/26  
Router ISP3 GE3/0 - 26.10.84.193/26  

Розділення мережі 26.10.84.0/24 на 4 підмережі 26.10.84.0/26:  
Діапазон:  
26.10.84.0/26 62 hosts  
26.10.84.64/26 62 hosts  
26.10.84.128/26 62 hosts  
26.10.84.192/26 62 hosts  

![1_gen..png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/1_gen..png)

![2_cl3_ping_isp2.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/2_cl3_ping_isp2.png)

![3_serv_ping+isp3.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/3_serv_ping+isp3.png)

![4_pc1_ping_isp1.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/4_pc1_ping_isp1.png)

2. **Налаштування VLAN в Data Center
Перевірка зв’язку між серверами**  
![5_ping_serv.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/5_ping_serv.png)

3.  **Зміна маски підмережі на серверах на 255.255.255.192. Перевірка зв’язку між серверами.**

Пінг відсутній через те, що змінилася маска мережі та адреси знаходятся в різних підмережах.
![6_change_mask_ping serv_No_ping.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/6_change_mask_ping%20serv_No_ping.png)

4.  **Зміна приналежністі портів Switch Data Center VLAN. Перевірка зв’язку між серверами. Створення відповідних додаткових VLAN.**  
Пінг відсутній через знаходження сереверів у різних VLAN.
![7_add_vlan_intr_on_switch.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/7_add_vlan_intr_on_switch.png)
![8_create_vlan234_no_ping.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/8_create_vlan234_no_ping.png)

4. **Налаштування маршрутизації між VLAN Data Center switch в режимі trunk**  
![9_f01_trunk.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/9_f01_trunk.png)

5.  **Режим CLI на маршрутизаторі isp3, створено три subinterface і їх
налаштуванно.**   

![10_mod_isp3.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/10_mod_isp3.png)

Перевірка зв’язку між серверами.  

![11_ping_serv_yes.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/02d7171f75582c3271fcac786911c0b5bcf52e07/m3/task3.2/images/11_ping_serv_yes.png)
