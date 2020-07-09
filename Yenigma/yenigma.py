from Yenigma.enigma import Enigma


class Yenigma(Enigma):
    def gen_reflect(self, key):
        self.random.seed(key)
        tempAlpha = list(self.alpha)
        output = [0] * 26

        for i in range(13):
            tempSet = (self.random.randint(0, 25 - (i * 2)), self.random.randint(0, 24 - (i * 2)))
            if tempSet[0] == tempSet[1]:
                tempSet = (tempAlpha.pop(tempSet[0]),) * 2
            else:
                tempSet = tempAlpha.pop(tempSet[0]), tempAlpha.pop(tempSet[1])
            output[self.alpha.index(tempSet[0])] = tempSet[1]
            output[self.alpha.index(tempSet[1])] = tempSet[0]

        return output

    def encrypt(self, plaintext):
        ciphertext = ""
        through = False

        for letter in plaintext:
            current = self.alpha.index(letter)
            try:
                current = self.alpha.index(self.plugboard[self.alpha[current]])
                through = True
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
            if not through:
                self.rotate(len(self.setup[0]) - 1)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        through = False

        for letter in ciphertext:
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
                through = True
            except KeyError:
                pass
            plaintext += self.alpha[current]
            if not through:
                self.rotate(len(self.setup[0]) - 1)
        return plaintext
