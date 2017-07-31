import datetime
import re

def Now():
	msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	return msg;

#-------------------------------------------

def find_numbers(string, ints=False):
    numexp = re.compile(r'[-]?\d[\d,]*[\.]?[\d{2}]*') #optional - in front
    numbers = numexp.findall(string)
    numbers = [x.replace(',','') for x in numbers]
    if ints is True:
        return [int(x.replace(',','').split('.')[0]) for x in numbers];
    else:
        return numbers;

#-------------------------------------------
############################################################################
# 			M A I N
############################################################################
sName = "junk.txt"
with open(sName, 'w') as fh1:
	fh1.write("beep")
fh1.close
print("Should have a file " + sName + ", created at: " + Now() )
exit()
#########################################################
s = ""
while s != '\x18':			#Ctrl-X to exit
	s = raw_input("==>")
	print("You typed ", s, "        to exit: 'Ctrl-X'")

if 0 == 1:
	for i in range(0, 10):
		j = 5
		print("Here's i = ", i )

	input("give me a digit ")

	print ("variable i = ", i, ",  and variable  j = ", j)    #HUH ??  I thought it would be ZERO, not 9 !!!

#-------------------------------------------

sSpindle = "fadfdf.dfaiiididdsnn443.8tr#?"

print ( find_numbers(sSpindle)  )

iBeg = sSpindle.find("443")
print("iBeg = ", iBeg)
