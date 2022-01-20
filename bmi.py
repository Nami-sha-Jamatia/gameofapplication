height=float(input("enter ur height in m: "))
weight=float(input("enter ur weight in kg: "))
bmi=weight/height**2
b_m_i=float("{:.2f}".format(bmi))
print(f"your body mass index is:{b_m_i}")
if b_m_i<18.5:
    print("sorry!!!you are underweight")
elif b_m_i<25:
    print("great!!you have normal weight")
elif b_m_i<35:
    print("ohhhhh!!!u are overweight")
else:
    print("you are clinically obese")