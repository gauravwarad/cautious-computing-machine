class Solution:
    def decodeString(self, s: str) -> str:
        op = ""
        stacku = []
        i = 0
        while i < len(s):
            print("beginning of outer while")
            print(stacku)
            print(s[i])
            if s[i] == ']':


                # while len(stacku) > 0 and stacku[-1] != '[':
                j = stacku.pop()
                print("j is, ", j)
                # j has the chars
                # if stacku[-1] == '[':
                stacku.pop() # the [
                k = int(stacku.pop())
                print("k is, ", k)
                # k has the integer
                if len(stacku) > 0 and stacku[-1].isalpha():
                    temp = stacku.pop()
                    stacku.append(temp + j*k)
                else:
                    stacku.append(j*k)

                i += 1

            elif s[i] == '[':
                stacku.append(s[i])
                i += 1
                # possibliities ==> i is int or i is char
            elif s[i].isdigit():
                k = ""
                while i < len(s) and s[i].isdigit():
                     k = k + s[i]
                     i += 1
                stacku.append(k)

            elif s[i].isalpha():
                j = ""
                while i < len(s) and s[i].isalpha():
                    j = j + s[i]
                    i += 1
                if len(stacku) > 0 and stacku[-1].isalpha():
                    temp = stacku.pop()
                    stacku.append(temp + j)
                else:
                    stacku.append(j)

        return "".join(stacku)
    
    def decodeString2(self, s: str) -> str:
        # what needcode did ---
        stacku = []
        for i in s:
            if i != ']':
                stacku.append(i)
            else:
                # get the string
                substr = ""
                while stacku[-1] != '[':
                    substr = stacku.pop() + substr
                
                print("the substring here is, ", substr)
                stacku.pop() # popping the [

                # getting the number k
                k = ""
                while len(stacku) > 0 and stacku[-1].isdigit():
                    k = stacku.pop() + k
                
                stacku.append(int(k)*substr)
                print("the stack is ,", stacku)

        return "".join(stacku)


# s = "3[a]2[bc]"
s = "3[a2[c]]"
# s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(Solution().decodeString(s))