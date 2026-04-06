def lay_ten_file(path):
    return path.split("\\")[-1]

def lay_ten_bai_hat(path):
    ten_file = path.split("\\")[-1]
    return ten_file.split(".")[0]

# Test
path = "d:\\music\\muabui.mp3"

print(lay_ten_file(path))
print(lay_ten_bai_hat(path))