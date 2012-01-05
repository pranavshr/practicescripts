#!/usr/bin/python

infile = open("cloudscheduler", "r")
line = infile.readline()
i = 0
j = 0

while line :
	if 'VMDestroyCmd - Destroyed' in line :
		i = i + 1
	if 'Scheduler - Nimbus create command executed.' in line:
		j = j + 1
	line = infile.readline()


print "The event  \"VMDestroyCmd - Destroyed\" occured ", i, "times"
print "The event \"Scheduler - Nimbus create command executed.\" occured ", j, "times"	
