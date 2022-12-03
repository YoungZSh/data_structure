from ds import Stack


def backtracking(item_list, capicity):
    """
    回溯法解决背包问题,返回二维列表
    """
    i = 0
    bag = Stack()
    cur = 0
    outlist = []
    while True:
        if cur <= capicity:
            bag.push(i)
            cur += item_list[i]
        if cur == capicity:
            stack_list = bag.stackToList()
            outlist.append(stack_list.copy())
        if i == len(item_list) - 1:
            i = bag.pop()
            cur -= item_list[i]
            if i == len(item_list) - 1:
                if bag.isEmpty() == True:
                    break
                i = bag.pop()
                cur -= item_list[i]
        i += 1
    return outlist


def add_volume(index, volume):
    sum = 0
    for i in index:
        sum += volume[i]
    return sum


def DP(volume, value, cap):
    """
    动态规划解决背包问题，返回最大价值
    """
    dp = [0 for _ in range(cap + 1)]
    for i in range(len(volume)):
        for j in reversed(range(volume[i], cap + 1)):
            dp[j] = max(dp[j], dp[j - volume[i]] + value[i])
    return dp[cap]


def solution1():
    volumes = input("请输入待装入物品大小:")
    capicity = input("请输入背包大小:")
    volume_list = []
    for volume in volumes.split(" "):
        volume_list.append(int(volume))
    print(
        "-----------------------------------------------------------------------------"
    )
    print("结果为:")
    result = backtracking(volume_list, int(capicity))
    for i in result:
        for j in i:
            print(volume_list[j], end=" ")
        print(" ")
    print(
        "-----------------------------------------------------------------------------"
    )
    return None


def solution2():
    volumes = input("请输入待装入物品大小:")
    values = input("请输入各物品价值:")
    capicity = int(input("请输入背包大小:"))
    volume_list = []
    value_list = []
    for volume in volumes.split(" "):
        volume_list.append(int(volume))
    for value in values.split(" "):
        value_list.append(int(value))
    result = DP(volume_list, value_list, capicity)
    out_list = backtracking(value_list, result)
    print(
        "-----------------------------------------------------------------------------"
    )
    print("最大价值为:", result)
    print("装入方案为:")
    for i in out_list:
        if add_volume(i, volume_list) > capicity:
            continue
        for j in i:
            print(volume_list[j], end=" ")
        print(" ")
    print(
        "-----------------------------------------------------------------------------"
    )
    return None


if __name__ == "__main__":
    """
    主函数
    """
    # solution1()
    solution2()
"""
volume:1 8 4 3 5 2
value:1 1 1 1 1 1
capicity:10
"""