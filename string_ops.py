# problem Number one
def f(s):
    try:
        counter = 0
        emptyString = " "
        if s[0] == " ":
            emptyString = s[0]
        else:
            if  s[0] == s[2]:
                emptyString = s[0] + s[1]

            elif s[0] == s[3]:
                emptyString = s[0] + s[1] + s[2]
            else:
                emptyString = s
            counter = s.count(emptyString)
        tuple = (emptyString,counter)
        return tuple
    except:
        print("Value Error")

# problem Number two
def solve (a,b):
    try:
        asterix = "*"
        if a == b :
            print(True)
        elif "*" in a :
            if (len(a) - 1) <= len(b):
                return True
            else:
                return False
        else:
            return False 
    except:
        print("Value Error")


# problem number three
def is_palindrome(string):
    if string == string[::-1]:
            return True
    else:
        return False

# problem Number four find nth occurrence
def find_nth_occurrence(substring, text, occurrence=1):
    text = "This is an example. Return the nth occurrence of example in this example string example." 
    
    dic = {}
    y = text.rfind(substring)
    counter = text.count(substring)
    if occurrence > counter or occurrence < 1  :
        print (-1)
    else:
        while y != -1:
            while counter != 0:
                dic.update({counter:y})
                counter -=1
                y = text[:y].rfind(substring)
            #print(dic)
            c = dic.get(occurrence)
            return c
    #string = "This is an example. Return the nth occurrence of example in this example string example."    
