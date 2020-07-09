from Yenigma import enigma
from Yenigma import yenigma

pb = ("ab", "dg", "ch")

e = enigma.Enigma()

y = yenigma.Yenigma()

y.set_plug(pb)

y.set_key(([1, 2], 3))
y.set_rotation([3, 2])
y.set_base([6, 3])
test = y.encrypt("abc")
print(test)

y.set_key(([1, 2], 3))
y.set_rotation([3, 2])
y.set_base([6, 3])
test = y.decrypt(test)
print(test)

e.set_plug(pb)

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
