"""
Author - Abhijeet Debadwar
"""

reliabiility_sequence32 = [1,2,3,5,9,17,4,6,10,7,18,11,19,13,21,25,8,12,20,14,15,22,27,26,23,29,16,24,28,30,31,32]
import random
import numpy as np

def DefineParam():
    
    N = int(input("Enter Codeword Length: "))
    k = int(input("Enter message Length: "))
    
    return N,k

def makeProper(raw_msg,N,rel_msg_channels):
    
    msg = []
    ind=0
    for i in range(N):
        if(i+1 in rel_msg_channels):
            msg.append(int(raw_msg[ind]))
            ind+=1

        else:
            msg.append(0)

    return msg


def operate(part):
    
    res = []
    
    h = int(len(part)/2)
    
    for i in range(h):
        a = part[i]^part[i+h]
        res.append(a)
        
    res+= part[h:]
        
    return res
        
def Encoder(msg,c,N):
    
    if(c==1):
        return

    else:
        Encoder(msg,int(c/2),N)

        for i in range(int(N/c)):
            msg[i*c:i*c+c] = operate(msg[i*c:i*c+c])
            
            
def ApplyBPSK(codeword):
    
    res = []
    for i in codeword:
        
        if(i==0):
            res.append(1)
        else:
            res.append(-1)
            
    return res

            
def minSum(r1,r2):
    
    L = np.sign(r1)*np.sign(r2)*np.min((abs(r1),abs(r2)))
    
    return L
        
def cal_lbelief(codeword):  
    
    res = []    
    h = int(len(codeword)/2)
     
    for i in range(h):

        f = minSum(codeword[i], codeword[i+h])
        res.append(f)
            
    return res

def cal_rbelief(codeword,correct1):
    
    res = []
    
    h = int(len(codeword)/2)
        
    for i in range(h):
            
        g = codeword[i+h]+((1-2*correct1[i])*codeword[i])
        res.append(g)
            
    return res
   
def combine(a,b):
    
    res = []
    for i in range(len(a)):
        
        temp = a[i]^b[i]
        res.append(temp)
        
    res+=b
    
    return res
                           
def Decoder(codeword, rel_msg_channels,i,decoded):
    
    if(len(codeword)==1):
        i[0]+=1
        
        if(i[0] not in rel_msg_channels):
            decoded[i[0]-1]=0
            return [0]
    
        else:
            if(codeword[0]>=0):
                decoded[i[0]-1]=0
                return [0]

            else:
                decoded[i[0]-1]=1
                return [1]
    
    lbelief = cal_lbelief(codeword)
    correct1 = Decoder(lbelief,rel_msg_channels,i,decoded)
    rbelief = cal_rbelief(codeword,correct1)
    correct2 = Decoder(rbelief,rel_msg_channels,i,decoded)
    
    return combine(correct1,correct2)


def finalDecoding(decoded, rel_msg_channels):
    
    final_dec = []
    
    for j in range(len(decoded)):
        if(j+1 in rel_msg_channels):
            final_dec.append(decoded[j])
            
    return final_dec
