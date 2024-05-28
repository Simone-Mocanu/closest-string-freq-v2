import random


#input
strings = ["cotal", "pomap", "pitll", "simnp", "slbap"]
solution_string = ""

#hamming_dist calculates the hamming distance between two strings with the same length
def hamming_dist(s1, s2):
    if len(s1) != len(s2):
        raise Exception("Length of string1 is not equal to the length of string2")

    length = len(s1)

    if length <= 1:
        raise Exception("Length must be greater than 1")

    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

length = len(strings[0])
for string in strings:
    if len(string) != length:
        raise Exception("All strings should have the same length")
    
#hda - hamming distances array
hda = []

#populate the hamming distance array
for i in range(length):
    hda.append(0)

#lfda - letter frequency dictionary array
#populate lfda
lfda = []
for i in range(length):

    lfd = {}
    #i - index of string(letter)
    # lfd - letter frequency dictionary
    for string in strings:
        if string[i] not in lfd:
            lfd[string[i]] = 1
        else:
            lfd[string[i]] += 1

    # print(lfd)

    #hhd - highest hamming distance
    hhd = list(lfd.values())[0]

    #get the hhd value in each array
    for key, value in lfd.items():
        if hhd < value:
            hhd = value

    #populate the array(char_arr) with characters that have the hhd
    char_arr = []
    for key, value in lfd.items():
        if value == hhd: 
            char_arr.append(key)

    #if we got more than one character with the hhd, we select one of the characters randomly
    #else we select the only character in the array
    if len(char_arr) > 1:
        solution_string += random.choice(char_arr)
    else:
        solution_string += char_arr[0]

    #ssl - solution string length
    ssl = len(solution_string)
    #tsa - temporary string array
    tsa = []
    for string in strings:
        temp_str = ""
        for j in range(len(solution_string)):
            temp_str += string[j]

        tsa.append(temp_str)

    print("solution string: " + solution_string)   

print("")
print("Hamming distances between the solution string and the input")
print("-------------------------")
for string in strings:
    print(solution_string, string, hamming_dist(solution_string, string))


print("-------------------------")

