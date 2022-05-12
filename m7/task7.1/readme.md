**Task7.1**

**Part1**
**1. Install MySQL server on VM.**
```
ubuntu@ip-172-31-26-144:~$ sudo apt update
ubuntu@ip-172-31-26-144:~$ sudo apt install mysql-server
ubuntu@ip-172-31-26-144:~$ sudo apt install mysql-client
ubuntu@ip-172-31-26-144:~$ mysql --version
mysql  Ver 8.0.29-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))
ubuntu@ip-172-31-26-144:~$ sudo mysql –u root –p
ubuntu@ip-172-31-26-144:~$ sudo mysql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'testsql';
mysql> FLUSH PRIVILEGES;
ubuntu@ip-172-31-26-144:~$ sudo mysql -u root -p
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
```

#create DB
``mysql> CREATE DATABASE exchange_test;``
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| exchange           |
| exchange_test      |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| testDB             |
+--------------------+
7 rows in set (0.00 sec)
```
``mysql> use exchange_test;``
```
Database changed
mysql> CREATE TABLE IF NOT EXISTS `exchange_test`.`usr` (
    ->   `idusr` INT NOT NULL AUTO_INCREMENT,
    ->   `name` VARCHAR(45) NOT NULL,
    ->   `surname` VARCHAR(45) NOT NULL,
    ->   `email` VARCHAR(45) NOT NULL,
    ->   PRIMARY KEY (`idusr`))
    -> ENGINE = InnoDB;
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE IF NOT EXISTS `exchange_test`.`cryptocurrency` (
    ->   `idcryp` INT NOT NULL AUTO_INCREMENT,
    ->   `name` VARCHAR(45) NOT NULL,
    ->   `description` VARCHAR(100) NOT NULL,
    ->   PRIMARY KEY (`idcryp`))
    -> ENGINE = InnoDB;
Query OK, 0 rows affected (0.03 sec)
```
``mysql> show columns from cryptocurrency from exchange_test;``
```
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| idcryp      | int          | NO   | PRI | NULL    | auto_increment |
| name        | varchar(45)  | NO   |     | NULL    |                |
| description | varchar(100) | NO   |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
```
```
mysql> CREATE TABLE IF NOT EXISTS `exchange_test`.`order` (
    ->   `idorder` INT NOT NULL AUTO_INCREMENT,
    ->   `idusr` INT NOT NULL,
    ->   `idcryp` INT NOT NULL,
    ->   `sum` DECIMAL(10,2) NOT NULL,
    ->   PRIMARY KEY (`idorder`),
    ->   INDEX `usr_idx` (`idusr` ASC) VISIBLE,
    ->   INDEX `cryptocur_idx` (`idcryp` ASC) VISIBLE,
    ->   CONSTRAINT `usr`
    ->     FOREIGN KEY (`idusr`)
    ->     REFERENCES `exchange_test`.`usr` (`idusr`)
    ->     ON DELETE CASCADE
    ->     ON UPDATE CASCADE,
    ->   CONSTRAINT `cryptocur`
    ->     FOREIGN KEY (`idcryp`)
    ->     REFERENCES `exchange_test`.`cryptocurrency` (`idcryp`)
    ->     ON DELETE CASCADE
    ->     ON UPDATE CASCADE)
    -> ENGINE = InnoDB;
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+-------------------------+
| Tables_in_exchange_test |
+-------------------------+
| cryptocurrency          |
| order                   |
| usr                     |
+-------------------------+
3 rows in set (0.00 sec)
```
**#add info into tables**
``mysql> INSERT INTO usr (name, surname, email)
    -> VALUES ('Ivan', 'Ivanov', 'ivanov@test.ua');``
```
Query OK, 1 row affected (0.01 sec)```

mysql> INSERT INTO usr (name, surname, email) VALUES ('Petr', 'Petrov', 'petrov@test.ua');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO usr (name, surname, email) VALUES ('Sidor', 'Sidorov', 'sidorov@test.ua');
Query OK, 1 row affected (0.01 sec)

mysql> select * from usr;
+-------+-------+---------+-----------------+
| idusr | name  | surname | email           |
+-------+-------+---------+-----------------+
|     1 | Ivan  | Ivanov  | ivanov@test.ua  |
|     2 | Petr  | Petrov  | petrov@test.ua  |
|     3 | Sidor | Sidorov | sidorov@test.ua |
+-------+-------+---------+-----------------+
3 rows in set (0.01 sec)

mysql> INSERT INTO cryptocurrency (name, description) VALUES ('BTC', 'bitcoin-this is old crypto');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO cryptocurrency (name, description) VALUES ('ETH', 'ethereum-tis is smart contracts');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO cryptocurrency (name, description) VALUES ('DOGECOIN', 'Doge
tis is mem token');
Query OK, 1 row affected (0.01 sec)

mysql> select * from cryptocurrency;
+--------+----------+---------------------------------+
| idcryp | name     | description                     |
+--------+----------+---------------------------------+
|      1 | BTC      | bitcoin-this is old crypto      |
|      2 | ETH      | ethereum-tis is smart contracts |
|      3 | DOGECOIN | Doge tis is mem token           |
+--------+----------+---------------------------------+
3 rows in set (0.00 sec)
```

