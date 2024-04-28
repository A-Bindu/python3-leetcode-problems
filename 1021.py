class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l=[]
        c=0
        for i in range(len(s)):
            if c==0:
                c+=1
            elif c!=0 and s[i]=='(':
                c=c+1
                l.append(s[i])
            elif c==1 and s[i]==")":
                c=c-1
            else:
                c=c-1
                l.append(s[i])
        return "".join(l)
                