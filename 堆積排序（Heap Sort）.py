def heapify(arr, n, i):
    # 將以 i 為根的子樹調整為最大堆
    largest = i  # 初始化最大值為根節點
    left = 2 * i + 1  # 左子節點
    right = 2 * i + 2  # 右子節點

    # 如果左子節點存在且大於根節點
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子節點存在且大於目前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根節點
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交換
        # 重新堆化受影響的子樹
        heapify(arr, n, largest)

def heap_sort(arr):
    # 堆積排序的實現函數
    n = len(arr)

    # 建立最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一個一個地從堆中取出元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 將當前根節點與末尾節點交換
        heapify(arr, i, 0)  # 調整縮小後的堆

# 測試堆積排序的範例
test_array = [12, 11, 13, 5, 6, 7]

print("Original array:", test_array)  # 輸出原始數組
heap_sort(test_array)
print("Sorted array:", test_array)    # 輸出排序後的數組

# 重要事項：
# - 堆積排序是一種基於比較的排序算法，利用堆這種數據結構來排序數列。
# - 堆積排序的主要步驟包括建立最大堆和不斷從堆中取出最大元素來進行排序。
# - `heapify` 函數用來將子樹調整為最大堆，`heap_sort` 函數則首先建立最大堆，
#   然後進行排序。
# - 堆積排序的時間複雜度為 O(n log n)，其中 n 是數列的長度。
# - 儘管堆積排序的最壞、最好的情況下的時間複雜度都是 O(n log n)，
#   但它並不是一種穩定的排序算法。
# - 堆積排序是一種就地排序算法，不需要額外的內存空間。
