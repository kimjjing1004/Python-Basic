# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
# 같은 표현법: 변수 = {" ", " ", "..."} = 변수 = set([" ", " ", "..."])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# intersection = & 같은 뜻 (교집합)
print(java & python)
print(java.intersection(python))


# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# union = | 같은 뜻 (합집합)
print(java | python)
print(java.union(python))


# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# difference = - 같은 뜻 (차집합)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
# add = 값을 추가
python.add("김태호")
print(python)

# java를 잊었어요
# remove = 값을 삭제
java.remove("김태호")
print(java)