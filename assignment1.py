inter_name=input("enter name:")
age=int(input("enter aage:"))
email=input("enetr a email:")
grad=int(input("enter a grades:"))
contact=(input("enter a contact:"))
if age>=18:
    if grad>60:
        if len(contact)==10:
            print("student is eligible for the internship")
        else:
            print("student is not eligible for internship")
    else:
        print("grade must be greater than or above 60")
else:
    print("age must be greater than the 18")