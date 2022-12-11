# Python3 program to count number if sink nodes
  
# Return the number of Sink NOdes. 
def countSink(n, m, edgeFrom, edgeTo):
      
    # Array for marking the non-sink node. 
    mark = [0] * (n + 1)
  
    # Marking the non-sink node.
    for i in range(m):
        mark[edgeFrom[i]] = 1
  
    # Counting the sink nodes. 
    count = 0
    for i in range(1, n + 1):
        if (not mark[i]): 
            count += 1
  
    return count
  
# Driver Code
if __name__ == '__main__': 
      
    n = 4
    m = 2
    edgeFrom = [2, 4] 
    edgeTo = [3, 3]
  
    print(countSink(n, m, edgeFrom, edgeTo))