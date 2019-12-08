from math import floor

class DayOne:
    def read_file(self, file_name):
        with open(file_name,'r') as out:
                return out.read().splitlines()

    def calculateAllFuel(self, masses):
        allCalculatedFuel = 0
        for mass in masses:
            remainder = self.__calculateFuel(mass)

            while(remainder > 0):
                allCalculatedFuel += remainder
                remainder = self.__calculateFuel(remainder)

        return allCalculatedFuel
    
    def __calculateFuel(self, mass):
       return floor((int(mass) / 3) - 2)


day_one = DayOne()
lines = day_one.read_file('Day_One/input.txt')
day_one.calculateAllFuel(lines)
    

