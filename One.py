import os,time

def yo(start,stop,step):
    for x in range(start,stop,step):
        os.system('clear')
        print('Sheju','-' * x,'ChandraMauli', sep='' )
        print('Ghooom Phir K Bhai')
        time.sleep(0.1)


def yo2( start,stop,step=1 ):
    yo(start,stop,step)
    yo(stop,start,-step)

#for x in range(1,10): 
yo2(0,35)


