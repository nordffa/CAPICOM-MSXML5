import os
import shutil
import subprocess

def copiar_e_registrar_dll(nome_dll, pasta_destino):
    caminho = os.path.join(pasta_destino, nome_dll)

    if not os.path.exists(caminho):
        shutil.copy(nome_dll, caminho)
        print(f'O arquivo {nome_dll} foi copiado para a pasta {pasta_destino}')
    else:
        print(f'O arquivo {nome_dll} ja existe na pasta {pasta_destino}')

    subprocess.run(["regsvr32", "/s", caminho], check=True)
    print(f'O arquivo {nome_dll} foi registrado')
