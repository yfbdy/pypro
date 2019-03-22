import pandas as pd
import numpy as np

a = pd.Series(data=list("ABC"),index=list("abc"),name="title")
print(a)

b = pd.Series(data=list("ABC"))
print(b)

for _ in b.index:
    print(_,end=' ')

for _ in b.values:
    print(_,end=' ')

print()

t = pd.DataFrame(np.arange(12).reshape(3,4))
print(t)

t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t2)

data = {'name':['AAA','BBB','CCC'],'marks':['100','200','300']}
df = pd.DataFrame(data,index=list("abc"))
print(df)