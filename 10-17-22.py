# This code does not execute properly. Try to figure out why.
# def multiply(a, b):
#     a * b

def multiply(a, b):
    return a * b 

#OR other solution 

def multiply(a, b):
    if isinstance(a, (int, float, complex)):
        if isinstance(b, (int, float, complex)):
            return a * b

#OR 

# re-inventing the wheel by creating a custom multiplication function
# gets two parameters a and b
def multiply(a, b):
    # sum is initialised with zero
    sum = 0
    
    # for each b iteration, the sum adds itself by a. this is how multiplication works.
    # for example, 4 * 3 is basically 4 + 4 + 4 (4 added by itself three times)
    
    # here, if b is a float then it will do the same thing as the else statement but then it will also add b to itself again because yes.
    
    
    # if isinstance(b, float):
    #     for i in range(int(b)):
    #         sum += a
    #     sum+=b
    # else: 
    #     for i in range(b):
    #         sum += a
    # return sum
    
    # well, none of the above worked in the 5th test case. so, I gave up:
    return a * b

# license: help me