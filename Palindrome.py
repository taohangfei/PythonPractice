def isPalindrome(s):
    s_i = 0
    e_i = len(s)-1
    while s_i<=e_i and s_i <len(s) and e_i>=0:
        if not s[s_i].isalnum():
            s_i+=1
            continue
        if not s[e_i].isalnum():
            e_i-=1
            continue
        if s[s_i]!=s[e_i]:
            return False
        else:
            s_i+=1
            e_i-=1
    return True

if __name__ == '__main__':
    import sys
    while True:
        a=raw_input("Enter a string: ")
        if isPalindrome(a):
            print "%s is a Palindrome" % a
        else:
            print "%s is not a Palindrome" %a

