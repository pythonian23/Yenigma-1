from Yenigma import enigma

e = enigma.Enigma()

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
