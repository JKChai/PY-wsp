def datatype_statistic(ls):
     my_list=len(ls)
     print("There are "+str(my_list)+" elements in this list" )
     for item in ls:
        obj[type(item).__name__] = item

obj = {} ## empty dictionary

datatype_statistic([1,'2',3.5, 0.5, None, (1,1)]) 

print(obj) ## output