class SevenSegmentDisplay:
    segment = [[0 for _ in range(4)] for _ in range(5)]

    @staticmethod
    def lightA():
        SevenSegmentDisplay.segment[0][0] = 1
        SevenSegmentDisplay.segment[0][1] = 1
        SevenSegmentDisplay.segment[0][2] = 1
        SevenSegmentDisplay.segment[0][3] = 1

    @staticmethod
    def lightB():
        SevenSegmentDisplay.segment[0][3] = 1
        SevenSegmentDisplay.segment[1][3] = 1
        SevenSegmentDisplay.segment[2][3] = 1

    @staticmethod
    def lightC():
        SevenSegmentDisplay.segment[2][3] = 1
        SevenSegmentDisplay.segment[3][3] = 1
        SevenSegmentDisplay.segment[4][3] = 1

    @staticmethod
    def lightD():
        SevenSegmentDisplay.segment[4][0] = 1
        SevenSegmentDisplay.segment[4][1] = 1
        SevenSegmentDisplay.segment[4][2] = 1
        SevenSegmentDisplay.segment[4][3] = 1

    @staticmethod
    def lightE():
        SevenSegmentDisplay.segment[2][0] = 1
        SevenSegmentDisplay.segment[3][0] = 1
        SevenSegmentDisplay.segment[4][0] = 1

    @staticmethod
    def lightF():
        SevenSegmentDisplay.segment[0][0] = 1
        SevenSegmentDisplay.segment[1][0] = 1
        SevenSegmentDisplay.segment[2][0] = 1

    @staticmethod
    def lightG():
        SevenSegmentDisplay.segment[2][0] = 1
        SevenSegmentDisplay.segment[2][1] = 1
        SevenSegmentDisplay.segment[2][2] = 1
        SevenSegmentDisplay.segment[2][3] = 1

    @staticmethod
    def display():
        for index in SevenSegmentDisplay.segment:
            for input in index:
                if input == 1:
                    print("# ", end="")
                else:
                    print("  ", end="")
            print()

    @staticmethod
    def inputValue(value):
        if len(value) > 7:
            value = value[:7]

        for index in value:
            if index not in ['0', '1']:
                raise ValueError("Input must be 0 or 1")

        for index in range(len(value)):
            bit = value[index]
            if bit == '1':
                if index == 0:
                    SevenSegmentDisplay.lightA()
                elif index == 1:
                    SevenSegmentDisplay.lightB()
                elif index == 2:
                    SevenSegmentDisplay.lightC()
                elif index == 3:
                    SevenSegmentDisplay.lightD()
                elif index == 4:
                    SevenSegmentDisplay.lightE()
                elif index == 5:
                    SevenSegmentDisplay.lightF()
                elif index == 6:
                    SevenSegmentDisplay.lightG()

    def MainDisplay(self,value):
        display = SevenSegmentDisplay()
        value = input("ENTER 0s and 1s and 1 at the end to on or 0 to off ")
        display.inputValue(value)
        display.display()


##frank = sev
##00001101