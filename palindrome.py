"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #1 - Paul's Palindrome Password (palindrome.py)


Author: Chris Lai

Difficulty Level: 1/10

Prompt: Paul has a brand new autonomous driving RACECAR that requires a password input 
before unlocking and allowing the user to drive. Since Paul can never remember his exact 
password, he set the following rule for a valid password: “If the password given to the 
RACECAR is more than 6 letters long and is a palindrome, unlock the car”. Write a Python
script that it returns “True” if the given password unlocks the car (is more than 6 
characters long and is a palindrome) and returns “False” if the given password is invalid.

Extra Challenge: Solve this problem in 1 line of code! (Excluding function definitions) 

Test Cases:
Input: “racecar”    Output: True
Input: “314156”     Output: False
Input: “dad”        Output: False
"""

class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
        if len(s) > 6:
            new_string = ""
            for index in range(len(s)):
                new_string += s[len(s) - 1 - index]
            if new_string == s:
                return True
            else:
                return False
        else:
            return False
            #type s: string
            #return type: boolean

def main():
    tc1 = Solution()
    tc1.isPalindrome("1234321")
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()