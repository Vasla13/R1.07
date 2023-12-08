def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)

tab = [5, 2, 4, 8, 1, 3]

selection_sort(tab)

print(sorted(tab))

tab.sort()
print(tab)
