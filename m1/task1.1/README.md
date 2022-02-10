**task1.1**
1. Try training https://learngitbranching.js.org/  Done
2. ```git --version```
3. ```git config --global user.name "Ivan Lovkin"```
4. ```git config --global user.email "terra144481@gmail.com"```
5. ```git config -l```
6. create account on github, private repo  - **https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2**
7. Using public ssh key for auth on github.
8. ```git clone git@github.com:terra144481/DevOps_online_Odessa_2022Q1Q2.git```
9. ```mkdir task1.1```
10. ```echo "" > readme.txt```
11. ``git add .``
12. ```git commit -m "create readme.txt file"```
13. ```git status```
14. ```git checkout -b develop```
15. ```echo "" > index.html```
16. ```git add .```
17. ```git commit -m "create index.html file"```
18. ```git status```
18. ```git checkout -b images```
19. ```mkdir images``` add 3 files to folder images
20. ```git add .```
21. ```git commit -m "add some images to dir images"```
22. ```git status```
23. ```cat index.html``` , modify index.html
22. ```git add .```
23. ```git commit -m "change index.html"```
24. ```git status```
25. ```git checkout develop```
26. ```git checkout -b styles```
27. ```notepad styles.css```
28. ```git add .```
29. ```git commit -m "add styles.css file"```
30. ```git status```
31. ```notepad index.html```
32. ```cat index.html```
33. ```git add .```
34. ```git commit -m "modify index.html"```
35. ```git checkout develop```
36. ```git merge images```  
Updating 6454900..ff45ad3  
Fast-forward  
 task1.1/images/235789_600.jpg | Bin 0 -> 7055 bytes  
 task1.1/images/english.jpg    | Bin 0 -> 33740 bytes  
 task1.1/images/pupil.jpg      | Bin 0 -> 30743 bytes  
 task1.1/index.html            | Bin 6 -> 266 bytes   
 4 files changed, 0 insertions(+), 0 deletions(-)  
 create mode 100644 task1.1/images/235789_600.jpg  
 create mode 100644 task1.1/images/english.jpg  
 create mode 100644 task1.1/images/pupil.jpg  
37. ```git merge styles```  
warning: Cannot merge binary files: task1.1/index.html (HEAD vs. styles)  
Auto-merging task1.1/index.html  
CONFLICT (content): Merge conflict in task1.1/index.html  
Automatic merge failed; fix conflicts and then commit the result.
38. modify index.html
39. ```git add .```
40. ```git commit -m "fix bug merge"```
41. ```git status```
42. ```git checkout main```
43. ```git merge develop```
44. ```git log```
45. ```git push origin --all```
46. ```git reflog```
47. create file [task1.1_GIT.txt](https://github.com/terra144481/DevOps_online_Odessa_2022Q1Q2/blob/main/m1/task1.1_GIT.txt)  
***
***What is DevOps?***
> DevOps is a beautiful and inexhaustible world of automation. First you have a work, then the machine has a work. So, but you learning some new technology now. You implement it. Learning - using - debuging - learning. There are no boundaries for perfection. It's all called DevOps!  
***
