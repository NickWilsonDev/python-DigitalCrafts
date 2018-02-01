# word_histogram.py

msg = list(raw_input("Please enter a sentence: ").split(' '))

histogram = {}

for word in msg:
    if word in histogram:
        histogram[word] = histogram[word] + 1
    else:
        histogram[word] = 1
print histogram
