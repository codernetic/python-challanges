statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(online_list):
    count = 0
    for x in online_list.values():
        if x == 'online':
            count += 1
    return count

print(online_count(statuses))

