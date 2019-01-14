#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[9]:


class triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s = (self.a +self.b + self.c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
      
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
obj=triangle(a,b,c)
print("Area of triangle:",obj.area())
 
print()


# 1.2. Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# In[9]:


def filter_long_words(list,n):
    words = []
    for word in list:
        if len(word)>n:
            words.append(word)
    return (words)
print(filter_long_words(['abc','long','filters','rat'],4))



# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# 
# 
# 
# Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[12]:


listOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
print("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))


# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[16]:


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




