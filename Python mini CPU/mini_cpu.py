registers = [0,0,0,0,0,0]
pc = 0


program = open("testminicpu.txt","r").readlines()
while pc < len(program):
	line = program[pc]
	print(line)
	instruct = line[:3]
	dest = int(line[4])
	if instruct == 'ADD':
		registers[dest] = int(line[6]) + int(line[8])
		pc += 1
	elif instruct == 'SUB':
		registers[dest] = int(line[6]) - int(line[8])
		pc += 1
	elif instruct == 'JMP':
		pc = dest
	elif instruct == 'LDA':
		registers[dest] = registers[int(line[6])]
		pc += 1
	elif instruct == 'IFL':
		if registers[int(line[6])] < registers[int(line[8])]:
			pc = dest
		else:
			pc += 1
	elif instruct == "LDV":
		registers[dest] = int(line[6])
		pc += 1
	else:
		raise ValueError, 'Invalid Instruction ' + line
	print(registers)
