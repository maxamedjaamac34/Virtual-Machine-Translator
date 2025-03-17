# Grab a file from Command Line!
import sys

with open(sys.argv[1], "r") as file_input:
    lines = file_input.readlines()

# Create a list for command words
command_words = ["push", "pop", "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not", "goto", "if-goto", "label"]

# Create a list or dictorary for locations, ASM_table, commmand_table
locations = ["local", "argument", "this", "that", "constant", "pointer", "temp", "static"]
ASM_table = {"local": "@LCL", "argument":"@ARG", "this":"@THIS", "that":"@THAT", "static":"@16"}

# making a list for our translator ASM
hold_ASM = []

# Grab an input from the user and assign it to variable called command!
# command = input("Give a push [local|argument|this|that|constant] <i> or pop [local|argument|this|that] <i> command. ")
# print(command)
# Make command all lowercase words
# command = command.lower()
# Next split command into a list of words.
# word_list = command.split()
# print(word_list)

def translateASM(the_end:bool = False, otherCommands:bool = False):
    # Use the word_List to decide how to tranlate the command into ASM
    # Check if commandWord condition is true or false

    if otherCommands == False:
    # Push
        if word_list[0] == command_words[0]:
            hold_ASM.append("// Push")
            hold_ASM.append("@"+word_list[2])
            hold_ASM.append("D=A")
            # Pushing Constant
            if word_list[1] == locations[4]:
                hold_ASM.append("// Constant")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M+1")
            # Pushing Pointer
            elif word_list[1] == locations[5]:
                hold_ASM.append("// Pointer")
                hold_ASM.append(ASM_table["this"])
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=M")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M+1")
            # Pushing Temp
            elif word_list[1] == locations[6]:
                hold_ASM.append("// Temp")
                hold_ASM.append("@5")
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=M")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M+1")
            # Pushing Static
            elif word_list[1] == locations[7]:
                hold_ASM.append("// Static")
                hold_ASM.append(ASM_table[word_list[1]])
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=M")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M+1")

            # Pushing location in ASM_table
            else:
                hold_ASM.append("// " + word_list[1])
                hold_ASM.append(ASM_table[word_list[1]])
                hold_ASM.append("A=D+M")
                hold_ASM.append("D=M")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M+1")
    # Pop
        elif word_list[0] == command_words[1]:
            hold_ASM.append("// Pop")
            hold_ASM.append("@"+word_list[2])
            hold_ASM.append("D=A")
            # Pop Pointer
            if word_list[1] == locations[5]:
                hold_ASM.append("// Pointer")
                hold_ASM.append(ASM_table["this"])
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=A")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("A=A-1")
                hold_ASM.append("D=M")
                hold_ASM.append("A=A+1")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M-1")
            # Pop Temp
            elif word_list[1] == locations[6]:
                hold_ASM.append("// Temp")
                hold_ASM.append("@5")
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=A")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("A=A-1")
                hold_ASM.append("D=M")
                hold_ASM.append("A=A+1")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M-1")
            # Pop Static
            elif word_list[1] == locations[7]:
                hold_ASM.append("// Static")
                hold_ASM.append("@16")
                hold_ASM.append("A=D+A")
                hold_ASM.append("D=A")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("A=A-1")
                hold_ASM.append("D=M")
                hold_ASM.append("A=A+1")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M-1")
            # Poping in ASM_table
            else:
                hold_ASM.append("// " + word_list[1])
                hold_ASM.append(ASM_table[word_list[1]])
                hold_ASM.append("A=D+M")
                hold_ASM.append("D=A")
                hold_ASM.append("@SP")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("A=A-1")
                hold_ASM.append("D=M")
                hold_ASM.append("A=A+1")
                hold_ASM.append("A=M")
                hold_ASM.append("M=D")
                hold_ASM.append("@SP")
                hold_ASM.append("M=M-1")

    elif otherCommands == True:
        hold_ASM.append("// " + word_list[0])
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("A=A-1")
        hold_ASM.append("D=M")
        hold_ASM.append("A=A-1")
        # And
        if word_list[0] == command_words[8]:
            hold_ASM.append("M=D&M")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # Add
        elif word_list[0] == command_words[2]:
            hold_ASM.append("M=D+M")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # Sub
        elif word_list[0] == command_words[3]:
            hold_ASM.append("M=M-D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # Neg
        elif word_list[0] == command_words[4]:
            hold_ASM.append("M=-D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # Or 9
        elif word_list[0] == command_words[9]:
            hold_ASM.append("M=M|D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # Not 10
        elif word_list[0] == command_words[10]:
            hold_ASM.append("M=!D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
        # eq 6
        elif word_list[0] == command_words[6]:
            hold_ASM.append("D=M-D")
            hold_ASM.append("@EQ")
            hold_ASM.append("D;JEQ")
            hold_ASM.append("M=0")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
            hold_ASM.append("@END")
            hold_ASM.append("0;JMP")
            hold_ASM.append("(EQ)")
            hold_ASM.append("@SP")
            hold_ASM.append("A=M")
            hold_ASM.append("A=A-1")
            hold_ASM.append("A=A-1")
            hold_ASM.append("M=1")
        # gt 7
        elif word_list[0] == command_words[7]:
            hold_ASM.append("D=M-D")
            hold_ASM.append("@GT")
            hold_ASM.append("D;JGT")
            hold_ASM.append("M=0")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
            hold_ASM.append("@END")
            hold_ASM.append("0;JMP")
            hold_ASM.append("(GT)")
            hold_ASM.append("@SP")
            hold_ASM.append("A=M")
            hold_ASM.append("A=A-1")
            hold_ASM.append("A=A-1")
            hold_ASM.append("M=1")
        # lt 8
        elif word_list[0] == command_words[8]:
            hold_ASM.append("D=M-D")
            hold_ASM.append("@LT")
            hold_ASM.append("D;JLT")
            hold_ASM.append("M=0")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
            hold_ASM.append("@END")
            hold_ASM.append("0;JMP")
            hold_ASM.append("(EQ)")
            hold_ASM.append("@LT")
            hold_ASM.append("A=M")
            hold_ASM.append("A=A-1")
            hold_ASM.append("A=A-1")
            hold_ASM.append("M=1")
    
    if the_end == True:
        hold_ASM.append("(END)")    
        hold_ASM.append("@END")
        hold_ASM.append("0;JMP")
    # print(hold_ASM)

def asmBranching(command:str, label:str):
    # For Branching we need the ability to put down label, then goto to label or if-goto label.
    # command = word_list[0]
    # label = word_list[1]

    # label <label>
    if command == "label":
        hold_ASM.append("(" + label + ")") 

    # goto <label>
    if command == "goto":
        hold_ASM.append("@" + label)
        hold_ASM.append("0;JMP")

    # If-goto <label>
    if command == "if-goto":
        hold_ASM.append("@SP")
        hold_ASM.append("M=M-1")
        hold_ASM.append("A=M")
        hold_ASM.append("D=M")
        hold_ASM.append("@" + label)
        hold_ASM.append("D;JNE")

def asmFunctions():
    # For Functions in ASM, we need to call, function and return
    command = word_list[0]
    f_name = word_list[1]
    n_arg = word_list[2]

    memorySegments = ["LCL", "ARG", "THIS", "THAT"]

    # Call function
    if command == "call":
        # Push the returnAddress
        hold_ASM.append("@returnAddress")
        hold_ASM.append("D=A")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("M=M+1")
        # Pushing MemorySegments
        pushingMSegments()
        # Repositioning ARG
        hold_ASM.append("@SP")
        hold_ASM.append("D=M")
        hold_ASM.append("@5")
        hold_ASM.append("D=D-A")
        hold_ASM.append("@" + n_arg)
        hold_ASM.append("D=D-A")
        hold_ASM.append("@ARG")
        hold_ASM.append("M=D")
        # Repositioning LCL
        hold_ASM.append("@SP")
        hold_ASM.append("D=M")
        hold_ASM.append("@LCL")
        hold_ASM.append("M=D")
        asmBranching("goto", f_name)
        asmBranching("label", "returnAddress")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")

    if command == "function":
        asmBranching("label", f_name)
        for i in range(n_arg):
            hold_ASM.append("@SP")
            hold_ASM.append("A=M")
            hold_ASM.append("M=0")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M+1")

    if command == "return":
        # Temp LCL 
        hold_ASM.append("@LCL")
        hold_ASM.append("D=M")
        hold_ASM.appeend("@R13")
        hold_ASM.append("M=D")
        # Temp ReturnAddress
        hold_ASM.append("@5")
        hold_ASM.append("A=D-A")
        hold_ASM.append("D=M")
        hold_ASM.append("@R14")
        hold_ASM.append("M=D")
        # ARG 0 = return anwser
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("A=A-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M-1")
        hold_ASM.append("@ARG")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        # Move SP after ARG 0
        hold_ASM.append("@ARG")
        hold_ASM.append("D=M+1")
        hold_ASM.append("@SP")
        hold_ASM.append("M=D")
        # Reposition Memory
        repositionMemory()
        hold_ASM.append("@R14")
        hold_ASM.append("A=M")
        hold_ASM.append("0;JMP")


def repositionMemory():
    for i in range(len(memorySegments)-1, 0,  -1):
        hold_ASM.append("@13")
        hold_ASM.append("A=M")
        hold_ASM.append("A=A-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@13")
        hold_ASM.append("M=M-1")
        hold_ASM.append("@" + memorySegments[i])
        hold_ASM.append("M=D")
        
def pushingMSegments():
    for i in range(len(memorySegments)):
        hold_ASM.append("@" + memorySegments[i])
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")


# Use the lists of words and see if the first word is in command_words list. 
# If not, say the command is not valid.
num_of_lines = 0
for line in lines:
    num_of_lines += 1

    line = line.lower()
    line = line.strip()
    word_list = line.split()

    print(word_list)

    if line.startswith("//") or line == "":
        continue

    elif word_list[0] in command_words and len(word_list) > 1:
        # Check if pop constant was input!
        if word_list[0] == command_words[1] and word_list[1] == locations[4]:
            print("This command is not valid")
        # Else if second word in word_list is in location!
        elif word_list[1] in locations:
            if word_list[2].isdigit():
                # print("True!")
                if num_of_lines == len(lines):
                    translateASM(the_end=True)
                else:
                    translateASM()
            else:
                print("is not a valid number")
        # Else if second word is not in location!
        else:
            print("non valid location!")
    # Else check if there is only 1 command word from command table in the word_list.
    elif word_list[0] in command_words and len(word_list) == 1:
        if word_list[0] in ["push",  "pop"]:
            print("Needs more data!")
        elif num_of_lines == len(lines):
            translateASM(the_end=True, otherCommands=True)
        else:
            translateASM(otherCommands=True)
    # Else say there is any error with the command!
    else:
        print("Command is not a valid command!")



with open("TranslatedVM.asm", "w") as file_output:
        for line in hold_ASM:
            file_output.write(line + " \n")