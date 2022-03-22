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

