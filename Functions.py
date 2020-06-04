## FUNCTIONS


#/ Procedures

#def hiUser(firstName, lastName):
#    print("Welcome " + firstName + " " + lastName)

#hiUser("Jeri", "Chaudhry")


#hiUser("Bill", "Steves")

#def hiUser(firstName, lastName):
#    print("Hello" + " " + firstName + " " + lastName)


#Functions

#def addCalc(number1, number2):
#    answer = number1 * number2
#    return answer

#addedNumber = addCalc(5,4)

#print(addedNumber + 3)


#def hey_user(first_name, second_name):
#   return "Hey " + first_name + second_name

#message = hey_user("Jeri", " Chaudhry")
#print(message)

#Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
#The program should give the students name and an ICT grade based on Homework(/25), Assessment(/50), Final Exam(/100).

def score ():
    name=input("Enter Your Name: ")
    homework_score=int(input("Homework Score: "))
    assessment_score=int(input("Assessment Score: "))
    final_exam_score=int(input("Final exam Score: "))
    total = homework_score + assessment_score + final_exam_score
    if total >= 150:
        grade = "A"
    else:
        grade = "F"

    return name + " Achieved Grade of: " + grade
print(score())


