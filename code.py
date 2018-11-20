data=[]
m=''
g=''
with open("input.txt", "rb") as text_file:
    for line in text_file:
        data.append(line)
for d in data[0]:
    if(d=='0' or d=='1'):
        m+=d
for d in data[1]:
    if(d=='0' or d=='1'):
        g+=d
def Xor (a,b):
    i=0
    result=''
    while(i<len(a)):
        if(int(a[i])^int(b[i])==1):
            result+='1'
            i=i+1
        else:
             result+='0'
             i=i+1
    return result
def calculateRemainder(m,g):
    #appending zeros to the message 
    for i in range(1,len(g)):
                   m+='0'
    temp1=m[0:len(g)]
    for i in range (len(g),len(m)+1):
        if(temp1[0]=='1'):
            temp2=g
        else:
            temp2='0'
            for j in range(1,len(g)):
                temp2+='0'
        div=Xor(temp1,temp2)
        if(i<len(m)):
             temp1=div[1:]+m[i]
        else:
            temp1=div[1:]
    return temp1
def generator(m,g):
    rem=calculateRemainder(m,g)
    return m+rem
def verifier(m,g):
    rem=calculateRemainder(m,g)
    if(int(rem)==0):
        return "message is correct"
    else:
        return "message is not correct"
def alter(m,bit):
    m_list=list(m)
    if(m_list[bit-1]=='1'):
        m_list[bit-1]='0'
    else:
         m_list[bit-1]='1'
    return "".join(m_list)
def main(m,g):
    result=generator(m,g)
    file = open("result.txt","w") 
    file.write("message:               "+m+'\n')
    file.write("generatorFn:           "+g+'\n')
    file.write("transmitted message:   "+result+'\n')
    file.write("verifier output:       "+verifier(result,g)+'\n')
    bit=input("enter index to alter with")
    alteredMessage=alter(m,bit)
    file.write("altered message by "+str(bit)+"   "+alteredMessage+'\n')
    file.write("verifier output:       "+verifier(alteredMessage,g))
    
    
main(m,g)