size = 8
disk_size = 200
 

def CLOOK(arr, head):
     
    seek_count = 0
    distance = 0
    cur_track = 0
 
    left = []
    right = []
 
    seek_sequence = []
 
   
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
        right.sort()
 
  
    for i in range(len(right)):
        cur_track = right[i]
         
        
        seek_sequence.append(cur_track)
 
        
        distance = abs(cur_track - head)
 
        
        seek_count += distance
 
        
        head = cur_track
 
   
    seek_count += abs(head - left[0])
    head = left[0]
 
    
    for i in range(len(left)):
        cur_track = left[i]
 
        
        seek_sequence.append(cur_track)
 
        
        distance = abs(cur_track - head)
 
        
        seek_count += distance
 
        
        head = cur_track
 
    print("Total number of seek operations =",
          seek_count)
    print("Seek Sequence is")
 
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])
 

arr = [ 176, 79, 34, 60,
        92, 11, 41, 114 ]
head = 50
 
print("Initial position of head:", head)
 
CLOOK(arr, head)
 
