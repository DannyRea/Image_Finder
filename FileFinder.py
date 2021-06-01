import os, stat
import shutil
import time

output = ""


def scanFiles(source, destination):
    global startTime
    global filesFound

    startTime = time.time()
    result = []

    for root, dir, files in os.walk(source):
        for file in files:
            if file not in ('Program Files', 'Program Files (x86)', 'ProgramData', 'Windows'):
                if file.endswith(('.jpg', '.mov')) or file.endswith(('.mp4', '.wmv', '.flv')):
                    result.append(os.path.join(root, file))

    filesFound = len(result)

    copyFiles(result, destination)


def copyFiles(result, destination):
    global error
    global finalTime
    global completePath
    finalTime = time.time() - startTime
    error = 0
    for i in result:
        copySource = i
        fileName = os.path.basename(copySource)
        completePath = destination + '/' + fileName

        try:
            shutil.copy2(copySource, destination)
            os.remove(copySource)
        except:

            error += 1

    logSet(str(filesFound), str(finalTime), str(error), str(result))


def logGet():
    return output


def logSet(found, time, error, results):
    global output
    output = found, time, error, results
