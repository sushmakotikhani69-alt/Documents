name=input("enter a employee name:")
id=int(input("enter a employee id:"))
salary=float(input("enter a basic salary:"))
HRA=0.20*salary
DA=0.10*salary
PF=0.11*salary
netsalary=HRA+DA-PF
print("HRA is:",HRA)
print("DA is:",DA)
print("PF is:",PF)
print("netsalary is:",netsalary)