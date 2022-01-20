x=int(input("enter your first number: "))
y=int(input("enter your second number: "))
temp=x
x=y
y=temp
print(x)
print(y)


'''height=float(input("enter ur height in m: "))
weight=float(input("enter ur weight in kg: "))
bmi=weight/height**2
b_m_i="{:.2f}".format(bmi)
print(f"your body mass index is:{b_m_i}") '''


'''scores=input("enter the list of the no: ").split()
for i in range(0,len(scores)):
    scores[i]=int(scores[i])
highestscore=0
for score in scores:
    if score>highestscore:
         highestscore+=score
print(f"highest no: {highestscore}")'''
