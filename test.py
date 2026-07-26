import random

print('''
======== 🌍 초성 퀴즈 🌍 ========
    초성 퀴즈 게임을 시작합니다.
''')

while True:
    quiz_bank = {
        "대한민국": "ㄷㅎㅁㄱ",
        "미국": "ㅁㄱ",
        "프랑스": "ㅍㄹㅅ",
        "이탈리아": "ㅇㅌㄹㅇ",
        "베트남": "ㅂㅌㄴ",
        "일본": "ㅇㅂ",
        "영국": "ㅇㄱ",
        "브라질": "ㅂㄹㅈ",
        "독일": "ㄷㅇ",
        "캐나다": "ㅋㄴㄷ",
        "스페인": "ㅅㅍㅇ",
        "호주": "ㅎㅈ",
        "중국": "ㅈㄱ",
        "인도": "ㅇㄷ",
        "러시아": "ㄹㅅㅇ",
        "멕시코": "ㅁㅅㅋ",
        "그리스": "ㄱㄹㅅ",
        "스위스": "ㅅㅇㅅ",
        "싱가포르": "ㅅㄱㅍㄹ",
        "태국": "ㅌㄱ"}

    country, initial = random.choice(list(quiz_bank.items()))
    print(f"초성: {initial}")

    answer = input("이 국가는 어디일까요?: ").strip()
    if answer == country:
        print("\n🎉 정답입니다 🎉")
    else:
        print(f"\n틀렸습니다😭😭😭 정답은 [{country}]였습니다.")

    # 게임 계속 여부
    answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
    if answer.lower() == "y":
        print("\n초성 퀴즈 게임을 다시 시작합니다!")
        continue
    elif answer.lower() == "n":
        print("\n메인 화면으로 돌아갑니다.")
        exit()
    else:
        print("\nY or N 중에서 다시 입력해주세요. ")