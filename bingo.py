import random

class Bingo:
    def __init__(self,num):
        Bingo.all = num*num
    def b_random(self):
        bingolist = list(range(1,Bingo.all+1))
        random.shuffle(bingolist)
        return bingolist
    def index_li(self,binposition):
        b_num = int((input('數字：')))
        while b_num not in li or li.index(b_num)+1 in binposition :
            if b_num not in li:
                print('不在賓果範圍內')
            else :
                print('已輸入過此數字')
            b_num = int(input('請再次輸入數字：'))
        return li.index(b_num)+1
    def allyoko(self,atama) :
        yoko = []
        while len(yoko) != kazu :
            yoko.append(atama)
            atama += 1
        return yoko
    def alltate(self,atama) :
        tate = []
        while len(tate) != kazu :
            tate.append(atama)
            atama += kazu
        return tate
    def hnaname(self,atama) :
        naname = []
        while len(naname) != kazu :
            naname.append(atama)
            atama += (kazu+1)
        return naname
    def mnaname(self,atama) :
        naname = []
        while len(naname) != kazu :
            naname.append(atama)
            atama += (kazu-1)
        return naname

kazu = int(input('請輸入寬度：'))        
while kazu < 3 or kazu > 10 :
    kazu = int(input('請輸入3~9：'))
    
bingo = Bingo(kazu)
li = bingo.b_random()
# 隨機排序數字
j=1
for i in li :
    if j % kazu != 0 :
        print('{0:>3}'.format(i),end='')
        j+=1
    else:
        print('{0:>3}'.format(i),'\n',end='')
        j+=1
# 賓果排版

allsen = []
yokoatama = 1
while len(allsen) != kazu:
    allsen.append(bingo.allyoko(yokoatama))
    yokoatama += kazu
# allsen = 所有線組合

tateatama = 1
while len(allsen) != kazu*2 :
    allsen.append(bingo.alltate(tateatama))
    tateatama += 1
    
allsen.append(bingo.hnaname(1))
allsen.append(bingo.mnaname(kazu))

binposition = []
binwake = []
line = 0

from itertools import combinations
while line < 2 :
    line = 0
    li_list = bingo.index_li(binposition)
    # bingo.index_li() = 輸入賓果數字 回傳該數字位置
    # li_list = 該數字的位置
    
    binposition.append(li_list)
    binposition.sort()
    # binposition = 輸入過的數字照大小排列
    
    binwake = list(combinations(binposition,kazu))
    # binposition = 照kazu個數分組
    
    a=0
    while a != len(binwake) :
        binwake[a] = list(binwake[a])
        a+=1
    # list化binwake裡面的值 （原本是tuple）
    
    for i in allsen:
        for j in binwake:
            if i == j:
                line += 1
                    
    if line == 1 :
        print('1條線')
        line = 0
    elif line == 0 :
        print('目前還沒有線')

print('\n賓果～')
print(f'共{line}條線')