# 컬렉션 타입

# 정수(int), 실수(float), 문자열(String)등 데이터 타입과 달리 여러가지를 하나로 묶어서 사용하는 것
# - 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 세트(set)
#
# LIST        - []
# TUPLE       - ()
# DICTIONARY  - {}
# SET         - {}, set([])
#
#
# List
# - mutable(가변성)
# - 순서대로 정리된 항목 담는 자료구조
# - 데이터 수정, 순서 필요
#
# Dictionary
# - mutable(가변성)
# - key, value 로 구성되어 있는 자료구조
# - 상황에 따라
#
# Tuple
# - immutable(불변성)
# - 수정이나 삭제 불가능, 비정적인 객체 담는데 사용하는 자료구조
# - 데이터의 읽기만 필요한 경우
#
# Set
# - mutable(가변성)
# - 중복을 허용하지 않음, 순서가 없는 자료구조
# - 중복된 값을 불허하는 경우, 순서가 불필요한 경우


# 자료구조의 변경

# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))