# 3. 로또 번호 맞추기

import random


def game_lotto():
    while True:
        # 게임 시작 화면
        print('''
        === 🎰 로또 번호 맞추기 게임 🎰 ===
          로또 번호 맞추기 게임을 시작합니다.
        ''')

        # 정답 무작위 선택
        lotto_number = random.sample(range(1, 46), 6)
        lotto_number.sort()

        # 사용자에게 입력받기
        user = input("1~45 사이의 숫자를 입력해주세요: ")
        user_number = list(map(int, user.split()))

        # 입력된 숫가자 6개가 아니면 다시 입력
        if len(user_number) != 6:
            print("❌ 정확히 6개의 숫자를 입력해주세요.")
            continue
        if len(set(user_number)) != 6:
            print("❌ 중복된 숫자가 있습니다.\n서로 다른 6개의 숫자를 입력해주세요.")
            continue

        # 숫자 오름차순 정렬
        user_number.sort()
        print(f"\n당신의 선택: {user_number}")
        print(f"로또 당첨 번호: {lotto_number}")

        # 두 리스트에서 서로 일치하는 숫자의 개수 계산
        matched = len(set(user_number) & set(lotto_number))

        # 등수 결과 출력
        if matched == 6:
            print(f"{matched}개 일치 => 🎉 1등 당첨 🎉")
        elif matched == 5:
            print(f"{matched}개 일치 => 🎉 2등 당첨 🎉")
        elif matched == 4:
            print(f"{matched}개 일치 => 🎉 3등 당첨 🎉")
        elif matched == 3:
            print(f"{matched}개 일치 => 🎉 4등 당첨 🎉")
        elif matched == 2:
            print(f"{matched}개 일치 => 🎉 5등 당첨 🎉")
        elif matched == 1:
            print(f"{matched}개 일치 => 🎉 6등 당첨 🎉")
        else:
            print("아쉽게도 낙첨입니다. 다음 기회에!")

        # 게임 계속 여부
        answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
        if answer.lower() == "y":
            print("\n로또 번호 맞추기 게임을 다시 시작합니다!")
            continue
        elif answer.lower() == "n":
            print("\n메인 화면으로 돌아갑니다.")
            break