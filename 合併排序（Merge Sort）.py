def merge_sort(arr):
    # 合併排序的主函數
    if len(arr) > 1:
        mid = len(arr) // 2  # 找到數組的中間點
        left_half = arr[:mid]  # 左半部分
        right_half = arr[mid:]  # 右半部分

        # 遞迴地對每個部分進行排序
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # 合併左右兩部分
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 檢查是否有剩餘的元素
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 測試合併排序的範例
test_array = [38, 27, 43, 3, 9, 82, 10]

print("Original array:", test_array)  # 輸出原始數組
merge_sort(test_array)
print("Sorted array:", test_array)    # 輸出排序後的數組

# 重要事項：
# - 合併排序是一種基於分治法的排序算法。它將數組分為兩部分，
#   遞迴地對這兩部分進行排序，然後合併這兩部分來得到排序結果。
# - 合併排序的時間複雜度為 O(n log n)，其中 n 是數列的長度，
#   在所有情況下都是這個複雜度，因此是一種高效且穩定的排序算法。
# - 合併排序是穩定排序，這意味著相同鍵值的元素在排序後保持相對位置不變。
# - 然而，合併排序需要額外的內存空間來存儲中間結果，因此對於非常大的數組，
#   這可能會是個問題。