**Construct and execute SELECT operator with WHERE, GROUP BY and ORDER BY**
``
mysql> select * from usr where name='Sidor';
``
```
+-------+-------+---------+-----------------+
| idusr | name  | surname | email           |
+-------+-------+---------+-----------------+
|     3 | Sidor | Sidorov | sidorov@test.ua |
+-------+-------+---------+-----------------+
1 row in set (0.00 sec)
```

**#инструкция SQL перечисляет число юзеров с одинаковыми именами**
``
mysql> SELECT COUNT(email), name FROM usr GROUP BY name;``
```
+--------------+-------+
| COUNT(email) | name  |
+--------------+-------+
|            1 | Ivan  |
|            2 | Petr  |
|            1 | Sidor |
+--------------+-------+
3 rows in set (0.00 sec)
```

**#инструкция SQL перечисляет число юзеров с одинаковыми именами, отсортированных с высоким до низкого:**
``mysql> SELECT COUNT(idusr), name FROM usr GROUP BY name ORDER BY COUNT(idusr) DESC;``
```
+--------------+-------+
| COUNT(idusr) | name  |
+--------------+-------+
|            2 | Petr  |
|            1 | Ivan  |
|            1 | Sidor |
+--------------+-------+
3 rows in set (0.00 sec)
```

**7. Execute other different SQL queries DDL, DML, DCL.**

``mysql> DELETE FROM usr WHERE email='info@test.com';
Query OK, 1 row affected (0.00 sec)``

**8) Create a database of new users with different privileges. Connect to the
database as a new user and verify that the privileges allow or deny certain
actions.**
**#create new user**
```
mysql> CREATE USER user@localhost IDENTIFIED BY 'abcd';

Query OK, 0 rows affected (0.02 sec)

mysql> CREATE USER 'user2'@'localhost' IDENTIFIED BY 'abcd';
Query OK, 0 rows affected (0.01 sec)
```
**#просмотр прав**
```
mysql> SHOW GRANTS FOR user@localhost;``

+------------------------------------------+
| Grants for user@localhost                |
+------------------------------------------+
| GRANT USAGE ON *.* TO `user`@`localhost` |
+------------------------------------------+
1 row in set (0.00 sec)

ubuntu@ip-172-31-26-144:~$ sudo mysql -u user -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.29-0ubuntu0.20.04.2 (Ubuntu)
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
+--------------------+
1 row in set (0.00 sec)
```
**#предоставление прав SELECT `exchange_test`.`usr`**
```
mysql> GRANT SELECT ON usr TO user@localhost;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW GRANTS FOR user@localhost;
+-------------------------------------------------------------+
| Grants for user@localhost                                   |
+-------------------------------------------------------------+
| GRANT USAGE ON *.* TO `user`@`localhost`                    |
| GRANT SELECT ON `exchange_test`.`usr` TO `user`@`localhost` |
+-------------------------------------------------------------+
2 rows in set (0.00 sec)
```

