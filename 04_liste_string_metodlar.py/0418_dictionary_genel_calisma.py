# region dictionary yaratma
# dict()
"""
from typing import SupportsAbs

superLigSiralama = {
    'Birinci': 'BJK',
    'İkinci': 'GS',
    'Üçüncü': 'FB',
    'Dördüncü': 'TS'
}

print(superLigSiralama)
print(superLigSiralama['Birinci'])

''' ELEMAN EKLEME '''

superLigSiralama['Beşinci'] = "Hatayspor"
print(superLigSiralama)

superLigSiralama['aytuncu'] = ['Antalyaspor']
print(superLigSiralama)
#hatalı yazdık nasıl düzeltiriz ?

superLigSiralama.pop('aytuncu')
superLigSiralama['Altıncı'] = 'Antalyaspor'
'''
birden fazla eleman eklerken

degisim = {
    'Altıncı' : 'Antalyaspor'
}
superLigSiralama.update(degisim)
'''
print(superLigSiralama)

a = superLigSiralama.items()
print(a)
b = superLigSiralama.keys()
print(b)
c = superLigSiralama.values()
print(c)

for keys, value in superLigSiralama.items():
    print(keys,':', value)


sekizinci = superLigSiralama.get('sekizinci')
print(sekizinci) #None
"""
# endregion 

# region elemanlar üzerinde dönme


webMarketler = {
    'Yemeksepeti' : 'Nevzat Aydın',
    'Banabi' : 'Nevzat Aydın',
    'Getir' : 'Nazım Salur'
}
"""
for market, kurucu in webMarketler.items():
    print(f'{market}, firmasının kurucusu → {kurucu}')

for kurucular in webMarketler.values():
    print(kurucular)
"""

def harfSay(metin):
    '''
    Ör. {'a':'3','b':'7'}
    '''
    harfler = dict()
    for harf in metin:

        if harf.isalpha():
            if harf in  harfler.keys():
                harfler[harf] += 1
            else:
                harfler[harf] = 1
    return harfler

metin = 'Bu metinde hangi harften kaç tane var'
harfSozlugu = harfSay(metin)
print(harfSozlugu)