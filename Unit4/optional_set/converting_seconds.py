# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def calc_hours(input):
	hours = 0
	hours_result = 0
	while input >= 3600:
		input = input - 3600
		hours = hours + 1        
	if hours < 1 or hours > 1:
		hours_result = str(hours) + ' hours, '
	else:	
		hours_result = str(hours) + ' hour, '
	return hours_result, input

def calc_mins(hours_result, input):
	mins = 0
	mins_result = 0
	while input >= 60:
		input = input - 60
		mins = mins + 1
	if mins < 1 or mins > 1:
		mins_result = hours_result + str(mins) + ' minutes, '
	else:
		mins_result = hours_result + str(mins) + ' minute, '
	return mins_result, input

def convert_seconds(input):
	hours_result, throughput = calc_hours(input)
	
	mins_result, seconds = calc_mins(hours_result, throughput)

	seconds_result = str(seconds)
	if seconds < 1 or seconds > 1:
		seconds_result = seconds_result + ' seconds.'
	else:
		seconds_result = seconds_result + ' second.'
	return mins_result + seconds_result

			
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds