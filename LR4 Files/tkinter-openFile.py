import tkinter.filedialog as fd
target = fd.askopenfilename()
for line in open(target):
    print(line, end='')
