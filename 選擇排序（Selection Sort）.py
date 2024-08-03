def selection_sort(arr):
    # 選擇排序的實現函數
    n = len(arr)
    for i in range(n):
        # 假設當前元素是最小值
        min_index = i
        # 在未排序部分尋找最小值
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 將找到的最小值與當前元素交換
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 測試選擇排序的範例
test_array = [64, 25, 12, 22, 11]

print("Original array:", test_array)  # 輸出原始數組
selection_sort(test_array)
print("Sorted array:", test_array)    # 輸出排序後的數組

# 重要事項：
# - 選擇排序是一種簡單且直觀的排序算法，其工作原理是將數組分為已排序和未排序部分，
#   然後反覆從未排序部分中選出最小（或最大）的元素，並將其放到已排序部分的末尾。
# - 外層循環每執行一次，找到一個元素的最小值並將其放置在已排序部分的末尾。
# - 由於每次選擇最小值的操作需要遍歷整個未排序部分，選擇排序的平均和最壞情況時間複雜度為 O(n^2)。
# - 優點是選擇排序不需要額外的內存空間（就地排序，In-place Sorting），
#   並且進行的交換次數較少。
