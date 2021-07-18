# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
#
# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --
#
# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *

users = range(1, 21) # range 타입으로 1부터 20까지 숫자를 생성

users = list(users) # # list 타입으로 변환됨

shuffle(users)  # shuffle 로 섞음

winners = sample(users, 4) # sample 로 4명 뽑음

print(" -- 당첨자 벌표 -- ")
print("치킨 당첨자 : {0}".format(winners[0])) # 4명 중 배열 0번째(1명)를 치킨으로 선택
print("커피 당첨자 : {0}".format(winners[1:])) # 4명 중 나머지 배열 1 ~ 3번째 까지 커피로 선택
print(" -- 축하합니다 -- ")