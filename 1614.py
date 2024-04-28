class Solution:
    def maxDepth(self, s: str) -> int:
        #s = "(1+(2*3)+((8)/4))+1"
        st=[]
        m=0
        for i in s:
            if i=='(':
                st.append(i)
            elif i==')':
                st.pop()
            if len(st)>m:
                m=len(st)        
        return m