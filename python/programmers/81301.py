# 숫자 문자열과 영단어(2021 카카오 채용연계형 인턴십)
def solution(s):
    english = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    _tmp = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    ans = s
    for a, b in enumerate(_tmp):
        # print("a >>> ", type(a))
        # print("b >>> ", b)

        ans = ans.replace(b, str(a))

    # for n in english:
    #     s = s.replace(n, english[n])

    return ans


print(solution("one4seveneight"))
