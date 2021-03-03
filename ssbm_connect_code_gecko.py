import sys
from math import floor


###############################################################################
# Currently have options for left dpad, right dpad, down dpad (to clear), and #
# up dpad to use last code.                                                   #
# To use code, type 1 or 2 connect codes after script name                    #
# Eg from terminal: python3 ssbm_connect_code_gecko.py "RISK#546" "RAND#000"  #
#                                                                             #
# risky business                                                              #
# 3/1/21                                                                      #
###############################################################################



def CharLookup(char1):
    char1 = str(char1).upper()

    charOrder = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '_', '_', '_', '_', '_', '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    startIndex = 79
    decLookupVal = startIndex + charOrder.index(char1)
    lookupVal = DigitFormat(hex(decLookupVal))

    # print(char1, decLookupVal, lookupVal)

    return lookupVal


def DigitFormat(hex1):
    # print(hex1)
    tempVal = str(hex1).split("x")[1].upper()
    if len(tempVal) == 1:
        tempVal = "0" + tempVal

    return tempVal


def BranchDistance(dist1, branchType):
    if branchType == "Equal":
        branchPre = "4182"
    elif branchType == "Always":
        branchPre = "4800"

    hex1 = DigitFormat(hex(dist1 * 4))
    if len(hex1) == 1:
        branchDist = branchPre + "000" + hex1
    elif len(hex1) == 2:
        branchDist = branchPre + "00" + hex1
    elif len(hex1) == 3:
        branchDist = branchPre + "0" + hex1
    elif len(hex1) == 4:
        branchDist = branchPre + hex1
    else:
        print("JUMP DISTANCE TOO FAR")

    return branchDist


def CalcNumLines(num1):
    hex1 = DigitFormat(hex(num1))

    if len(str(hex1)) == 2:
        numOfLines = "000000" + str(hex1)
    elif len(str(hex1)) == 3:
        numOfLines = "00000" + str(hex1)
    elif len(str(hex1)) == 4:
        numOfLines = "0000" + str(hex1)
    elif len(str(hex1)) == 5:
        numOfLines = "000" + str(hex1)
    elif len(str(hex1)) == 6:
        numOfLines = "00" + str(hex1)
    elif len(str(hex1)) == 7:
        numOfLines = "0" + str(hex1)
    elif len(str(hex1)) == 8:
        numOfLines = str(hex1)

    return numOfLines


try:
    leftPlayerName = sys.argv[1]
    rightPlayerName = sys.argv[2]
except:
    pass


# lis r3, 0x0046
# ori r3, r3, 0xb109    # 0x0046b109 is a memory location that stores button press information
# lbz r5, 0(r3)         # load value of button pressed into r5
# cmpwi r5, 1           # 1 is left
# beq 0x
# cmpwi r5, 2           # 2 is right
# beq 0x
# cmpwi r5, 4           # 4 is down
# beq 0x
# cmpwi r5, 4           # not 4 causes loop to run again (this will only be if not 1, 2, or 4)
# bne -0x28             # go to top of code


geckoCodeList = ["C2196860", "tempNumOfLines", "3C600046", "6063B109", "88A30000", "2C050008", "tempBranchToEnd", "2C050001", "tempBranchToLeft", "2C050002", "tempBranchToRight", "2C050004", "tempBranchToBlank", "2C050004", "4082FFD0"]

branchToLeftDist = len(geckoCodeList) - geckoCodeList.index("tempBranchToLeft")
branchToLeft = BranchDistance(branchToLeftDist, "Equal")
geckoCodeList[geckoCodeList.index("tempBranchToLeft")] = branchToLeft

branchToRightDist = len(geckoCodeList) - geckoCodeList.index("tempBranchToRight")

branchToBlankDist = len(geckoCodeList) - geckoCodeList.index("tempBranchToBlank")

branchToEndDist = len(geckoCodeList) - geckoCodeList.index("tempBranchToEnd")

