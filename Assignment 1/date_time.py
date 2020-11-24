from datetime import datetime

class Date_Time:
    # To check if the date entered is valid
    def validate_date(self, prompt):
        while True:
            try:
                date_text = input(prompt)
                return datetime.strptime(date_text, '%d/%m/%Y')
            except ValueError:
                print("Incorrect data format, should be DD/MM/YYYY or date is not valid.")

    # To check if the time entered is valid
    def validate_time(self, prompt):
        while True:
            try:
                time_text = input(prompt)
                return datetime.strptime(time_text, '%H:%M')
            except ValueError:
                print("Incorrect data format, should be HH:MM or time is not valid.")

    # To check whether have feeding or observation details between dates
    def isBetweenDates(self, start_date, end_date, objects):
        if start_date <= objects.date and end_date >= objects.date:
            return True
        return False

    # It does not allow feed or observe at the same date and same time 
    def check_time(self, animal_no, date, time, objects):
        for i in objects:
            if animal_no == i.animalNo and i.date == date and i.time == time:
                print("Your are not allow to feed or observe animal at the same time and same date\n\n")
                return False
        return True

    # To check if the date entered is the day after the animal's birth date
    def checkDate(self, no, date, animal):
        for a in animal:
            if a.animalNo == no and a.birthDate <= date:
                return True
        return False

    # To check whether the date entered is valid range
    def compareDates(self, datetime_end, datetime_start, feeding):
        for f in feeding:
            if datetime_end >= f.date and datetime_start <= f.date:
                return True
        return False