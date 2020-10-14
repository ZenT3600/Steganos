from random import randint
from PIL import Image


class Steganos:
    def __init__(self, image=None, size=2048, tries=0):
        self.__tries = tries
        self.size = size
        if not image:
            self.imageName = "ecnrypted_image_" + str(randint(111, 999)) + ".png"
        else:
            self.image = image

    def cypherRoutine(self, message=None):
        self.image = Image.new('RGB', (self.size, self.size), color=(0, 0, 0))
        if not message:
            message = "-".join(input("Message: ").split(" "))
        return self._encryptMessage(message)

    def __createInstruction(self, lookingAt):
        while True:
            maxW = 122
            maxH = 122
            instruction = self._createColorFromInstruction(randint(-maxW, maxH), randint(-maxW, maxH))
            if not maxW or not maxH:
                raise Exception("Bruh the image is full...")
            if not 0 < (instruction[1] - 122) - lookingAt[0] < self.image.width:
                maxW -= 1
                continue
            elif not 0 < (instruction[2] - 122) - lookingAt[1] < self.image.height:
                maxH -= 1
                continue
            else:
                try:
                    if self.image.getpixel(
                            (lookingAt[0] + (122 - instruction[1]), lookingAt[1] + (122 - instruction[2]))) != (
                    0, 0, 0):
                        maxW -= 1
                        maxH -= 1
                        continue
                    else:
                        return instruction
                except IndexError:
                    maxW -= 1
                    maxH -= 1
                    continue

    def _encryptMessage(self, message):
        lookingAt = (0, 0)
        localTries = 0
        for i, char in enumerate(message):
            for _ in range(randint(5, 15)):
                while True:
                    try:
                        if self.__tries > 10:
                            return
                        if localTries > 200:
                            self.size += 128
                            self.cypherRoutine(message)
                            return
                        instruction = self.__createInstruction(lookingAt)
                        self.image.putpixel(lookingAt, instruction)
                        break
                    except IndexError:
                        localTries += 1
                lookingAt = list(lookingAt)
                lookingAt[0] += 122 - instruction[1]
                lookingAt[1] += 122 - instruction[2]
                lookingAt = tuple(lookingAt)

            while True:
                try:
                    if self.__tries > 10:
                        return
                    if localTries > 200:
                        self.__tries += 1
                        self.size += 128
                        self.cypherRoutine(message)
                        return
                    color = self._createColorFromChar(char, i - 1 == len(message), lookingAt)
                    self.image.putpixel(lookingAt, color)
                    break
                except IndexError:
                    localTries += 1
            lookingAt = list(lookingAt)
            lookingAt[0] += 5 - int(str(color[2])[0])
            lookingAt[1] += 5 - int(str(color[2])[1])
            lookingAt = tuple(lookingAt)

        self.image.save(self.imageName)
        return self.imageName

    def _createColorFromChar(self, char, last, lookingAt):
        ordinal = ord(char)
        while True:
            RGB = tuple([randint(22, 88), ordinal, randint(22, 88)])
            if last:
                RGB = tuple([255, ordinal, 255])
            if self.image.getpixel(
                            (lookingAt[0] + (5 - int(str(RGB[2])[0])),
                             lookingAt[1] + (5 - int(str(RGB[2])[1])))
                            ) != (0, 0, 0):
                continue
            break
        return RGB

    def decipherRoutine(self):
        lookingAt = (0, 0)
        lookingAtLog = []
        message = ""
        img = Image.open(self.image)
        dechypering = True
        while dechypering:
            if img.getpixel(lookingAt)[0] == 255:
                break
            trying = True
            while trying:
                pixel = img.getpixel(lookingAt)

                if pixel[0] >= 122:
                    lookingAt = list(lookingAt)
                    lookingAt[0] += 122 - pixel[1]
                    lookingAt[1] += 122 - pixel[2]
                    lookingAt = tuple(lookingAt)
                else:
                    trying = False
            lookingAt = list(lookingAt)
            try:
                lookingAt[0] += 5 - int(str(pixel[2])[0])
                lookingAt[1] += 5 - int(str(pixel[2])[1])
            except IndexError:
                break
            lookingAt = tuple(lookingAt)
            lookingAtLog.append([lookingAt, img.getpixel(lookingAt)])
            message += chr(pixel[1])
        return " ".join(message.split("-"))

    @staticmethod
    def _createColorFromInstruction(right, down):
        RGB = tuple([randint(178, 250), 122 + right, 122 + down])
        return RGB


if __name__ == '__main__':
    s = Steganos()
    s.cypherRoutine()
    s = Steganos(input("Image Name: "))
    print(s.decipherRoutine())
