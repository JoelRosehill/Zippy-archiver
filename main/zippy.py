def main():
    version = 'test 1.0'

    # ---------------------------------------------- #

    import os

    # ---------------------------------------------- #

    print("Zippy archiver")
    print("Version:", version)


    directory = os.listdir("./storage")
    if len(directory) == 0:
        print("\n\nFound nothing in /storage folder, please add items to /storage folder and try again.\n")
        return
    else:
        print("\n\nFound these items in /storage folder:")
        print("-------------------------------------")

    for i in range(len(directory)):
        if i != len(directory) - 1:
            print(directory[i] + "[" + str(i + 1) + "]", end=", ")
        else:
            print(directory[i] + "[" + str(i + 1) + "]")