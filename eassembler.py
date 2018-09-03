def openfile():
    """
    função para ler os arquivos para o assembler
    """
    user_input = input("Entre com o nome do arquivo: ")
    opcodes = '/Users/renata.cavalheiro/OPCODES.esym'
    regcodes = '/Users/renata.cavalheiro/REGCODES.esym'
    if user_input == 'opcodes':
        opcodes_open = open(opcodes, 'r')
        print(opcodes_open.read())
        opcodes_open.close()
    elif user_input == 'regcodes':
        regcodes_open = open(regcodes, 'r')
        print(regcodes_open.read())
        regcodes_open.close()
    

    
    
    
    
                
    
