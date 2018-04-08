import re

def checkIfPythonCode(fileContent):
    regex = r"(import [a-zA-Z]+)"

    lines = fileContent.split("\n")
    for line in lines:
        found = re.findall(regex, line)
        print found


def parsers():
    fileContent = open("dumpFile.txt")
    content = fileContent.read()
    checkIfPythonCode(content)

def main():
    parsers()


if __name__ == '__main__':
    main()