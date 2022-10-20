def findChecksum(SentMessage, k):
   
    
    c1 = SentMessage[0:k]
    c2 = SentMessage[k:2*k]
    c3 = SentMessage[2*k:3*k]
    c4 = SentMessage[3*k:4*k]
 
    
    Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]
 
    
    if(len(Sum) > k):
        x = len(Sum)-k
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < k):
        Sum = '0'*(k-len(Sum))+Sum
 
    
    Checksum = ''
    for i in Sum:
        if(i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
    return Checksum
 


def checkReceiverChecksum(ReceivedMessage, k, Checksum):
   
    
    c1 = ReceivedMessage[0:k]
    c2 = ReceivedMessage[k:2*k]
    c3 = ReceivedMessage[2*k:3*k]
    c4 = ReceivedMessage[3*k:4*k]
 
    
    ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) +
                      int(c3, 2)+int(c4, 2)+int(Checksum, 2))[2:]
 
    
    if(len(ReceiverSum) > k):
        x = len(ReceiverSum)-k
        ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]
 
   
    ReceiverChecksum = ''
    for i in ReceiverSum:
        if(i == '1'):
            ReceiverChecksum += '0'
        else:
            ReceiverChecksum += '1'
    return ReceiverChecksum
 
 

SentMessage = "10010101011000111001010011101100"
k = 8

ReceivedMessage = "10010101011000111001010011101100"

Checksum = findChecksum(SentMessage, k)
 

ReceiverChecksum = checkReceiverChecksum(ReceivedMessage, k, Checksum)
 

print("SENDER SIDE CHECKSUM: ", Checksum)
print("RECEIVER SIDE CHECKSUM: ", ReceiverChecksum)
finalsum=bin(int(Checksum,2)+int(ReceiverChecksum,2))[2:]
 

finalcomp=''
for i in finalsum:
    if(i == '1'):
        finalcomp += '0'
    else:
        finalcomp += '1'
 

if(int(finalcomp,2) == 0):
    print("Receiver Checksum is equal to 0. Therefore,")
    print("STATUS: ACCEPTED")
     

else:
    print("Receiver Checksum is not equal to 0. Therefore,")
    print("STATUS: ERROR DETECTED")
