def fractionToDecimal(numerator, denominator):
    result=""
    result+=str(numerator/denominator)
    remainder = numerator%denominator
    if remainder == 0:
        return result
    float_l = []
    re_dict = {} 
    count = 0
    while remainder!= 0:
        re_dict[remainder]=count
        count += 1
        float_l.append(remainder*10/denominator)
        remainder = (remainder*10)%denominator
        print "remainder:",remainder
        print re_dict
        if remainder in re_dict:
            float_l = float_l[:re_dict[remainder]]+['('] +float_l[re_dict[remainder]:]+[')']
            break
    return result+'.'+''.join(float_l)

fractionToDecimal(int(raw_input()),int(raw_input()))