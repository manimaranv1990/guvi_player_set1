def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

mystr = input("Enter a String:")
print("Given String: ", mystr)
print("Reversed String: ", reverse(mystr))
