from mypackage import config
from mypackage import networkscan

# Access and print the DEBUG configuration variable
print(config.DEBUG)

# Call the network_scan function
results = networkscan.network_scan("192.168.0.0/24", "22,80,443", "config.json")
print(results)
```

Replace `"config.json"` with the actual path to your configuration file.