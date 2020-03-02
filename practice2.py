import copy

def main():
    #1
    print("-------------------1------------------")
    row2=['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
    ptable1=["H", "Xe", row2]
    #it will create shallow copy
    ptable2=ptable1[:]

    #both of them are list
    print(str(type(ptable1)) + " " + str(type(ptable2)))
    print(row2)
    print(ptable1)
    print(ptable2)

    '''it would not change ptable1 since it was a shallow copy
        it will create new instance for ptable2'''
    ptable2[1] = "He"

    print(row2)
    print(ptable1)
    print(ptable2)

    #Since row2 refence to both ptables, the change will
    #effect all of them
    ptable2[-1][-1] = "Ne"

    print(row2)
    print(ptable1)
    print(ptable2)
    
    #2
    print("-------------------2------------------")

    row2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
    ptable1 = ["H", "Xe", row2]
    ptable2=copy.deepcopy(ptable1)

    #Since we created a deepcopy changes it would not affect rest
    ptable2[-1][-1] = "Ne"
    print(row2)
    print(ptable1)
    print(ptable2)
    
    #3
    print("-------------------3------------------")

    #it will create shallow copy
    a = [1,2,3]
    b = list(a)

    print(a)
    print(b)

    b[1] = 3

    print(a)
    print(b)
    
    #4
    print("-------------------4------------------")

    word = input()
    shift = int(input())
    for i in word:
        normalize_char(i, shift)

    #5
    print("-------------------5------------------")
    #combining words letter by letter
    word_1 = input("Enter Word 1")
    word_2 = input("Enter Word 2")
    
    new_word = ""
    for i in range(len(word_1)):
        new_word += word_1[i] + word_2[i]
    print(new_word)

    #7
    print("-------------------7------------------")

    number = input("Enter a number")
    condition = []
    for i in range(len(number)):
        condition.append((i + 2 <= len(number) - 1) and (number[i] == number[i + 2]))



def normalize_char(val, shift):
    temp = ord(val) #converts to ascii values
    if val.islower(): #checks whether characters lowercase or not
        temp = temp - 32 # make the same level with uppercase characters
    temp = temp - 65 # put characthers between 0 to 64

    char = ((temp + shift) % 26) + 65 #shift characters if exceeds alphabet lengts
    if val.islower(): #ascii to characters again
        char = char + 32
    print(chr(char), end="")

if __name__ == "__main__":
    main()