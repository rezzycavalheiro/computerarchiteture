def assemble():
    """
    função para ler os arquivos para o assembler
    """
    user_input = input("Entre com o nome do arquivo: ")
    opcodes = '/Users/renata.cavalheiro/OPCODES.esym'
    regcodes = '/Users/renata.cavalheiro/REGCODES.esym'
    if user_input == 'opcodes':
        opcodes_open = open(opcodes, 'r')
        print(opcodes_open.read())
        #opcodes_open.close()
    elif user_input == 'regcodes':
        regcodes_open = open(regcodes, 'r')
        print(regcodes_open.read())
        #regcodes_open.close()

def dictionary(var):
    d = {
        "NOP": 0,
        "HALT": 1,
        "MOV_RR": 2,
        "MOV_RM": 3,
        "MOV_MR": 4,
        "MOV_RI": 5,
        "MOV_MI": 6,
        "ADD": 7,
        "SUB": 8,
        "CMP": 9,
        "JMP": 10,
        "JZ": 11,
        "JG": 12,
        "JL": 13,
        "OUT": 14,
        "INC": 15,
        "DEC": 16,
        "MUL": 17,
        "DIV": 18
        }
    #opcodes = '/Users/renata.cavalheiro/OPCODES.esym'
    #code = open(opcodes, 'r')
    #code.read()
    code = [var]
    for i in d:
        for line in code:
            if line == i:
                position = d[i]
                return position
    
                
 
    
                
    
