# 2. 업다운 게임

import random


def game_upDown():
    # 게임 시작 화면
    print('''
    ======= 👍업다운 게임👎 =======
        업다운 게임을 시작합니다.
    ''')

    # 정답 무작위 선택
    number = random.randint(1, 50)
    # 시도 횟수 카운트
    count = 0

    while True:
        # 사용자에게 입력받기
        user = int(input("숫자를 입력해주세요: "))
        count += 1

        # 잘못된 입력 확인
        if not 1 <= user <= 50:
            print("❌ 1~50 중의 숫자 하나를 입력해주세요. ")
            continue

        # 정답 비교 판정
        if user < number:
            print("🔺 UP!")
        elif user > number:
            print("🔻 DOWN!")
        else:
            print(f"🎉 정답입니다! 🎉\n{count}번 만에 맞추셨습니다")

            # 게임 계속 여부
            retry_game = False

            while True:
                answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
                if answer.lower() == "y":
                    print("\n업다운 게임을 다시 시작합니다!")
                    number = random.randint(1, 50)  # 새로운 정답으로 리셋
                    count = 0  # 시도 횟수 리셋
                    break
                elif answer.lower() == "n":
                    print("\n메인 화면으로 돌아갑니다.")
                    return
                else:
                    print("\nY or N 중에서 다시 입력해주세요. ")

            if retry_game:
                continue