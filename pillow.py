from PIL import Image

im = Image.open('D:\log.png')   # 就是打开文件
print(im.format, im.size, im.mode)  # print些可能需要用到的信息
im.show()

# 以下是打开并保存
try:
    Image.open('D:\log.png').save('D:\log3.png')
except IOError:
    print("Cant Save")