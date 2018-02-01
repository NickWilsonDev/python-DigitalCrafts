# String_ex.py

str = "hello nick"
print str.upper()


print str.lower()


print str.capitalize()


print ''.join(reversed(str))


def leetspeak(str):
    leet_str = ""
    length = len(str)
    i = 0
    while i < length:
        if str[i] == 'A':
            leet_str += '4'
            i += 1
        elif str[i] == 'E':
            leet_str += '3'
            i += 1
        elif str[i] == 'G':
            leet_str += '6'
            i += 1
        elif str[i] == 'I':
            leet_str += '1'
            i += 1
        elif str[i] == 'O':
            leet_str += '0'
            i += 1
        elif str[i] == 'S':
            leet_str += '5'
            i += 1
        elif str[i] == 'T':
            leet_str += '7'
            i += 1
        else:
            leet_str += str[i]
            i += 1
    return leet_str

print leetspeak("NICK")

def long_vowels(str):
    newstr = ""
    length = len(str)
    i = 0

    while i < length:
        if i > 0:
            if str[i] == 'o' and str[i - 1] == 'o':
                newstr += 'o' * 3
                newstr += str[i]
                i += 1
            elif str[i] == 'e' and str[i - 1] == 'e':
                newstr += 'e' * 3
                newstr += str[i]
                i += 1
            else:
                newstr += str[i]
                i += 1
        else:
            newstr += str[i]
            i += 1
    return newstr

print long_vowels("good")
