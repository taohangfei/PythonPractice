class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        print 's is : %s \n p is : %s' %(s,p)
        slice_start = 0
        slice_end = 1
        s_position = 0
        while slice_start<len(p) and slice_end<=len(p):
            if p[slice_start]=='*':
                while slice_end<len(p) and p[slice_end]=='*':
                    slice_end += 1
            else:
                while slice_end<len(p) and p[slice_end]!='*':
                    slice_end += 1
            slice = p[slice_start:slice_end]
            if slice[0]=='*':
                slice_start = slice_end 
                slice_end += 1
                continue
            else:
                flag = False
                while s_position<len(s):
                    flag = False
                    tmp = s_position
                    for i in slice:
                        if tmp >=len(s):
                            print 'No matched string'
                            return False
                        if s[tmp] == i or i=='?':
                            tmp += 1
                            flag = True
                            continue
                        else:
                            print 'not matched at positin %d' %s_position
                            flag = False
                            s_position += 1
                            break
                    if flag:
                        s_position += len(slice)
                        break
                if flag:
                    print 'slice ', slice, ' matched at position', s_position   
                    slice_start = slice_end
                else:
                    return False
                
        if p=='':
            return False
        if s_position < len(s) and p[-1]!='*':
            print 'Not all matched, s still has chars remained'
            return False
        return True

S = Solution()
s = raw_input()
p = raw_input()
print S.isMatch(s,p)
