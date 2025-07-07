#!/usr/bin/python3

fruits = [ "mango", "orange", "lemon", "pineapple", "grapes" ]

print(fruits[0])
print(fruits[-1])

new_fruit = input("Which fruit would you like to add to the list?: ")

fruits.append(new_fruit)

print(fruits)

for i in range(len(fruits)):
    print(f"Index: {i} & Fruit: {fruits[i]}")
