# Python-mini-CPU
A simple ISA implementation written in Python

This CPU has 6 registers and 8 instructions.

The instructions:

ADD DESTINATION VALUE VALUE - adds two values and stores them in register specified

SUB DESTINATION VALUE VALUE - subtracts two values and stores them in register specified

JMP DESTINATION - jumps to line in program

LDA DESTINATION SOURCE - loads value from register to destination

IFL DESTINATION SOURCE SOURCE - compares values from registers and jumps if true

LDV DESTINATION VALUE - loads value into register

ADR DESTINATION SOURCE SOURCE - adds two values from registers and places result in destinaiton

SUR DESTINATION SOURCE SOURCE - subtracts two values from registers and places result in destinaiton

Tested On Linux
