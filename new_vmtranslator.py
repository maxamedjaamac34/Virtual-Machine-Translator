import sys

# with open(sys.argv[1], "r") as file_input:
#     lines = file_input.readlines()

def translateASM(word_list, hold_ASM, the_end=False, otherCommands=False):
    command_words = ["push", "pop", "add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not", "goto", "if-goto", "label"]
    locations = ["local", "argument", "this", "that", "constant", "pointer", "temp", "static"]
    ASM_table = {"local": "@LCL", "argument": "@ARG", "this": "@THIS", "that": "@THAT", "static": "@16"}

    # Push Command
    if word_list[0] == "push":
        hold_ASM.append(f"// push {word_list[1]} {word_list[2]}")
        hold_ASM.append(f"@{word_list[2]}")
        hold_ASM.append("D=A")
        
        if word_list[1] == "constant":
            hold_ASM.append("@SP")
            hold_ASM.append("A=M")
            hold_ASM.append("M=D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M+1")
        elif word_list[1] in ASM_table:
            hold_ASM.append(ASM_table[word_list[1]])
            hold_ASM.append("A=D+M")
            hold_ASM.append("D=M")
            hold_ASM.append("@SP")
            hold_ASM.append("A=M")
            hold_ASM.append("M=D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M+1")

    # Pop Command
    elif word_list[0] == "pop":
        hold_ASM.append(f"// pop {word_list[1]} {word_list[2]}")
        hold_ASM.append(f"@{word_list[2]}")
        hold_ASM.append("D=A")
        
        if word_list[1] in ASM_table:
            hold_ASM.append(ASM_table[word_list[1]])
            hold_ASM.append("D=D+M")
            hold_ASM.append("@R13")
            hold_ASM.append("M=D")
            hold_ASM.append("@SP")
            hold_ASM.append("M=M-1")
            hold_ASM.append("A=M")
            hold_ASM.append("D=M")
            hold_ASM.append("@R13")
            hold_ASM.append("A=M")
            hold_ASM.append("M=D")

    # Arithmetic Commands
    elif otherCommands:
        hold_ASM.append(f"// {word_list[0]}")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M-1")
        hold_ASM.append("A=M")
        hold_ASM.append("D=M")
        hold_ASM.append("A=A-1")
        
        if word_list[0] == "add":
            hold_ASM.append("M=D+M")
        elif word_list[0] == "sub":
            hold_ASM.append("M=M-D")
        elif word_list[0] == "and":
            hold_ASM.append("M=D&M")
        elif word_list[0] == "or":
            hold_ASM.append("M=D|M")
        elif word_list[0] == "neg":
            hold_ASM.append("M=-M")
        elif word_list[0] == "not":
            hold_ASM.append("M=!M")
        
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")
    
    # End Handling
    if the_end:
        hold_ASM.append("(END)")
        hold_ASM.append("@END")
        hold_ASM.append("0;JMP")

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_file>")
        return
    
    input_file = sys.argv[1]
    hold_ASM = []
    
    with open(input_file, "r") as file_input:
        lines = file_input.readlines()
    
    for line in lines:
        line = line.strip().lower()
        if line.startswith("//") or line == "":
            continue
        
        word_list = line.split()
        if word_list[0] in ["push", "pop"] and len(word_list) > 1:
            translateASM(word_list, hold_ASM)
        elif word_list[0] in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]:
            translateASM(word_list, hold_ASM, otherCommands=True)
        else:
            print(f"Invalid command: {line}")
    
    with open("newtranslte.asm", "w") as file_output:
        for line in hold_ASM:
            file_output.write(line + "\n")

if __name__ == "__main__":
    main()