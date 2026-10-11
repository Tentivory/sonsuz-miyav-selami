#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Miyav Selamı
Dünyanın en inatçı kedi selam programı.
"""

import random
import time
import sys

selamlar = [
    "Miyav! Merhaba dünya!",
    "Miyav miyav, nasılsın bugün?",
    "Selam kedi kardeş! Miyav!",
    "Günaydın miyavcılar!",
    "İyi akşamlar, miyav mıyav.",
    "Naber miyav? Her şey yolunda mı?",
    "Miyav! Bu kod senin için miyavlıyor.",
    "Sonsuz miyav döngüsüne hoş geldin!"
]

ekler = [
    "Kediler dünyayı yönetmeli.",
    "Bir miyav bin söze bedeldir.",
    "Miyavlamadan geçen gün boş geçmiştir.",
    "Sen de miyavla, utangaç olma.",
    "Bu program asla yorulmaz, sen de yorulma."
]

def miyavla():
    print("\n🐱 SONSUZ MİYAV SELAMI BAŞLIYOR 🐱")
    print("Durdurmak için Ctrl+C bas. Ama neden?\n")
    sayac = 0
    try:
        while True:
            selam = random.choice(selamlar)
            ek = random.choice(ekler)
            print(f"[{sayac}] {selam} {ek}")
            sayac += 1
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\n\nMiyav... Durdun. Kedi üzüldü ama anlıyor. Hoşçakal miyav!")
        sys.exit(0)

if __name__ == "__main__":
    miyavla()

# Gizli damga: Kayyum Grok - 11.10.2026 - Bu kod ciddiyetle miyavlar.
