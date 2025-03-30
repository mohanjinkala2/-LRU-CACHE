# **INTRODUTION**:

Designed a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# **IMPLEMENTATION**:

 To implement This, Here We Used Doubly Linked List And Hash Map
 
 # **STEPS**:
 
  1)Implement the LRUCache class which contain:
  
     i)LRUCache(int capacity): Initialize the LRU cache with positive size capacity. # capacity is a attribute of lrucache class
     
     ii)int get(int key) Return the value of the key if the key exists, otherwise return -1. # get is a method of lrucache class
     
     iii)void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
   the capacity from this operation, evict the least recently used key.  # put is a method of lrucache class
   
  2)create Doubly linked class which contain:
     i)value(int)
     ii)Next node
     iii)previous node
  3)create a object for lrucache class by passing capacity.
  4)perform put operation on Lrucache by placing key in doubly linked list.
    i)if hash map is null and  length of hash map is less then capacity then create a doubly linked node as node1 by passing key value.initialize 
    head<=node1,tail<=node1.
    ii)if hash map is not null and length of hash map is less then capacity and  there is no key present in hash map then create a doubly linked node as node1 by 
    passing key value.initialize node1.next<=head,head.previous<=node1,head<=node1.
    iii)if length of hash map is greater then capacity and  there is no key present in hash map then perform tail=tail.previous,tail.next=null.and then create a 
    doubly linked node as node1 by passing key value.initialize node1.next<=head,head.previous<=node1,head<=node1.
  5)perform get key value operation on Lrucache.
     i)if key is not present in hash map.return null.
     2)if key present in hash map then return key value.initialize this key as head.
     
  # **RESULT/USES**:
  
    RESULT/USES:Least Recently Used (LRU) cache is used in real life to improve performance, reduce latency, and
    optimize resource usage.EXAMPLES:1)Virtual Memory Paging– OS uses LRU to manage RAM, keeping frequently
    used pages in memory and discarding the least used ones.This improves speed of accessing Memory as CPU first
    Search in Cache for required data ,if it is not present in cache then it goes to RAM, if required data is not present in
    RAM then it goes to MAIN MEMORY.So if cpu move from cache->main memory accessing time increases and
    reduces performance,so we need to store data in cache or Ram by following LRU Priniciple to remove Least used data
    from cache if any new data is access by cpu,by removing least used data we can now store new data.
    
  # **EXAMPLE**:
  
    Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output:[null, null, null, 1, null, -1, null, -1, 3, 4]
    
  # **Explanation**:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
