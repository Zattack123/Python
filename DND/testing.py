from rolldice import *
import cv2

if __name__ == "__main__":
    newRollListDict = roll(4, 6)
    updateRollListStats(newRollListDict, True)