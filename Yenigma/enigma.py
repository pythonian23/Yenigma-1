class Enigma:
    import random

    alpha = tuple("abcdefghijklmnopqrstuvwxyz")
    setup = ([[]], [])
    rot = []
    plugboard = {}

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

        self.set_rotors()
        return

    def out_set(self):
        return self.setup

    def set_rotors(self):
        self.rot = [0]*len(self.setup[0])
        return

    def rotation_check(self, index):
        while (index != len(self.setup[0]) - 1) and (self.rot[index] >= 26):
            self.rot[index] -= 26
            self.rotate(index + 1)
        return

    def rotate(self, index):
        self.setup[0][index].append(self.setup[0][index].pop(0))
        self.rot[index] += 1
        self.rotation_check(index)
        return

    def set_rotation(self, key):
        for rotor in range(len(key)):
            for iteration in range(key[rotor]):
                self.rotate(rotor)
        return self.rot

    def set_base(self, base):
        for rotor in range(len(base)):
            for iteration in range(base[rotor]):
                self.setup[0][rotor].append(self.setup[0][rotor].pop(0))
        return

    def set_plug(self, sets):
        self.plugboard = {}
        for pair in sets:
            self.plugboard[pair[0]] = pair[1]
            self.plugboard[pair[1]] = pair[0]
        return self.plugboard

    def crypt(self, plaintext):
        ciphertext = ""

        for letter in plaintext:
            current = self.alpha.index(letter)
            try:
                current = self.alpha.index(self.plugboard[self.alpha[current]])
            except KeyError:
                pass
            for rotor in range(len(self.setup[0])):
                current = self.alpha.index(self.setup[0][rotor][current])
            current = self.alpha.index(self.setup[1][current])
            for rotor in range((len(self.setup[0]) - 1), -1, -1):
                current = self.setup[0][rotor].index(self.alpha[current])
            try:
                current = self.alpha.index(self.plugboard[self.alpha[current]])
            except KeyError:
                pass
            ciphertext += self.alpha[current]
            self.rotate(len(self.setup[0]) - 1)
        return ciphertext

    def reset(self):
        self.plugboard = {}
        self.setup = [[], 0]
        self.rot = 0
        return
