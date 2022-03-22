#! Refactorizamos código

class A:
    def value(self):
        return self

    def length(self, t):
        return len(t)

a = A
length = a.value
print(length(a))
aa = a()
print(aa is a())
value = aa.length
print(value(()))
print(a().length((a,)))
print(A.length(aa, (a, value)))
print(aa.length((value,1,'value')))


#! Reescribimos código equivalente para hacerlo más comprensible

class A:
    def value(self):
        return self

    def length(self, t):
        return len(t)

a = A

print(a.value(a))
# Prints the class name and the memory location

instance = a()
print(instance is a())
### Instances memory vary each time they are created. So instance memory is not the same as a() alocation.

print(A.length(()))  # Zero elements tuple, length = 0
print(A.length((a,)))  # One element tuple, length = 1
print(A.length((instance, (a, a.length))))  # Two element tuple (careful with tuple inside the tuple: counts as only one element)
print(A.length(((aa.length, 1, "value"))))  # Three string tuple: length = 3

#? In conclusion:

#? >>> <class>
#? False
#? 0
#? 1
#? 2
#? 3