class DayTwo:
    def read_file(self, file_name):
        with open(file_name,'r') as out:
                elements = out.read().split(',')
                return [int(element) for element in elements]

    def run_intcode(self, intcode):
        for i in range(0, len(intcode), 4):
            opcode = intcode[i]
            if(opcode == 99):
                break
            operation = Operation(intcode[i + 1], intcode[i + 2], intcode[i + 3], opcode, intcode)
            intcode = self.__perform_operation(operation)     
        return intcode

    def __perform_operation(self, operation):
        switch = {
            1: self.__add,
            2: self.__multiply
        }
   
        new_value = switch.get(operation.opcode, "Invalid opcode provided")(operation.intcode[operation.arg1_index], 
                                                                            operation.intcode[operation.arg2_index]) 
        operation.intcode[operation.result_index] = new_value
        return operation.intcode

    def __add(self, arg1, arg2):
        return arg1 + arg2

    def __multiply(self, arg1, arg2):
        return arg1 * arg2


class Operation:
    arg1_index = 0,
    arg2_index = 0,
    result_index = 0,
    opcode = 0,
    intcode = []

    def __init__(self, arg1_index, arg2_index, result_index, opcode, intcode):
        self.arg1_index = arg1_index
        self.arg2_index = arg2_index
        self.result_index = result_index
        self.opcode = opcode
        self.intcode = intcode

day_two = DayTwo()
intcode = day_two.read_file('Day_Two/input.txt')
intcode[1] = 12
intcode[2] = 2
day_two.run_intcode(intcode)
