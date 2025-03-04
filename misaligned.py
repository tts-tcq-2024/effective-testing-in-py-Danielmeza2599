
# Daniel Meza
## Jr Embedded Software Developer
### misaligned.py



#Problem: The print_color_map function is not aligning the indexes correctly. 
# The calculation i * 5 + j is not correct for the expected alignment.


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)


#a test has been added to verify that the indexes are correctly aligned.
# Additional test to check alignment
expected_output = [
    "0 | White | Blue",
    "1 | White | Orange",
    "2 | White | Green",
    "3 | White | Brown",
    "4 | White | Slate",
    "5 | Red | Blue",
    "6 | Red | Orange",
    "7 | Red | Green",
    "8 | Red | Brown",
    "9 | Red | Slate",
    "10 | Black | Blue",
    "11 | Black | Orange",
    "12 | Black | Green",
    "13 | Black | Brown",
    "14 | Black | Slate",
    "15 | Yellow | Blue",
    "16 | Yellow | Orange",
    "17 | Yellow | Green",
    "18 | Yellow | Brown",
    "19 | Yellow | Slate",
    "20 | Violet | Blue",
    "21 | Violet | Orange",
    "22 | Violet | Green",
    "23 | Violet | Brown",
    "24 | Violet | Slate"
]

# This will fail because the alignment is incorrect
assert(print_color_map() == expected_output)
print("All is well (maybe!)\n")

#misaligned.py: The test will fail because the indexes are not correctly aligned.
