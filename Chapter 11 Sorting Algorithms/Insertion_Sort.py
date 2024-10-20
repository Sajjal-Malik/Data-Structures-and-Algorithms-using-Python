def insertion_sort(data_list):
    for i in range(1, len(data_list)):
        temp = data_list[i]
        j = i - 1
        while j >= 0 and temp < data_list[j]:
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = temp
    print(data_list)


print("Insertion sort: ")
insertion_sort([34, 1, 23, 45, 2, 3, 67, 90])
