class Enigma:
    import random

    alpha = tuple("abcdefghijklmnopqrstuvwxyz")
    setup = ([[]], [])

    def __init__(self):
        self.gen_key(3, 100)

    def gen_reflect(self, key):
        self.random.seed(key)
        tempAlpha = list(self.alpha)
        output = [0]*26

        for i in range(13):
            tempSet = (tempAlpha.pop(self.random.randint(0, 25-(i*2))), tempAlpha.pop(self.random.randint(0, 24-(i*2))))
            output[self.alpha.index(tempSet[0])] = tempSet[1]
            output[self.alpha.index(tempSet[1])] = tempSet[0]

        return output

    def gen_rotor(self, key):
        self.random.seed(key)
        tempAlpha = list(self.alpha)
        output = []

        for i in range(26):
            tempSet = tempAlpha.pop(self.random.randint(0, 25 - i))
            output.append(tempSet)

        return output

    def gen_key(self, length, lim, set_key=True):
        output = [[]]
        for i in range(length):
            output[0].append(self.random.randint(0, lim))
        output.append(self.random.randint(0, lim))
        if set_key:
            self.set_key(tuple(output))
        return output

    def set_key(self, key):
        setup = []
        for keys in key[0]:
            setup.append(self.gen_rotor(keys))
        self.setup = (setup, self.gen_reflect(key[1]))
        return

    def out_keys(self):
        return self.setup
