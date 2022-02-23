def solution(participant, completion):
    dictionary = dict()

    for x in completion:
        if x in dictionary:
            dictionary[x] +=1
        else:
            dictionary[x] = 1
    for x in participant:
        if not x in dictionary or dictionary[x] == 0:
            return x
        if x in dictionary:
            dictionary[x] -=1

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    print(solution(participant, completion))