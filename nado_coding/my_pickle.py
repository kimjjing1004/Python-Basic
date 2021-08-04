import pickle

profile_file = open("profile.pickle", "wb") # pickle을 쓰기 위해서는 b(binary type)을 꼭 써야하고, 인코딩 설정 x
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()