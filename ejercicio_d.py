class Test():
    def __init__(self):
        self.logs = 0
        self.archive = open("logs.txt", "r")
        self.archive.write("--Start log--")


    def __del__(self):
        self.archive.write("--End log: {} log(s)--".format(self.logs))

test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada("{}ª llamada".format(i)) 