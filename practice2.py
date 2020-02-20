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

    
if __name__ == "__main__":
    main()