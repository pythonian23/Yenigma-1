from Yenigma import enigma
from Yenigma import yenigma

e = enigma.Enigma()

y = yenigma.Yenigma()

y.set_key(([1, 2], 3))
y.set_rotation([3, 2])
y.set_base([6, 3])
test = y.crypt("abc")
print(test)

y.set_key(([1, 2], 3))
y.set_rotation([3, 2])
y.set_base([6, 3])
test = y.crypt(test)
print(test)

e.set_key(([1, 2], 3))
e.set_rotation([3, 2])
e.set_base([6, 3])
test = e.crypt("abc")
print(test)
e.set_key(([1, 2], 3))
e.set_rotation([3, 2])
e.set_base([6, 3])
test = e.crypt(test)
print(test)
