# This code implements Newton's method for finding a root(s) of the function
#
# f(x) = x^3 + 4x^2 - 10,
#
# i.e. the value(s) of x for which f(x) = 0.

# The algorithm starts from an initial guess and computes successive improved
# guesses according to the formula:
# 
# x_new = x_old - f(x_old) / f'(x_old)
#
# where f' is the derivative of f.

# The code has 3 parts:
#   1) the function that evaluates f at a given value of x
#   2) the function that evaluates f' at a given value of x
#   3) the iteration loop

# When run, the code should print the iteration number, the new value
# of x, x_new, and the value of f(x_new) at each iteration.

  def f(x):
  # evaluate f at x
  return x**3 + 4*x**2 - 10

def fprime(x)
  # evaluate f' at x
    return 3*x + 8*x

# set initial value
x_initial = 0.1

# perform 10 iterations of Newton's method, printing out 
for i in range(10):
    x_od = x_new
    X_new = x_old - f(x_old) / fprime(x_old)

print(i, x_new, f(x_new))
