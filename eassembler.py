import string

def assemble():
    """
    função para ler os arquivos para o assembler
    """
    opcodes = 'C:/Users/Ana/Desktop/Topicos/OPCODES.esym'
    regcodes = 'C:/Users/Ana/Desktop/Topicos/REGCODES.esym'
    vetor = []
    vetor2 = []
    opcodes_open = open(opcodes, 'r')
    for line in opcodes_open:
        if line.strip() == "" or line[0] == ';':
            continue
        x = line.split(';')[0]
        x1 = line.split('\t')[0]
        vetor.append(x1.strip())
        
    regcodes_open = open(regcodes, 'r')
    for line in regcodes_open:
        if line.strip() == "" or line[0] == ';':
            continue
        x = line.split(';')[0]
        x1 = line.split('\t')[0]
        vetor2.append(x1.strip())
        
    d = {}
    i = 0
    for line in vetor:
        d[line] = i
        i += 1
    print(d)

    d2 = {}
    j = 0
    for code in vetor2:
        d2[code] = j
        j += 1
    
    print(d2)
                
                
    """
    funcao para ler e traduzir o arquivo
    """
    principal = 'C:/Users/Ana/Desktop/Topicos/fibo.asm'
    vetor3 = []
    traduzido = []
    flag = 0
    flag2= 0
    principal_open = open(principal, 'r')
   
    for line in principal_open:
        if line.strip() == "" or line[0] == ';':
            continue
        x = line.split(';')[0]
        vetor3.append(x.strip())
    print(vetor3)
    for linec in vetor3:
        flag = 0
        flag2= 0
        if "MOV" in linec:
            a,b,c = linec.split(' ')
            print(a)
            print(b)
            print(c)
            if '[' in b:
                for aux in vetor2:
                    if aux == c:
                        traduzido.append("MOV_MR")
                        flag = 1
                        break
                if flag != 1:
                    traduzido.append("MOV_MI")
                    
            elif '[' in c:
                traduzido.append("MOV_RM")
            else:
                for auxiliar in vetor2:
                    if auxiliar == c:
                        traduzido.append("MOV_RR")
                        flag2 = 1
                        break
                if flag2 != 1:
                    traduzido.append("MOV_RI")
        else:
            for aux2 in d:
                if aux2 in linec:
                    traduzido.append(aux2)
    print(traduzido)
    saida = []     
    for part in traduzido:
        for word in d:
            if word == part:
                print(d[word])
                saida.append(d[word])
        for word2 in d2:
            if word2 == part:
                saida.appende(d[word2])
    print(saida)
            
    
