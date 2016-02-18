import pythoncom, pyHook, datetime, threading, time, sys
from core import objthread_down, objthread_up
print('initializing the thread.....')
time.sleep(.5)

def OnKeyboardEventD(event):
    with threading.Lock():
        objthread_down(event.Key, event.WindowName, datetime.datetime.now())#3rd parameter is the position of key (down is 1)
        return True

def OnKeyboardEventU(event):
    with threading.Lock():
        objthread_up(event.Key, event.WindowName, datetime.datetime.now())#3rd parameter is the position of key (up is 0)
        return True


def main():
    try:
        if sys.argv[1] == '-l':
            print('script started in listening mode')
        if sys.argv[1] == '-e':
            print('make sure that you have enough data in the tree to compare')
            time.sleep(1)
            print('script started in execution mode...')
    except:
        print('exception reaised: start the program in listening mode (-l) or execution mode (-e)')
    else:
        # create a hook manager
        hm = pyHook.HookManager()
        # watch for all mouse events
        hm.KeyDown = OnKeyboardEventD
        hm.KeyUp = OnKeyboardEventU
        # set the hook
        hm.HookKeyboard()
        # wait forever
        pythoncom.PumpMessages()





'''import pythoncom, pyHook, datetime, threading
from core import objthread
listt = []
def OnKeyboardEventD(event):
    vald = 'with threading.Lock():'
    vald = vald + 'objthread(' + event.Key + ', ' + event.WindowName + ', ' + str(datetime.datetime.now()) + ', ' + str(1) + ')'#3rd parameter is the position of key (down is 1)
    listt.append(vald)
    if event.Key == 'Escape':
        f = open('indata.txt', 'w+')
        f.write(str(listt))
        f.close
    return True

def OnKeyboardEventU(event):
    valu = 'with threading.Lock():'
    valu =  valu + 'objthread(' + event.Key + ', ' + event.WindowName + ', ' + str(datetime.datetime.now()) + ', ' + str(0) + ')'
    listt.append(valu)
    return True

def main():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEventD
    hm.KeyUp = OnKeyboardEventU
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()
'''
if __name__ == '__main__':
    main()