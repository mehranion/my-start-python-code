pali = str(input())
pali = pali.lower()
ipal = ''
for i in range(len(pali)):
    ipal = ipal + pali[len(pali)-i-1]
if pali == ipal:
    print('palindrome')
else:
    print('not palindrome')

