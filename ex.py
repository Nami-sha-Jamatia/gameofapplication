'''x=int(input("enter:"))
if x%2==0 :
    if 2<x and x<6:
        print(" Not Weird")
    elif x>20:
        print("Not Weird")
    else:
        print("Weird")  
else:
    print("Weird")   '''
'''n=int(input("enter the no: "))
for i in range (1,n+1):
        print(i**2)'''
def leap(year):
    if year%4==0:
        return True 
    elif year%400==0:
        return True
    elif year%100==0:
        return False 
    else: 
        return False             
year = int(input())
print (leap(year))

