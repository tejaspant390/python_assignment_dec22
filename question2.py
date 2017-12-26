# a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after
# sorting them alphabetically

word = str(input("Enter the word separated by comma : "))

sorted_word = sorted(word.split(','))
final_word = ",".join(sorted_word)

print(final_word)