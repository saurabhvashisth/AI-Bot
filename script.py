import subprocess
def bashcommand(command):
    
        bashCommand = command
        process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output
t=100
ct=0
while t>0:
        o=bashcommand("python evaluator_code.py 1")
        a=o.split('\n')[-4]
        b=o.split('\n')[-3]
        print "Test "+str(101-t),
        if a==b:
            print "Win"
            ct+=1
        else:
            c=o.split('\n')[-2]
            if c=="COMPLETE":
                print "Lost" +c
            elif c=="DRAW":
                print "Draw"
            elif c=="MORE BLOCKS":
                print "More Blocks"
            else:
                print "Lost" ,c
                print o
                break
        t-=1
print ct

