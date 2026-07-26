# 6. 미니 타자 연습

def typing_game():
    # 게임 시작 화면
    print('''
    ====== ⌨️  미니 타자 연습 게임 ⌨️  ======
        미니 타자 연습 게임을 시작합니다.
    ''')

    words = ["python", "computer", "programming", "database", "algorithm", "developer", "keyboard"]
    target_word = random.choice(words)

    print("\n화면에 나오는 단어를 정확하게 입력하세요!")
    print(f"👉  {target_word}  👈")

    input("시작하려면 Enter를 누르세요...")
    start_time = time.time()

    user_input = input("입력: ").strip()
    end_time = time.time()

    if user_input == target_word:
        elapsed_time = end_time - start_time
        print(f"🎉 정확히 입력했습니다! 소요 시간: {elapsed_time:.2f}초")
    else:
        print(f"❌ 틀렸습니다! (입력한 단어: {user_input} / 원래 단어: {target_word})")