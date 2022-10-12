# Letter of words:
# The program that prints the words with the first letter 'a' out of 10 words entered on the keyboard.
# Klavyede girilen 10 kelimeden ilk harfi 'a' olan kelimeleri yazdıran program.

mList = []

for i in range(3):
    word = input("Enter word: ")
    if word[0] == "a":
        mList.append(word)

for isim in mList:
    print(isim)

print("Words starting with 'a' =", len(mList))