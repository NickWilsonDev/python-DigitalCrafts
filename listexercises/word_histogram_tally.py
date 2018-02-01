# word_histogram_tally.py

def second_element_tuple(tup):
    return tup[1]

msg = list(raw_input("Please enter a sentence: ").split(' '))

histogram = {}

for word in msg:
    if word in histogram:
        histogram[word] = histogram[word] + 1
    else:
        histogram[word] = 1
#print histogram

dict_list = []
for key, value in histogram.iteritems():
    temp = [key, value]
    dict_list.append(temp)

dict_list = sorted(dict_list, key=second_element_tuple, reverse=True)
#print dict_list

if len(dict_list) >= 3:
    print "The top three words are: "
    print dict_list[0]
    print dict_list[1]
    print dict_list[2]
else:
    print "The top word is: "
    print dict_list[0]
