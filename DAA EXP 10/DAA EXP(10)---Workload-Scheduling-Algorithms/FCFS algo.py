def main():
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

    print("\nProcesses\tBurst time\tWaiting time\tTurnaround time")
    for i in range(n):
        print(f"P[{i + 1}]\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage waiting time is {avgwt}")
    print(f"Average turnaround time is {avgtat}")

if __name__ == "__main__":
    main()
