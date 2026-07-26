# 1. 가위바위보

import random


def game_rps():
    # 게임 시작 화면
    print('''
    ===== ✊✌️🖐️ 가위바위보 게임 =====
        가위바위보 게임을 시작합니다.
    ''')

    choice = ["가위", "바위", "보"]

    while True:
        # 사용자에게 입력받기
        user = input("가위, 바위, 보 중 하나를 입력해주세요: ")
        # 컴퓨터 무작위 선택
        computer = random.choice(choice)

        # 잘못된 입력 확인
        if user not in choice:
            print("❌ 가위, 바위, 보 중에서 입력해주세요.")
            continue

        print(f"당신: {user} / 컴퓨터: {computer}")

        # 승패 판정
        if user == computer:
            print("비겼습니다.")
        elif user == "가위" and computer == "보" or user == "바위" and computer == "가위" or user == "보" and computer == "바위":
            print("🎉당신이 이겼습니다🎉")
        else:
            print("컴퓨터가 이겼습니다😭😭😭")

        # 게임 계속 여부
        answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
        if answer.lower() == "y":
            print("\n가위바위보 게임을 다시 시작합니다!")
            continue
        elif answer.lower() == "n":
            break