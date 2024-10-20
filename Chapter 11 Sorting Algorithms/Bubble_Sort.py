def bubble_sort(data_list):
    for r in range(1, len(data_list)):
        for i in range(len(data_list) - r):
            if data_list[i] > data_list[i + 1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
    print(data_list)


print("Bubble sort: ")
bubble_sort([34, 1, 23, 45, 2, 3, 67, 90])
