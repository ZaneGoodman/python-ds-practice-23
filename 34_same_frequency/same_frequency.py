def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) == len(num2):
        if {i: num1.count(i) for i in num1} == {j: num2.count(j) for j in num2}:
            return True
        return False
    else: return False
        
        


