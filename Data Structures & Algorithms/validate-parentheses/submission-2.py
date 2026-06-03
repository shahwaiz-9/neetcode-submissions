class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 0:
            return True

        for i in range (len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                print(stack)
            else:

                if len(stack) == 0:
                    return False
                
                if s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop() 
                    continue
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop() 
                    continue
                else:
                    return False         
        if len(stack) == 0:
            return True
        else:
            return False                 


        