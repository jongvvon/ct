"""
1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3

어떤 국가에서는 자국 내 방송국에서 스파이가 활동하는 사실을 알아냈다. 스파이는 영상물에 암호 코드를 삽입하여 송출하고 있었다. 스파이의 암호 코드에 다음과 같은 규칙이 있음을 발견했다.

1. 암호코드는 8개의 숫자로 이루어져 있다.

2. 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수가 되어야 한다.

    ex) 암호코드가 88012346일 경우,
    ( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 + 6) = 60은 10의 배수이므로 올바른 암호코드다.

    ex) 암호코드가 19960409일 경우,
    ( ( 1 + 9 + 0 + 0 ) x 3 ) + ( 9 + 6 + 4 + 9) = 58은 10의 배수가 아니므로 잘못된 암호코드다.

이 암호코드들을 빠르고 정확하게 인식할 수 있는 스캐너를 개발하려고 한다.

스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.

직사각형 배열은 1, 0으로만 이루어져 있고, 암호코드 이외의 부분은 전부 0으로 주어진다.

암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.

암호코드의 각 숫자가 암호화되는 규칙은 다음과 같다.

비정상적인 암호코드(가로 길이가 56이 아닌 경우, 아래 규칙대로 해독할 수 없는 경우)는 주어지지 않는다.

암호코드 정보가 포함된 2차원 배열을 입력으로 받아 올바른 암호코드인지 판별하는 프로그램을 작성하라.

[입력]

가장 첫줄은 전체 테스트 케이스의 수이다.

각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).

그 다음 N개의 줄에 걸쳐 N x M 크기의 직사각형 배열이 주어진다.

[출력]

각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다. 이때 C는 케이스의 번호이다.

주어진 암호코드가 올바른 암호코드일 경우, 암호코드에 포함된 숫자의 합을 출력하라. 만약 잘못된 암호코드일 경우 대신 0을 출력하라.

[예제 풀이]

1번 케이스의 암호코드 정보를 추출하면 아래와 같다.

01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011
01110110110001011101101100010110001000110100100110111011

이 숫자가 나타내는 정보는 각각 아래와 같다.
0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)

검증코드가 맞는지 살펴보면, (7 + 7 + 5 + 2) * 3 + 5 + 5 + 0 + 7 = 80 이므로 올바른 암호코드라고 할 수 있다. 따라서 1번의 출력 값은 38이 된다.

2번 케이스도 같은 방식으로 계산할 경우, 잘못된 암호코드임을 알 수 있다. 따라서 2번의 출력 값은 0이 된다.
"""
# 문제 분별 x