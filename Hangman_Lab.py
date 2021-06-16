#!/usr/bin/env python
# coding: utf-8

# In[26]:


### 1.载入package
import re
import random
import time


# In[64]:



LINES = '''         ______
        |  |
        |  
        | 
        |  
        |  
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | 
        |  
        | 
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | /
        |  
        | 
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | /|
        |  |
        |  
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | /|\ 
        |  |
        |  
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | /|\ 
        |  |
        | /  
        |_____
        |     |____
        |__________|
         ______
        |  |
        |  O
        | /|\ 
        |  |
        | / \ 
        |_____
        |     |____
        |__________|

'''


# In[29]:


### 2.取随机单词
def randword():
    wd = open('words.txt')
    wd_str = wd.read()
    wd.close()
    
    wd_box = re.split(' ',wd_str)
    wd_chs = wd_box[random.randint(0,len(wd_box))]
    return wd_chs


# In[191]:


### 3.玩家输入
def guess(gslst,failure=0):
    print('mistakes:',failure,'')
    gs=input('Guess: ')
    
    gslst.append(gs)
    print('Your guessing order:','\n'+''.join(gslst))
    return (gs,gslst)


# In[192]:


### 4.判断猜测是否正确
def judge(gs,wd,lines,failure=0,success=0):
    n = len(wd)
    lst=list(lines)
    index=0
    for i in range(0,n-1):
        if gs==wd[i] and gs!=lst[i]:
            lst[i] = gs
            index=1
        elif gs==lst[i]:
            index=2
        
            
    if index==0:
        failure += 1
    elif index==1:
        success += 1
    else:
        print('repeated! Try another letter.'.center(20))
    
    return(''.join(lst),failure,success)


# In[96]:


### 5.输出
def print_hangman(disply='',mistakes = 0):
    '''
    print hangman : from 0 (hang) to 6 (hanged)
    '''

    lines = LINES.split('\n')
    start = mistakes * 9
    for line in lines[start: start+4]:
        print('%-30s%-20s'%(' ',line))
    print('%-30s%-20s'%(disply,lines[start+4]))
    for line in lines[start+5:start+9]:
        print('%-30s%-20s'%(' ',line))


# In[151]:


###  6.切换
def switch(success=0,failure=0):
    num = failure + success
    ss = '----------------------  '+ str(num) + '  ----------------------\n'
    print('\n\n',ss.center(50))


# In[200]:


### 主体部分
### 初始化代码
def hangman():
    wd = randword()
    failure = 0
    success = 0
    lines=len(wd)*'_'
    gslst=[]
    pl=re.sub('',' ',lines)
    switch()
    ### 初始化文件
    st_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f=open('Guess.csv','a+')
    f.write(str(st_time)+','+wd+',')

    while failure<6 and success<len(wd):
    
        st_time=time.time() ###计时开始
        gs,gslst = guess(gslst,failure)
        
        lines,failure,success = judge(gs,wd,lines,failure,success)
        pl=re.sub('',' ',lines)
        print_hangman(pl,failure) 
        switch(success,failure)
        ed_time=time.time()-st_time ###计时结束
        f.write(gs+','+str(ed_time)+',')

    f.write(''.join(gslst)+','+' round end\n') 
    if failure==6:
        lines='YOU LOSE!'
        print_hangman(lines,6)
        print('\nThe correct answer is: ',wd)

    elif success==len(wd):
        lines='YOU WIN!'
        print_hangman(lines,failure)
        print('\nCongratulations! The word is: ',wd)


# In[203]:


### 运行部分
c='y'
while c=='y':    
    hangman()
    c=input('Try again?[y/n]')


# In[ ]:




