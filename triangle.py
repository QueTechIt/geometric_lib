def horse_racing():
    N = int(input())
    wealth = list(map(int, input().split()))
    wealth.sort(reverse=True)
    result = []
    remaining_tugriks = wealth.copy()
    for i, w in enumerate(wealth):
        for j in range(len(result)):
            if all(result[k] >= w for k in range(j)):
                if remaining_tugriks[i] > 0:
                    remaining_tugriks[i] -= 1
                    result.insert(j, w)
                    break
        else:
            result.append(w)
    if result:
        print(' '.join(map(str, result)))
    else:
        print(':(')

horse_racing()