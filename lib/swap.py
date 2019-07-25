def swap(txt, m, n):
    swaped = ""
    for i in range(len(txt)):
        if i == m:
            swaped += txt[n]
        elif i == n:
            swaped += txt[m]
        else:
            swaped += txt[i]
    return swaped

