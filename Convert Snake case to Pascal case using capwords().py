import string

test_str = 'rahul_sharma_is_best'

print("The original string is : " + test_str)

res = string.capwords(test_str.replace("_", " ")).replace(" ", "")

print("The String after changing case : " + str(res))