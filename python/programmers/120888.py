# 중복된 문자 제거
def solution_dict(my_string):
    data = {}

    for text in my_string:
        data[text] = ""

    answer = "".join(data.keys())
    return answer


def solution_set(my_string):
    answer = ""
    tickets = set(my_string)

    for i in my_string:
        if i in tickets:
            answer += i
            tickets.remove(i)

    return answer


print(solution_dict("people"))
print(solution_dict("We are the world"))
