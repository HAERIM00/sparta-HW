cnt = 0
while cnt < 5:
    n = input("숫자를 입력해 주세요:")
    try:
        print(2*int(n))
    except ValueError:
        print(f"당신이 입력한 문자는{n} 입니다.")
    if n == "exit":
        print("종료합니다")
        exit()
    cnt +=1 