if 'leftPlayerName' in globals():
    leftCount = 0
    for i in range(8):
        if len(leftPlayerName) > i and leftPlayerName[i] != "#":
            DigitFormat(hex(leftCount))
            geckoCodeList.append("38A00082")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A000{}".format(CharLookup(leftPlayerName[i])))
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

        elif len(leftPlayerName) > i and leftPlayerName[i] == "#":
            geckoCodeList.append("38A00081")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00094")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

        else:
            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(leftCount))))
            leftCount += 1
            branchToRightDist += 2
            branchToBlankDist += 2
            branchToEndDist += 2

# will have to change this
# branchAfterLeft = "48000188"
branchAfterLeftDist = 0
geckoCodeList.append("tempBranchAfterLeft")

branchToRight = BranchDistance(branchToRightDist + 1, "Equal")
geckoCodeList[geckoCodeList.index("tempBranchToRight")] = branchToRight

branchToBlankDist += 1
branchToEndDist += 1

if 'rightPlayerName' in globals():
    rightCount = 0
    for i in range(8):
        if len(rightPlayerName) > i and rightPlayerName[i] != "#":
            DigitFormat(hex(rightCount))
            geckoCodeList.append("38A00082")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A000{}".format(CharLookup(rightPlayerName[i])))
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

        elif len(rightPlayerName) > i and rightPlayerName[i] == "#":
            geckoCodeList.append("38A00081")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00094")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

        else:
            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2

            geckoCodeList.append("38A00000")
            geckoCodeList.append("98BF00{}".format(DigitFormat(hex(rightCount))))
            rightCount += 1
            branchToBlankDist += 2
            branchAfterLeftDist += 2
            branchToEndDist += 2


branchAfterRightDist = 0
geckoCodeList.append("tempBranchAfterRight")


branchToBlank = BranchDistance(branchToBlankDist + 1, "Equal")
geckoCodeList[geckoCodeList.index("tempBranchToBlank")] = branchToBlank

branchToEndDist += 1
branchAfterLeftDist += 1


blankCount = 0
for i in range(8):
    DigitFormat(hex(blankCount))
    geckoCodeList.append("38A00000")
    geckoCodeList.append("98BF00{}".format(DigitFormat(hex(blankCount))))
    blankCount += 1
    branchAfterLeftDist += 2
    branchAfterRightDist += 2
    branchToEndDist += 2

    geckoCodeList.append("38A00000")
    geckoCodeList.append("98BF00{}".format(DigitFormat(hex(blankCount))))
    blankCount += 1
    branchAfterLeftDist += 2
    branchAfterRightDist += 2
    branchToEndDist += 2

    geckoCodeList.append("38A00000")
    geckoCodeList.append("98BF00{}".format(DigitFormat(hex(blankCount))))
    blankCount += 1
    branchAfterLeftDist += 2
    branchAfterRightDist += 2
    branchToEndDist += 2

branchAfterLeft = BranchDistance(branchAfterLeftDist + 1, "Always")
geckoCodeList[geckoCodeList.index("tempBranchAfterLeft")] = branchAfterLeft

branchAfterRight = BranchDistance(branchAfterRightDist + 1, "Always")
geckoCodeList[geckoCodeList.index("tempBranchAfterRight")] = branchAfterRight

branchToEnd = BranchDistance(branchToEndDist, "Equal")
geckoCodeList[geckoCodeList.index("tempBranchToEnd")] = branchToEnd

geckoCodeList.append("880DAFA3")
geckoCodeList.append("60000000")

numOfLines = CalcNumLines(floor(len(geckoCodeList) / 2))
geckoCodeList[geckoCodeList.index("tempNumOfLines")] = numOfLines

geckoCode = ""
for i, val in enumerate(geckoCodeList):
    geckoCode += val
    if i % 2 == 0:
        geckoCode += " "
    else:
        geckoCode += "\n"

if i % 2 == 0:
    geckoCode += "00000000\n"

print(geckoCode)

with open("tempCode.txt", 'w') as out_file:
     out_file.write(geckoCode)
