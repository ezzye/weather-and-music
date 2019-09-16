sort_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def swap(i):
    temp = sort_list[i]
    sort_list[i] = sort_list[i + 1]
    sort_list[i + 1] = temp


print('start.......')
while True:
    swap_made = 0
    print("iterate: {}".format(sort_list))
    for i in range(len(sort_list) - 1):
        # print(list[i], list[i + 1])
        if sort_list[i + 1] > sort_list[i]:
            swap(i)
            print("*** swap ***")
            print(sort_list[i], sort_list[i + 1])
            swap_made += 1
    if swap_made < 1:
        break
print(sort_list)
print('end.......')

