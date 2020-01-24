# multithreaded port scanner


import threading
from queue import Queue
import time
import socket
from queue import Queue
import sys

print_lock = threading.Lock()
q =Queue();
def threader():
	while True:
		m = q.get();
		#print(m)
		port_scan(m);
		q.task_done()


def thread():
	for x in range(500):
		t= threading.Thread(target=threader)
		#print(t)
		t.daemon =True;
		t.start()
		


host = raw_input("input ypur ip : ")

print("------- please  wait  port scaning going on  \t" +host+ "")

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p = socket.gethostbyname(host)
	print(p)

except socket.error:
	print("[ - ] " +str(host) +" unable to resolve" +"-->\t please input in right format");
	sys.exit()

thread();


def port_scan(m):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((p,m))
		with print_lock:
			print('port',m)
			con.close()
	except:
		pass
        
	


list =[80,443,5]
	
for i in range(500):
	q.put(i);
q.join()

	#print(p)
