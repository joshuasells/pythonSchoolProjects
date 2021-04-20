# Joshua Sells, Intro to computer science, 09/08/2019, lab 1.py, this program computes your letter grade.

#prompt user for grade.

numberGrade = float(input('Enter grade (0-100): '))

#prompt user to answer if they are a graduate student.

graduateStudent = input('Graduate student (Y/N): ')

#if graduate student, then reduce grade by 10%

if graduateStudent == 'Y':
    numberGrade = numberGrade * 0.9

#compute letter grade.

if numberGrade >= 90 and numberGrade <= 100:
    letterGrade = 'A'
    feedback = 'Excellent!'
elif numberGrade >= 80 and numberGrade < 90:
    letterGrade = 'B'
    feedback = 'Excellent!'
elif numberGrade >= 70 and numberGrade < 80:
    letterGrade = 'C'
    feedback = 'Could Improve.'
elif numberGrade >= 60 and numberGrade < 70:
    letterGrade = 'D'
    feedback = 'Could Improve.'
elif numberGrade >= 0 and numberGrade < 60:
    letterGrade = 'F'
    feedback = 'Need work.'

#display grade and feedback.

print('Your letter grade is: ', letterGrade)
print(feedback)

#this is just to keep the command line open until you press enter. I don't know another way yet on how to test programs.
input('press enter to exit')

