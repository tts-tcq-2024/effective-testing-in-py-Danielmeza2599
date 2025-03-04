
# Daniel Meza
# Jr Embedded Software Developer
# tshirts.py

#Problem: The size function does not correctly handle the case where cms is exactly 38 or 42. 
# According to the current logic, 38 should be 'S' and 42 should be 'L', but the implementation does not.



def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

#tests were added for borderline cases (38 and 42).
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(38) == 'S')  # This should fail because 38 is not handled correctly
assert(size(42) == 'L')  # This should fail because 42 is not handled correctly
print("All is well (maybe!)\n")

#tshirts.py: The test will fail because the edge cases (38 and 42) are not handled correctly.
