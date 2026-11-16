# write a python program to
# a)Read students name,Usn, and marks of three course
# b)Calculate the total and Average marks
# c)display the student details in a formatted way

# input section
name=str(input("Enter the students name:"))
usn=str(input("Enetr the students USN:"))
physics_marks=int(input("Enter the studensts marks in physics:"))
chemistry_marks=int(input("Enter the students marks in chemistry:"))
maths_marks=int(input("Enter the students marks in maths:"))

# processing section
total_marks=physics_marks+chemistry_marks+maths_marks
average_marks=total_marks/3

# output section
print("students name is:\t",name)
print("students USN is:\t",usn)
print("students marks in physics is:\t",physics_marks)
print("students marks in chemistry is:\t",chemistry_marks)
print("students marks in maths is:\t",maths_marks)
print("Total marks obtained is:\t",total_marks)
print("Average marks obtained is:\t",format(average_marks,'.2f'))
