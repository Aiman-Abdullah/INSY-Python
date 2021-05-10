# Qeuation 1
# This program will implement take 3 string form user and do some taks on them
from _ast import Return

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")
str3 = input("Enter Third String: ")
concatenate = str1 + str2
print("concatenate = ", concatenate)

if (concatenate == str3):
    print("The two strings are equal")
else:
    str_reverse = str2 + str1
    if (str_reverse == str3):
        print("The two strings are equal")
    else:
        print("The two strings are not equal")

# ===========================================================
# Quation2
# Read number from user and do some tasks

try:
    while True:
        get_num = input(" Enter Num 3 Or 4: ")
        while True:
            if get_num.isdigit():
                break
            else:
                get_num = input(" Enter Num 3 Or 4: ")

        select = int(get_num)
        if select == 3 or select == 4:
            break
        else:
            continue
except:
    print("Your Enter Not Integer, Please Try again!")

list_num = []
count = 0
while count < select:
    num = input("Enter Your Number: ")
    while True:
        if num.isdigit():
            break
        else:
            num = input(" Your Input Must be Integer! : ")

    n = int(num)
    count = count + 1
    list_num.append(n)
print("List:", list_num)


# Function To fin the Average
def average(list_num):
    counter = 0
    avg = 0
    for i in list_num:
        counter = counter + i

    avg = counter / len(list_num)
    print("Average is:" + "{:.2f}".format(avg))


average(list_num)


# Function to Find Max num
def max(list_num):
    max_value = None
    for i in list_num:
        if (max_value == None):
            max_value = i
        if (max_value < i):
            max_value = i

    print("Max is: ", max_value)


max(list_num)


# Function to Find Min num
def min(list_num):
    min_value = None
    for i in list_num:
        if (min_value == None):
            min_value = i
        if (min_value > i):
            min_value = i

    print("Min is: ", min_value)


min(list_num)


# Find median
def median(list_num):
    #  list.sort()
    list_num.sort()
    print("sorted List: ", list_num)

    leng = len(list_num)
    # To check if the list has lenght of Even num
    if leng % 2 == 0:
        median1 = list_num[leng // 2]
        median2 = list_num[leng // 2 - 1]
        median = (median1 + median2) / 2  # get the median of the two medians
    else:
        # if Length of List not even
        median = list_num[leng // 2]
    print("Median is: " + str(median))


median(list_num)

# ========================================================================================
# Question #3
# Steps:
# read positive Integer from User
# 2- Check if Prime or Composite Or neither
# input > 1
# Prime is num that divide on itself and 1 with no Remainder


while True:
    in_num = input("Enter Positive Integer: ")
    if in_num.isdigit():
        q = int(in_num)
        if q == 2:
            print("Its Prime Integer")
        if q == 3:
            print("Its Prime Integer")
        if q > 2 and q > 3:
            if (q % 2 == 0 or q % 3 == 0):
                print("Its Composite Integer")

            else:
                print("Its Prime Integer")
        if (q == 0 or q == 1):
            print("It is neither prime nor composite")
    else:
        if in_num.isalpha():
            print("You did not enter a Positive Integer ")
            print("You entered characters. Program Finished bye!")
            break
        else:
            print("You did not enter a positive integer ")


# ==============================================================================
# Write function SimpleInterest()  that take 3 agruments principle amount (float), interest rate(float), Year(int)


def SimpleInterest(principle_amount, interset_rate, year):
    result = (principle_amount * interset_rate * year) / 100

    return result


def main():
    while True:
        n1 = input("Enter principle amount: ")
        while True:
            if n1.isalpha():
                print("You Should Enter principle amount As -> (float) Value ")
                n1 = input("Enter principle amount: ")
            else:
                break

        n2 = input("Enter interset rate: ")
        while True:
            if n2.isalpha():
                print("You Should Enter interset rate As -> (float) Value ")
                n2 = input("Enter interset rate: ")
            else:
                break

        n3 = input("Enter year/s: ")
        while True:
            if n3.isalpha():
                print("You Should Enter Year as -> (Integer)")
                n3 = input("Enter year/s: ")
            else:
                break

        principle_amount = float(n1)
        interset_rate = float(n2)
        year = int(n3)
        break

    result = SimpleInterest(principle_amount, interset_rate, year)
    print("the interest amount is: ", result)


# This line will Run the first method will run ("Its the Main method")
if __name__ == '__main__': main()


# =============================================================================
# Question 5

# get input of two opposite num of Rectangle as int or float
# uild function called is_rectangle which return True or False
# Error! Bookmark not defined. -> we can change it to Coordinate not define


def is_rectangle(x1, y1, x2, y2, input_x, input_y):
    x3 = x1
    y3 = y2
    x4 = x2
    y4 = y1

# Coordinate on x=+ , y=+
    if input_x > x1 and input_x < x2:
        if input_y > y1 and input_y < y2:
            return True
        else:
            return False
# Coordinate on x=- y=+
    if input_x < x1 and input_x > x2:
        if input_y > y1 and input_y < y2:
            return True
        else:
            return False

# Coordinate on x=- y=-
    if input_x < x1 and input_x > x2:
        if input_y < y1 and input_y > y2:
            return True
        else:
            return False

# Coordinate on x=+ y=-
    if input_x > x1 and input_x < x2:
        if input_y < y1 and input_y > y2:
            return True
        else:
            return False

    else:
        return False


def main():
    while True:
        while True:
            n1 = input("Enter X1: ")
            while True:
                if n1.isalpha():
                    print("Coordinates not defined! ")
                    n1 = input("Enter X1: ")
                else:
                    break

            n2 = input("Enter Y1: ")
            while True:
                if n2.isalpha():
                    print("Coordinates not defined! ")
                    n2 = input("Enter Y1: ")
                else:
                    break

            n3 = input("Enter X2: ")
            while True:
                if n3.isalpha():
                    print("Coordinates not defined! ")
                    n3 = input(" Enter X2: ")
                else:
                    break
            n4 = input("Enter Y2: ")
            while True:
                if n4.isalpha():
                    print("Coordinates not defined! ")
                    n4 = input("Enter Y2: ")
                else:
                    break
            n5 = input("Enter x: ")
            while True:
                if n5.isalpha():
                    print("Coordinates not defined! ")
                    n5 = input("Enter X: ")
                else:
                    break

            n6 = input("Enter Y: ")
            while True:
                if n6.isalpha():
                    print("Coordinates not defined! ")
                    n6 = input(" Enter Y: ")
                else:
                    break

            x1 = int(n1)
            y1 = int(n2)
            x2 = int(n3)
            y2 = int(n4)
            input_x = int(n5)
            input_y = int(n6)
            break

        result = is_rectangle(x1, y1, x2, y2, input_x, input_y)
        print("The Result is: ", result)
        done = input("Do you want to Contiune?")
        if done == "y" or done == "Y":
            continue
        if done == "n" or done == "N":
            print("Goodbye!")
            break


if __name__ == '__main__': main()


















