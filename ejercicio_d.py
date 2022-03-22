class Test()


test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada("{}ª llamada".format(i)) 