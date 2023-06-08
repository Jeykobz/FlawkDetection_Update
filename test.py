import json

# Configure detection and update frequency
valid_bt_freq = False
while(not valid_bt_freq):
    bt_frequency = input("Please provide the prefered bluetooth capturing frequency. (Default=10s) bt_frequency = ")
    try:
        bt_frequency = int(bt_frequency)
    except:
        print("Invalid value!")
        continue

    if bt_frequency <= 180 and bt_frequency >= 1:
        valid_bt_freq = True
        print(f"Bluetooth frequency configured: {bt_frequency}s")
    else:
        print("Out of valid range [1, 180].")
    
valid_occupancy_freq = False
while(not valid_occupancy_freq):
    occ_frequency = input("Please provide the prefered occupancy/views capturing frequency. (Default=120s) occupancy_frequency = ")
    try:
        occ_frequency = int(occ_frequency)
    except:
        print("Invalid value!")
        continue

    if occ_frequency <= 3600 and occ_frequency >= 30:
        valid_occupancy_freq = True
        print(f"Occupancy frequency configured: {occ_frequency}s")
    else:
        print("Out of valid range [30, 3600].")

valid_ip_freq = False
while(not valid_ip_freq):
    ip_frequency = input("Please provide the prefered IP capturing frequency. (Default=30s) ip_frequency = ")
    try:
        ip_frequency = int(ip_frequency)
    except:
        print("Invalid value!")
        continue
    
    if ip_frequency > occ_frequency - 10:
        print(f"IP capturing frequency can't be higher than {occ_frequency - 10}")
    else:
        if ip_frequency <= 3600 and ip_frequency >= 30:
            valid_ip_freq = True
            print(f"IP capturing frequency configured: {ip_frequency}s")
        else:
            print("Out of valid range [10, 120].")

valid_update_freq = False
while(not valid_update_freq):
    print("Please provide the prefered database update frequency. After how many x occupancy measurements should an update be sent to the database? (Default=3)")
    update_frequency = input("update_frequency = ")
    try:
        update_frequency = int(update_frequency)
    except:
        print("Invalid value!")
        continue

    if (update_frequency * occ_frequency <= 7200) and update_frequency >= 1:
        valid_update_freq = True
        print(f"Update frequency configured: {update_frequency}. In other words: Approx. every '{update_frequency} x {occ_frequency} = {update_frequency*occ_frequency}' seconds a new update is sent to the database.")
    else:
        print(f"Out of valid range [1, {round(7200/occ_frequency)}].")

# Load configuration to config.json
config = {"ble_frequency": bt_frequency, "occupancy_frequency": occ_frequency, "ip_frequency": ip_frequency, "update_frequency": update_frequency}
f_path = "/FlawkDetection/DataHandler/config.json"
with open(f_path, "w") as f:
    f.write(json.dumps(config))