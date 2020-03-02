import re

def capt_first_letter():
    #sentence = input()
    #split = sentence.split(" ")
    print([i[0].upper() + i[1:] for i in input().split(" ")])

def count_char(dic, key):
    if key in dic:
        dic[key] = dic[key] + 1
    elif key is " ":
        pass
    else:
        dic[key] = 1

def occurence():
    sentence = input()
    factor = int(input())
    mod = len(sentence) / factor
    
def subs():
    #substitution
    #"abc def ghi" -> "word word word"
    k = "abc def ghi"
    f = re.sub("\w+", "word", k)
    print(f)

def split_f():
    #split 
    #"1+2x*3-y" -> 1 2x 3 y
    f = "1+2x*3-y"
    g = re.split("[+\-*/]", f) 
    print(g)

def find_pattern():
    k = "123:456,7891-1356"
    g = re.findall("\d{3}", k)
    print(g)

def groupping():
    k = "sukru eraslan s143 cng445"
    #(\w+ \w+) (\w+) (\w+)
    g = re.match("(\w+ \w+) (\w+) (\w+)", k).groups()
    print(g)

def test():
    a = 5
    b = 0
    try:
        print(a/b)
    except Exception as e:
        print(e)

def main():
    #dic = {}
    #sentence = input()
    #for key in sentence:
    #    count_char(dic, key)
    #test()


if __name__ == "__main__":
    main()

#\d{3}-\d{3}-\d{4}
#-\d{3}-\d{3-7}-\d{4}