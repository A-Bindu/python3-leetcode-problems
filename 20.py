class Solution:
    def isValid(self, s: str) -> bool:
        #s=" "
        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            elif((i==')' or i==']' or i=='}') and len(st)==0):
                return False
            elif i==')' and st[-1]!='(':
                return False
            elif i==']' and st[-1]!='[':
                return False
            elif i=='}' and st[-1]!='{':
                return False
            else:
                st.pop()
        if len(st)==0:
            return True
        return False