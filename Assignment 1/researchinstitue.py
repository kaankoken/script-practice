import sys
from staff import Staff
from animal import Animal
from food import Food
from enviroinment_condition import EnvironmentConditions
from feeding import Feeding
from observation import Observation

from file import File
from date_time import Date_Time
from main import Main

# Main function
def main(argv, argc):
    # Helper Classes
    file_operations = File()
    date_time_operations = Date_Time()
    main_operations = Main()
    
    file = []

    # Lists we hold to manage our objects in main
    staff = []
    food = []
    animal = []
    observation = []
    feeding = []

    if argc > 1:
        file.extend(file_operations.read_file(argv[1]))
        for i in file:
            i = file_operations.load_file(i)
            for j in i:
                if j.__class__.__name__ == "Animal":
                    animal.append(j)
                elif j.__class__.__name__ == "Food":
                    food.append(j)
                elif j.__class__.__name__ == "Staff":
                    staff.append(j)
                elif j.__class__.__name__ == "Observation":
                    observation.append(j)
                else:
                    feeding.append(j)
    else:
        app_name = input("Enter a app name (default name: app): ")
        if (len(app_name) < 1):
            app_name = "app.txt"
        else:
            app_name += ".txt"

        sys.argv.append(app_name)

    # To create application menu 
    choice = 0
    while choice != 7:
        print("\nWelcome to application!\n1. Add a new staff\n2. Add a new animal along with the environment conditions\n3. Add a new food\n4. Add a report of animal feeding\n5. Add a report of animal observation\n6. Show reports\n7. EXIT")
        choice = main_operations.input_number("\nEnter choice: ", False)
        while choice < 1 or choice > 7:
            print("Please choose a number between the 1 and 7.")
            choice = main_operations.input_number("\nEnter choice: ", False)

        # To add a new staff
        if choice == 1:
            fname = input("Enter name: ")
            surname = input("Enter surname: ")
            staff.append(Staff(firstName=fname, lastName=surname))
            print("{} {} is added successfully.\nStaff ID: {}\nOffice: {}\nTel: {}".format(fname, surname, staff[-1].staffId, staff[-1].office,staff[-1].tel))

        # To add a new animal along with the environment conditions
        elif choice == 2:
            gender = input("Enter gender: ")
            birthDate = date_time_operations.validate_date("Enter birth date (dd/mm/yyyy): ")
            colour = input("Enter colour: ")
            weight = main_operations.input_number("Enter weight(kg): ", True)
            humidity = main_operations.input_number("Enter relative humidity: ", False)
            enclosureSize = main_operations.input_number("Enter enclosure size: ", False)
            temperature = main_operations.input_number("Enter temperature: ", True)
            light = main_operations.input_number("Enter hours of light per day: ", False)

            env = EnvironmentConditions(humidity, enclosureSize, temperature,light)
            animal.append(Animal(gender=gender,birthDate=birthDate,colour=colour,weight=weight,conditions=env))

            print("Animal is added successfully.\nAnimal No: {}".format(animal[-1].animalNo))

        # To add a new food
        elif choice == 3:
            food_name = input("Enter food name: ")
            manufacturer = input("Enter manufacturer of food: ")
            food.append(Food(foodName=food_name, manufacturer=manufacturer))
            print("Food is added successfully.")

        # To add a report of animal feeding
        elif choice == 4:
            animalNo = input("Enter animal no: ")
            if main_operations.isAnimal(animalNo, animal):
                fDate = date_time_operations.validate_date("Enter date (dd/mm/yyyy): ")
                if main_operations.feed_count(animalNo, fDate, feeding) and date_time_operations.checkDate(animalNo, fDate, animal):
                    fTime = date_time_operations.validate_time("Enter time (hh:mm): ")
                    if date_time_operations.check_time(animalNo, fDate, fTime, feeding):
                        foodName = input("Enter food name: ")
                        manufacturer = input("Enter manufacturer name: ")
                        if main_operations.isFood(foodName, manufacturer, food):
                            weight = main_operations.input_number("Enter weight(gr): ", False)
                            staffName = input("Enter staff name: ")
                            staffSurname = input("Enter staff surname: ")
                            if main_operations.isStaff(staffName, staffSurname, staff):
                                feeding.append(Feeding(animalNo=animalNo,date=fDate,time=fTime,foodName=foodName,manufacturer=manufacturer,weight=weight,staffName=staffName,staffSurname=staffSurname))
                                print("\nFeeding report is added successfully.")
                            else:
                                print("\nThis staff does not exist.")
                        else:
                            print("\nThis food with this manufacturer does not exist.")
                else:
                    print("\nYou can not add a report of animal feeding. Because an animal should not be fed more than two times in a day or please check your date to feeding.")
            else:
                print("\nThis animal does not exist.")

        # To add a report of animal observation
        elif choice == 5:
            animalNo = input("Enter animal no: ")
            if main_operations.isAnimal(animalNo, animal):
                oDate = date_time_operations.validate_date("Enter date (dd/mm/yyyy): ")
                if date_time_operations.checkDate(animalNo, oDate, animal):
                    oTime = date_time_operations.validate_time("Enter time (hh:mm): ")
                    if date_time_operations.check_time(animalNo, oDate, oTime, observation):
                        weight = main_operations.input_number("Enter weight(kg): ", True)
                        temp = main_operations.input_number("Enter temperature: ", True)
                        note = input("Enter note: ")
                        staffName = input("Enter staff name: ")
                        staffSurname = input("Enter staff surname: ")
                        if main_operations.isStaff(staffName, staffSurname, staff):
                            observation.append(Observation(animalNo=animalNo,date=oDate,time=oTime,weight=weight,temperature=temp,note=note,staffName=staffName,staffSurname=staffSurname))
                            print("\nObservation report is added successfully.")
                            main_operations.observation_count(animalNo, oDate, observation)
            else:
                print("\nThis animal does not exist.")

        # To show reports
        elif choice == 6:
            main_operations.displayAndPrintStaff(staff)
            aNo = input("\nEnter animal no for feeding details: ")
    
            if main_operations.isAnimal(aNo, animal):
                datetime_start = date_time_operations.validate_date("Enter start date for feeding details (dd/mm/yyyy): ")
                datetime_end = date_time_operations.validate_date("Enter end date for feeding details (dd/mm/yyyy): ")
                open("feeding_record.txt", 'w').close()
                print("\nAnimal Feeding Record\n----------------------\nAnimal No: {}\nDate\t\t\t\tTime\t\tFood Name\tManufacturer\tWeight(gr)\t\t\t\tStaff".format(aNo))
                file_operations.write_file("feeding_record.txt", "Animal No: {}\nDate\tTime\tFood Name\tManufacturer\tWeight(gr)\tStaff".format(aNo))
                for f in feeding:
                    if f.animalNo == aNo and date_time_operations.compareDates(datetime_end, datetime_start, feeding):
                        if date_time_operations.isBetweenDates(datetime_start, datetime_end, f):
                            main_operations.displayAndPrintFeeding(f)
            else:
                print("\nThis animal does not exist.")

            open("observation_record.txt", 'w').close()
            main_operations.displayAndPrintAnimal(aNo, animal)
            print("Date\t\t\tTime\t\tAnimal Weight(kg)\tTemperature(C)\tNote\t\t\tStaff")
            file_operations.write_file("observation_record.txt", "\nDate\tTime\tAnimal Weight(kg)\tTemperature(C)\tNote\tStaff")
            status = False
            for o in observation:
                if o.animalNo == aNo and date_time_operations.compareDates(datetime_end,datetime_start, feeding) :
                    if date_time_operations.isBetweenDates(datetime_start, datetime_end, o):
                        main_operations.displayAndPrintObservation(o)
                        status = True
            if not status:
                print("\nThere is no record between these dates for animal feeding or observation record.")        

                  

        # To exit and writes to application txt  
        else:
            open(argv[1], 'w').close()
            if len(staff) > 0:
                dump = file_operations.dump_file(staff)
                file_operations.write_byte_file(argv[1], dump)

            if len(food) > 0:
                dump = file_operations.dump_file(food)
                file_operations.write_byte_file(argv[1], dump)

            if len(animal) > 0:
                dump = file_operations.dump_file(animal)
                file_operations.write_byte_file(argv[1], dump)

            if len(observation) > 0:
                dump = file_operations.dump_file(observation)
                file_operations.write_byte_file(argv[1], dump)

            if len(feeding) > 0:
                dump = file_operations.dump_file(feeding)
                file_operations.write_byte_file(argv[1], dump)

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))