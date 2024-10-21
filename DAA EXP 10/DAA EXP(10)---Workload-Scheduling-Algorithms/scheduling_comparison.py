def fcfs():
    n = int(input("Enter the number of processes: "))
    bt = [0] * n  # Burst time
    wt = [0] * n  # Waiting time
    tat = [0] * n  # Turnaround time
    avgwt = 0
    avgtat = 0

    print("\nEnter burst time for processes:")
    for i in range(n):
        bt[i] = int(input(f"P[{i + 1}]: "))

    # Calculate waiting times
    wt[0] = 0
    for i in range(1, n):
        wt[i] = sum(bt[j] for j in range(i))  # Sum of burst times for previous processes

    # Calculate turnaround times and averages
    for i in range(n):
        tat[i] = wt[i] + bt[i]
        avgwt += wt[i]
        avgtat += tat[i]

    avgwt /= n
    avgtat /= n

    print("\nFCFS Results:")
    print("Processes\tBurst time\tWaiting time\tTurnaround time")
    for i in range(n):
        print(f"P[{i + 1}]\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage waiting time is {avgwt}")
    print(f"Average turnaround time is {avgtat}\n")

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
        return
    middle = n // 2
    left = a[:middle]
    right = a[middle:]
    merge_sort(left, middle)
    merge_sort(right, n - middle)
    merge(a, left, middle, right, n - middle)

def priority():
    n = int(input("Enter the number of processes: "))
    burst_time = [0] * n
    priority = [0] * n
    wt = [0] * n
    tat = [0] * n
    total = 0

    for i in range(n):
        burst_time[i], priority[i] = map(int, input(f"Enter the burst time and priority for process {i + 1}: ").split())

    # Sorting based on priority (lower priority number = higher priority)
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
    print(f"Average turnaround time is {avg_tat}\n")

def round_robin():
    n = int(input("Enter the number of processes: "))
    arrival_time = [0] * n
    burst_time = [0] * n
    remaining_time = [0] * n
    wait_time = 0
    turn_around_time = 0

    for i in range(n):
        arrival_time[i], burst_time[i] = map(int, input(f"Enter the arrival and burst time for process {i + 1}: ").split())
        remaining_time[i] = burst_time[i]

    time_quantum = int(input("Enter time quantum: "))
    
    print("\nProcess\t| TAT\t| Waiting Time")
    
    time = 0
    remain = n
    count = 0
    flag = 0

    while remain != 0:
        if remaining_time[count] <= time_quantum and remaining_time[count] > 0:
            time += remaining_time[count]
            remaining_time[count] = 0
            flag = 1
        elif remaining_time[count] > time_quantum and remaining_time[count] > 0:
            remaining_time[count] -= time_quantum
            time += time_quantum

        if flag == 1:
            remain -= 1
            tat = time - arrival_time[count]  # Turnaround time
            waiting_time = tat - burst_time[count]  # Waiting time
            print(f"P[{count + 1}]\t| {tat}\t| {waiting_time}")
            wait_time += waiting_time
            turn_around_time += tat
            flag = 0

        if count == n - 1:
            count = 0
        elif arrival_time[count + 1] <= time:
            count += 1
        else:
            count = 0

    avg_wait_time = wait_time / n
    avg_turnaround_time = turn_around_time / n

    print(f"Average waiting time is: {avg_wait_time}")
    print(f"Average turnaround time is: {avg_turnaround_time}\n")

def sjf():
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
    print(f"Average turnaround time is: {avg_tat}\n")

def main():
    print("Select Scheduling Algorithm:")
    print("1. FCFS (First Come First Serve)")
    print("2. Priority Scheduling")
    print("3. Round Robin Scheduling")
    print("4. Shortest Job First (SJF)")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        fcfs()
    elif choice == 2:
        priority()
    elif choice == 3:
        round_robin()
    elif choice == 4:
        sjf()
    else:
        print("Invalid choice! Please select a valid option.")
        
if __name__ == "__main__":
    main()
