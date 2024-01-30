#  Given a list of words, create a list of their lengths.


original_str = "The quick brown rhino jumped over the extremely lazy fox".split()
original_list = list(original_str)
num_words = len(original_list)
for i in original_list:
    print(len(i))