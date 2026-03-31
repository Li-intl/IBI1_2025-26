age=float(input("age input "))
weight=float(input("weight input "))
Cr=float(input("Cr input "))
gender=str(input("male or female "))#gender should be male or female
#first we check these input, if it doesn't fit the condition, we do not start to caculate and output variable needs corrected
#then we should distinguish male or female and caculate 
if 0<age<100 and 20<weight<80 and 0<Cr<100 and (gender=="male" or "female"):#if I don't add parentheses,it will result in an error.
    if gender=="male":
        CrCl=(140-age)*weight/(72*Cr)
        print("CrCl is "+ str(CrCl))
    if gender=="female":
        CrCl=(140-age)*weight*0.85/(72*Cr)
        print("CrCl is "+ str(CrCl))
else:
    print("input variable needs corrected")
