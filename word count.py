text=input("koi sentance likho :")
word= text.split()  #space se toda aage
char_count= len(text)
word_count= len(word)

print(" \n ===Result===")
print(f"Total word:{word_count}")
print(f"Total characters: {char_count}")
print(f"Average word length: {char_count/word_count:.2f}")