import re

sSpindle = "fadfdf.dfaiiididdsnn443.8tr#?"

#print ( find_numbers(sSpindle)  )

iBeg = sSpindle.find("4[43]")


p = re.compile('ab*', re.IGNORECASE)


print("iBeg = ", iBeg)

p = re.compile('\d+')
sp =  p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print( sp )


#p = re.compile('[or]+ange | o[ra]+nge | or[an]+ge | oran[ge]+', re.IGNORECASE)
p = re.compile(
                "[or]{1,3}ange"
                "|oran[ge]+"
                "|ora[ng]+e"
                , re.IGNORECASE)
sp =  p.findall(
#                "Roange...Orange...oRAAANAge...Range...oOange...oragne...oraneg...ornge...orange...orane...orage...ooorrrrrange..."
                r"Roange...Orange...oraneg...ornge...orange...orane...orage...ooorrrrrange...ORANEG...oraneg"
                )
print( sp )
