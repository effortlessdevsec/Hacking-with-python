import zipfile
import threading
a = input("enter path")
b = input("enter path of dictionary file")

passFile = open(b)
count = len(open(b).readlines( ))
print(count)
print_lock = threading.Lock()
zFile = zipfile.ZipFile(a);

def pass_crack():
	for i in passFile.readlines():
		password = i.strip('\n')
		try:
			#print("[+]  checking Password =" +str(password));
			zFile.extractall(pwd=password)
			with print_lock:
				print('[+]  Password = ' + password + '\n')
				exit(0)
		except Exception as e:
			pass





for i in range(count):
	t= threading.Thread(target= pass_crack)
	t.daemon =True;
	t.start()
	
	
