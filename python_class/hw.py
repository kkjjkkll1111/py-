'''
giho = input("기호: ")
array = input("문자열: ")
result = giho[0] + array + giho[1]
print(f"결과: {result}")

name_list = []
names = ""
for i in range(0,5):
    name = input(f"{i+1}번 이름 : ")
    name_list.append(name)
print(f"결과 : {'/'.join(name_list)}")

r = input('반지름 : ')
h = input('높이 : ')
result = 3.14159 * float(r) ** 2 * float(h)
print(f"원기둥의 부피 : {result}")

human = input('인원 : ')
pizza = input('피자 수량 (판) : ')
piece = input('피자 조각 (판당) : ')
tot_pizza = int(pizza) * int(piece)
div_pizza = tot_pizza // int(human)
left_pizza = tot_pizza % int(human)
print(f'결과 : 인당 {div_pizza}조각, 남은 조각 {left_pizza}조각')

fst_grade = float(input("1학기 학점 : "))
sec_grade = float(input("2학기 학점 : "))
avg_grade = (float(fst_grade) + float(sec_grade))/2
vol_time = int(input("봉사시간 : "))
scholarship = "확정" if avg_grade >= 3.5 and vol_time >= 8 else "탈락"
print(f"장학금 대상 여부 : {scholarship}")
'''
select = input("도형 선택(1:사각, 2:삼각, 3:원):")
if int(select) == 1:
    length = input('가로 입력 : ')
    width = input('세로 입력 : ')
    area = int(length) * int(width)
    print(f"도형의 넓이 : {area}")
elif int(select) == 2:
    bottom = input('밑변 입력 : ')
    height = input('높이 입력 : ')
    area = float(bottom) * float(height) / 2
    print(f"도형의 넓이 : {area:.2f}")
elif int(select) == 3:
    r = input('반지름 입력 : ')
    area = float(r)**2*3.14
    print(f"도형의 넓이 : {area:.2f}")
else:
    print("잘못한 입력")

























