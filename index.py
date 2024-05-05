import random

coin = 100

for turn in range(coin):
    dangcheom = random.randrange(1, 1000)

    if dangcheom <= 2:
        print(turn+1, "코인: 이주년 ㄱㅇㅈㅇㄱ 스패셜 패키지")

    elif dangcheom > 2 and dangcheom <= 6:
        print(turn+1, "코인: 이주년 ㄱㅇㅈㅇㄱ 사진 1")

    elif dangcheom > 6 and dangcheom <= 10:
        print(turn+1, "코인: 이주년 ㄱㅇㅈㅇㄱ 사진 2")

    elif dangcheom > 10 and dangcheom <= 110:
        print(turn+1, "코인: 지쿠빌런 고은가람 사진")

    elif dangcheom > 110 and dangcheom <= 210:
        print(turn+1, "코인: 의자도둑 고은가람 사진")

    elif dangcheom > 210 and dangcheom <= 310:
        print(turn+1, "코인: 편의점빌런 고은가람 사진")

    elif dangcheom > 310 and dangcheom <= 500:
        print(turn+1, "코인: 청룡열차 ㄱㅇㅈㅇㄱ 사진")

    elif dangcheom > 500 and dangcheom <= 700:
        print(turn+1, "코인: 청룡열차 사진")

    else:
        print(turn+1, "코인: 오송역")