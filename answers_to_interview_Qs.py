#    Aswers to prelimanry test questions
Monday=['Blue','Blue','Blue','Blue','Blue','Blue','Brown','Cream','Green','Green','Green','Orange','Orange','Pink','Red','White','White','Yellow','Yellow']
Tuesday=['Arsh','Blue','Blue','Blue','Blue','Blue','Blue','Blue','Brown','Brown','Green','Orange','Orange','Pink','Pink','Red','White','White','White']
Wednesday=['Blue','Blue','Blue','Blue','Blue','Brown','Green','Green','Orange','Orange','Pink','Red','Red','Red','White','White','White','Yellow','Yellow']
Thursday=['Blue','Blue','Blue','Blue','Blue','Blue','Blue','Brown','Cream','Green','Green','Orange','Orange','Pink','Red','White','White','White','Yellow']
Friday=['Black','Blue','Blue','Blue','Blue','Blue','Blue','Brown','Green','Green','Orange','Red','Red','Red','White','White','White','White','White']
sum=Monday+Tuesday+Wednesday+Thursday+Friday

#Qusetion 1
#'sum' being used is declared in the above section
mean=sum/len(sum)
print(f'the mean colour is - {mean}')

#Qusetion 2
#'sum' being used is declared in the above section
count=(0,0)
for x in sum:
    occurrance=sum.count(x)
    if occurrance > count[0]:
        count=(occurrance,x)
    else:
        pass
print(f'the clour that is mostly worn is -{count[1]} and it was worn {count[0]}')
#Note: This will pass an error when it is run because the items in the list are strings and they cannot be iretated. if they were numbers this will run

#Qusetion 3
#'sum' being used is declared in the above section
sum.sort()
if len(sum)%2 != 0:
    median=(len(sum) - 1)/2
    print(median)
elif len(sum)%2 == 0:
    median_1=len(sum)/2
    median_2=median_1 - 1
    median=(median_1+median_2)/2
    print(median)
else:
    pass
print(f'the median colour(in alphabetical order) is in the {median}th position.')

#Qusetion 4

#Question 5
#'sum' being used is declared in the above section
find=sum.sort()
count=0
for x in find:
    if x=='Red':
        count=count+1
        prob_is_red=count/len(sum)
    else:
        pass     
print(f'probability that it is red is {prob_is_red}')
#Note: This will give an error because the items in the list cannot be iretated.

#Question 6

#Qusetion 7

#Question 8
#to get the firt 50 fibonacci numbers
a=0
b=1
for i in range(0,50):
    c=a+b
    a=b
    b=c
    print(c)

#to get the sum of the first 50 fibonacci numbers
a=0
b=1
Sum=a+b
for x in range(0,50):
    c=a+b
    Sum+=c
    a=b
    b=c
print(Sum)
#fib_sum(50)

