marks=int(input("enter the marks:"))
if marks>100 and marks<0:
    print("invalid marks")
elif marks>=90 and marks<=100:
    print("GRADE:A")
elif marks>=75 and marks<=75:
    print("Grade:B")
elif marks>=50 and marks<=50:
    print("Grade:c")
elif marks>=35 and marks>=35:
    print("Grade:D")
else:
    print("Fail")