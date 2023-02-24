from PIL import Image,ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    filelist = ["jpg","jpeg","png"]
    filename1,filetype1 = sys.argv[1].lower().strip().split(".")
    filename2,filetype2 = sys.argv[2].lower().strip().split(".")
    print(sys.argv[1])

    if filetype1 == filetype2 and filetype1 in filelist:
        try:
            student = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png", mode='r', formats=None)
            shirtsize = shirt.size
            student = ImageOps.fit(student,shirtsize)
            student.paste(shirt, shirt)
            student.save(sys.argv[2], format=None)

        except FileNotFoundError:
           sys.exit("Input does not exist")
    elif filetype1 != filetype2 and filetype1 in filelist and filetype2 in filelist:
        sys.exit("Input and output have different extensions")
    elif filetype2 not in filelist:
        sys.exit("Invalid output")
else:
    print("Unknown Condition")
