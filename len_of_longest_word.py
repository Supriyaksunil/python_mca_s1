def length(words):
    return max(len(word)for word in words)
word_list=input("Enter a list of words separated by space:").split()
print("length of longest word:",length(word_list))