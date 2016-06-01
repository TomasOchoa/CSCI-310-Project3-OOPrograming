# CSCI 310 Organization of Programming Languages, Spring 2014
# Program #3: Procedural Programming
# Author: Tomas Ochoa
# Date Due: 20 April 2015
#
# This program illustrates the procedural programming paradigm.
"""
    Function:   hlbackwards
    Paramaters: A list entered by the user

    Purpose:    This function takes a list from the console and reverses it
                and prints it back out.

                *NOTE* This function does not reverse the list with sublists
                       (The next function does)
"""
def hlbackwards(input_list):
    length = len(input_list)
    s = length
    new_list = [None]*length
    for item in input_list:
        s = s - 1
        new_list[s] = item
    return new_list
#-------------------------------------------------------------------------------------------
"""
    Function:   llbackwards
    Parameters: A list entered by the user

    Purpose:    This function takes a list from the console and reverses it
                and prints it back out, this time INCLUDING sublists.
"""
def llbackwards(input_list):
    reversed_list = []
    for sublist in input_list:
        if isinstance(sublist, list):
            reversed_list.append(llbackwards(sublist))
        else:
            reversed_list.append(sublist)

    reversed_list.reverse()
    return reversed_list

# Helper function to Check if a list
def is_list(input_list):
    return isinstance(input_list, list)
#-------------------------------------------------------------------------------------------
"""
    Function:   palindrome
    Parameters: A list entered by the user

    Purpose:    This function takes a list from the user and determines if it is
                a palindrome or not. If it is, then it returns the original list,
                else it makes it a palindrome
"""
def palindrome(input_list):
    # this is the list reversed (to check compare with original list)
    reversed_input_list = llbackwards(input_list)
    # compare
    if input_list == reversed_input_list:
       return input_list
    else:
        head, *tail = reversed_input_list
        #print(tail)
        #input_list.append(tail)
        pal = input_list + tail
        return pal
#-------------------------------------------------------------------------------------------
"""
    Function:   permutations
    Parameters: A list entered by the user

    Purpose:    This function takes a list as input and generates a list containing all possible
                permutations of the list elements.
"""
def permutations(input_list):
    from itertools import permutations
    perms = []
    var = permutations(input_list)
    for perm in var:
        perms.append([perm])
    return  perms
#-------------------------------------------------------------------------------------------
"""
    Function:   ionah
    Parameters: An integer

    Purpose:    This function takes a list as input and solves the infamous towers
                of hanoi problem
"""
# Helper function that does ionah
def doIonah(n,to,From,u):
    def print_move(From,to):
        print("Move disk from peg '{}' to peg '{}'".format(From,to))
    if n > 0:
        doIonah(n-1,u,From,to)
        print_move(From,to)
        doIonah(n-1,to,u,From)
# Main function that calls the helper
def ionah(n):
    doIonah(n,3,1,2)
#-------------------------------------------------------------------------------------------
"""
    Function:   sequence
    Parameters: An integer

    Purpose:    This functions takes in a single integer as input and prints out a
                list containing that many terms of the sequence defined by the given sequence

                sn = { 0 if n = 1
                     { 1 if n = 2
                     { 2(Sn - 1) + (Sn - 2) if n > 2
"""
def sequenceDefinition():
    if n == "suc"
# Helper function that defines the sequence and returns each Sn
def sequenceDefinition(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        N = 0
        N = 2 * sequenceDefinition(n - 1) + sequenceDefinition(n - 2)
        return N
# Main function
def sequence(n):
    seq_list = []
    if n == 1:
        return [0]
    elif n == 2:
        return [1]
    elif n > 2:
        # Store the value of the seqDef and append to a list recursively
        N = [sequenceDefinition(n)]
        seq_list = N + sequence(n - 1)
    return seq_list

print("hello?")
print("hello?")
print("yes?")
print("really?")
print("hello?")
print("your final exam you say?")
print("Listen come to room 319 and a half at 4 oclock tmrw?")
print("you heard me/ and hang up"?")
#-------------------------------------------------------------------------------------------
"""
    Function:   argue
    Parameters: A list entered by user

    Purpose:    This functions takes in a list as input and changes the pronouns to negate
                them thus creating a simple AI that argues with the user.
"""
def argue(sentence):
    for i in range(0,len(sentence)):
        if sentence[i] == 'you':
            sentence[i] = 'i'
        elif sentence[i] == 'i':
            sentence[i] = 'you'
        elif sentence[i] == 'am':
            sentence[i] = 'are not'
        elif sentence[i] == 'are':
            sentence[i] = 'am not'
        elif sentence[i] == 'are not':
            sentence[i] = 'am'
        elif sentence[i] == 'is':
            sentence[i] = 'is not'
        elif sentence[i] == 'is not':
            sentence[i] = 'is'
        elif sentence[i] == 'your':
            sentence[i] = 'my'
        elif sentence[i] == 'my':
            sentence[i] = 'your'
        elif sentence[i] == 'does':
            sentence[i] = 'does not'
        elif sentence[i] == 'does not':
            sentence[i] = 'does'
    return sentence
#-------------------------------------------------------------------------------------------
"""
    Function:   bubblesort
    Parameters: A list entered by user

    Purpose:    This functions takes in a list as input and sorts it via the bubblesort
                algorithmic
"""
def bubblesort(input_list):
    temp = []
    for nextNum in range(len(input_list) - 1, 0 , - 1):
        for i in range(nextNum):
            if input_list[i] > input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp

    return input_list
