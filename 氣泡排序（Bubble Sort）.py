def bubble_sort(arr):
    # 氣泡排序的實現函數
    n = len(arr)
    for i in range(n):
        # 外層循環遍歷整個數組
        # 內層循環比較相鄰元素
        for j in range(0, n-i-1):
            # 如果前一個元素大於後一個元素，則交換它們的位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 測試氣泡排序的範例
test_array = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", test_array)  # 輸出原始數組
bubble_sort(test_array)
print("Sorted array:", test_array)    # 輸出排序後的數組

# 重要事項：
# - 氣泡排序是一種簡單的排序算法，其工作原理是重複地遍歷待排序的數列，
#   並且逐對比較相鄰的元素。如果前一個元素比後一個元素大，就交換它們的位置。
# - 外層循環每執行一次，最大的元素會移動到數列的末尾，
#   因此內層循環的次數可以逐漸減少。
# - 氣泡排序的平均和最壞情況時間複雜度為 O(n^2)，
#   因此在大規模數據集上效率不高。
# - 優點是實現簡單且不需要額外的內存空間（就地排序，In-place Sorting）。
