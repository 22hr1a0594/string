"""
Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
Sample Input:
Cyfuno
Sample Output:
Words: 1
Letters: 6
"""
def fun(string):
    words = string.split()
    word_count = len(words)
    character_count = len(string)
    print(f"Words: {word_count}")
    print(f"Letters: {character_count}")
input_string = input()
fun(input_string)
