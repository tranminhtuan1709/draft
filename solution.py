month = ["January", "February", "March", "April", "May", "June",
         "July","August", "September", "October", "November", "December"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(6, len(month)):
    d = ""
    s = "COUNTIF(...!F:F, FALSE) + COUNTIF(...!H:H, FALSE)+ COUNTIF(...!J:J, FALSE) + COUNTIF(...!L:L, FALSE) + "
    d += s.replace('...', month[i], -1)
    print(d)
