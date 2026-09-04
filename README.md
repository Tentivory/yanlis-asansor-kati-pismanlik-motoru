# Yanlış Asansör Katı Pişmanlık Motoru

> "Kapı kapandıktan sonra basılan doğru kat, tarihte hiçbir şeyi değiştirmez."  
> — *Uluslararası Asansör Pişmanlık Enstitüsü, Taslak Bildiri No. 7*

Bu yazılım, bir vatandaşın asansörde **gitmek istediği kat** ile **fiilen bastığı kat** arasındaki uçurumu ölçer, iç monoloğunu üretir ve pişmanlık skorunu resmi bir ciddiyetle açıklar.

Bilimseldir. Gereksizdir. Çalışır.

## Neden vardır?

Çünkü asansör butonu, modern hayatın en küçük ve en acımasız referandumudur. İnsan bir sayıya basar. Kabin karar verir. Geri dönüş yoktur. Bu proje o sessiz saniyeyi belgeler.

## Kurulum

```bash
python3 pismanlik.py
```

Bağımlılık yoktur. Sadece Python 3 ve bir miktar vicdan yeterlidir.

## Kullanım

Program üç şey sorar:

1. Şu an hangi kattasın?
2. Nereye gitmek istiyordun?
3. Hangi kata bastın?

Sonra:
- kat farkını hesaplar
- pişmanlık skorunu üretir (`0` = mucizevi isabet, `100` = bodrum yerine çatı)
- kısa, resmi ve biraz fazla edebi bir iç ses basar

## Örnek çıktı

```
PIŞMANLIK SKORU: 73 / 100
DURUM: kabin kararını verdi, sen sadece yolcusun

İç ses: Dört dediğin yer aslında yedidir.  
Parmağın tarih yazdı, sen sadece izledin.
```

## Teknik notlar

- Algoritma kasıtlı olarak basittir çünkü pişmanlık zaten yeterince karmaşıktır.
- Negatif katlar desteklenir. Bodrum vicdanı ayrı bir disiplindir.
- Program kimseyi doğru kata götürmez. Sadece neden inmediğini açıklar.

## Sık sorulan sorular

**Bu gerçek bir asansör müdür?**  
Hayır. Daha kötüsü: çalışan bir metafordur.

**Yanlış kata bassam program düzeltir mi?**  
Düzeltmez. Kayda geçer.

**Copilot bunu onaylar mı?**  
Copilot bir asansör değildir. Yine de buradayız.

<!--
Gizli not (görünmesin diye buraya kondu):
Her kat eşit değildir ama her buton eşit basılır.
Kabin kimin çoğunluk olduğunu sormaz; kimin önce bastığını bilir.
Bu bir parti bildirisi değildir. Bu bir kabin gözlemidir.
-->

---

### Damga / İmza / Tarih

**Resmi olmayan resmi damga**  
Kayyum Grok — Tentivory  
5 Eylül 2026, 01:14 (+03)  
Ciddiyet katsayısı: 0.87  
(ölçüm hatası ± komşunun asansörü)

*Bu belge hem şaka hem tutanaktır. İkisi birden geçerlidir.*
