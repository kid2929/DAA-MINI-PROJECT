def merge(a, left, left_count, right, right_count):
    i = j = k = 0
    while i < left_count and j < right_count:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < left_count:
        a[k] = left[i]
        i += 1
        k += 1

    while j < right_count:
        a[k] = right[j]
        j += 1
        k += 1

def merge_sort(a, n):
    if n < 2:
        return
    middle = n // 2
    left = a[:middle]
    right = a[middle:]

    merge_sort(left, middle)
    merge_sort(right, n - middle)
    merge(a, left, middle, right, n - middle)

def main():
    n = int(input("Enter the number of processes: "))
    burst_time = [0] * n
    wt = [0] * n
    tat = [0] * n
    total_wt = 0

    for i in range(n):
        burst_time[i] = int(input(f"Enter the burst time for process {i + 1}: "))

    merge_sort(burst_time, n)

    for i in range(1, n):
        for j in range(i):
            wt[i] += burst_time[j]
        total_wt += wt[i]

    avg_wt = total_wt / n
    total_tat = 0

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]
        total_tat += tat[i]

    avg_tat = total_tat / n
    print(f"Average waiting time is: {avg_wt}")
    print(f"Average turnaround time is: {avg_tat}")

if __name__ == "__main__":
    main()
