// Push 
@0 
D=A 
// Constant 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// Pop 
@0 
D=A 
// local 
@LCL 
A=D+M 
D=A 
@SP 
A=M 
M=D 
A=A-1 
D=M 
A=A+1 
A=M 
M=D 
@SP 
M=M-1 
// Push 
@1 
D=A 
// Constant 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// Pop 
@1 
D=A 
// local 
@LCL 
A=D+M 
D=A 
@SP 
A=M 
M=D 
A=A-1 
D=M 
A=A+1 
A=M 
M=D 
@SP 
M=M-1 
// Push 
@1 
D=A 
// local 
@LCL 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// Push 
@1 
D=A 
// argument 
@ARG 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// gt 
@SP 
A=M 
A=A-1 
D=M 
A=A-1 
D=M-D 
@EQ 
D;JEQ 
M=0 
@SP 
M=M-1 
@END 
0;JMP 
(EQ) 
@SP 
A=M 
A=A-1 
A=A-1 
M=1 
// Push 
@0 
D=A 
// local 
@LCL 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// Push 
@0 
D=A 
// argument 
@ARG 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// add 
@SP 
A=M 
A=A-1 
D=M 
A=A-1 
M=D+M 
@SP 
M=M-1 
// Pop 
@0 
D=A 
// local 
@LCL 
A=D+M 
D=A 
@SP 
A=M 
M=D 
A=A-1 
D=M 
A=A+1 
A=M 
M=D 
@SP 
M=M-1 
// Push 
@1 
D=A 
// local 
@LCL 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// Push 
@1 
D=A 
// Constant 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// add 
@SP 
A=M 
A=A-1 
D=M 
A=A-1 
M=D+M 
@SP 
M=M-1 
// Pop 
@1 
D=A 
// local 
@LCL 
A=D+M 
D=A 
@SP 
A=M 
M=D 
A=A-1 
D=M 
A=A+1 
A=M 
M=D 
@SP 
M=M-1 
// Push 
@0 
D=A 
// local 
@LCL 
A=D+M 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
