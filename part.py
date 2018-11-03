import sys

partition_number = 1
def part(n, list):
	if n == 0:
		global partition_number
		print(f"{partition_number} - {list} == {sum(list)}")
		partition_number += 1
		return
	
	for i in range(n,0,-1):
		if len(list) > 0 and i < list[-1]:
			continue
		part(n - i, list + [i])

n = int(sys.argv[1])
part(n,[])
