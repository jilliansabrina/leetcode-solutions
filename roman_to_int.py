def romanToInt(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    
    valuesList = []
    
    # Using dictionaries is super slow.
    # Roman_dict = {
    #         "I" : 1,
    #         "V" : 5,
    #         "X" : 10,
    #         "L" : 50,
    #         "C" : 100,
    #         "D" : 500,
    #         "M" : 1000
    #     }
    # for letter in s:
    #     valuesList.append(Roman_dict[letter])

    # Most efficient runtime and use of memory.
    for letter in s:
            match letter:
                case "I":
                    valuesList.append(1)
                case "V":
                    valuesList.append(5)
                case "X":
                    valuesList.append(10)
                case "L":
                    valuesList.append(50)
                case "C":
                    valuesList.append(100)
                case "D":
                    valuesList.append(500)
                case "M":
                    valuesList.append(1000)
                case _:
                    return;
    
    num = 0
    ctr = 0

    for value in valuesList:
        if(ctr == len(valuesList) - 1):
            num += value
            return num;
        print(value)
        if(valuesList[ctr + 1] > value):
            num -= value
        else:
            num += value
        ctr += 1

print(romanToInt("MCMXCIV"))