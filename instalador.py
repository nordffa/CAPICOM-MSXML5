import os
import shutil


def copiar_dll(nome_dll, pasta_destino):
    caminho = os.path.join(pasta_destino, nome_dll)

    if not os.path.exists(caminho):
        shutil.copy(nome_dll, caminho)
        print(f'O arquivo {nome_dll} foi copiado para a pasta {pasta_destino}')
    else:
        print(f'O arquivo {nome_dll} ja existe na pasta {pasta_destino}')


def registrar_dll(nome_dll, pasta_destino):
    caminho = os.path.join(pasta_destino, nome_dll)
    os.system("regsvr32 " + caminho + " /s")
    print(f'O arquivo {nome_dll} foi registrado\n')


def main():
    sistema_x64 = os.path.join(os.environ['WINDIR'], "SysWOW64")
    sistema_x32 = os.path.join(os.environ['WINDIR'], "System32")

    if os.path.exists(sistema_x64):
        pasta_destino_dll = sistema_x64
        print('*** Sistema 64 bits detectado ***\n')
    else:
        pasta_destino_dll = sistema_x32
        print('*** Sistema 32 bits detectado ***\n')

    dlls = ["capicom.dll", "msxml5.dll", "msxml5r.dll"]
    for dll in dlls:
        copiar_dll(dll, pasta_destino_dll)
        if dll != "msxml5r.dll":
            registrar_dll(dll, pasta_destino_dll)
        else:
            print(f'O arquivo {dll} nao precisa de registro')

    print('\n*** CAPICOM e MSXML5 instalados ***\n')
    os.system("PAUSE")

if __name__ == "__main__":
    main()
