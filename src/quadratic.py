'''This solves ax**2+bx+c=0 and returns the result(s)'''

import numpy as np 

a =  float(input('enter a: '))
b =  float(input('enter b: '))
c = float(input('enter c: '))

disc = np.sqrt(b**2-4*a*c)
if disc < 0:
   print("the solution is not real")
else:
    solution_1= (-b + np.sqrt(b**2-4*a*c))/(2*a)
    solution_2= (-b - np.sqrt(b**2-4*a*c))/(2*a)
    print(solution_1,solution_2)
    print("solution 1 is {} and solution 2 is {}.".format(solution_1, solution_2))


