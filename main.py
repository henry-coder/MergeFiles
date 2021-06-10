from tkinter.filedialog import askopenfilenames
def browse_directory():
    while True:
        print('Selecione os arquivos no seu gerenciador!')
        print('Abrindo gerenciador de arquivos')
        files = askopenfilenames()
        if files==None:
            print('\033[1;31mNenhum arquivo foi selecionado\033[m')
            continue
        break
    return files
def list_files():
    print('Os seus arquivos serão unidos na seguinte sequência:')
    print('\033[1;33m', end='')
    for archive in files:
        path = archive.split('/')
        print(path[len(path)-1])
    print('\033[m',end='')
def merge_files():
    while True:
        name = input('Digite o nome que deseja dar ao novo arquivo no formato \033[1;36m(nome.extensão)\033[m: ')
        try:
            new = open(name,'x',encoding='utf8')
            for archive in files:
                with open(archive,'r',encoding='utf8') as a:
                    for line in a:
                        if(line!='\n' and line!=''):
                            if(line.endswith('\n')):
                                line = line[0:len(line)-2]
                            new.write(f'{line}\n')
                    new.write('\n\n')
            new.close()
            print('\033[1;31mJunção concluída com sucesso!\033[m')
            break
        except FileExistsError:
            print(f'\033[1;30;33mO arquivo \033[1;30;34m{name} \033[1;30;33mjá existe!\033[m')
        except:
            print(f'\033[1;30;41mErro interno!\033[m')
def show_options():
    print(f'\nVocê Selecionou \033[0;35m{quantity} arquivos\033[m!')
    while True:
        print('\nDigite:')
        print('\033[1;35m 1\033[m Para \033[4mlistar\033[m os arquivos do diretório.')
        print(f'\033[1;35m 2\033[m Para \033[4munir\033[m os \033[0;35m{quantity} arquivos\033[m.')
        opc = int(input('Digite o \033[4mnúmero\033[m da opção desejada: '))
        if(opc==1):
            list_files()
        elif(opc==2):
            merge_files()
            break
        else:
            print('\033[1;31mOpção Inválida!\033[m')
if __name__ == '__main__':
    print('Este programa \033[4mune os arquivos\033[m de um diretório como um \033[4múnico outro arquivo\033[m')
    files = browse_directory()
    quantity = len(files)
    if(quantity>1):
      show_options()  
    elif(quantity==1):
        print(f'Você selecionou apenas \033[0;35m{quantity}\033[m arquivo!')
input('Pressione ENTER para finalizar...')