import string

def assemble():
    """
    função para ler os arquivos para o assembler
    """
    opcodes = 'C:/Users/renata.cavalheiro/Topicos/OPCODES.esym'
    regcodes = 'C:/Users/renata.cavalheiro/Topicos/REGCODES.esym'
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
    print('\n')
    d1 = {}
    i = 0
    for line in vetor2:
        d1[line] = i
        i+= 1
    
    print(d1)
    print('\n')            
                
    """
    funcao para ler e traduzir o arquivo
    """
    principal = 'C:/Users/renata.cavalheiro/Topicos/fibo.asm'
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
    print('\n')
    for linec in vetor3:
        flag = 0
        flag2= 0
        if "MOV" in linec:
            a,b = linec.split(' ')
            k,l = b.split(',')
            if '[' in k:
                for aux in d1:
                    if aux == l:
                        traduzido.append("MOV_MR")
                        m = k.strip('[]')
                        traduzido.append(m)
                        traduzido.append(aux)
                        flag = 1
                        break
                if flag != 1:
                    traduzido.append("MOV_MI")
                    m = k.strip('[]')
                    traduzido.append(m)
                    traduzido.append(l)
                    
            elif '[' in l:
                traduzido.append("MOV_RM")
                traduzido.append(k)
                m = l.strip('[]')
                traduzido.append(m)
            else:
                for auxiliar2 in d1:
                    flag2 = 0
                    if auxiliar2 == k:
                        for auxiliar in d1:
                            if auxiliar == l:
                                traduzido.append("MOV_RR")
                                traduzido.append(auxiliar2)
                                traduzido.append(auxiliar)
                                flag2 = 1
                                break
                        if flag2 != 1:
                            traduzido.append("MOV_RI")
                            traduzido.append(auxiliar2)
                            traduzido.append(l)
                            
        elif "ADD" in linec:
            a,b = linec.split(' ')
            e,c = b.split(',')
            traduzido.append("ADD")
            for linha in d1:
                if linha == e:
                    traduzido.append(linha)
            for linha2 in d1:
                if linha2 == c:
                    traduzido.append(linha2)
        elif "SUB" in linec:
            a,b = linec.split(' ')
            e,c = b.split(',')
            traduzido.append("SUB")
            for linha in d1:
                if linha == e:
                    traduzido.append(linha)
            for linha2 in d1:
                if linha2 == c:
                    traduzido.append(linha2)
        elif "CMP" in linec:
            a,b = linec.split(' ')
            e,c = b.split(',')
            traduzido.append("CMP")
            for linha in d1:
                if linha == e:
                    traduzido.append(linha)
            for linha2 in d1:
                if linha2 == c:
                    traduzido.append(linha2)
        elif "OUT" in linec:
            b,c = linec.split(' ')
            traduzido.append("OUT")
            for linha in d1:
                if linha == c:
                    traduzido.append(linha)
        elif "INC" in linec:
            b,c = linec.split(' ')
            traduzido.append("INC")
            for linha in d1:
                if linha == c:
                    traduzido.append(linha)
        elif "DEC" in linec:
            b,c = linec.split(' ')
            traduzido.append("DEC")
            for linha in d1:
                if linha == c:
                    traduzido.append(linha)
        elif "MUL" in linec:
            a,b = linec.split(' ')
            e,c = b.split(',')
            traduzido.append("MUL")
            for linha in d1:
                if linha == e:
                    traduzido.append(linha)
            for linha2 in d1:
                if linha2 == c:
                    traduzido.append(linha2)
        elif "DIV" in linec:
            a,b = linec.split(' ')
            e,c = b.split(',')
            traduzido.append("DIV")
            for linha in d1:
                if linha == e:
                    traduzido.append(linha)
            for linha2 in d1:
                if linha2 == c:
                    traduzido.append(linha2)
        elif "JMP" in linec:
            a,b = linec.split(' ')
            traduzido.append("JMP")
            traduzido.append(b)
        elif "JZ" in linec:
            a,b = linec.split(' ')
            traduzido.append("JZ")
            traduzido.append(b)
        elif "JG" in linec:
            a,b = linec.split(' ')
            traduzido.append("JG")
            traduzido.append(b)
        elif "JL" in linec:
            a,b = linec.split(' ')
            traduzido.append("JL")
            traduzido.append(b)
        elif "NOP" in linec:
            traduzido.append("NOP")
        elif "HALT" in linec:
            traduzido.append("HALT")
            
    print(traduzido)
    print('\n')
    saida = []
    for part in traduzido:
        for word in d:
            if part == word:
                saida.append(d[word])
        for word2 in d1:
            if part == word2:
                saida.append(d1[word2])
        if part.isdigit():
            saida.append(part)
        if '-' in part:
            saida.append(part)
                
    print(saida)
    print('\n')
    
    arquivo_saida = open('C:/Users/renata.cavalheiro/Topicos/Resultado.txt', 'w')
    y = ' '.join(str(x) for x in saida)
    print(y)
    arquivo_saida.write(y)
    
assemble()
