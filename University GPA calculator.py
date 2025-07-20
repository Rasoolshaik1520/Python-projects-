#University GPA Calculator using Grade and Credit Input

# grade to point mapping
grade_points= {
    'S' : 10,
    'A' : 9,
    'B' : 8,
    'C' : 7,
    'D' : 6,
    'RA' : 0
} 

# to get the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

#List to store the grades and credits for each subject
subjects = []

#input loop
for i in range(num_subjects):
    print(f"\nsubject{i + 1}:")
    grade = input("Enter the grade(S/A/B/C/D/RA):").upper()

    #credit input
    credit = int(input("Enter the credits for this subject:"))

    #Append (grade, credit)pair
    subjects.append((grade, credit))

# GPA calculation
total_points = 0
total_credits = 0

for grade, credit in subjects:
    point = grade_points[grade]
    total_points += point * credit
    total_credits += credit

# calculate GPA
GPA= total_points / total_credits if total_credits > 0 else 0

# output the result
print(f"\nyour GPA is: {GPA:.2f}")

