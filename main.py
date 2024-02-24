import numpy as np
from time import perf_counter_ns
import plotly.express as px
import pandas as pd

def mergesort_main(n):
    vals = np.random.randint(0, 100, n).tolist()

    def merge(left, right):
        result = []
        i ,j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def mergesort(list1):
        if len(list1) < 2:
            return list1
        middle = len(list1) // 2
        
        left = mergesort(list1[:middle])
        right = mergesort(list1[middle:])
        return merge(left, right)
    
    return mergesort(vals)


def ins_sort(n):
    k = np.random.randint(0, 100, n).tolist()
    
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #create i's copy (or not)
        temp = k[j]              #temp will be used for comparison with previous items, and sent to the place it belongs
        while j > 0 and temp < k[j-1]: #j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp
    
    return k

def runner(n):

    start_1 = perf_counter_ns()
    for i in range(999):
        np.random.seed(i)
        res_merge = mergesort_main(n)
    diff_1 = perf_counter_ns() - start_1

    start_2 = perf_counter_ns()
    for i in range(999):
        np.random.seed(i)
        res_ins = ins_sort(n)
    diff_2 = perf_counter_ns() - start_2

    # Uncomment below for print statements of each n value

    # print(f"=======n={n}=============")
    # print(f"Mergesort     : {diff_1}")
    # print(f"Insertion Sort: {diff_2}")

    return [diff_1, diff_2]


def main():
    timesdict = {}
    timesdict["Input Size"] = []
    timesdict["Time (nanoseconds)"] = []
    timesdict["Algorithm"] = []

    for i in range(25, 116, 5):
        timesdict["Input Size"].append(i)
        timesdict["Input Size"].append(i)
        vals = runner(i)

        timesdict["Time (nanoseconds)"].append(vals[0])
        timesdict["Algorithm"].append("Merge Sort")
        
        timesdict["Time (nanoseconds)"].append(vals[1])
        timesdict["Algorithm"].append("Insertion Sort")

    df = pd.DataFrame(data=timesdict)

    fig = px.line(df, x="Input Size", y="Time (nanoseconds)", color="Algorithm")
    fig.show()

main()