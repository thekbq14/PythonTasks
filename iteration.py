maths = int(input("What is your Maths mark? "))
chemistry = int(input("What is your Chemistry mark? "))
physics = int(input("What is your Physics mark? "))

average = (int(maths + chemistry + physics)/3)
print (average)

if average >= 70:
    print("A")
elif average >= 60:
    print("B")
elif average >= 50:
    print("C")
elif average >=40:
    print("D")
else:
    print("Fail")