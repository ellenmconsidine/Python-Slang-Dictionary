#Ellen Considine, TA: Ranga, Assignment 10

def CreateDictionary(filename):
    my_dict = {}
    lines = []
    f = open(filename, 'r') #opening input file
    x = f.readline()
    while x != "":
        lines.append(x)
        x = f.readline()
    f.close() #closing input file
    for i in range(len(lines)):
        key = ""
        value = ""
        for j in range(lines[i].find(',')):
            key = key + lines[i][j]
        for k in range(len(key)+1,len(lines[i])):
            value = value + lines[i][k]
        my_dict[key] = value #making dictionary entries
    return my_dict

def Deslang(str, dict):
    words = str.split(' ')
    English = ""
    for word in words: #building the phrase in English
        if word in dict: #checking if each key is in the dictionary
            English = English + dict[word].strip("\n") + " "
        else:
            English = English + word + " "
    return English


def main():
    #1
    slang_dict = CreateDictionary("textTOEnglish.txt")
    #2
    text = raw_input("Enter a text abbreviation: ")
    if text in slang_dict:
        print Deslang(text, slang_dict)
    else:
        print "Not found"
    text = raw_input("Enter a text abbreviation, or 'quit': ")
    while text != "quit":
        if text in slang_dict:
            print Deslang(text, slang_dict)
        else:
            print "Not found"
        text = raw_input("Enter a text abbreviation, or 'quit': ")
    #3
    text = raw_input("Enter some text abbreviations, separated by a space: ")
    texts = text.split()
    valid = True
    for t in texts:
        if t in slang_dict:
            valid = True
        else:
            valid = False
    if valid:
        print Deslang(text, slang_dict)
    else:
        print "Not found"
    text = raw_input("Enter some text abbreviations, separated by a space, or 'quit': ")
    while text != "quit":
        texts = text.split()
        valid = True
        for t in texts:
            if t in slang_dict:
                valid = True
            else:
                valid = False
        if valid:
            print Deslang(text, slang_dict)
        else:
            print "Not found"
        text = raw_input("Enter some text abbreviations, separated by a space, or 'quit': ")
if __name__ == '__main__':
    main()
