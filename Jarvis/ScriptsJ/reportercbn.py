# Imprimindo o links dos sites da pagina de resultado

import requests
from bs4 import BeautifulSoup
import urllib3


i = 0
j = 0
w = 0


pagina_de_busca = requests.get('http://audio.globoradio.globo.com/podcast/feed/623/reporter-cbn')
soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
#print(soup)

def clen_file():
        arq2 = open('link.txt', 'w')
        arq = open('titulo.txt', 'w')
        podcast = open('server.txt', 'w')
        arq.close()
        arq2.close()
        podcast.close

clen_file()        
for titulo in soup.find_all('title'):
        data2 = str(titulo)
        i = i + 1
        titulo = data2.replace("<title>O Assunto</title>","").replace("<title>","").replace("</title>","")
        #print(titulo)
        arq = open('titulo.txt', 'a')
        arq.write(titulo)
        arq.write("\n")
        arq.close()
        

        
for item in soup.find_all('guid', attrs={'isPermaLink': ''}):
        data = str(item)
        j = j + 1
        link = data.replace('<guid ispermalink="false">','').replace('</guid>','')
        #print(link)
        arq2 = open('link.txt', 'a')
        arq2.write(link)
        arq2.write("\n")
        arq2.close()


links = open('link.txt', 'r')
titulos = open('titulo.txt', 'r')

t2 = (links.readlines())
t3 = (titulos.readlines())

t2s = len(t2)
t3s = len(t3)

podcast = open('server.txt', 'a')
podcast.write("#EXTM3U")
podcast.write("\n")
podcast.close()
for t in range(0,t2s):
        
        
        #print(t)
        rt = str(t3[2+t].replace("\n","")) #,
        rt2 = str(t2[t].replace("\n",""))
        print('#EXTINF:-1 tvg-id="" tvg-logo="",'+rt+'')
        print(rt2)

        podcast = open('server.txt', 'a')
        podcast.write('#EXTINF:-1 tvg-id="" tvg-logo="",'+rt+'')
        podcast.write("\n")
        podcast.write(rt2)
        podcast.write("\n")
        podcast.close()

import subprocess
vlc = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
subprocess.call([vlc,'server.txt'])
