def quick_sort(arr):
    # 快速排序的主函數
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 選擇第一個元素作為樞軸
        less = [x for x in arr[1:] if x <= pivot]  # 小於或等於樞軸的元素
        greater = [x for x in arr[1:] if x > pivot]  # 大於樞軸的元素
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 測試快速排序的範例
test_array = [10, 7, 8, 9, 1, 5]

print("Original array:", test_array)  # 輸出原始數組
sorted_array = quick_sort(test_array)
print("Sorted array:", sorted_array)  # 輸出排序後的數組

# 重要事項：
# - 快速排序是一種基於分治法的排序算法。它通過選擇一個樞軸元素，然後將數組分為
#   小於等於樞軸的部分和大於樞軸的部分，遞迴地對這兩部分進行排序。
# - 樞軸的選擇對於快速排序的性能有很大的影響。在最壞情況下（例如數組已經有序），
#   快速排序的時間複雜度為 O(n^2)。然而，平均時間複雜度為 O(n log n)。
# - 快速排序是就地排序算法，但需要用到遞迴，因此需要考慮遞迴深度對空間的影響。
# - 儘管快速排序不一定是穩定的排序算法（相同元素的順序可能改變），
#   但由於其高效性，通常是排序的大量數據的首選算法。
