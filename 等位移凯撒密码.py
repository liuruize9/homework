n=input("请输入明文:")
i = 1
for p in n:
      if ord("a") < ord(p) < ord("z"):
            print(chr(ord("a")+((ord(p)-ord("a")+i)%26)-32),end='')
            i = i+1
      elif ord("A") < ord(p) < ord("Z"):
            print(chr(ord("A")+(ord(p)-ord("Z")+i)%26),end='')
            i = i+1
      else:
            print(p,end='')
            i = i+1
