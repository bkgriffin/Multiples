#!/usr/bin/python
#
# author: Brandon Griffin <brandon.k.griffin@gmail.com>
# ver:    0.1
# date:   11/25/13
#
#
#
# Project Euler:
#
# - Multiples of 3 and 5 -
#
# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

class Multiples:
    """
        Multiples class.
        Tests for multiple of numbers.
        """
    # Multiples attributes.
    
    # Determines if an X and Y is a multiple of Number.
    def MultipleOfBoth(self, X, Y, number):
        if X % number == 0 and Y % number == 0:
            return True
        else:
            return False

    # Finds a sum of multiple 'X' in the range from 1..n.
    def SumOfMultiples(self, X, n):
        totalSum = 0
        for i in xrange(0, n):
            if i % X == 0:
                totalSum += i
                print 'Total Sum: ' + str(totalSum)
        return totalSum

    # Finds the sum of both multiples in the range from 1..n.
    def SumOfBothMultiples(self, X, Y, n):
        totalSum = 0
        for i in xrange(0, n):
            if i % X == 0 and i % Y == 0:
                totalSum += i
                print 'Total Sum Subtracted: ' + str(totalSum)
        return totalSum

# Main entry point.
def main():
    multipleMachine = Multiples()
    print (multipleMachine.SumOfMultiples(3, 1000) + multipleMachine.SumOfMultiples(5, 1000) - multipleMachine.SumOfBothMultiples(3, 5, 1000))

if __name__ == "__main__":
    main()