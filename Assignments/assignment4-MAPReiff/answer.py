 #!/usr/bin/python

# I pledge my honor that I have abided by the Stevens Honor System

"""
Python  Functions
"""

def valid_brackets(s):
      """
      Finish the function valid_brackets() to solve the following question.

      Given a string s containing just the characters '(', ')' determine if the input string is valid.
      An input string is valid if:
      1.All brackets are closed in the correct order.
      2.Open bracket must be placed before close bracket.

      Example 1:
       Input: s = "()"
       Output: True
      Example 2:
       Input: s = "("
       Output: False
      Example 3:
       Input: s = "(()"
       Output: False
      Example 4:
       Input: s = ")("
       Output: False
      Example 5:
       Input: s = "()()"
       Output: True
      Example 6:
       Input: s = "(()())"
       Output: True
      Example 7:
       Input: s = ""
       Output: True
      """

      brackets = list(s)  # split the input
      log = []  # var to save open brackets

      for i in range(len(brackets)):
          if brackets[i] == "(":  # if it is an open bracket
            log.append(brackets[i])  # add to the log
          else:  # if it is a closing bracket
            if len(log) == 0:  # if the log is empty
              return False  # it is false
            else:
              log.pop()  # remove from log var
      if len(log) == 0:  # if the log is empty
          return True  # it is true
      else:
          return False  # if the log is not empty, it is false




def is_prime(n):
      """
      Finish the function is_prime() to solve the following question.

      Given a number n determine if the number string is Prime number.

      Example 1:
          Input: n = 1
          Output: False

      Example 2:
          Input: n = 2
          Output: True

      Example 3:
          Input: n = 6
          Output: False

      Example 4:
          Input: n = 97
          Output: True

      Example 5:
          Input: n = 9973
          Output: True

      """
      number = int(n)  # string to int

      if number > 1:  # prime must be more than 1
        for i in range(2, number):  # loop from 2 until input number
          if (number % i) == 0:  # check if input number is divisible by i
            return False
        else:
          return True
      else:  # less than 1 is not prime
        return False
        



def GCD(a, b):
      """
      Finish the function GCD() to solve the following question.

      Find Greatest Common Divisor of two positive integer a and b. 

      Example 1:
          Input: a = 6 , b = 12
          Output: 6

      Example 2:
          Input: a = 9 , b = 12
          Output: 3

      Example 3:
          Input: a = 42 , b = 12
          Output: 6

      Example 4:
          Input: a = 97 , b = 7
          Output: 1
      """

      if a > b:  # determine which input var is lowest
        low = b
      else:
        low = a

      for i in range(1, low + 1):  # loop from 1 until lowest input var
        if ((a % i == 0) and (b % i == 0)):  # if both are divisible by i
          gcd = i
        # no need for an else
        
      return gcd