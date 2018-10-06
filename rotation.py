def rotated_left_2(s):
    s1 = s[0:2]
    s2  = s[2:len(s)]
    s3 = s2+s1
    print(s3)
    return s3


if rotated_left_2("Hello") == "lloHe":
    print ("correct")
else:
    print("no")
