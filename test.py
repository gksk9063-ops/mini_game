import random

print('''
   ===== 가위바위보 게임 =====
   가위바위보 게임에 시작합니다.
   ''')

choice = ["가위", "바위", "보"]

while True:
    user = input("가위, 바위, 보 중 하나를 입력해주세요: ")
    computer = random.choice(choice)

    if user not in choice:
        print("가위, 바위, 보 중에서 입력해주세요.")
        continue

    print(f"당신: {user} / 컴퓨터: {computer}")

    if user == computer:
        print("비겼습니다.")
    elif user == "가위" and computer == "보" or user == "바위" and computer == "가위" or user == "보" and computer == "바위":
        print("🎉당신이 이겼습니다🎉")
    else:
        print("컴퓨터가 이겼습니다😭😭😭")

    answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
    if answer.lower() == "y":
        continue
    elif answer.lower() == "n":
        break