# 튜플이 리스트 보다 속도가 빠르다
menu = ("돈까스", "치즈까스")  # 튜플의 기본형태
print(menu[0])
print(menu[1])

# menu.add("생선까스")  # 튜플은 add 기능을 제공하지 않음

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")  # 튜플 형태로 한번에 나타낼 수 있다.
# 서로 다른 변수의 서로 다른 값들을 순서대로 나열 한 것(튜플 형태로)
print(name, age, hobby)