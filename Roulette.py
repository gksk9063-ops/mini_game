# 4. 러시안 룰렛
import random
import time

def russian_roulette():
    while True:
        # 게임 시작 화면
        print('''
        ========== 🔫 러시안 룰렛 게임 🔫 ==========
            러시안 룰렛 게임을 시작합니다.
        (아무도 안 죽고 한 바퀴 돌면 총알이 추가됩니다!)
        ''')

        # 선공 결정하기
        turn = random.choice(["플레이어", "컴퓨터"])
        print(f"선공을 정합니다... [선공: {turn}]")
        time.sleep(1)

        # 1. 초기 총 세팅 (6개 중 1개만 총알)
        gun = [0, 0, 0, 0, 0, 0]
        bullet_index = random.randint(0, 5)
        gun[bullet_index] = 1

        current_gun = 0  # 현재 발사할 탄창의 위치
        round_shots = 0  # 이번 라운드에 몇 명이 쐈는지 세는 변수

        # 생사가 갈릴 때까지 번갈아 쏘기
        while True:
            print(f"\n현재 탄창 상태: 총 6칸 중 총알 {gun.count(1)}개 장전됨")

            # 💡 [핵심] 턴에 따른 행동 선택
            if turn == "플레이어":
                print("--------------------------------")
                print(" 1: 그냥 방아쇠 당기기")
                print(" 2: 탄창 드르륵 섞고 방아쇠 당기기")
                print("--------------------------------")
                choice = input(f"[{turn} 턴] 행동을 선택하세요 (1 / 2): ")

                if choice == "2":
                    print("\n드르륵...!! 탄창을 무작위로 다시 섞었습니다!")
                    # 현재 위치(current_gun) 이후의 남은 칸들만 분리해서 섞기
                    remains = gun[current_gun:]
                    random.shuffle(remains)
                    gun[current_gun:] = remains
                    time.sleep(0.8)
            else:
                # 컴퓨터: 남은 칸 중 총알 확률이 50% 이상이면 섞음
                remain_slots = gun[current_gun:]
                hit_chance = remain_slots.count(1) / len(remain_slots)

                print(f"\n[{turn} 턴] 컴퓨터가 고민 중입니다...")
                time.sleep(1)

                if hit_chance >= 0.5:
                    print("컴퓨터: '위험하군...' 드르륵! 탄창을 섞었습니다!")
                    remains = gun[current_gun:]
                    random.shuffle(remains)
                    gun[current_gun:] = remains
                    time.sleep(0.8)
                else:
                    print("컴퓨터: '그냥 당기겠습니다.'")

            print("달칵... 방아쇠를 당겼습니다")
            time.sleep(1)

            # 총알이 발사된 경우 (게임 종료)
            if gun[current_gun] == 1:
                print("\n💥 탕!!! 총알이 발사되었습니다!")
                if turn == "플레이어":
                    print("당신이 패배했습니다... 💀 Game Over 💀")
                else:
                    print("컴퓨터가 쓰러졌습니다!\n 🎉 당신의 승리 🎉")

                answer = input("\n게임을 계속 진행하겠습니까? ( Y / N ) ")
                if answer.lower() == "y":
                    print("\n러시안 룰렛 게임을 다시 시작합니다!")
                    break
                elif answer.lower() == "n":
                    print("\n메인 화면으로 돌아갑니다.")
                    exit()

            # 빈 총인 경우
            else:
                print("\n휴... 다행히 빈 총성입니다. 살았습니다!")
                current_gun += 1
                round_shots += 1
                turn = "컴퓨터" if turn == "플레이어" else "플레이어"

                # 플레이어와 컴퓨터가 한 번씩 다 쐈다면 (총알 추가)
                if round_shots == 2:
                    print(
                        "\n ⚠️ 두 분 다 살아남으셨군요! 탄창에 총알이 1개 더 추가됩니다...⚠️"
                    )
                    time.sleep(1)

                    empty_slots = []
                    for i in range(current_gun, 6):
                        if gun[i] == 0:
                            empty_slots.append(i)

                    if len(empty_slots) > 0:
                        new_bullet = random.choice(empty_slots)
                        gun[new_bullet] = 1
                        print("🚨 탄창에 새로운 총알이 장전되었습니다 🚨")
                    else:
                        print("🚨 이미 모든 탄창에 총알이 가득 찼습니다 🚨")

                    round_shots = 0