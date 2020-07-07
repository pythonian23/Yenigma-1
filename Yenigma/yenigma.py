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

    def crypt(self, plaintext):
        pass

    def encrypt(self, plaintext):
        ciphertext = ""

        for letter in plaintext:
            current = self.alpha.index(letter)
            for rotor in range(len(self.setup[0])):
                current = self.alpha.index(self.setup[0][rotor][current])
            current = self.alpha.index(self.setup[1][current])
            for rotor in range((len(self.setup[0]) - 1), -1, -1):
                current = self.setup[0][rotor].index(self.alpha[current])
            ciphertext += self.alpha[current]
        self.rotate(len(self.setup[0]) - 1)
        return ciphertext  # plugboard check

    def decrypt(self, ciphertext):
        plaintext = ""

        for letter in ciphertext:
            current = self.alpha.index(letter)
            for rotor in range(len(self.setup[0])):
                current = self.alpha.index(self.setup[0][rotor][current])
            current = self.alpha.index(self.setup[1][current])
            for rotor in range((len(self.setup[0]) - 1), -1, -1):
                current = self.setup[0][rotor].index(self.alpha[current])
            plaintext += self.alpha[current]
        self.rotate(len(self.setup[0]) - 1)
        return plaintext  # plugboard check
