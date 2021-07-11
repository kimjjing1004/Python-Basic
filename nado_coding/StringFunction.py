python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java")) # replace("찾고싶은 문자", "바꾸고 싶은 문자")

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))  # find는 찾는 값이 없을때 -1
#print(python.index("Java")) # index는 없을때 그냥 에러
print("hi") # find 이후 hi 출력 가능, index 에러시 hi출력 불가능    

print(python.count("n"))
