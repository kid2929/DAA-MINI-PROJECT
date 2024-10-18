def merge(a, left, leftcount, right, rightcount):
    i = j = k = 0
    while i < leftcount and j < rightcount:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    
    while i < leftcount:
        a[k] = left[i]
        i += 1
        k += 1

    while j < rightcount:
        a[k] = right[j]
        j += 1
        k += 1

def merge_sort(a, n):
    if n < 2:
        return  # Base condition: if the array has only one element, it is already sorted
    middle = n // 2
    left = a[:middle]
    right = a[middle:]

    merge_sort(left, middle)
    merge_sort(right, n - middle)
    merge(a, left, middle, right, n - middle)

def main():
    n = int(input("Enter the number of processes: "))
    burst_time = [0] * n
    priority = [0] * n
    wt = [0] * n
    tat = [0] * n
    total = 0

    for i in range(n):
        burst_time[i], priority[i] = map(int, input(f"Enter the burst time and priority for process {i + 1}: ").split())

    # Sorting based on priority (higher priority number means lower priority)
    merge_sort(priority, n)
    merge_sort(burst_time, n)

    # Calculate waiting times
    for i in range(1, n):
        wt[i] = sum(burst_time[j] for j in range(i))
        total += wt[i]

    avg_wt = total / n
    total = 0

    # Calculate turnaround times and output results
    for i in range(n):
        tat[i] = burst_time[i] + wt[i]
        total += tat[i]
        print(f"P[{i + 1}]\t\t{burst_time[i]}\t{tat[i]}\t{wt[i]}")

    avg_tat = total / n
    print(f"Average waiting time is {avg_wt}")
    print(f"Average turnaround time is {avg_tat}")

if __name__ == "__main__":
    main()
