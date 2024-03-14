h, b, c, s = map(int, input().split())
MB_ch = 1/8/1024/1024
pcm = h*b*c*s*MB_ch
print(format(pcm, '.1f'), 'MB')