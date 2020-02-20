def main():
    #1
    print("--------------1---------------")

    a_str = "acd"
    print(a_str[1]) #displays 1 character which is 'c'
    
    #since strings are non mutable objects, it will throw error
    #a_str[1] = 'b'

    a_list = [1,3,2,4]
    ''' since list are mutable object, it will not throw error,
        and change the value'''
    a_list[1] = 2

    print(a_list)

    #2
    print("--------------2---------------")

    row1 = ["H", "He"]
    row2 = ["Li","Be","F","Ar"]
    row3 = ["Na","Mg","Cl","Ne"]
    
    '''ptable will refer to row1, any changes on row1 or ptable 
        both of them will have the same changes
    '''
    ptable = row1
    #it will copy the content of row2 to ptable
    ptable.extend(row2)
    ptable.extend(row3)

    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

    #Changes will be only row2
    row2[-1] = "Ne"

    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

    #row1 and ptable will be affected now row3
    ptable[-1] = "Ar"

    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

    #3
    print("--------------3---------------")

    row1 = ["H","He"]
    row2 = ["Li","Be","F","Ar"]
    row3 = ["Na","Mg","Cl","Ne"]
    ptable = [row1]
    ptable.append(row2)
    ptable.append(row3)

    #ptable will have the references of both row2 & row3
    
    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

    #changes will affect both row2 & ptable
    row2[-1] = "Ne"
    
    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

    #changes will affect both row3 & ptable
    ptable[-1][-1] = "Ar"

    print(row1)
    print("-------------------")
    print(row2)
    print("-------------------")
    print(row3)
    print("-------------------")
    print(ptable)

if __name__ == "__main__":
    main()