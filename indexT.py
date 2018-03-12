from index import Index

I = Index(1)
I.register(["page","news","recent","newB"],2)
I.register(["page","news","hot","newA"],0)
I.register(["page","games","zelda"],3)
I.register(["users","space"],5)
I.register(["admin","users"],4)

print("\nRaw index:\n",I.root_dict)
print("\nTree:\n"+I.tree().__str__())
print("\nTest search:\n",I.search("users"))
print("\nGet objection:\n",I.get(I.search("users")[1])) 
#Caution. Sometimes the order of list can be changed