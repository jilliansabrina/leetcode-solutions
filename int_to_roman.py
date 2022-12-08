def intToRoman(num: int) -> str:
        num = str(num)
        roman = ''

        Roman_dict = {
            0 : "I",
            1 : "V",
            2 : "X",
            3 : "L",
            4 : "C",
            5 : "D",
            6 : "M"
        }

        for digit in range(len(num)):
            # Index of the integer to traverse through from right to left.
            idx = len(num) - 1 - digit

            if int(num[idx]) == 9:
                roman = Roman_dict[digit * 2] + Roman_dict[digit * 2 + 2] + roman
            elif int(num[idx]) >= 5:
                roman = Roman_dict[digit * 2 + 1] + Roman_dict[digit * 2] * (int(num[idx]) - 5) + roman
            elif int(num[idx]) >= 4:
                roman = Roman_dict[digit * 2] + Roman_dict[digit * 2 + 1] + roman
            else:
                roman = Roman_dict[digit * 2] * int(num[idx]) + roman
        return roman

print(intToRoman(1994))