**#проверим работу SELECT.**
```
mysql> SELECT * FROM usr;
+-------+-------+---------+-----------------+
| idusr | name  | surname | email           |
+-------+-------+---------+-----------------+
|     1 | Ivan  | Ivanov  | ivanov@test.ua  |
|     2 | Petr  | Petrov  | petrov@test.ua  |
|     3 | Sidor | Sidorov | sidorov@test.ua |
+-------+-------+---------+-----------------+
3 rows in set (0.00 sec)
```

**# попытаемся добавить записи  в таблицу;**
```
mysql> INSERT INTO usr (name, surname, email) VALUES ('new', 'new', 'new@test.ua');
ERROR 1142 (42000): INSERT command denied to user 'user'@'localhost' for table 'usr'
```

**#add rule from user use command  INSERT;**
```
mysql> GRANT INSERT ON usr TO user@localhost;
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW GRANTS FOR user@localhost;
+---------------------------------------------------------------------+
| Grants for user@localhost                                           |
+---------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `user`@`localhost`                            |
| GRANT SELECT, INSERT ON `exchange_test`.`usr` TO `user`@`localhost` |
+---------------------------------------------------------------------+
2 rows in set (0.00 sec)
```
**#use command INSERT for user**
```
mysql> INSERT INTO usr (name, surname, email) VALUES ('new', 'new', 'new@test.ua');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM usr;
+-------+-------+---------+-----------------+
| idusr | name  | surname | email           |
+-------+-------+---------+-----------------+
|     1 | Ivan  | Ivanov  | ivanov@test.ua  |
|     2 | Petr  | Petrov  | petrov@test.ua  |
|     3 | Sidor | Sidorov | sidorov@test.ua |
|     5 | new   | new     | new@test.ua     |
+-------+-------+---------+-----------------+
4 rows in set (0.00 sec)
```
**#list all users SQL**
``mysql> SELECT User, Host FROM mysql.user;``

**#delete privilegue**
```
mysql> REVOKE SELECT ON usr FROM user@localhost;
Query OK, 0 rows affected (0.01 sec)
```
**#DELETE user**
```
mysql> DROP user user@localhost;
Query OK, 0 rows affected (0.01 sec)
```

**Part2**

**10.Make backup of your database.**
**#dumpsql**
```
ubuntu@ip-172-31-26-144:~/backupSQL$ sudo mysqldump -u root -p exchange_test > dump.sql
Enter password:
ubuntu@ip-172-31-26-144:~/backupSQL$ ls
dump.sql
```

**#restore dump**
```
sudo mysql -u root -p exchange_test < dump.sql
```

**13.Transfer your local database to RDS AWS. Connect to your database.**
```
[ec2-user@ip-172-30-2-118 ~]$ mysql -h database.c8lldljnaiou.eu-central-1.rds.amazonaws.com -P 3306 -u admin -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 29
Server version: 8.0.28 Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

MySQL [(none)]> create database mydb;
Query OK, 1 row affected (0.01 sec)

MySQL [(none)]> use mydb;
Database changed
MySQL [mydb]> source dump.sql;
Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)


MySQL [mydb]> show tables;
+----------------+
| Tables_in_mydb |
+----------------+
| cryptocurrency |
| order          |
| usr            |
+----------------+
3 rows in set (0.00 sec)

MySQL [mydb]> select * from cryptocurrency;
+--------+----------+---------------------------------+
| idcryp | name     | description                     |
+--------+----------+---------------------------------+
|      1 | BTC      | bitcoin-this is old crypto      |
|      2 | ETH      | ethereum-tis is smart contracts |
|      3 | DOGECOIN | Doge tis is mem token           |
+--------+----------+---------------------------------+
3 rows in set (0.00 sec)
```
**Create the dump of your database.**
```
[ec2-user@ip-172-30-2-118 ~]$ mysqldump -h database.c8lldljnaiou.eu-central-1.rds.amazonaws.com -P 3306 -u admin -p mydb > dummp.sql
Enter password:
[ec2-user@ip-172-30-2-118 ~]$ ls
dummp.sql  dump.sql
```

