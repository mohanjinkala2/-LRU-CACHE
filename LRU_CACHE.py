class double:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.pre=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=None
        self.tail=None
        self.w={}
    def get(self, key: int) -> int:
        if key in self.w:
            node=self.w[key]
            if self.head==node and self.tail==node:
                return node.val
            elif node==self.tail:
                self.tail=node.next
                node.next.pre=None
                node.next=None
                self.head.next=node
                node.pre=self.head
                self.head=node
            elif self.head==node:
                return node.val
            else:
                node.next.pre=node.pre
                node.pre.next=node.next
                node.pre=None
                node.next=None
                self.head.next=node
                node.pre=self.head
                self.head=node
            return node.val
        return -1
    def put(self, key: int, val: int) -> None:
        if key in self.w:
            node=self.w[key]
            node.val=val
            if self.head==node and self.tail==node:
                return
            elif node==self.tail:
                self.tail=node.next
                node.next.pre=None
                node.next=None
                self.head.next=node
                node.pre=self.head
                self.head=node
            elif self.head==node:
                return
            else:
                node.next.pre=node.pre
                node.pre.next=node.next
                node.pre=None
                node.next=None
                self.head.next=node
                node.pre=self.head
                self.head=node  
        else:
            if self.head==None and self.tail==None:
                node=double(key,val)
                self.w[key]=node
                self.head=self.tail=node
            elif len(self.w)<self.capacity:
                node=double(key,val)
                self.w[key]=node
                self.head.next=node
                node.pre=self.head
                self.head=node
            elif len(self.w)>=self.capacity:
                node=double(key,val)
                if self.head==self.tail:
                    del self.w[self.head.key]
                    self.w[node.key]=node
                    self.head=self.tail=node
                    return
                temp=self.tail
                self.tail=self.tail.next
                self.tail.pre=None
                temp.next=None
                del self.w[temp.key]
                self.w[key]=node
                self.head.next=node
                node.pre=self.head
                self.head=node
