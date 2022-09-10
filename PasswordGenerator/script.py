#!/usr/bin/python3
# Noob code
import random

# Global Variables
characters = ['a', 'b', 'c', 'd', 'e', 'f']
special_characters = ['#', '!', '@', '^', '&', '$', '{', '}']
numbers = ['1', '2', '3', '4', '5', '6']
string = characters + special_characters + numbers

def password_generator(string):
    for i in range(20):
        print(random.choice(string), end='')

password_generator(string)

