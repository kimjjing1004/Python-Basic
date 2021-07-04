# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3 # age가 3살 이상이면 adult이다 True(boolean)

''' 이렇게
하면
여러문장이 주석처리
됩니다'''

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # +와 ,는 같은 기능이며 변수값을 출력하게한다.
print(name + "는 어른일까요? " + str(is_adult))
# age(정수형), is_adult(boolean) 값은 str(문자열)로 바꾸어서 출력해야합니다.