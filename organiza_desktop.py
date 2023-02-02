import os
import shutil

#=============================================================================
# LISTANDO ARQUIVOS
#=============================================================================

sufixos = ('.txt', '.jpeg', '.png', '.jpg', '.html', '.pdf', '.gif', '.iso', '.bin', '.pptm', '.pptx')
base_dir =  'caminho para a pasta que deseja organizar. ex:C:/Users/Bacel/Desktop/'

pasta = [os.path.abspath(y) for y in os.listdir(base_dir)]

i = 1

while i <= 2:
    for s in sufixos:
        arr = [os.path.abspath(x) for x in os.listdir(base_dir) if x.endswith(s)]

        for x in arr:
            x1 = x.replace('\\', '/')
            arquivo = x1.split("/")[5]
            texto = base_dir + arquivo
            print(texto)

        if s == ".pdf" or s == ".pptm" or  s == ".pptx" or s == ".html":
            dir = 'caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/documentos'
            if "caminho para a pasta que deseja organiza. ex: c:\\Users\\Bacel\\Desktop\\organiza_desktop\\documentos" in pasta:
                for x in arr:
                    x1 = x.replace('\\', '/')
                    arquivo = x1.split("/")[5]
                    documentos = base_dir + arquivo
                    print(documentos)
                    shutil.move(documentos,dir)
            else:
                try:
                    os.mkdir('caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/documentos')
                except:
                    for x in arr:
                        x1 = x.replace('\\', '/')
                        arquivo = x1.split("/")[5]
                        documentos = base_dir + arquivo
                        print(documentos)
                        shutil.move(documentos,dir)
        elif s == ".jpeg" or s == ".png" or  s == ".jpg":
            dir = 'caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/imagens'
            if "caminho para a pasta que deseja organiza. ex:c:\\Users\\Bacel\\Desktop\\organiza_desktop\\imagens" in pasta:
                for x in arr:
                    x1 = x.replace('\\', '/')
                    arquivo = x1.split("/")[5]
                    imagens = base_dir + arquivo
                    print(imagens)
                    shutil.move(imagens,dir)
            else:
                try:
                    os.mkdir('caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/imagens')
                except:
                    for x in arr:
                        x1 = x.replace('\\', '/')
                        arquivo = x1.split("/")[5]
                        imagens = base_dir + arquivo
                        print(imagens)
                        shutil.move(imagens,dir)
        elif s == ".iso" or s == ".bin":
            dir = 'caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/isos'
            if "caminho para a pasta que deseja organiza. ex:c:\\Users\\Bacel\\Desktop\\organiza_desktop\\isos" in pasta:
                for x in arr:
                    x1 = x.replace('\\', '/')
                    arquivo = x1.split("/")[5]
                    isos = base_dir + arquivo
                    print(isos)
                    shutil.move(isos,dir)
            else:
                try:
                    os.mkdir('caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/isos')
                except:
                    for x in arr:
                        x1 = x.replace('\\', '/')
                        arquivo = x1.split("/")[5]
                        isos = base_dir + arquivo
                        print(isos)
                        shutil.move(isos,dir)
        elif s == ".gif":
            dir = 'caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/gifs'
            if "caminho para a pasta que deseja organiza. ex:c:\\Users\\Bacel\\Desktop\\organiza_desktop\\gifs" in pasta:
                for x in arr:
                    x1 = x.replace('\\', '/')
                    arquivo = x1.split("/")[5]
                    gifs = base_dir + arquivo
                    print(gifs)
                    shutil.move(gifs,dir)
            else:
                try:
                    os.mkdir('caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/gifs')
                except:
                    for x in arr:
                        x1 = x.replace('\\', '/')
                        arquivo = x1.split("/")[5]
                        gifs = base_dir + arquivo
                        print(gifs)
                        shutil.move(gifs,dir)
        elif s == ".txt":
            dir = 'caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/texto'
            if "caminho para a pasta que deseja organiza. ex:c:\\Users\\Bacel\\Desktop\\organiza_desktop\\texto" in pasta:
                for x in arr:
                    x1 = x.replace('\\', '/')
                    arquivo = x1.split("/")[5]
                    texto = base_dir + arquivo
                    print(texto)
                    shutil.move(texto,dir)
            else:
                try:
                    os.mkdir('caminho para a pasta que deseja organiza. ex:C:/Users/Bacel/Desktop/texto')
                except:
                    for x in arr:
                        x1 = x.replace('\\', '/')
                        arquivo = x1.split("/")[5]
                        texto = base_dir + arquivo
                        print(texto)
                        shutil.move(texto,dir)

    i = i + 1