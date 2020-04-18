import nltk
from nltk import pos_tag
from nltk.probability import FreqDist
from nltk.corpus import treebank
from newspaper import Article, fulltext
import requests, string


url = 'https://tr.sputniknews.com/koronavirus-salgini/202004021041740093-yunanistan-siginmacilarin-koronavirus-testi-pozitif-cikinca-kampi-karantinaya-aldi/'

a = Article(url)
a.download()
a.parse()
metin = a.text
başlık = a.title
resim = a.top_image

a.nlp()
test2 = a.keywords
özet = a.summary
yazar = a.authors
tarih = a.publish_date


print(özet)
print("\n")

#Cümlelere ayırır.
cümleler = nltk.sent_tokenize(metin)

#Genel kelime havuzu oluşturur.
genelKelimeler = nltk.word_tokenize(metin)

#Cümlelere göre kelime ayırır.
kelimeler = []
for cümle in cümleler:
    kelimeler.append(nltk.word_tokenize(cümle))

#NOKTALAMALARI YOK ET:
temizMetin = metin.translate(str.maketrans('','', string.punctuation))
print(temizMetin)

#Genel kelime havuzunda en çok kullanılan 10 kelimeyi tespit eder.
fd = nltk.FreqDist(genelKelimeler)
print(fd.most_common(10))

print("\n")


#Kelime Etiketleme:
tagged_sent = pos_tag(kelimeler[1])
print(tagged_sent)
propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
collocation = [word for word,pos in tagged_sent if pos == 'CD']
print(propernouns)   #Özel isimler, cümle içinde geçen özel isimleri buluyor kısatlaması NNP
print(collocation)   #Eşdizimli, cümle içinde sayı, tarih, ve rakamsal değerleri buluyor. Kısaltması CD
