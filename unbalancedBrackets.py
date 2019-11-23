# QID: #3069 
# Goal: Check unbalanced brackets 
#       N lines of input    
#       check brackets in every line of input and print result in Y/N 
#
# Sample Input: 
#   4
#   <[A()B]{}NTU>
#   ())
#   ()[1[2[3[[]
#   [CSIE}


def chk(s):
    di = {
        ')':'(',
        ']':'[',
        '}':'{',
        '>':'<'
        }

    symbolL = di.values()   
    symbolR = di.keys()      
    #print(symbolL)
    #print(symbolR)

    # when seeing a left bracket, put it in the list
    # when seeing a right bracket, look for the paired left bracket in the dictionary 
    # remove the paired left bracket from end of the list
    # if the list becomes empty, all brackets are balanced 

    lst = []
    result = True
    for c in s:
        if c in symbolL:
            lst.append(c)
        elif c in symbolR:          
            if len(lst) < 1:       
                result = False
                break
            elif di[c] == lst[-1]: 
                lst.pop()          
            else:                  
                result = False
                break
        else:                      
            continue
    if lst != []:                  
        result = False
    
    return result


        
n = int(input())

st = []
for i in range(n):
    st.append(input())

for i in st:
    #print(chk(i))     
    if chk(i) == True:
        print('Y')
    else:
        print('N')
