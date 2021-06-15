### 一个随机字典替换加密法

def dic_code(ss,seed=1):
    ### import random and set seed
    import random
    random.seed(seed)
    
    ### create two list
    ### from A-Za-z
    ### lst2 is shuffled randomly
    lst1=[]
    lst2=[]
    for i in range(65,65+26,1):
        lst1.append(chr(i))
        lst2.append(chr(i))
    for i in range(97,97+26,1):
        lst1.append(chr(i))
        lst2.append(chr(i))
        
    random.shuffle(lst2)
    
    ### return a global var. dic_pin for uncode
    global dic_pin 
    dic_pin = dict(zip(lst1,lst2))
    
    ### replace the word in ss into random text
    ### symbols and space will stay
    otlst=[]
    for i in ss:
        if(i in d.keys()):
            otlst.append(d[i])
        else:
            otlst.append(i)
    otlst=''.join(otlst)        
    return otlst
  
  
  
  ### example here:
  ss = '''
What Is June Anyway?
BY DAVID BUDBILL
After three weeks of hot weather and drought,
           we've had a week of cold and rain,
just the way it ought to be here in the north,
            in June, a fire going...
'''
  dic_code(ss)
  >>> "\ngsif jc FHGS xGkEik?\nJZ WxyjW JMWJjzz\nxOfSe fseSS ESSqc NO sNf ESifsSe iGD DeNHRsf,\n           ES'QS siD i ESSq NO hNBD iGD eiAG,\nbHcf fsS Eik Af NHRsf fN KS sSeS AG fsS GNefs,\n            AG FHGS, i OAeS RNAGR...\n"
  
  dic_uncode(dic_code(ss),dic_pin)
  >>>
  What Is June Anyway?
  BY DAVID BUDBILL
  After three weeks of hot weather and drought,
            we've had a week of cold and rain,
  just the way it ought to be here in the north,
              in June, a fire going...
