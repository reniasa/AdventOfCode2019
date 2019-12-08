from math import floor

class DayOne:
    def read_file(self, file_name):
        with open(file_name,'r') as out:
                return out.read().splitlines()

    def calculateAllFuel(self, masses):
        allCalculatedFuel = 0
        for mass in masses:
            allCalculatedFuel += self.__calculateFuel(mass)
        return allCalculatedFuel
    
    def __calculateFuel(self, mass):
       return floor((int(mass) / 3) - 2)


day_one = DayOne()
lines = day_one.read_file('input.txt')
day_one.calculateAllFuel(lines)
    

