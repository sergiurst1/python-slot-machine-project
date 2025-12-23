# Slot Machine în Consolă 🎰

Un proiect simplu, dar complet, de slot machine în consolă, scris în Python. Este un exercițiu excelent pentru a exersa conceptele de bază ale programării, cum ar fi buclele, funcțiile, dicționarele și gestionarea input-ului de la utilizator.

Jocul simulează o experiență de bază de la cazinou, permițând utilizatorului să depună bani, să parieze pe un număr variabil de linii și să rotească pentru a câștiga.


*(Pentru a crea un GIF similar, poți folosi un tool gratuit precum [Terminalizer](https://terminalizer.com) sau [ScreenToGif](https://www.screentogif.com/)).*

## ✨ Funcționalități

- **💰 Gestionarea Balanței:** Utilizatorul începe prin a depune o sumă de bani, iar balanța este actualizată după fiecare rotire.
- **🎰 Pariuri Variabile:** Jucătorii pot alege pe câte linii să parieze (între 1 și 3) și ce sumă să parieze pe fiecare linie (între $1 și $100).
- **🔄 Rotiri Aleatorii:** Simbolurile de pe role sunt generate aleatoriu la fiecare rotire, folosind modulul `random` din Python.
- **🏆 Logică de Câștig:** Câștigurile sunt calculate automat dacă trei simboluri identice apar pe o linie activă.
- **📊 Simboluri cu Valori Diferite:** Fiecare simbol are o valoare și o frecvență diferită, creând o ierarhie a câștigurilor.
- **✅ Validarea Input-ului:** Programul gestionează elegant input-urile incorecte (ex: text în loc de numere, pariuri în afara limitelor permise).
- **🔁 Joc Continuu:** După fiecare rotire, utilizatorul poate alege să joace din nou sau să se retragă cu balanța rămasă.

## 🛠️ Tehnologii Folosite

- **Python 3**
- Nicio dependență externă, folosește doar module standard.

## 📋 Cerințe

- **Python 3.x** instalat pe sistemul tău.

## 🚀 Rulare Locală

Pentru a rula acest proiect pe mașina ta locală, urmează pașii de mai jos:

**1. Clonează Repozitoriul**
```bash
1. git clone https://github.com/sergiurst1/python-slot-machine-project.git
2. cd python-slot-machine-project
3. python main.py
