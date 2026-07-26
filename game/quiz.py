# 5. 국가 이름 초성 퀴즈

import random

def game_quiz():
    # 게임 시작 화면
    print('''
    ======== 🌍 초성 퀴즈 🌍 ========
        초성 퀴즈 게임을 시작합니다.
            (주제: 국가이름)
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

        while True:
            current_quiz_bank = quiz_bank.copy()
            correct_count = 0

            for i in range(1, 4):
                print(f"\n[{i}번째 문제]")

                # 복사본 딕셔너리에서 무작위로 하나 선택
                country, initial = random.choice(list(current_quiz_bank.items()))
                print(f"초성 힌트: {initial}")

                # 중복 방지
                del current_quiz_bank[country]

                # 정답 입력받기
                answer = input("이 국가는 어디일까요?: ").strip()

                if answer == country:
                    print("\n🎉 정답입니다! 🎉")
                    correct_count += 1  # 정답 시 카운트 증가
                else:
                    print(f"\n 틀렸습니다😭😭😭 정답은 [{country}]였습니다.")

            # 등급 판정
            print("\n=================================")
            print(f"게임 종료! 총 3문제 중 {correct_count}문제를 맞추셨습니다.")

            # 등급 매기기
            if correct_count == 3:
                grade = "A"
                print("대단해요! 완벽한 실력입니다!")
            elif correct_count == 2:
                grade = "B"
                print("훌륭합니다! 훌륭한 성적이에요.")
            elif correct_count == 1:
                grade = "C"
                print("조금만 더 연습하면 잘할 수 있어요!")
            else:
                grade = "F"
                print("앗... 한 문제도 맞추지 못했어요.")

            print(f"🎖️ 최종 등급: [{grade}]")
            print("=================================")

            # 게임 계속 여부 처리
            retry_game = False

            while True:
                answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
                if answer.lower() == "y":
                    print("\n초성 퀴즈 게임을 다시 시작합니다!")
                    retry_game = True  # 바깥 loop를 새로 돌리기 위한 신호
                    break
                elif answer.lower() == "n":
                    print("\n메인 화면으로 돌아갑니다.")
                    return  # 메인으로 복귀
                else:
                    print("Y or N 중에서 다시 입력해주세요.")

            if retry_game:
                continue