import random
import time
from datetime import datetime

def main():
    n = int(input("자릿수를 이용해 주세요: "))
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_list)
    random_numbers = number_list[0:n]
    print(random_numbers)

    # num = list(map(int, input("숫자를 입력해주세요: ").split()))
    # print(num)

    start_time = time.time()
    try_count = 0

    while True:
        input_number = input("값을 입력해주세요(exit 입력하면 종료): ").split()
        if input_number == "exit":
            exit()
        try_count += 1
        out_count = 0

        ball_count = 0
        strike_count = 0
        for i, v in enumerate(input_number):
            v = int(v)
            # print(i, v)
            if v not in random_numbers:
                out_count += 1
            else:
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1

        if strike_count == n:
            print("###############")
            print("정답입니다")
            print(f"소요 시간: {time.time() - start_time:.2f}")
            print(f"클리어 일자 : {datetime.now()}")
            print("###############")
            return
        print(f"{ball_count}볼 {strike_count}스트라이크 {out_count}아웃 ")

main()
