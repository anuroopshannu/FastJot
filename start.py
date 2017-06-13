from pubnub import Pubnub
import subprocess
import pickle

pubnub=Pubnub(publish_key='pub-c-800c1668-57d0-45ec-9700-74d251ed134b', subscribe_key='sub-c-5936b224-0eca-11e7-92d3-02ee2ddab7fe')

def write(start,pic,upload,subject,date,time):
	v={
		'start':start,
		'pic':pic,
		'upload':upload,
		'sub':subject,
		'date':date,
		'time':time
		}
	with open('var.txt','wb')as handle:
		pickle.dump(v,handle)

def start(cmd):
	subs=['gnss','iafm','mcc','rs','project','seminar']
	if cmd[1] in subs:
		write(True,False,False,cmd[1],cmd[2],cmd[3])
		Subprogram = subprocess.Popen(['xterm','-hold', '-e', 'python ./speech1.py'],stdout=subprocess.PIPE)
	

def _callback(m,channel):
	print(m)
        cmd=m.split('+')
	#print(cmd[0])
	if(cmd[0]=='Start'):
		start(cmd)
	elif(cmd[0]=='stop'):
		write(False,False,False,cmd[1],cmd[2],cmd[3])
	elif(cmd[0]=='resume'):
		write(True,False,False,cmd[1],cmd[2],cmd[3])
	elif(cmd[0]=='picture'):
		write(True,True,False,cmd[1],cmd[2],cmd[3])
	elif(cmd[0]=='upload'):
		write(False,False,True,cmd[1],cmd[2],cmd[3]) 

def _error(e):
        print('error: '+str(e))


pubnub.subscribe(channels='smart_notes', callback=_callback, error=_error)


