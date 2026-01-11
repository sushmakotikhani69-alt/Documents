courses={
    "pythonprogamming":5000,
    "data anlysist":8000,
    "ai&ml":12000
}
course_name=input("enter a course:")
is_student=input("are you a student(yes/no):")
is_early_registration=input("are you early registred(yes/no):")
if course_name not in courses:
    print("course not found")
else:
    original_fees=courses[course_name]
    discount=0
    if is_student=="yes":
        discount+=0.10
    if is_early_registration=="yes":
        discount+=0.05
    total_discount=original_fees*discount
    final_fees=original_fees-total_discount
print("course name:",course_name)
print("original fees:",original_fees)
print(" total discount:",total_discount)
print("final payable amount:",final_fees)
