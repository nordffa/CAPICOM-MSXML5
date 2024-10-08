import os
import shutil
import subprocess


def copiar_dll(nome_dll, pasta_destino):
    caminho = os.path.join(pasta_destino, nome_dll)

    if not os.path.exists(caminho):
        shutil.copy(nome_dll, caminho)
        print(f'O arquivo {nome_dll} foi copiado para a pasta {pasta_destino}')
    else:
        print(f'O arquivo {nome_dll} ja existe na pasta {pasta_destino}')


def registrar_dll(nome_dll, pasta_destino):
    caminho = os.path.join(pasta_destino, nome_dll)

    subprocess.run(["regsvr32", "/s", caminho], check=True)
    print(f'O arquivo {nome_dll} foi registrado\n')


def main():
    sistema_64x = os.path.join(os.environ['WINDIR'], "SysWOW64")
    sistema_32x = os.path.join(os.environ['WINDIR'], "System32")

    if os.path.exists(sistema_64x):
        pasta_destino_dll = sistema_64x
        print('*** Sistema 64 bits detectado ***\n')
    else:
        pasta_destino_dll = sistema_32x
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
