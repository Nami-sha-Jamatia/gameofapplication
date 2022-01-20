year=int(input("enter the year to check is it a leap year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("the entered year is a leap year")
        else:
            print("your entered year is not a leap year")
    else:
        print("your entered year a leap year")
else:
    print("your entered year is not a leap year")