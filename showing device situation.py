```python
import psutil

def get_battery_usage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    return f"Battery: {percent}% (Plugged in: {plugged})"

def get_storage_status():
    disk_usage = psutil.disk_usage("/")
    total = disk_usage.total / (1024**3) 
    
    used = disk_usage.used / (1024**3)
    free = disk_usage.free / (1024**3)

    return f"Storage: Total: {total:.2f} GB, Used: {used:.2f} GB, Free: {free:.2f} GB"

def get_data_usage():
    network = psutil.net_io_counters()
    total_sent = network.bytes_sent / (1024**2)  
    
    total_received = network.bytes_recv / (1024**2)

    return f"Data usage: Sent: {total_sent:.2f} MB, Received: {total_received:.2f} MB"


if __name__ == "__main__":
    battery_usage = get_battery_usage()
    storage_status = get_storage_status()
    data_usage = get_data_usage()

    print(battery_usage)
    print(storage_status)
    print(data_usage)
```

```
pip install psutil
```