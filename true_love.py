print("welcome to the love calculator")
name1=input("enter ur name: ").lower()
name2=input("enter ur partner's name: ").lower()
combine=name1 + name2
t=combine.count("t")
r=combine.count("r")
u=combine.count("u")
e=combine.count("e")
true=t+r+u+e
l=combine.count("l")
o=combine.count("o")
v=combine.count("v")
e=combine.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"your love score is {love_score}%")
elif love_score>=40 and love_score<=50:
    print(f"your love score is {love_score}%,keep it up")
else:
    print(f"your love score is {love_score}%,dnt fght that much")