class IO:
    supporttedSrcs = ["console", "file"]
    def read(src):
        if  src not in  IO.supporttedSrcs:
            print("not supported")
        else:
            print("Read from", src)

print(IO.supporttedSrcs)
IO.read("file")
IO.read("INETR")