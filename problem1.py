def arithmetic_arranger(problems, show):
    arr = list()
    p1 = list()
    sign = list()
    p2 = list()

    for i in problems:
        arr.append(i.split())

    index = 0
    while index < len(arr):
        p2lg = len(arr[index][2])

        p1.append(arr[index][0])
        sign.append(arr[index][1])
        p2.append(arr[index][2])
        index += 1
    #print(p1, sign, p2)

    #Check for errors
    if len(p1) > 5:
        print("Error: Too many problems")
        return
    if '*' in sign or '/' in sign:
        print("Error: Operator must be '+' or '-'.")
        return
    for i in p1:
        if not i.isdecimal():
            print("Error: Numbers must only contain digits.")
            return
        if len(i) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return
    for i in p2:
        if not i.isdecimal():
            print("Error: Numbers must only contain digits.")
            return
        if len(i) > 4:
            print("Error: Numbers must only contain digits.")
            return

    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""
    for i in range(len(p2)):
        maxi = max(len(p1[i]), len(p2[i]))
        lg1 = len(p1[i])
        lg2 = len(p2[i])

        for j in range(maxi + 2 - lg1):
            first_row += " "
        first_row += p1[i]
        first_row += "    "

        second_row += sign[i]
        for j in range(maxi + 2 - lg2 - 1):
            second_row += " "
        second_row += p2[i]
        second_row += "    "

        for j in range(maxi + 2):
            third_row += "-"
        third_row += "    "

        if(sign[i] == '+'):
            result = int(p1[i]) + int(p2[i])
        else:
            result = int(p1[i]) - int(p2[i])

        result = str(result)
        for j in range(maxi + 2 - len(result)):
            fourth_row += " "
        fourth_row += result
        fourth_row += "    "


    print(first_row)
    print(second_row)
    print(third_row)
    if(show is True):
        print(fourth_row)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
