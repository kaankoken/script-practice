from file import File

class Main(File):
    # To print the staff room list and print it to the file
    def displayAndPrintStaff(self, staff):
        open("staff_list.txt", 'w').close()
        print("\nStaff Room List\n----------------\nStaff ID\tFirst Name\tLast Name\t\tOffice\tTel")
        
        self.write_file("staff_list.txt", "Staff ID\tFirst Name\tLast Name\tOffice\tTel\n")
        
        for s in staff:
            print("{}\t\t{}\t\t{}\t\t\t{}\t{}".format(s.staffId,s.firstName,s.lastName,s.office,s.tel))
            self.write_file("staff_list.txt", "{}\t{}\t{}\t{}\t{}\n" .format(s.staffId,s.firstName,s.lastName,s.office,s.tel))

    # To print the animal feeding record with feeding details and print it to the file
    def displayAndPrintFeeding(self, f):
        print("{}\t\t\t{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t\t{} {}".format(f.date.strftime("%d/%m/%Y"),f.time.strftime("%H:%M"),f.foodName,f.manufacturer,f.weight,f.staffName,f.staffSurname))
        self.write_file("feeding_record.txt", "\n{}\t{}\t{}\t{}\t{}\t{} {}".format(f.date.strftime("%d/%m/%Y"),f.time.strftime("%H:%M"),f.foodName,f.manufacturer,f.weight,f.staffName,f.staffSurname))

    # To print the animal record card with animal details and print it to the file
    def displayAndPrintAnimal(self, aNo, animal):
        print("\nAnimal Record Card\n-------------------\n*Animal Information*\nAnimal No: {}".format(aNo))
        self.write_file("observation_record.txt", "Animal Information\nAnimal No: {}".format(aNo))
        for a in animal:
            if a.animalNo == aNo:
                print("Gender: {}\nBirth date: {}\nColour: {}\n*Environment Conditions*\nRelative Humidity: {}\nEnclosure Size(m^2): {}\nTemperature: {}\nHours of light per day: {}".format(a.gender, a.birthDate.strftime("%d/%m/%Y"), a.colour,a.conditions.humidity,a.conditions.enclosureSize,a.conditions.temperature, a.conditions.light))
                self.write_file("observation_record.txt", "Gender: {}\nBirth Date: {}\nColour: {}\nEnvironment Conditions\nRelative Humidity: {}\nEnclosure Size(m^2): {}\nTemperature: {}\nHours of light per day: {}" .format( a.gender, a.birthDate, a.colour,a.conditions.humidity,a.conditions.enclosureSize,a.conditions.temperature, a.conditions.light))

    # To print the animal record card with animal details and print it to the file
    def displayAndPrintObservation(self, o):
        print("{}\t\t{}\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{} {}" .format(o.date.strftime("%d/%m/%Y"),o.time.strftime("%H:%M"),o.weight,o.temperature,o.note,o.staffName,o.staffSurname))
        self.write_file("observation_record.txt", "\n{}\t{}\t{}\t{}\t{}\t{} {}" .format(o.date.strftime("%m/%d/%Y"),o.time.strftime("%H:%M"),o.weight,o.temperature,o.note,o.staffName,o.staffSurname))

    # To be able to check on whether there is an animal with this No
    def isAnimal(self, num, animal):
        for a in animal:
            if num == a.animalNo:
                return True
        return False

    # To be able to check on whether there is a staff with this name and surname
    def isStaff(self, name, surname, staff):
        for s in staff:
            if name == s.firstName and surname == s.lastName:
                return True
        return False

    # To be able to check on whether there is a food with this name and manufacturer
    def isFood(self, name, man, food):
        for f in food:
            if name == f.food_name:
                if f.manufacturer == man:
                    return True
        return False

    # To check the feeding count
    def feed_count(self, animal_no, date, feeding):
        count = 0
        for i in feeding:
            if (animal_no == i.animalNo and date == i.date):
                count += 1

        if count <= 1:
            return True
        else:
            return False

    # To check the observation count      
    def observation_count(self, animal_no, date, observation):
        count = 0
        for i in observation:
            if (animal_no == i.animalNo and date == i.date):
                count += 1

        if count < 3:
            print("An animal should not be fed more than two times in a day and should be observed more than three times in a day. Your current observation count is: {}".format(count))

    # To check whether the input entered is valid
    def input_number(self, prompt, isFloat):
        while True:
            try:
                if isFloat:
                    return float(input(prompt))
                return int(input(prompt))
            except ValueError:
                print("Please enter a number with correct format!")
