def file_is_allowed(file):
    t = file.endswith(".py")
    t &= "__Init__" not in file.title()
    t &= "Sample_City" not in file.title()
    return t
