student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for grades in student_scores:
  if grades >= 91:
    student_grades+=grades[student_scores]
    elif grades >= 81 or grades <= 90:
    student_grades+=grades[student_scores]
    elif  grades >= 71 or grades <= 80 :
    student_grades+=grades[student_scores]
    elif grades <= 70 : 
    student_grades+=grades[student_scores]

  

  
  

# 🚨 Don't change the code below 👇
print(student_grades)