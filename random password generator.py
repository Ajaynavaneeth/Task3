#random password generator
print("********PASSWORD GENERATOR********")
#importing random module for the random generation
import random
#getting length for the random password 
l=int(input("Enter the length of password needed : "))
#assingning the what are the characters should be in password
lo="abcdefghijklmnopqrstuvwxyz"
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
sym="!@#$%^&*()_+{}[];:<>?/="
password=""
#assigning the variable that contains the all the types in it
pas=lo+up+num+sym
#sample()-inbuild module return random sequence with the length that we needed
password=password.join(random.sample(pas,l))
print("The random password generated is ",password)

