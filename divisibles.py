print("We will check if the numerator is divisible by the denominator.")
numerator=float(input("Please enter the numerator."))
denominator=float(input("Please enter the denominator."))
if numerator % denominator==0:
    print (str(numerator),"is divisible by",str(denominator))
else:
    print (str(numerator),"is not divisible by",str(denominator))
