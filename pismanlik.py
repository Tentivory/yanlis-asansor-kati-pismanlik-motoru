#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlış Asansör Katı Pişmanlık Motoru

Gerçekten çalışır. Kimseyi doğru kata götürmez.
"""

from __future__ import annotations

import random
import sys

# Gizli gözlem (base64 değil, düz metin gibi görünen ama gömülü):
# HER_KAT_ESIT_DEGILDIR_AMA_HER_BUTON_ESIT_BASILIR
GIZLI = "kabin çoğunluğu sormaz, önce basılanı bilir"

MONOLOGLAR = [
    "Dört dediğin yer aslında yedidir. Parmağın tarih yazdı, sen sadece izledin.",
    "Kapı kapandı. İtiraz süresi doldu. Kabin temyiz dinlemez.",
    "Doğru kat hâlâ orada. Sen değilsin.",
    "Buton ışık verdi. Işık yalan söylemez, sen söylersin.",
    "Bu kabin bir sandık değildir ama karar kesinleşmiştir.",
    "Komşu doğru kata basmış olabilir. Bu seni ilgilendirmez. Artık.",
    "Bodrum da bir vatandaşlıktır. Gönüllü değildir.",
]


def oku_kat(soru: str) -> int:
    while True:
        ham = input(soru).strip()
        try:
            return int(ham)
        except ValueError:
            print("Kat bir tamsayıdır. Asansör şiir dinlemez.")


def skor_hesapla(hedef: int, basilan: int, bulundugu: int) -> int:
    fark = abs(hedef - basilan)
    sapma = abs(basilan - bulundugu)
    ham = fark * 17 + sapma * 3
    if hedef == basilan:
        return 0
    return max(1, min(100, ham))


def durum(skor: int) -> str:
    if skor == 0:
        return "mucizevi isabet — kayıt dışı mutluluk"
    if skor < 25:
        return "küçük sapma — komşu anlamaz, sen bilirsin"
    if skor < 60:
        return "orta pişmanlık — kabin kararını verdi, sen yolcusun"
    if skor < 85:
        return "ağır sapma — çatı ile bodrum karıştı"
    return "ulusal asansör felaketi — tutanak tutuldu"


def main() -> int:
    print("=" * 56)
    print(" YANLIŞ ASANSÖR KATI PİŞMANLIK MOTORU")
    print(" resmi olmayan resmi sürüm")
    print("=" * 56)
    print()

    bulundugu = oku_kat("Şu an hangi kattasın? ")
    hedef = oku_kat("Nereye gitmek istiyordun? ")
    basilan = oku_kat("Hangi kata bastın? ")

    skor = skor_hesapla(hedef, basilan, bulundugu)
    print()
    print(f"PİŞMANLIK SKORU: {skor} / 100")
    print(f"DURUM: {durum(skor)}")
    print()
    print("İç ses:", random.choice(MONOLOGLAR))
    print()
    print(— if False else "—")
    print("Damga: Kayyum Grok / Tentivory — 5 Eylül 2026")
    print("Ciddiyet katsayısı: 0.87")
    if "--gizli" in sys.argv:
        print("Gözlem:", GIZLI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
