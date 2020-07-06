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
    if i==key_location:
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
print("Joe's total expenses:",total) #repeating same thing again

#now same above code using funtion

def calculate_total (exp):
total=0
for item in exp:
    total=total+item
return total

tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)

print("Tom's total expenses:",toms_total)
print("Joe's total expenses:",joes_total)



  """
    multi 
    line 
    strings
    
    """
    
#sum using function
total=0
def sum(a,b): # default number (a,b=0)
    print("a:",a)
    print("b:",b)
    
    total=a+b
    print("Total inside funtion ",total)
    return total

n=sum(5,6) #Also we can (b=5,a=6)#position argument, name argument
#print(total) Global vs local, will give error as its local 
print("Total outside function:",n)

print("Total outside function:",total) #output 0


#Dictionaries (Maps,Hashtables,Associated Arrays) and Tuples 

d={"tom":7326789820, "rob":7325730239,"joe":7320923203}
d
d["tom"]
d["sam"]=7395679879
d
del d["sam"]#delete
d


for key in d:
    print("key:",key,"value:",d[key])
    
for k,v in d.items():
    print("key:",key,"value:",v)

"tom" in d #True

"samir" in d #False

d.clear()
d

""" 
List- All the value have same meaning
(Homogeneous)

Tuple- All values have different

meaning(heterogeneous)

List eg:
expense_list=[2300,2500,2900,6700]
#Every item is an expense

list_of names=["Bob","Tom","Partha"]
#Every item is a name of the person

Tuple eg:
point=(4,5)#4 is x coordinate, 5 is y coordinate
address=("1 purple street","new york",10001)



 """
#Tuple
point=(5,9) 
point[0]

point[1]

#Tuples are immutable
# point [0]= 50 will get error 

#installing matplotlib
import matplotlib

"""
Modules is a way to reuse a code written
by someone else

"""

""" 
'acos','acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 
'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 
'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 
'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 
'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
'tan', 'tanh', 'tau', 'trunc'  

"""

import math
dir(math) # to know all the funtions in model
print(math.sqrt(16))
print(math.pow(2,5))
print(math.pi)
print(math.log10(100))
print(math.log10(1000))
print(math.floor(2.3))
print(math.ceil(2.3))


""" 'Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 
'IllegalMonthError', 'IllegalWeekdayError', 'January',
'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 
'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', 
'_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_colwidth', '_locale', '_localized_day', '_localized_month', 
'_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 
'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 
'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 
'month_name', 'monthcalendar', 'monthlen', 'monthrange', 'nextmonth', 
'prcal', 'prevmonth', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 
'sys', 'timegm', 'week', 'weekday', 'weekheader'] """

import calendar
cal=calendar.month(2016,1)
print(cal)

calendar.isleap(2016) #check if its a leap year

dir(calendar)

"""
import modules.functions as f
area=f.calculate_square_area(5)
print(area)

"""
""" second file

def calculate_triangle_area(base,height):
    print(return 1/2*(base*height))

def calculate_square_area(length):
  return length*length

"""


import sys
sys.path.append("C:/Users/prasa/Desktop/modules")
import functions as f
area=f.calculate_square_area(5)
print(area)


f.calculate_triangle_area(6,7)

"""
JSON

Create address book and write some records
into it

Read this address book

"""
book= {}
book['tom']={
    
    'name':'tom',
    'address':'1 red street, NY',
    'phone':98989898
    
    }
book['bob']={
    
    'name':'bob',
    'address':'1 green street, NY',
    'phone':23424234
    
    }

""" Write the above book using json in text"""
import json
s=json.dumps(book)
print(s)
with open("C:/Users/prasa/Desktop/modules/book.text","w") as f:
    f.write(s)

f=open("C:/Users/prasa/Desktop/modules/book.text","r")
s=f.read()
print(s)

import json
book=json.loads(s)
print(book)
type(book)#dictionary

print(book["bob"] )
book["bob"]["phone"]

for person in book:
    print(book[person])
    
    


'''  if __name__ == "__main__" '''

"""This in another file caller.py"""

import sys
sys.path.append("C:/Users/prasa/Desktop/py codes/")
import practice_python
print("I am in caller.py")
area.calculate_area(5,10)


"""Area.py"""

def calculate_area(base,height):
    print("__name__:",__name__)
    return 1/2*(base*height)

if __name__ == "__main__":
    a=calculate_area(10,20)
    print("area:",a)


# Exception Handling
    
1/0 #error
'abc'+2 #string to int error

#New


x=input("Enter number1:")
y=input("Enter number2:")
try:
    z=int(x)/int(y)
except Exception as e:
    print('exception occured:',e) 
    z = None
print("Division is:",z)


#Find the exception

x=input("Enter number1:")
y=input("Enter number2:")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception') 
    z = None
except Exception as e:
    print("exception type:",type(e).__name__) #We'll get the type error exception
    z=None
print("Division is:",z)


"""
except TypeError as e:
    print('Type error exception')
    z=None
"""


# Class and Objects

"""
class is abstraction of entity 
contaning comman set of properties and 
methods

object is instance of class


"""

class Human:
    def __init__ (self, n, o):
        self.name= n
        self.occupation= o
        
    def do_work(self):
        if self.occupation =="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")
    
    def speaks (self):
        print(self.name,"says how are you?") 

tom = Human("tom cruise","actor")           
tom.do_work ()
tom.speaks ()

maria = Human("maria sharapova","tennis player")
maria.do_work ()
maria.speaks ()


