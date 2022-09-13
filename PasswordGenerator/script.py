#!/usr/bin/python3 
# Noob Code 
import random

# Global Variables 
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x']
special_characters = ['#', '!', '@', '$', '%', '^', '&', '}', '{']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
password_length = int(input("input the password lenght:"))
string = characters + special_characters + numbers

def password_generator(string, password_length):
    for i in range(password_length):
        final_pass = print(random.choice(string), end='')

password_generator(string, password_length)
