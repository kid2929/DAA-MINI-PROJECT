def main():
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
    print(f"Average turnaround time is: {avg_turnaround_time}")

if __name__ == "__main__":
    main()
