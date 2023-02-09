#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,5,6]
l


# In[2]:


# now we have to add +1 to each element  so how can we do that?
# one way is as below one by one karigai


# In[3]:


l[0]+1


# In[4]:


l1=[]
l1


# In[5]:


l1.append(l[0]+1)
l1


# In[6]:


l1[0]


# In[7]:


l1[0]+1


# In[8]:


l2=[]
l2


# In[9]:


l2.append(l1[0]+1)
l2


# In[10]:


# but this is a lengthy process take too much time 
# so the same work can be done through loops and that too very fast


# In[11]:


# for loop


# In[12]:


l


# In[13]:


for x in l:
    print(x)


# In[14]:


# what happens  it will  go to list in that to ist index i,e[0]th 
# there it finds 1 when it finds 1 loop has to store it somewhere temporarly
# so it stores it in temporarly with address (x) so x is temporary variable that is why we write for x in list(l)


# In[15]:


# example of error


# In[16]:


for x in l:
    print(l)


# In[17]:


# now the question is we have to add +1 to each element using loop


# In[18]:


for x in l:
    print(x+1)


# In[19]:


# though it added 1 to each element but we need list whose each elemt is added with 1
# so what to do


# In[20]:


l4=[]
for x in l:
    print(x+1)
    l4.append(x+1)
l4

    


# In[21]:


# one ways each string ko nikalo then convert it into upper case fir ic ko list ma lovv  but that is lenthy process


# In[22]:


lx=["sudh","kumar","pwskills","course"]
lx


# In[23]:


l2=[]
for x in lx:
    print(x)
    l2.append(i.upper())
l2


# In[ ]:


# ex no 2


# In[ ]:


l=[1,2,3,4,4,"sudh","kumar",324,34.456,"abc"]
l


# In[ ]:


# question is interger alag  hojaya aur string alag hojaya


# In[ ]:


es kai liya pehlia 2 list banana hai


# In[ ]:


l1


# In[ ]:


l1_num=[]
l2_str=[]
for x in l:
    if type(x)==int or type(x)==float:
        l1_num.append(x)
    else:
        l2_str.append(i)


# In[ ]:


l1_num


# In[ ]:


l2_str


# In[ ]:





# In[ ]:


l1=[1,2,3,4,]
l1


# In[ ]:


for i in l1:
    print(i)


# In[ ]:


for x in range(0,9):
    print(x)
    


# In[ ]:


l2=["sudh","kumar","kridh","naik"]
l2


# In[ ]:


for i in l2:
    if i == "naik":
        break
    print(i)
    else:
    print("do something")


# In[ ]:


l2


# In[ ]:


for i in l2:
    print(i)


# In[ ]:


for i in l2:
    if i== "kumar":
        break
    print(i)


# In[ ]:


for i in l2:
    if i == "kumar":
        break
    print(i)
else:
        print("do something")


# In[ ]:


for i in l2:
    if i == "kumar":
        continue
    print(i)
else:
        print("do something")


# In[ ]:


list(range(9))


# In[ ]:


tuple(range(9))


# In[ ]:


list(range(0,10,1)):
    print(list)
         


# In[ ]:


range(5)


# In[ ]:


list(rangec)


# In[ ]:


l


# In[ ]:


list(range(0,20,2))


# In[ ]:


len(l)


# In[ ]:


list(range(len(l)))
    


# In[ ]:


lx=["sudh","kumar","krish","naik"]
lx


# In[ ]:


for i in lx:
    print(i)


# In[ ]:





# In[ ]:


list(range (5))


# In[ ]:


list(range(0,5,1))


# In[ ]:


list(range(0,20,2))


# In[ ]:


list(range(-10,0))


# In[ ]:


lx


# In[ ]:


len(lx)


# In[ ]:


list(range(len(lx)))


# In[ ]:


for i in range(len(lx)):
    print(lx[i])


# In[ ]:





# In[ ]:


lx


# In[ ]:


len(lx)


# In[ ]:


list(range(len(lx)-1,-1,-1))


# In[ ]:


for i in range(len(lx)-1,-1,-1):
    print(lx[i])


# In[ ]:


lx


# In[ ]:


range(5)


# In[ ]:


list(range(5))


# In[ ]:


list(range(0,5,1))


# In[ ]:


range(0,20,2)


# In[ ]:


list(range(0,20,2))


# In[ ]:


list(range(-10,0))


# In[24]:


lx


# In[25]:


len(lx)


# In[26]:


list(range(len(lx),0))


# In[27]:


list(range(len(lx),0,-1))


# In[28]:


list(range(len(lx)-1,-1,-1))


# In[29]:


for i in range(len(lx)-1,-1,-1):
    print(lx[i])


# In[30]:


for i in [3,2,1,0]:
    print(lx[i])


# In[31]:


lc=[21,3,4,5,6,87,23,45,67,67,]
lc


# In[32]:


len(lc)


# In[33]:


list(range(0,10,2))


# In[34]:


list(range(0,len(lc),2))


# In[35]:


for i in range(0,len(lc),2):
    print(lc[i])


# In[36]:


lt=[2,1,3,4,5,65,6,7,8,9]
lt


# In[37]:


sum(lt)


# In[38]:


result=0
for i in lt:
    result=result+i
result


# In[40]:


t=(2,3,4,5,6,7,8,9,1,0)
t


# In[41]:


sum(t)


# In[42]:


result=0
for i in t:
    result=result+i
result


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




