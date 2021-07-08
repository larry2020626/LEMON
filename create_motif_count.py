import sys
name = sys.argv[1]

input_file = open("graph/" + name + "_count.out")
output = open("graph/" + name + "_motif.count", "w")
for line in input_file:
    nums = [int(x) for x in line.split()]
    output.write(str(nums[0]) + " " +str(nums[1]+nums[2]) + " " + str(nums[3]) + " " + str(nums[4]+nums[5]) + " ")
    output.write(str(nums[6]+nums[7]) + " " +str(nums[8]) + " " + str(nums[9]+nums[10]+nums[11]) + " " + str(nums[12]+nums[13]) + " "+str(nums[14])+"\n")
input_file.close()
output.close()
