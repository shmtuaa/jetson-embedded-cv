import os
import os.path
import cv2
from xml.dom import minidom
from os.path import basename

classList = {"without_mask": 0, "with_mask": 1, "mask_weared_incorrect": 2}

workFolder = os.getcwd()
dataFolder = workFolder + "/dataset"
labelFolder = workFolder + "/dataset"
backupFolder = workFolder + "/backup"
trainList = "train.txt"
testList = "test.txt"

data = [
    'classes = 3',
    'train = train.txt',
    'valid = test.txt',
    'backup = backup',
    'names = mask.names'
]

for i in range(1, len(data)):
    t = data[i].split(" ")
    data[i] = t[0] + " " + "= " + workFolder + t[2]

for i in range(len(data)):
    data[i] += "\n"

with open('mask.data', 'w') as File:
    File.writelines(data)

name = ['without_mask',
        'with_mask',
        'mask_weared_incorrect'
        ]

for i in range(len(name)):
    name[i] += "\n"

with open('mask.names', 'w') as File:
    File.writelines(name)

if not os.path.exists(backupFolder):
    os.makedirs(backupFolder)


def transferYolo(xmlFilepath, imgFilepath):
    global dataFolder

    img_file, img_file_extension = os.path.splitext(imgFilepath)
    img_filename = basename(img_file)

    img = cv2.imread(imgFilepath)
    imgShape = img.shape
    img_h = imgShape[0]
    img_w = imgShape[1]

    labelXML = minidom.parse(xmlFilepath)
    labelName = []
    labelXmin = []
    labelYmin = []
    labelXmax = []
    labelYmax = []

    tmpArrays = (labelXML.getElementsByTagName("name"))
    for elem in tmpArrays:
        labelName.append(str(elem.firstChild.data))

    tmpArrays = labelXML.getElementsByTagName("xmin")
    for elem in tmpArrays:
        labelXmin.append(int(elem.firstChild.data))

    tmpArrays = labelXML.getElementsByTagName("ymin")
    for elem in tmpArrays:
        labelYmin.append(int(elem.firstChild.data))

    tmpArrays = labelXML.getElementsByTagName("xmax")
    for elem in tmpArrays:
        labelXmax.append(int(elem.firstChild.data))

    tmpArrays = labelXML.getElementsByTagName("ymax")
    for elem in tmpArrays:
        labelYmax.append(int(elem.firstChild.data))

    yoloLabel = os.path.join(labelFolder, img_filename + ".txt")

    with open(yoloLabel, 'a') as the_file:
        i = 0
        for className in labelName:
            if className in classList:
                classID = classList[className]
                x = (labelXmin[i] + (labelXmax[i] - labelXmin[i]) / 2) * 1.0 / img_w
                y = (labelYmin[i] + (labelYmax[i] - labelYmin[i]) / 2) * 1.0 / img_h
                w = (labelXmax[i] - labelXmin[i]) * 1.0 / img_w
                h = (labelYmax[i] - labelYmin[i]) * 1.0 / img_h
                the_file.write(str(classID) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')
                i += 1

    the_file.close()


fileCount = 0

trainListFile = open(trainList, 'w')
testListFile = open(testList, 'w')

for file in os.listdir(dataFolder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()

    if file_extension == ".jpg" or file_extension == ".png" or file_extension == ".jpeg" or file_extension == ".bmp":
        imgfile = os.path.join(dataFolder, file)
        xmlfile = os.path.join(dataFolder, filename + ".xml")
        if os.path.isfile(xmlfile):
            if fileCount % 5 == 0:
                testListFile.write(imgfile + '\n')

            trainListFile.write(imgfile + '\n')

            transferYolo(xmlfile, imgfile)
            fileCount += 1

trainListFile.close()
testListFile.close()
