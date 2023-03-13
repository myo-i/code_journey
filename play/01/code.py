# [二要素の足し算の組み合わせ]
# ・説明
# →solution 関数には int 型の配列 nums と、 int 型の値 target が引数として与えられています。
# solution 関数の戻り値として、 nums[i] + nums[j] = target となる、index i と j をペアの総数を int 型でプログラムを作成してください。
# なお、順序を入れ替えただけのペアは同じものとしてみなされます。
# また、同じ数字の組み合わせのペアがあったとしても、ペア間で配列要素のインデックスが一つでも異なっていれば、それらは別のペアとしてみなされます。
# 例1:
# 入力: nums = [1,2,3,4,3], target = 6
# 出力: 2
# 説明: 足して6になるペアは、2+4 と 3+3 となり、2が正解
# 例2:
# 入力: nums = [1,5,3,3,3], target = 6
# 出力: 4
# 説明: 足して6になるペアは、1+5 と 3つの異なる 3+3 （3番目の要素と4番目の要素、3番目の要素と5番目の要素、4番目の要素と5番目の要素）となり、4が正解。
# 前提
# ・2 ≦ len(nums) ≦ 10000
# ・nums[i] と target は -inf < nums[i], target < inf を満たす任意の int である

# [テストケース]
# [1,5,3,3,3]　target 6
# [1,2,3,4,3] target 6
# [1,5,3,3,3] target 6
# [1,1,1,1,1] target 2

import queue

# 値とインデックスをキー・バリューにすればキーを選択すれば値を取れる

def solution(input, target):
    keyValue = {}
    # インプットの値をキー、インデックスをキューとしてバリューに格納している
    for index,value in enumerate(input):
        if value in keyValue:
            keyValue[value].put(index)
        else:
            keyValue[value] = queue.Queue()
            keyValue[value].put(index)
    # Output -> keyValue = {1:[0], 5:[1], 3[2,3,4]}

    sum = 0
    for value in input:
        # Queueなのでgetしたら先頭の要素は削除される
        keyValue[value].get()
        disc = target - value
        if disc in keyValue:
            sum += keyValue[disc].qsize()

    return sum

print(solution([1,5,3,3,3], 6))
