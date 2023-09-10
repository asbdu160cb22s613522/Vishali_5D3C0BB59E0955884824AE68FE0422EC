def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
  return sorted_students


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


# Example usage:
students = [
    Student("Anitha", "A123", 3.8),
    Student("Niranjan", "B456", 3.5),
    Student("Sasumi", "C789", 3.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number:{student.roll_number}, CGPA:{student.cgpa}"
  )
