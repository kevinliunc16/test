# https://jgirl.ddns.net/problem/0/3069
# ()、[]、{}、<>
#st[0]=<[A()B]{}NTU>
#s='<[A()B]{}NTU>'

def chk(s):
    di = {
        ')':'(',
        ']':'[',
        '}':'{',
        '>':'<'
        }

    symbolL = di.values()   # 左右要相反,出現右邊要當key去找lst中有無成對左邊
    symbolR = di.keys()
    #print(symbolL)
    #print(symbolR)

    lst = []
    result = True
    for c in s:
        if c in symbolL:
            lst.append(c)
        elif c in symbolR:
            if len(lst) < 1:       # 有右邊但lst為空即不成對
                result = False
                break
            elif di[c] == lst[-1]: # 右刮去di找value,跟lst末位同即成對,刪
                lst.pop()
            else:                  # 同上,找value != lst末位,即不成對
                result = False
                break
        else:                      # 非括弧符號跳回最前
            continue
    if lst != []:                  # lst 最後沒 pop 完,即不成對
        result = False
    
    return result
# 以上 chk(s) 結束

# 輸入 n 代表會有 n 行輸入字串        
        
n = int(input())

st = []
for i in range(n):
    st.append(input())
#print(st)

for i in st:
    #print(chk(i))     
    if chk(i) == True:
        print('Y')
    else:
        print('N')
