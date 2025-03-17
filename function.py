# Add additional commands for function handling
command_words += ["call", "function", "return", "label", "goto", "if-goto"] 

def translateFunction(word_list):
    # Handle function call: push return address, save LCL, ARG, THIS, THAT
    if word_list[0] == "call":
        function_name = word_list[1]
        num_args = word_list[2]
        return_address = "RET_" + function_name

        # Push return address
        hold_ASM.append(f"@{return_address}")
        hold_ASM.append("D=A")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")

        # Save LCL
        hold_ASM.append("@LCL")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")

        # Save ARG
        hold_ASM.append("@ARG")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")

        # Save THIS
        hold_ASM.append("@THIS")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")

        # Save THAT
        hold_ASM.append("@THAT")
        hold_ASM.append("D=M")
        hold_ASM.append("@SP")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M+1")

        # Reposition ARG
        hold_ASM.append(f"@SP")
        hold_ASM.append(f"D=M")
        hold_ASM.append(f"@{num_args}")
        hold_ASM.append(f"D=D-A")
        hold_ASM.append(f"@5")
        hold_ASM.append(f"D=D-A")
        hold_ASM.append(f"@ARG")
        hold_ASM.append(f"M=D")

        # Reposition LCL
        hold_ASM.append("@SP")
        hold_ASM.append("D=M")
        hold_ASM.append("@LCL")
        hold_ASM.append("M=D")

        # Goto function
        hold_ASM.append(f"@{function_name}")
        hold_ASM.append("0;JMP")

        # Return address label
        hold_ASM.append(f"({return_address})")

    # Handle return command
    elif word_list[0] == "return":
        # Store LCL in temp variable @R13
        hold_ASM.append("@LCL")
        hold_ASM.append("D=M")
        hold_ASM.append("@R13")
        hold_ASM.append("M=D")

        # Save return address in @R14
        hold_ASM.append("@5")
        hold_ASM.append("A=D-A")
        hold_ASM.append("D=M")
        hold_ASM.append("@R14")
        hold_ASM.append("M=D")

        # Reposition return value to ARG[0]
        hold_ASM.append("@SP")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@ARG")
        hold_ASM.append("A=M")
        hold_ASM.append("M=D")

        # Move SP to ARG + 1
        hold_ASM.append("@ARG")
        hold_ASM.append("D=M+1")
        hold_ASM.append("@SP")
        hold_ASM.append("M=D")

        # Restore THAT from saved frame
        hold_ASM.append("@R13")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@THAT")
        hold_ASM.append("M=D")

        # Restore THIS
        hold_ASM.append("@R13")
        hold_ASM.append("M=M-1")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@THIS")
        hold_ASM.append("M=D")

        # Restore ARG
        hold_ASM.append("@R13")
        hold_ASM.append("M=M-1")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@ARG")
        hold_ASM.append("M=D")

        # Restore LCL
        hold_ASM.append("@R13")
        hold_ASM.append("M=M-1")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append("@LCL")
        hold_ASM.append("M=D")

        # Goto return address
        hold_ASM.append("@R14")
        hold_ASM.append("A=M")
        hold_ASM.append("0;JMP")

def translateLabelGoto(word_list):
    if word_list[0] == "label":
        hold_ASM.append(f"({word_list[1]})")
    elif word_list[0] == "goto":
        hold_ASM.append(f"@{word_list[1]}")
        hold_ASM.append("0;JMP")
    elif word_list[0] == "if-goto":
        hold_ASM.append("@SP")
        hold_ASM.append("A=M-1")
        hold_ASM.append("D=M")
        hold_ASM.append(f"@{word_list[1]}")
        hold_ASM.append("D;JNE")
        hold_ASM.append("@SP")
        hold_ASM.append("M=M-1")

# Update the main loop to include function/label/goto handling
for line in lines:
    num_of_lines += 1

    line = line.lower()
    line = line.strip()
    word_list = line.split()

    print(word_list)

    if line.startswith("//") or line == "":
        continue

    elif word_list[0] in ["function", "call", "return"]:
        translateFunction(word_list)

    elif word_list[0] in ["label", "goto", "if-goto"]:
        translateLabelGoto(word_list)

    elif word_list[0] in command_words and len(word_list) > 1:
        # Memory-related and arithmetic commands
        if word_list[0] in ["push", "pop"]:
            if word_list[2].isdigit():
                if num_of_lines == len(lines):
                    translateASM(the_end=True)
                else:
                    translateASM()
            else:
                print("is not a valid number")
        else:
            print("non valid location!")

    elif word_list[0] in command_words and len(word_list) == 1:
        if word_list[0] in ["push", "pop"]:
            print("Needs more data!")
        elif num_of_lines == len(lines):
            translateASM(the_end=True, otherCommands=True)
        else:
            translateASM(otherCommands=True)

    else:
        print("Command is not a valid command!")