**PART 3 – MongoDB**

**Create a database. Use the use command to connect to a new database (If it
doesn't exist, Mongo will create it when you write to it).**

```
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.13.0-1022-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed May 11 21:36:45 UTC 2022

  System load:  0.27              Processes:             106
  Usage of /:   18.6% of 7.69GB   Users logged in:       0
  Memory usage: 20%               IPv4 address for eth0: 172.31.27.55
  Swap usage:   0%

1 update can be applied immediately.
To see these additional updates run: apt list --upgradable

```
``ubuntu@ip-172-31-27-55:~$ sudo apt update``
```
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
```
```
ubuntu@ip-172-31-27-55:~$ wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
OK
```
``ubuntu@ip-172-31-27-55:~$ sudo apt-get update``
```
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-backports InRelease
Ign:4 https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 InRelease
Get:5 https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 Release [4417 B]
```
```
ubuntu@ip-172-31-27-55:~$ sudo systemctl start mongod
ubuntu@ip-172-31-27-55:~$ sudo systemctl status mongod
● mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: active (running) since Wed 2022-05-11 21:42:03 UTC; 19s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 2566 (mongod)
     Memory: 67.2M
     CGroup: /system.slice/mongod.service
             └─2566 /usr/bin/mongod --config /etc/mongod.conf
```
```
ubuntu@ip-172-31-27-55:~$ mongosh
Current Mongosh Log ID: 627c2e08cf22478a277bbabd
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.3.1
Using MongoDB:          5.0.8
Using Mongosh:          1.3.1
```
```
test> db
test
```
**Create a collection. Use db.createCollection to create a collection. I'll leave the
subject up to you. Run show dbs and show collections to view your database and
collections.**
```
test> use myNewDatabase
switched to db myNewDatabase
myNewDatabase> db.myCollection.insertOne( { x: 1 } );
{
  acknowledged: true,
  insertedId: ObjectId("627c2e9a5a4d4e15acac13d1")
}
myNewDatabase> db
myNewDatabase
myNewDatabase> use sample_mflix
switched to db sample_mflix
sample_mflix>
```
**Create some documents. Insert a couple of documents into your collection. I'll
leave the subject matter up to you, perhaps cars or hats.**
```
sample_mflix> db.movies.insertMany([
...    {
.....       title: "Jurassic World: Fallen Kingdom",
.....       genres: [ "Action", "Sci-Fi" ],
.....       runtime: 130,
.....       rated: "PG-13",
.....       year: 2018,
.....       directors: [ "J. A. Bayona" ],
.....       cast: [ "Chris Pratt", "Bryce Dallas Howard", "Rafe Spall" ],
.....       type: "movie"
.....     },
...     {
.....       title: "Tag",
.....       genres: [ "Comedy", "Action" ],
.....       runtime: 105,
.....       rated: "R",
.....       year: 2018,
.....       directors: [ "Jeff Tomsic" ],
.....       cast: [ "Annabelle Wallis", "Jeremy Renner", "Jon Hamm" ],
.....       type: "movie"
.....     }
... ])
Browserslist: caniuse-lite is outdated. Please run:
  npx browserslist@latest --update-db
  Why you should do it regularly: https://github.com/browserslist/browserslist#browsers-data-updating
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("627c2fdd5a4d4e15acac13d2"),
    '1': ObjectId("627c2fdd5a4d4e15acac13d3")
  }
}
```

**Use find() to list documents out**
```
sample_mflix> db.movies.find({ "directors": "J. A. Bayona" })
[
  {
    _id: ObjectId("627c2fdd5a4d4e15acac13d2"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'movie'
  }
]
```
**delete data in DB**
```
sample_mflix> db.movies.deleteMany({})
{ acknowledged: true, deletedCount: 2 }
sample_mflix> db.movies.find( {} )
```
