import random

class Random_Generator:
    def random_generator(self, size):
        value = ""
        for i in range(0, size):
            value += str(random.randint(0,9))
        return value 