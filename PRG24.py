def transfer_time(file_size, unit="KiB", ethernet_speed=10):
     if unit=="KiB":
        file_size *= 1024
     elif unit == "Mib":
        file_size *= 1024**2
     elif unit == "GiB":
         file_size *= 1024**3
     file_size_bites = file_size * 8
     return file_size_bites / (ethernet_speed * 1e6)
print(transfer_time(80,"GiB",100))

        