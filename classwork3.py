def slices():
    text = "everything is pathetic"
    alist = list(text)
    print("Character List: ", alist)
    word1 = alist[0:10]
    word2 = alist[11:13]
    word3 = alist[14:23]

    print("Word 1: ", ''.join(word1))
    print("Word 2: ", ''.join(word2))
    print("Word 3: ", ''.join(word3))
def main():
    slices()
if __name__ == "__main__":
    main()        
