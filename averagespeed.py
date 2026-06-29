#The speed of 3 cyclers is 10, 20, 30 kmph. 
#Calculate the average and find out which cycler is driving slower than the average speed.
cycler1=10
cycler2=20
cycler3=30
totalcyclers=3
average=(cycler1+cycler2+cycler3)/totalcyclers
print("The average speed of the 3 cyclers is",average)
if cycler1<average and cycler2>average and cycler3>average:
    print("Only Cycler 1 is less than the average.")
elif cycler1<average and cycler2<average and cycler3>average:
    print("Cycler 1 and Cycler 2 are less than the average.")
elif cycler1<average and cycler2<average and cycler3<average:
    print("All three cyclers are less than the average.")
elif cycler1>average and cycler2<average and cycler3<average:
    print("Only Cycler 2 is less than the average.")
elif cycler1>average and cycler2<average and cycler3<average:
    print("Cycler 2 and Cycler 3 are less than the average.")
elif cycler1>average and cycler2>average and cycler3<average:
    print("Only Cycler 3 is less than the average.")
else:
    print("Invalid")


