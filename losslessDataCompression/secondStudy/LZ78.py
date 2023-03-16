CHARLIMIT = 256
import sys

class LZ78Compressor:

    def compress(self, filename, output_filename):
        f = open(filename, "rb")
        bytearr = f.read()
        f.close()
        inChars = tuple(bytearr)
        outChars = (inChars[0], )
        keyToArray = {tuple(): (0, ), (inChars[0], ): (1, )}
        basePointer = 1
        limitPointer = 1
        keyCounter = [2]
        while limitPointer < len(inChars):
            if limitPointer % 1000 == 0:
                print("Compressing... "+str(int((limitPointer/len(inChars)*100)))+"%", end="\r")
            if not inChars[basePointer:limitPointer + 1] in keyToArray:
                prepend = keyToArray[inChars[basePointer:limitPointer]]
                if sum(keyCounter) == 1:
                    prepend += tuple(
                        [0 for i in range(len(keyCounter) - len(prepend) - 1)])
                else:
                    prepend += tuple(
                        [0 for i in range(len(keyCounter) - len(prepend))])
                outChars += prepend + (inChars[limitPointer], )
                keyToArray[inChars[basePointer:limitPointer +
                                1]] = tuple(keyCounter)
                #print(keyCounter)
                for i in range(len(keyCounter)):
                    keyCounter[i] += 1
                    if keyCounter[i] != CHARLIMIT:
                        break
                    else:
                        keyCounter[i] = 0
                        if i == len(keyCounter) - 1:
                            keyCounter.append(1)
                basePointer = limitPointer + 1
            limitPointer += 1
        if inChars[basePointer:
                limitPointer] in keyToArray and basePointer != limitPointer:
            prepend = tuple(keyToArray[inChars[basePointer:limitPointer]])
            outChars += prepend + tuple(
                [0 for i in range(len(keyCounter) - len(prepend))])
        
        f = open(output_filename, "wb")
        f.write(bytes(outChars))
        f.close()
        return bytes(outChars)

    def uncompress(bytearr):
        inChars = tuple(bytearr)
        outChars = (inChars[0], )
        array = [tuple(), (inChars[0], )]
        readPointer = 1
        numIndexBytes = 1
        nextLimit = CHARLIMIT
        isChar = False
        i = 0
        while readPointer < len(inChars):
            if readPointer % 1000 == 0:
                print("Uncompressing... "+str(int((readPointer/len(inChars)*100)))+"%", end="\r")
            if isChar:
                outChars += (inChars[readPointer], )
                array.append(array[i] + (inChars[readPointer], ))
                isChar = False
                readPointer += 1
                if len(array) == nextLimit + 1:
                    numIndexBytes += 1
                    nextLimit *= CHARLIMIT
            else:
                i = 0
                multiplier = 1
                for j in range(numIndexBytes):
                    i += inChars[readPointer + j] * multiplier
                    multiplier *= CHARLIMIT
                if i >= len(array):
                    print(i, len(array))
                    print(bytes(outChars))
                outChars += array[i]
                readPointer += numIndexBytes
                isChar = True
        return bytes(outChars)
