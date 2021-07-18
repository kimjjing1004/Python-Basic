def profile(name, age, main_lang):
    print(name, age, main_lang)


# 키워드에 값을 넣으면 순서가 뒤바껴도 출력이 해당하는 키워드 값에 출력이 된다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

