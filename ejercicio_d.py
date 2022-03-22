class Test():
    def __init__(self):
        self.logs = 0
        self.file = open("logs.txt", "w")
        self.file.write("--Start log--\n")

    def llamada(self, text):
        self.file.write(text)
        self.logs += 1

    def __del__(self):
        self.file.write("--End log: {} log(s)--".format(self.logs))
        self.file.close()

test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada\n") 
   else: 
       test.llamada("{}ª llamada\n".format(i)) 