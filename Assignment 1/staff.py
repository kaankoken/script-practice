from random_generator import Random_Generator as rnd

class Staff:
    def __init__(self, staffId = "", firstName = "", lastName = "", office = "", tel = ""):
        if (len(staffId) > 1):
            self.staffId = staffId
        else:
            self.staffId = rnd.random_generator(self, 6)

        if (len(office) > 1):
            self.office = office
        else:
            self.office = "A-" + rnd.random_generator(self, 3)

        if (len(tel) > 1):
            self.tel = tel
        else:
            self.tel = rnd.random_generator(self, 4)
    
        self.firstName = firstName
        self.lastName = lastName