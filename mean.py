#The mean of 40 numbers is 38. Later on you detected that you misread the number 56 as 36. Find the correct mean.
mean1=38
incorrectnumber=36
correctnumber=56
totalnumbers=40
sum=mean1*totalnumbers
print("The sum of all of the numbers is,",sum)
correctsum=sum-incorrectnumber+correctnumber
print("The correct sum,",correctsum,"is found by subtracting the incorrect number,",incorrectnumber,"and adding the correct number,",correctnumber)
correctmean=correctsum/totalnumbers
print("The correct mean,",correctmean,"is found by dividing the total numbers,",40,"by the correct sum,",correctsum)

