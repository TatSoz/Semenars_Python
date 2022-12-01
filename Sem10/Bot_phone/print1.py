def veiw_all(file):
    list1 = []
    with open(file, encoding="utf-8") as data:
        for line in data:
            list1.append(line.replace(',', ' '))
    return list1