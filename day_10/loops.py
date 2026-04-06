# Count 1 - 10
count = 1
while count < 11:
    print(count)
    count += 1

# Count 10 - 1
for item in range(10, 1, -1):
    print(item)

#
##
###
####
#####         Expected output
######
####### 
result = "#"
while len(result) < 8:
    print(result)
    result += "#"

