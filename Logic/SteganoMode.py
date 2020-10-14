import string

from typing import List, Tuple
from random import randint
from PIL import Image
from statistics import mean
from itertools import chain


class Debug:
    #? Enumerate-like object to make code more readable.
    #? Stores readable names for Debug Types

    Visualize_Neighbors = 1
    Log_All = 2
    Check_Output = 3


class RGB_Values:
    #? Enumerate-like object to make code more readable.
    #? Stores readable names for RGB Values

    Red = 0
    Green = 1
    Blue = 2


class Steganos:
    def __init__(self, image: str = None, key: str = None, maxRejects: int = 50000, radius: int = 10, averageRadius: int = 8):
        #* Turning key string into key code
        self.__keyCode = "".join([str(ord(char) ** i) for i, char in enumerate(key * 3)])

        #* Figuring out constants based on the key
        self.maxRejectsConstant = maxRejects
        self.radiusConstant = radius
        self.averageRadiusConstant = averageRadius
        self.multiplierConstant = int(
            self.__keyCode[len(self.__keyCode) // 3 + 1:len(self.__keyCode) // 3 * 2]
        ) % 125 + 1

        #* Initializing miscellaneous variables
        self.done = False
        self.name = image
        self.image = Image.open(image)
        self.size = (self.image.width, self.image.height)
        self.coordsMatrix = []
        for x in range(self.image.width):
            row = []
            for y in range(self.image.height):
                row.append([x, y])
            self.coordsMatrix.append(row)
        self.visitedPixels = []
        self.alphabet = {0: "a"}
        self.alphabetBack = {"a": 0}
        letters = list(string.ascii_uppercase + "bcdefghijklmnopqrstuvwxyz" + string.digits + "-§")
        for i, char in enumerate(letters):
            self.alphabet[i + 1] = char
            self.alphabetBack[char] = i + 1
        self.message = ""

    def cypherRoutine(self, message: str = None, debug: int = None) -> str:
        #? The only function available to the end user used to cypher a message
        #? Parameters:
        #?      message <str>: The message to cypher. If None, the message is asked
        #?      debug <int>: The type of debug strategy to execute. If None, program is ran normally

        while True:
            try:
                self.message = "-".join(message.split(" ")) + "§"
                if not message and not self.message:
                    self.message = "-".join(input("Message: ").split(" ")) + "§"
                for i, char in enumerate(self.message):
                    if char not in self.alphabetBack.keys():
                        self.message = self.message.replace(char, "")
                return self.__encryptMessage(self.message, debug=debug)
            except RecursionError:
                self.image = Image.open(self.name)
                self.visitedPixels = []
                continue

    def __createInstruction(self, lookingAt: Tuple[int, int]) -> Tuple[int, ...]:
        #? Creates a valid instruction
        #? Parameters:
        #?      lookingAt <Tuple[int]>: The current coordinate the program is looking at

        maxW = 120
        maxH = 120
        rejects = 0
        while True:
            instruction = self.__createColorFromInstruction(
                randint(
                    -maxW // self.multiplierConstant,
                    maxH // self.multiplierConstant
                ),
                randint(
                    -maxW // self.multiplierConstant,
                    maxH // self.multiplierConstant
                ),
                lookingAt
            )
            average = self.__averageColor(lookingAt)
            if self.__instructionIsValid(instruction=instruction, average=average, lookingAt=lookingAt):
                return instruction
            rejects += 1
            if rejects > self.maxRejectsConstant:
                raise RecursionError("Max Rejects Exceeded")

    def __encryptMessage(self, message: str, debug: int = None) -> str:
        #? The function, hidden for the end user, used to cypher a message
        #? Parameters:
        #?      message <str>: The message to cypher.
        #?      debug <int>: The type of debug strategy to execute. If None, program is ran normally

        if debug == Debug.Log_All:
            print("-----Initial Values-----")
            print(f"Max Rejects Constant: {self.maxRejectsConstant}")
            print(f"Radius Constant: {self.radiusConstant}")
            print(f"Average Radius Constant: {self.averageRadiusConstant}")
            print(f"Multiplier Constant: {self.multiplierConstant}")

        lookingAt = (self.size[0] // 2, self.size[1] // 2)
        self.__addPositionToVisited(lookingAt)
        for _, char in enumerate(message):

            #* Adds the 5 to 10 instructions to reach the actual char
            for index in range(0, randint(5, 10)):
                instruction = tuple([int(rgb) for rgb in self.__createInstruction(lookingAt)])
                average = [int(rgb) for rgb in self.__averageColor(lookingAt)]
                self.image.putpixel(lookingAt, instruction)

                if debug == Debug.Log_All:
                    print(f"-----{lookingAt}-----")
                    print(f"Instruction: {instruction}")
                    print(f"Average: {average}")
                    print(f"Index: {index}")

                if debug == Debug.Visualize_Neighbors:
                    neighbors = self.__neighbors(self.radiusConstant, lookingAt[0], lookingAt[1], self.coordsMatrix)
                    for coord in neighbors[0]:
                        self.image.putpixel(coord, (255, 0, 0))
                    for coord in neighbors[-1]:
                        self.image.putpixel(coord, (255, 0, 0))
                    for row in neighbors:
                        self.image.putpixel(row[0], (255, 0, 0))
                        self.image.putpixel(row[-1], (255, 0, 0))

                lookingAt = self.__moveFollowing(
                    instruction=instruction,
                    lookingAt=lookingAt,
                    average=average,
                    components=(
                        RGB_Values.Green,
                        RGB_Values.Blue
                    )
                )
                self.__addPositionToVisited(lookingAt)

            #* Adds the actual char
            color = tuple([int(rgb) for rgb in self.__createColorFromChar(char, lookingAt)])
            average = [int(rgb) for rgb in self.__averageColor(lookingAt)]
            self.image.putpixel(lookingAt, color)

            if debug == Debug.Log_All:
                print(f"-----{lookingAt}-----")
                print(f"Instruction: {color}")
                print(f"Average: {average}")
                print(f"Char: {char}")

            if debug == Debug.Visualize_Neighbors:
                neighbors = self.__neighbors(self.radiusConstant, lookingAt[0], lookingAt[1], self.coordsMatrix)
                for coord in neighbors[0]:
                    self.image.putpixel(coord, (255, 0, 0))
                for coord in neighbors[-1]:
                    self.image.putpixel(coord, (255, 0, 0))
                for row in neighbors:
                    self.image.putpixel(row[0], (255, 0, 0))
                    self.image.putpixel(row[-1], (255, 0, 0))

            lookingAt = self.__moveFollowing(
                instruction=color,
                lookingAt=lookingAt,
                average=average,
                components=(
                    RGB_Values.Red,
                    RGB_Values.Red
                )
            )
            self.__addPositionToVisited(lookingAt)

        print()
        ext = self.name.split(".")[-1]
        self.image.save(self.name + "_encrypted." + ext)
        return self.name + "_encrypted." + ext

    def __createColorFromChar(self, char: str, lookingAt: Tuple[int, int]) -> Tuple[int, ...]:
        #? Creates a valid char instruction
        #? Parameters:
        #?      char <str>: The char to create the instruction for
        #?      lookingAt <Tuple[int]>: The current coordinates the program is looking at

        ordinal = str(self.alphabetBack[char])
        if len(ordinal) == 1:
            ordinal = "0" + ordinal
        ordinalG = int(ordinal[0])
        ordinalB = int(ordinal[1])
        average = self.__averageColor(lookingAt)
        rejects = 0
        while True:
            RGB = tuple(
                [average[0] - randint(2, 9),
                 average[RGB_Values.Green] - ordinalG,
                 average[RGB_Values.Blue] - ordinalB]
            )
            if self.__ColorIsValid(color=RGB, average=average, lookingAt=lookingAt):
                return RGB
            rejects += 1
            if rejects > self.maxRejectsConstant:
                raise RecursionError("Max Rejects Exceeded")

    def decipherRoutine(self, debug: int = None) -> str:
        #? The only function available to the end user used to decipher a message
        #? Parameters:
        #?      debug <int>: The type of debug strategy to execute. If None, program is ran normally

        if debug == Debug.Check_Output:
            with open(input("Expected Output File: "), "r") as f:
                lines = [line.strip() for line in f.readlines()]
                for i, line in enumerate(lines):
                    try:
                        lines[i] = eval(line)
                    except (SyntaxError, NameError):
                        pass
                linesIndex = 0

        lookingAt = (self.size[0] // 2, self.size[1] // 2)
        message = ""
        deciphering = True
        while deciphering:

            #* Go through the instructions
            index = 0
            while True:
                pixel = self.image.getpixel(lookingAt)
                average = [int(rgb) for rgb in self.__averageColor(lookingAt)]

                #* "It's an instruction, keep going"
                if average[RGB_Values.Red] == pixel[RGB_Values.Red]:

                    if debug == Debug.Log_All:
                        print(f"-----{lookingAt}-----")
                        print(f"Pixel: {pixel}")
                        print(f"Average: {average}")
                        print(f"Index: {index}")

                    if debug == Debug.Check_Output:
                        print(f"-----{lookingAt}-----")
                        linesIndex += 1
                        print(f"Pixel: {pixel[:3]}")
                        print(f"Expected Pixel: {lines[linesIndex]}")
                        print(f"Equal: {pixel[:3] == lines[linesIndex]}")
                        linesIndex += 1
                        print(f"Average: {average}")
                        print(f"Expected Average: {lines[linesIndex]}")
                        print(f"Equal: {average == lines[linesIndex]}")
                        linesIndex += 1
                        print(f"Index: {index}")
                        print(f"Expected Index: {lines[linesIndex]}")
                        print(f"Equal: {index == lines[linesIndex]}")
                        linesIndex += 1

                    lookingAt = self.__moveFollowing(
                        instruction=pixel,
                        lookingAt=lookingAt,
                        average=average,
                        components=(
                            RGB_Values.Green,
                            RGB_Values.Blue
                        )
                    )
                    index += 1

                #* "It's not an instruction, stop"
                else:
                    break

            #* Parses the actual char
            pixel = self.image.getpixel(lookingAt)
            average = [int(rgb) for rgb in self.__averageColor(lookingAt)]
            try:
                char = self.alphabet[
                    int(
                        str(average[RGB_Values.Green] - pixel[RGB_Values.Green])
                        +
                        str(average[RGB_Values.Blue] - pixel[RGB_Values.Blue])
                    )
                ]
            except (KeyError, ValueError):
                raise ValueError("Invalid Key")

            if debug == Debug.Log_All:
                print(f"-----{lookingAt}-----")
                print(f"Pixel: {pixel}")
                print(f"Average: {average}")
                print(f"Char: {char}")

            if debug == Debug.Check_Output:
                print(f"-----{lookingAt}-----")
                linesIndex += 1
                print(f"Pixel: {pixel[:3]}")
                print(f"Expected Pixel: {lines[linesIndex]}")
                print(f"Equal: {pixel[:3] == lines[linesIndex]}")
                linesIndex += 1
                print(f"Average: {average}")
                print(f"Expected Average: {lines[linesIndex]}")
                print(f"Equal: {average == lines[linesIndex]}")
                linesIndex += 1
                print(f"Char: {char}")
                print(f"Expected Char: {lines[linesIndex]}")
                print(f"Equal: {char == lines[linesIndex]}")
                linesIndex += 1

            if char == "§":
                break
            message += char
            lookingAt = self.__moveFollowing(
                instruction=pixel,
                lookingAt=lookingAt,
                average=average,
                components=(
                    RGB_Values.Red,
                    RGB_Values.Red
                )
            )

        return " ".join(message.split("-"))

    def __createColorFromInstruction(self, right: int, down: int, lookingAt: Tuple[int, int]) -> Tuple[int, ...]:
        #? Creates an instruction. Doesn't care if it's not valid
        #? Parameters:
        #?      right <int>: How far to the right the instruction needs to guide
        #?      down <int>: How far to down the instruction needs to guide
        #?      lookingAt <Tuple[int]>: The current coordinates the program is looking at

        average = self.__averageColor(lookingAt)
        RGB = tuple(
            [average[RGB_Values.Red],
             average[RGB_Values.Green] - right,
             average[RGB_Values.Blue] - down]
        )
        return RGB

    def __colorNeighbors(self, radius: int, rowNumber: int, columnNumber: int, matrix: List[List[List[int]]]) \
            -> List[List[Tuple[int, int, int]]]:
        #? Returns a pixel's neighbour's RGB values
        #? Parameters:
        #?      radius <int>: The maximum distance from the center for a pixel
        #?                    to still be considered neighbor
        #?      rowNumber <int>: The Y coordinate
        #?      columnNumber <int>: The X coordinate
        #?      matrix <List[List[List[int]]]>: The matrix containing all the image coordinates

        colorNeighbors = []
        for row in self.__neighbors(radius=radius,
                                    rowNumber=rowNumber,
                                    columnNumber=columnNumber,
                                    matrix=matrix):
            colorRow = []
            for cell in row:
                if cell:
                    colorRow.append(self.image.getpixel(tuple(cell))[:3])
                else:
                    colorRow.append((123, 123, 123))
            colorNeighbors.append(colorRow)

        return colorNeighbors

    @staticmethod
    def __neighbors(radius: int, rowNumber: int, columnNumber: int, matrix: List[List[List[int]]]) \
            -> List[List[List[int]]]:
        #? Returns a pixel's neighbour's coordinates
        #? Parameters:
        #?      radius <int>: The maximum distance from the center for a pixel
        #?                    to still be considered neighbor
        #?      rowNumber <int>: The Y coordinate
        #?      columnNumber <int>: The X coordinate
        #?      matrix <List[List[List[int]]]>: The matrix containing all the image coordinates

        #* Credits to "https://stackoverflow.com/questions/22550302/find-neighbors-in-a-matrix"
        neighbors = [[matrix[i][j] if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) else None
                      for j in range(columnNumber - 1 - radius, columnNumber + radius)]
                     for i in range(rowNumber - 1 - radius, rowNumber + radius)]

        #* Removes the center of the matrix
        for row in neighbors:
            if [rowNumber, columnNumber] in row:
                row[row.index([rowNumber, columnNumber])] = None

        return neighbors

    def __averageColor(self, position: Tuple[int, int]) -> List[int]:
        #? Calculates the average color of a set position's neighbors

        meanValues = []
        neighbors = self.__colorNeighbors(
            self.averageRadiusConstant,
            position[0],
            position[1],
            self.coordsMatrix
        )
        for i in range(3):
            meanValue = int(mean([value[i] for value in list(chain.from_iterable(neighbors))]))
            if meanValue >= 0:
                meanValues.append(meanValue)
            else:
                meanValues.append(0)

        return meanValues

    def __moveFollowing(self, instruction: Tuple[int, ...], lookingAt: Tuple[int, int],
                        average: List[int], components: Tuple[int, int]) -> Tuple[int, ...]:
        #? Moves the current position the program is looking at based on a few values
        #? Parameters:
        #?      instruction <Tuple[int]>: The instruction
        #?      lookingAt <Tuple[int]>: The current position the program is looking at
        #?      average <Tuple[int]>: The average color of a position's neighbors

        lookingAt = list(lookingAt)
        lookingAt[0] = (lookingAt[0] + (
                (average[components[0]] - instruction[components[0]]) * self.multiplierConstant)
                        ) % self.image.width
        lookingAt[1] = (lookingAt[1] + (
                (average[components[1]] - instruction[components[1]]) * self.multiplierConstant)
                        ) % self.image.height
        return tuple(lookingAt)

    def __addPositionToVisited(self, position: Tuple[int, ...]) -> None:
        #? Add a position and it's neighbors to the visitedPixels array
        #? Parameters:
        #?      position <Tuple[int]>: The position itself

        self.visitedPixels.append(position)
        for neighborRow in self.__neighbors(self.radiusConstant, position[0], position[1], self.coordsMatrix):
            for neighbor in neighborRow:
                if neighbor:
                    self.visitedPixels.append(tuple(neighbor))

    def __instructionIsValid(self,
                             instruction: Tuple[int, ...],
                             average: List[int],
                             lookingAt: Tuple[int, int]) -> bool:
        #? Checks if an instruction is valid
        #? Parameters:
        #?      instruction <Tuple[int]>: The instruction itself
        #?      average <Tuple[int[>: The average color of a position's neighbors
        #?      lookingAt <Tuple[int]>: The current position the program is looking at

        expectedPosition = self.__moveFollowing(
            instruction=instruction,
            lookingAt=lookingAt,
            average=average,
            components=(
                RGB_Values.Green,
                RGB_Values.Blue
            )
        )
        if average[RGB_Values.Red] < instruction[RGB_Values.Red] or instruction[RGB_Values.Red] < 0:
            return False
        if average[RGB_Values.Green] < instruction[RGB_Values.Green] or instruction[RGB_Values.Green] < 0:
            return False
        if average[RGB_Values.Blue] < instruction[RGB_Values.Blue] or instruction[RGB_Values.Blue] < 0:
            return False
        if not 0 < expectedPosition[0] < self.image.width:
            return False
        elif not 0 < expectedPosition[1] < self.image.height:
            return False
        else:
            try:
                if expectedPosition in self.visitedPixels:
                    return False
                return True
            except IndexError:
                return False

    def __ColorIsValid(self, color: Tuple[int, ...], average: List[int], lookingAt: Tuple[int, int]) -> bool:
        #? Checks if a color instruction is valid
        #? Parameters:
        #?      color <Tuple[int]>: The color instruction itself
        #?      average <Tuple[int[>: The average color of a position's neighbors
        #?      lookingAt <Tuple[int]>: The current position the program is looking at

        expectedPosition = self.__moveFollowing(
            instruction=color,
            lookingAt=lookingAt,
            average=average,
            components=(
                RGB_Values.Red,
                RGB_Values.Red
            )
        )
        if average[RGB_Values.Red] < color[RGB_Values.Red] or color[RGB_Values.Red] < 0:
            return False
        if average[RGB_Values.Green] < color[RGB_Values.Green] or color[RGB_Values.Green] < 0:
            return False
        if average[RGB_Values.Blue] < color[RGB_Values.Blue] or color[RGB_Values.Blue] < 0:
            return False
        if expectedPosition in self.visitedPixels:
            return False
        return True


if __name__ == '__main__':
    s = Steganos(input("Image: "), input("Key: "), 50000, 10, 9)
    s.cypherRoutine()
    s = Steganos(input("Image: "), input("Key: "), 50000, 10, 9)
    print("Message: " + s.decipherRoutine())
