
# Python Operators

#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators



# 1.  Arithmetic operators

# Name            Operator

#.Additon         =>   +       
#.Subtraction     =>   -
#.Multiplication  =>   *
#.Division        =>   /
#.Modulus         =>   %
#.Exponentiation  =>   **
#.Exponentiation  =>   //


# Example Code

a = 10

b = 30

print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)



# 2. Assignment operators

# Name                       Operator

#.Simple assignment          => =
#.Add and assign             => +=
#.Subtract and assign        => -=
#.Multiply and assign        => *=
#.Divide and assign          => /=
#.Modulus and assign         => %=
#.Exponentiation and assign  => **=
#.Floor division and assign  => //=

# Example code 

a = 30        

print(a)


a = 20 

a += 30

print(a)


a = 30

a -= 49

print(a)


a = 39

a *= 77

print(a)



a = 44

a  /= 55

print(a)


a = 44

a %= 55

print(a)


a = 66

a **= 77

print(a)


a = 22

a //= 33

print(a)



# 3.  Comparison operators

# Name                        Operator

#.Equal                       =>  ==
#.Not equal                   =>  !=
#.Greater than                =>  >
#.Less than                   =   <
#.Greater than or equal to    =>  >=
#.Less than or equal to       =>  <=


# Example code

c = 20

d = 20

print(c == d)


c = 40

d =  30

print(c != d)


c = 33

d = 30

print(c > 30)


c = 20

d = 30

print(c < d)


c = 10

d = 10

print(c >= d)


c = 8 

d = 12

print(c <= d)




# 4. Logical operators

# Description                                               Operator

#.Returns True if both statements are true                  => and
#.Returns True if one of the statements is true             => or
#.Reverse the result, returns False if the result is true   => not


# Example code



e = 10
f = 20

print(e > 5 and f > 15)


e = 10

f = 20

print(e > 15 or f > 15)


e = 10

print(not(e > 5))



# 5.Identity operators

#Description                                              Operator                     

#.Returns True if both variables are the same object      => is
#.Returns True if both variables are not the same object  => is not


# Example code

g = [1,2,3]

h = [1,2,3]

g = h

print(g is h)



g = [1,3,5]

i = [1,2,3]

g = i

print(g is not i)



# 6.Membership operators

#Description                                                                         Operator

#.Returns True if a sequence with the specified value is present in the object       => in
#.Returns True if a sequence with the specified value is not present in the object   => in not


# Example code

color = ["black" , "pink" , "red"]

print("black" in color)
print("pink" in color)


book = ["urdu" , "english" , "G.K"]

print("urdu" not in book)




# 7.Bitwise Operators

#Operator   Name                    Description

#. &        AND  	                Sets each bit to 1 if both bits are 1		
#. |	    OR	                    Sets each bit to 1 if one of two bits is 1	
#. ^	    XOR	                    Sets each bit to 1 if only one of two bits is 	
#. ~	    NOT	                    all the bits	
#. <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
#. >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	



# Example code 


j = 7

k = 9

print(j & k)

j = 7

k = 9

print(j | k)

j = 5

k = 3

print(j ^ k)


k = 9

print(~ k)


j = 7

k = 9

print(j << k)


j = 7

k = 9

print(j >> k)
