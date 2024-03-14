w, h, b = map(int, input().split())
mb_ch = 8*1024*1024
bmp = w*h*b/mb_ch
print(format(bmp, '.2f'), 'MB')
