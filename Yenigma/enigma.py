class Enigma:
    import random

    alpha = tuple("abcdefghijklmnopqrstuvwxyz")
    setup = ([{}], {})

    def __init__(self):
        self.gen_key(3, 100)

    def gen_reflect(self, key):
        self.random.seed(key)
        tempAlpha = list(self.alpha)
        output = {}

        for i in range(13):
            temp = (tempAlpha.pop(self.random.randint(0, len(tempAlpha)-1)),
                    tempAlpha.pop(self.random.randint(0, len(tempAlpha)-1)))
            output[temp[0]] = temp[1]
            output[temp[1]] = temp[0]
        return output

    def gen_rotor(self, key):
        self.random.seed(key)
        tempAlpha = list(self.alpha)
        output = {}

        for keys in self.alpha:
            output[keys] = tempAlpha.pop(self.random.randint(0, len(tempAlpha)-1))
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


class Yenigma(Enigma):
    import random
    del random


if __name__ == "__main__":
    e = Yenigma()
