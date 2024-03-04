word_list = []
for i in range(10):
    word = input("Tu palabra " + str(i+1) + ": ")
    word_list.append(word)
print("Tus palabras son:")
for word in word_list:
    print(word)