# Question 1

#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

#before
def reverse_words(str):
  strList = []
  for word in str.split(' '):
      strList.append(word[::-1])
  return ' '.join(strList)


#after
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

#question 2

#https://www.codewars.com/kata/525f50e3b73515a6db000b83

#before
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)

#after
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)