from rps import game_rps
from upDown import game_upDown
from lotto import game_lotto
from roulette import game_roulette
from quiz import game_quiz

while True:
    # 메뉴 출력
    print('''
    === 🎮 미니 오락실 🎮 ===
    1. 가위바위보
    2. 업다운 게임
    3. 로또 번호 맞추기
    4. 러시안 룰렛
    5. 국가 이름 초성 퀴즈
    0. 게임 종료
    ========================
    ''')

    # 선택 입력받기
    i = int(input("원하는 게임 번호를 선택하세요: "))

    if i == 1:
        game_rps()                      # 가위바위보 게임 진행
    elif i == 2:
        game_upDown()                   # 업다운 게임 진행
    elif i == 3:
        game_lotto()                    # 로또 번호 맞추기 진행
    elif i == 4:
        game_roulette()                 # 러시안 룰렛 진행
    elif i == 5:
        game_quiz()                     # 초성 퀴즈 진행
    elif i == 0:
        print("미니 오락실의 문을 닫겠습니다.\n다음에 또 오세요👋👋👋")
        break
    else:
        print("잘못된 선택입니다.\n숫자를 다시 입력해주세요.")
