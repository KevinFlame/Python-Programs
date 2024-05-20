# Write a program to print a student’s bio data having his/her Date of birth, Roll no,
# Section, Percentage and grade of matriculation and Intermediate. All the fields should
# be entered from the console at run time.

greetingsMessage = str(input('Greetings! Hopefully you are doing good Buddy. Press enter to continue.'))

botInformationMessage = str(input("I'm a builtin scripted bot. My job is to generate your Bio Data based on your inputs. Press enter to continue."))

welcomeMessage = str(input('Welcome to our Bio Data Generator! Press enter to continue.'))

studentName = str(input('Please enter your name here: '))
studentAge = int(input('Please enter your age here: '))

studentUniversityName = str(input('Please enter your university name here: '))
studentRollNo = int(input('Please enter your roll no here: '))
studentTechnology = str(input('Please enter your technology name here: '))
studentSection = str(input('Please enter your section here: '))

smartScript1 = str(input(
    "Now you don't have to write all your subjects name, our smartly written script will automatically generates a list and you can proceed without any delay. Press enter to continue."))

python = 'Python'
ict = 'ICT'
english = 'English'
calculus = 'Calculus'
physics = 'Physics'

alert1 = str(input('Please fill all the correct matriculation credentials. Press enter to continue.'))

studentMatriculationTotalMarks = int(input('Please enter your total marks of matriculation board here: '))
studentMatriculationObtainedMarks = int(input('Please enter your obtained marks of matriculation board here: '))

alert2 = str(input('Please fill all the correct intermediate credentials. Press enter to continue.'))

studentIntermediateTotalMarks = int(input('Please enter your total marks of intermediate board here: '))
studentIntermediateObtainedMarks = int(input('Please enter your obtained marks of intermediate board here: '))

smartScript2 = str(input(
    'Our smart script will automatically calculates your both matric and intermediate percentages so, you dont have to worry at all. Press enter to continue.'))

# Calculating Matriculation percentage
studentMatriculationPercentage = studentMatriculationObtainedMarks / studentMatriculationTotalMarks * 100

# Calculating Intermediate percentage
studentIntermediatePercentage = studentIntermediateObtainedMarks / studentIntermediateTotalMarks * 100

smartScript3 = str(input(
    'Grades will automatically be detect based on your matric and intermediate percentages. Press enter to continue.'))

# Determine the grade for matriculation percentage

if 80 <= studentMatriculationPercentage <= 100:
    studentMatriculationGrade = 'A+'
elif 70 <= studentMatriculationPercentage < 80:
    studentMatriculationGrade = 'A'
elif 60 <= studentMatriculationPercentage < 70:
    studentMatriculationGrade = 'B'
elif 50 <= studentMatriculationPercentage < 60:
    studentMatriculationGrade = 'C'
elif 40 <= studentMatriculationPercentage < 50:
    studentMatriculationGrade = 'D'
elif 30 <= studentMatriculationPercentage < 40:
    studentMatriculationGrade = 'E'
elif 20 <= studentMatriculationPercentage < 30:
    studentMatriculationGrade = 'F'
elif 10 <= studentMatriculationPercentage < 20:
    studentMatriculationGrade = 'G'
else:
    studentMatriculationGrade = 'Sorry to say but you are fail.'

# Determine the grade for intermediate percentage
if 80 <= studentIntermediatePercentage <= 100:
    studentIntermediateGrade = 'A+'
elif 70 <= studentIntermediatePercentage < 80:
    studentIntermediateGrade = 'A'
elif 60 <= studentIntermediatePercentage < 70:
    studentIntermediateGrade = 'B'
elif 50 <= studentIntermediatePercentage < 60:
    studentIntermediateGrade = 'C'
elif 40 <= studentIntermediatePercentage < 50:
    studentIntermediateGrade = 'D'
elif 30 <= studentIntermediatePercentage < 40:
    studentIntermediateGrade = 'E'
elif 20 <= studentIntermediatePercentage < 30:
    studentIntermediateGrade = 'F'
elif 10 <= studentIntermediatePercentage < 20:
    studentIntermediateGrade = 'G'
else:
    studentIntermediateGrade = 'Sorry to say but you are fail.'
    
smartScript4 = str(input('Loading...\n Your bio data is generated.\n Press enter to continue.'))

# Printing the student bio data

print('BIO DATA')
print('According to your given information your bio data involves the following:')

print('Your name is',studentName)
print('Your age is', studentAge)
print('Your roll no is',studentRollNo)
print('Your technology is',studentTechnology)
print('Your section is',studentSection)

print(f'Your subjects of BSC Software Technology Are:- \n 1) {python} \n 2) {ict} \n 3) {calculus} \n 4) {physics} \n 5) {english}')

print(f'Your percentage is {studentMatriculationPercentage:.2f}%')
print(f'Your percentage is {studentIntermediatePercentage:.2f}%')

print('Your matriculation grade is',studentMatriculationGrade)
print('Your intermediate grade is',studentIntermediateGrade)