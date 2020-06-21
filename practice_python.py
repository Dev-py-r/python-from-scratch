# -*- coding: utf-8 -*-

"Variable"
rent=1220
gas=202.5
groceries=305.6
print(rent)
total=rent+gas+groceries
print(total)

rent=1400
item1="rent"
item2="gas"
item3="groceries"
print("Expense items:",item1,item2,item3)

"Number"
12+34 #Add
3-4 #sub
3/4 #div
4*5 #Mul
11%2 #remider
3**2 #power

#finding time
total_distance=435
mph=65
time=total_distance/mph
print("Total time taken:", time) 
time=round(time, 3)
print(time)

#floating number
6-5.7
roundoff=round(6-5.7,2)
print(roundoff)

#Strings
text="ice cream"
text
#stored in index
text[0]
text[1]
#strings are immutable in python
#text[0]='g' will through error
text[0:3]
text[4:]
text[:3]
text='hello'
text="hello"
#text='let's learn python' will through error
text="let's learn python"

#three quotes for adding sentence in multi lines
address='''1 purple street
new york
usa'''

#Joining strings
s1="hello"
s2="world"
print(s1+s2)
print(s1+' '+s2)

#Need to convert number to string to join
s = "total states in usa #"
num=25 
#s+num will give us error
num=str(num) #convert num to str
print(s+ num)

#List 
item1="bread"
item2="pasta"
item3="fruits"
items=["bread","pasta","fruits","veggies"]
print(items)

items[0]
items[1]
items[0]="chips"
print(items[0])

items.append("butter") #add butter in list
print(items)
items.insert(1,"butter")
print(items)

food=["bread","pasta","fruits"]
bathroom=["shampoo","soap"]
items=food+bathroom
print(items)

#food+"soda" will give error both the items should be in list

print(len(items))

print("bread" in items)#lookup in python
print("soda" in items)

# if statement
num=input("Enter a number: ")
num=int(num)
if num%2 == 0: #if reminder is 0 then its even
    print("Entered number is even")
else:
    print("Entered number is odd")

#operators
4==4
4!=5
2>1
2<3
2>=1
3<=4

3>2 and 4>1
3>2 and 4>5
3>2 or 4>5
not True #negate 
not 4==4

#practical solution

indian=["samosa","daal","naan"]
chinese=["egg role","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter the dish name: ")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("Entered dish",dish  +" is not in the list.")

#For statement

exp= [2340,2500,2100,3100,2980]

#total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
total = 0
for item in exp:
    total = total + item
print(total)

#Range
for i in range (1,11):
    print(i*i)

#Length in range
exp= [2340,2500,2100,3100,2980]
total = 0
for i in range (len(exp)):
    print("Month",(i+1),"Expense:",exp[i])
    total=total+exp[i]
print("Total expense is:", total)


# for-break-else

key_location="chair"
locations=["garage","living room","chair","closet"]
for i in locations:
    if i==key location:
        print("key is found in", i)
        break
    else:
        print("key is not found in",i)

#Continue
        
for i in range (1,6):
    if i%2==0:
        continue
    print(i*1)

#while loop
i=1
while i<=5:
    print(i)
    i=i+1
    
#Functions
tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

total=0
for item in tom_exp_list:
    total=total+item
print("Tom's total expenses:",total)

total=0
for item in joe_exp_list:
    total=total+item
print("Joe's total expenses:",total)
    











