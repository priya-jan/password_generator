#!/usr/bin/env python
# coding: utf-8

# In[2]:


#password generator throgh python
import random 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')','-','+']
print("WELCOME to password generator!!!.....")
n_letters = int(input("How many letters you want to print - "))
n_num = int(input("How many numbers you want to print - "))
n_symbol = int(input("How many Symbols  you want to print - "))
password_list=[]
for i in range (1,n_letters+1):
    char = random.choice(letters)
    password_list+= char
for i in range (1,n_num+1):
    char = random.choice(num)
    password_list+= char
for i in range (1,n_symbol+1):
    char = random.choice(symbol)
    password_list+= char
    password_list+= char    
print(password_list)        # before shuffle'a','b','c','q...z','1','2','3....9','#','@'.....+
random.shuffle(password_list) # after shuffle 'q','!','2','A'...... random and shuffle numbers generate in the list
print(password_list)
password = ""
for  char in password_list:
    password += char
    
print("Your password will be!!!",password)


# In[ ]:





# In[ ]:




