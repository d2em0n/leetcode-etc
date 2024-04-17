# n = 6
# dirs = ['root/a', 'root/a/b', 'root/c/x', 'root/a/b/c', 'root', 'root/c']

# n = 4
# dirs = ['a/b/c/d', 'a/b', 'a/b/c', 'a']


n = int(input())
dirs = []
for i in range(n):
    dirs.append(input())

dirs.sort()
intend = '  '
print(dirs[0])
step = 0
for dir in dirs:
    step = 0
    a = dirs[step].split('/')
    b = dir.split('/')
    for name in b[len(a):]:
        if len(b) - len(a) == 1:
            print(intend*(step+1) + name)
        a.append(name)
        step += 1







print(n)

print(dirs)

a = 'root'
b = 'a'
a = '/'.join([a, b])
print(a)
print(intend*0 + '1')