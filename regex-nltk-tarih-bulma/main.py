import re
from nltk import tokenize

def tarihBul(self):
    aylar = "Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık"
    aylarRakamsal = "\d{2}"

    ayBul = "(" + aylar + "|" + aylarRakamsal + ")"
    
    ayırıcı1 = "[\s]"
    ayırıcı2 = "[\-]"
    ayırıcı3 = "[\/]"

    ayırıcılar = "(" + ayırıcı1 + "|" + ayırıcı2 + "|" + ayırıcı3 + ")"

    gün1 = "\d{2}"
    gün2 = "\d{1}"

    günler = "(" + gün1 + "|" + gün2 + ")"

    yıl = "\d{4}"

    regex = günler + ayırıcılar + ayBul + ayırıcılar + yıl


    cümleler = tokenize.sent_tokenize(self)
    for cümle in cümleler:
        tarih = (re.search(regex, cümle))
        print(tarih.group())
