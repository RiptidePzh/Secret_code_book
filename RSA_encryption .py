#!/usr/bin/env python
# coding: utf-8

# In[5]:

### RSA 加密方法，通过产生公钥和私钥实现加密交流
### 如何判断p是不是质数
def isPrime(x):
    from math import sqrt
    m = int(sqrt(x)) + 1
    for i in range(2,m):
        if x%i == 0:
            return False
    return True


# In[38]:


### 产生两个随机质数
def generatePrime(low=3,up=100):
    if low<3 or up<3:
        print("Wrong number!")
    elif low>up:
        up,low=low,up
    else:
        lst=[]
        for i in range(low,up+1):
            if isPrime(i):
                lst.append(i)
    from random import randint
    index = randint(0,len(lst)-1)
    a = lst.pop(index)
    index = randint(0,len(lst)-1)
    b = lst[index]
    return a,b


# In[129]:


### 判断e,N是否互质
def coPrime(e,N):
    if e>N:
        e,N = N,e 
        
    if isPrime(N):
        return True
    elif e==1:
        return True
    elif isPrime(e) and N%e != 0:
        return True
    elif N==e+1:
        return True
    elif N%2==1 and e==N-1:
        return True
    else:
        return False


# In[183]:


### choose e and d
def generate_e(O,N):
    lst=[]
    from random import randint
    for e in range(2,O):
        if coPrime(e,N) and coPrime(e,O):
            lst.append(e)
    e = lst[randint(0,len(lst)-1)]
    return e

def generate_d(e,O):
    n=0
    d=e+1
    while n!=1:
        n = e*d % O
        d += 1
    return d-1


# In[270]:


### 加密
def encryption(s,low=50,up=100):
    lst=[ord(i) for i in s]
    
    p,q = generatePrime(low,up)
    N = p*q
    O = (p-1)*(q-1)
    e = generate_e(O,N)
    d = generate_d(e,O)
    
    for i in range(0,len(lst)): 
        lst[i]=lst[i]**e % N
    
    output=''.join([chr(i) for i in lst])
    print('Your private pin is: p=%d, q=%d, e=%d'%(p,q,e))
    print('Public pin is: d=%d, N=%d'%(d,N))
    return(output)


# In[258]:


### 解码
### 输入密文 d 和 N
def decryption(s,d,N):
    lst=[ord(i) for i in s]
    
    for i in range(0,len(lst)):
        lst[i]=lst[i]**d % N
    
    output=''.join([chr(i) for i in lst])
    print(output)


# In[276]:


ss='Hello World!'


# In[277]:


encryption(ss)


# In[278]:


decryption('۞ߺŻŻဿ\u0c3c\u0ebfဿ్Ż\u087b\u083f',4259,4819)



# In[ ]:




