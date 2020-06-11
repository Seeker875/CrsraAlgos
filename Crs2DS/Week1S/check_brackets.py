# python3

from collections import namedtuple
#Bracket is udf type(given name, char is charcter of text
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, nextElem in enumerate(text):
        if nextElem in "([{":
            #char will be 1 of {[(
            temp =  Bracket(nextElem,i)
            #named tuple bracket in a list
            opening_brackets_stack.append(temp)

        if nextElem in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
                #print(i)
                
            #last element of stack, named tuple
            top =  opening_brackets_stack.pop()


            if not are_matching(top.char,nextElem):
                
                return i+1

    if len(opening_brackets_stack)!=0:
        top =  opening_brackets_stack.pop()
        return top.position+1
    else:
        return "Success"
         

#find_mismatch('{[}')


def main():
    text = input()
    
    mismatch = find_mismatch(text)
    #print(mismatch)
    return mismatch


if __name__ == "__main__":
    print(main())


