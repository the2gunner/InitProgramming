names = { 0:"ዜሮ",1:"አንድ",2:"ሁለት",3:"ሶስት",4:'አራት',5:'አምስት',6:'ስድስት',7:'ሰባት',8:'ስምንት',9:'ዘጠኝ',10:'አስር',11:'አስራ አንድ',\
            12:'አስራ ሁለት',13:'አስራ ሶስት',14:'አስራ አራት',15:'አስራ አምስት',16:'አስራ ስድስት',17:'አስራ ሰባት',18:'አስራ ስምንት',19:'አስራ ዘጠኝ',\
            20:'ሃያ',30:'ሰላሳ',40:'አርባ',50:'ሃምሳ',60:'ስልሳ',70:'ሰባ',80:'ሰማንያ',90:'ዘጠና'}
try:
    num=int(input("ቁጥር አስገባ:\n"))
    if num <= 100:
        if num in names:
            k = names.get(num)
            print(k)
        else:
            b = num % 10
            b = names.get(b)
            c = num // 10
            c = c * 10
            c = names.get(c)
            result = c + b
            print(result)
    elif num < 1000:
        if num % 100 == 0:
            a = names.get(num // 100)
            print(a + " መቶ")
        else:
            jj = names.get((num - (num % 100)) // 100)
            new_num = num - (num - (num % 100))
            l = new_num % 10
            l = names.get(l)
            m = new_num - (num % 10)
            m = names.get(m)
            final = jj + " መቶ " + m + f" {l}"
            print(final)

except:
    print("እባክዎ ትክክለኛ ቁጥር ያስገቡ እና እንደገና ይሞክሩ")
