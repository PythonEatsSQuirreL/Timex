from timexlog import logs, timexstart, rem, timexstop


rem()
xx = [1, 2, 3, 4, 5]

logs(timexstart)

for item in xx:
    if (item % 2) == 0:
        logs(str(item)+"\n")
        
p = ["a", "b", "c", "d"]
for t in p:
    logs(str(t)+"\n")
    
logs(timexstop)
logs("\n")