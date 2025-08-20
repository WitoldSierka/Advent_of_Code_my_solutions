import os
import numpy

#file_path = "example.txt"
file_path = "input.txt"

equations: list[str] = []

if not os.path.isfile(file_path):
    print(f"File '{file_path}' not found")
    exit(1)
else:
    with open(file_path) as f:
        for line in f:
            equations.append(line.strip("\n"))
        #f.close()

#PART ONE
#because there is only two possible operators, I used binary representation of a number of permutations
#like for case "3267: 81 40 27" there are 2 places, so operator arrangement could be represented as:
#00  or  + +
#01  or  + *
#10  or  * +
#11  or  * *
def part_one():
    sum1 = 0
    for eq in equations:
        temp = eq.split(" ")
        result = int(temp[0].rstrip(":"))
        temp.pop(0)
        nums = list(map(int, temp))
        places = len(nums) - 1
        possibilities = 2 ** places # number of times + and * can be arranged in given places
        #cand = 0
        for i in range(0, possibilities):
            operators: int = i
            cand = nums[0]
            for num in nums[1:]:
                if operators & 1:
                    cand += num
                else:
                    cand *= num
                operators = operators >> 1 # go to the next
            if result == cand:
                sum1 += cand
                break
    print(f"Total calibration result is {sum1}.")

#part_one()

#PART TWO
#third possible operator is added, which changes previous logic to base 3 numeric system.
#in order to not reinvent the wheel, I will use an external library.
#0  +
#1  *
#2  ||

def concat_numbers(a: int, b: int) -> int:
    return int(str(a) + str(b))


def part_two():
    sum2 = 0
    check: int = 0
    for eq in equations:
        temp = eq.split(" ")
        result = int(temp[0].rstrip(":"))
        temp.pop(0)
        nums = list(map(int, temp))
        places = len(nums) - 1
        possibilities = 3 ** places # number of times + and * can be arranged in given places
        for i in range(0, possibilities):
            operators: str = numpy.base_repr(i, base=3)
            operators = operators.zfill(places)
            cand = nums[0]
            for num in nums[1:]:
                if operators[-1] == "0":
                    cand += num
                elif operators[-1] == "1":
                    cand *= num
                else:
                    cand = concat_numbers(cand, num)
                operators = operators[:-1]
            if result == cand:
                sum2 += cand
                break
        print(f"iteration {check}")
        check += 1
    print(f"Part two: corrected calibration result is {sum2}.")

part_two()

#runtime ~30s