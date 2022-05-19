**Task8.1**

**1. Write easy program, which will display current date and time.**
```
from datetime import datetime
# Current date time in local system
print(datetime.now())
```
![1.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/1.png)
**2. Write python program, which will accept comma-separated numbers, and then it
should write tuple and list of them:  
Enter numbers: 1, 2, 7, 43, 9  
Output:  
List: [‘1’, ‘2’, ‘7’, ‘43’, ‘9’]  
Tuple: (‘1’, ‘2’, ‘7’, ‘43’, ‘9’)**  
```
list = []
num = ''
while len(list) < 5:
    num = input("Please, enter only number: ")
    list.append (num)
print(list, type (list))
tuple = tuple (list)
print (tuple, type(tuple))
```
![2.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/2.png)
**3. Write python program, which will ask file name. File should be read, and only even
lines should be shown.**
```
# open file in read mode
fn = open('demofile.txt', 'r')
# open other file in write mode
fn1 = open('output.txt', 'w')
# read the content of the file line by line
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
	if(i % 2 != 0):
		fn1.write(cont[i])
	else:
		pass
# close the file
fn1.close()
# open file in read mode
fn1 = open('nfile.txt', 'r')
# read the content of the file
cont1 = fn1.read()
# print the content of the file
print(cont1)
# close all files
fn.close()
fn1.close()
```
![3.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/3.png)
**4. Write python program, which should read html document, parse it, and show it’s
title.**
```
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://code.visualstudio.com/docs/python/python-tutorial')
bs = BeautifulSoup(html.read(), 'html.parser')
title = bs.find_all('title')
for t in title:
    print(t.get_text())
```
![4.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/4.png)
**5. Write python program, which will parse user’s text, and replace some emotions with
emoji’s (Look: pip install emoji)**
```
import emoji
text = input ('Please enter someting sentences with consists a words dog, cat , bird, book, sun : ')
word_replace = {'bird': ':bird:',
                   'cat': ':cat_face:',
                   'dog': ':dog_face:',
                   'book': ':open_book:',
                   'sun': ':sun:'}
# Iterate over all key-value pairs in dictionary
for key, value in word_replace.items():
# Replace key character with value character in string
text = text.replace(key, value)
print (emoji.emojize(text))
```
![5.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/5.png)
**6. Write program, that will show basic PC information (OS, RAM amount, HDD’s, and
etc.)**
```
import platform
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
```
![6.png](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/90e5f80f4e184f8c6dc4e6ace5ce0277f5fada12/m8/task8.1/images/6.png)
