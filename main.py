#1
my_string = "Hello, World!"
print(my_string)

#2
n = int(input().strip())
if n % 2 == 1:

    print("Weird")
elif n % 2 == 0 and (n >= 2 and n < 5):
    print("Not Weird")
elif n % 2 == 0 and (n >= 6 and n <= 20):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#3
if __name__ == '__main__':
    # Read two integers from input
    a = int(input())
    b = int(input())

    # Calculate sum, difference, and product
    sum_ab = a + b
    diff_ab = a - b
    prod_ab = a * b

    # Print the results
    print(sum_ab)
    print(diff_ab)
    print(prod_ab)
#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # Integer division
    print(a // b)

    # Float division
    print(a / b)

#5
if __name__ == '__main__':
    n = int(input())

    # Iterate from 0 to n-1 and print the square of each number
    for i in range(n):
        print(i ** 2)
#6
def is_leap(year):
    if year % 4 == 0:  # Check if the year is divisible by 4
        if year % 100 == 0:  # Check if the year is also divisible by 100
            if year % 400 == 0:  # Check if the year is divisible by 400
                return True  # If divisible by 400, it's a leap year
            else:
                return False  # If not divisible by 400, it's not a leap year
        else:
            return True  # If divisible by 4 but not divisible by 100, it's a leap year
    else:
        return False  # If not divisible by 4, it's not a leap year

# Reading input from STDIN




year = int(input())
print(is_leap(year))

#7
if __name__ == '__main__':
    n = int(input())

    # Iterate from 1 to n and print each number without spaces
    for i in range(1, n + 1):
        print(i, end='')  # Using end='' to print without any space or newline
#8
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convert the input to a list
    scores = list(arr)

    # Sort the list of scores in descending order
    scores.sort(reverse=True)

    # Find the runner-up score
    runner_up_score = None
    for score in scores:
        if score < scores[0]:
            runner_up_score = score
            break

    # Print the runner-up score
    print(runner_up_score)
#9
if __name__ == '__main__':
    # Read the number of students
    n = int(input())

    # Create a list to store students' names and grades
    students = []

    # Read students' names and grades
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the students list based on grades
    students.sort(key=lambda x: (x[1], x[0]))

    # Find the second lowest grade
    second_lowest_grade = None
    for i in range(1, n):
        if students[i][1] > students[0][1]:
            second_lowest_grade = students[i][1]
            break

    # Print the names of students with the second lowest grade
    for student in students:
        if student[1] == second_lowest_grade:
            print(student[0])
#10
if __name__ == '__main__':
    # Read the number of students' records
    n = int(input())

    # Create an empty dictionary to store students' marks
    student_marks = {}

    # Read students' records
    for _ in range(n):
        record = input().split()
        name = record[0]
        marks = list(map(float, record[1:]))
        student_marks[name] = marks

    # Read the name of the student to query
    query_name = input()

    # Calculate the average marks for the given student's name
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Print the average marks rounded to 2 decimal places
    print("{:.2f}".format(average_marks))

