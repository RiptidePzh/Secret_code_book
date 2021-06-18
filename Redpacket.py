### 微信抢红包小程序：
### 用户输入一个浮点数amount,以及人数n
### 给每个人分配一个随机金额
import random
def redpacket(amount=0,n=1):
    lst = [0]
    lst2 = []
    digit=max(len(str(amount)),100)
    #使用while 搭配 if not in语句以保证lst中元素不会重复
    while len(lst)<n: 
        x = random.randint(1,amount*digit)
        if x not in lst:
            lst.append(x)
    #将lst从小到大排序
    lst.sort()
    lst.append(amount*digit)
    #用减法实现随机数的生成
    for i in range(len(lst)-1):
        lst2.append((lst[i+1]-lst[i])/(digit))
        
    return lst2
### 这个程序的核心逻辑是：
### 如果我要生成x1+x2+x3=1的随机数
### 那么应该首生成三个独立的随机数 y1<y2<y3=1
### 令 x1 = y1 ; x2 = y2 - y1; x3 = y3 - y2
### 这样就能够保证 x1 + x2 + x3 = 1 了

### 第二个技巧是如何控制随机数的位数
### 例如我们希望保留0.01位
### 那么我们可以在randint中令上限乘以100，生成整数
### 在最后加入列表的时候除以100，就可以保证都是百分位了
