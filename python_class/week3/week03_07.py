# week03_07.py

test = "I am a BOY"

print(test.count('a'))
print(test.count('A'))

print(test.find('a'))
print(test.find('q'))
print(test.find('am'))
print(test.find('qm'))

print(test.index('a'))
# print(test.index('q'))
print(test.index('am'))
if "qm" in test:
    print(test.index('qm'))
else:
    print("없다")

print(test.upper())
print(test.lower())
print(test.title())
print(test.capitalize())
print("/".join(test))

test = "   JMT University   "
print("|" + test.strip() + "|")
print("|" + test.lstrip() + "|")
print("|" + test.rstrip() + "|")

print(test.replace("University","High School")) #바뀐 다음 저장하고 저장된 위치를 다시 알려준다 
print(test) # 원래 위치

print(test.split())
print(test.split("i")) # i기준으로 쪼개짐(단, 쪼개지는 기준은 삭제된다)

'''
print(len("a"))
print(len([1,2]))
print(len((1,2,3)))

# "a".len() 오류(함수)
"a".count("a")
# count("a") 오류(메소드)
#(1).count('a')
print("123".index('1'))
print([1,2.5,3].index(3))

a = "%d%%" % 10
print(a)
'''
