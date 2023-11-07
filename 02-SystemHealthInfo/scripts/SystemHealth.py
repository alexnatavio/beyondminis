import psutil


# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=True)


# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "free": memory.free,
    }


# Function to get disk usage
def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_usage = {}
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage[partition.device] = {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent,
        }
    return disk_usage


# Function to get active users
def get_active_users():
    users = []
    for user in psutil.users():
        users.append({
            "username": user.name,
            "terminal": user.terminal,
            "host": user.host,
            "started": user.started,
        })
    return users


# Function to get running processes
def get_running_processes():
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        processes.append({
            "pid": process.info['pid'],
            "name": process.info['name'],
        })
    return processes


# Main function to display system information
def main():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    active_users = get_active_users()
    running_processes = get_running_processes()

    print("CPU Usage (per core):")
    for core, usage in enumerate(cpu_usage):
        print(f"Core {core + 1}: {usage}%")

    print("\nMemory Usage:")
    for key, value in memory_usage.items():
        print(f"{key}: {value / (1024 ** 3):.2f} GB")

    print("\nDisk Usage:")
    for partition, usage in disk_usage.items():
        print(f"Partition {partition}:")
        for key, value in usage.items():
            print(f"{key}: {value / (1024 ** 3):.2f} GB")

    print("\nActive Users:")
    for user in active_users:
        print(f"Username: {user['username']}, Terminal: {user['terminal']}")

    print("\nRunning Processes:")
    for process in running_processes:
        print(f"PID: {process['pid']}, Name: {process['name']}")


if __name__ == "__main__":
    main()
