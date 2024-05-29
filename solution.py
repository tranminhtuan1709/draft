def customers(time, services):
    if (time < 0 or time > 8) and (services < 0 or services > 16):
        return "Invalid"
    if time <= 3 and services <= 5:
        return "New Customers"
    if time >= 4 and services > 6:
        return "Vip Customers"
    return "Potential Customers"

if __name__ == "__main__":
    time = [5, 4, 6, 2, 2, 13, 17, 15, -5]
    services = [-7, 5, 7, 7, 3, 4, 25, -9, -37]
    for i in range(len(time)):
        print(i + 1, customers(time[i], services[i]))
