# Pasiekimų žingsneliai

Naršyklėje veikianti programėlė vaiko pasiekimams žymėti „Pasiekimų žingsnelių“ lentelėse (1–3, 4–5, 5–6).

## Naudojimas

1. Atidarykite `Pasiekimu_zingsneliai.html` naršyklėje (Chrome / Edge). Šalia turi būti failas `pasiekimu_duomenys.js`.
2. Įrašykite vaiko vardą, pavardę ir datą.
3. Pasirinkite lapą, spalvą ir linijos storį, spauskite langelius (ugdymo sričių langelius arba kompetencijų rėmelius).
4. Spauskite „Išsaugoti šį lapą (JPG)“ arba „Išsaugoti visus 3 (JPG)“.

Žymėjimai automatiškai išsaugomi naršyklėje.

## Duomenų failo atnaujinimas

`pasiekimu_duomenys.js` sugeneruotas iš JPG failų (reikia Python su `numpy`, `Pillow`, `scipy`):

```
python irankiai/aptikti_langelius.py "<aplankas su JPG>"
python irankiai/sukurti_duomenis.py "<aplankas su JPG>"
```

Pirmasis skriptas suranda langelių ribas (`cells.json`), antrasis sukuria `pasiekimu_duomenys.js`.
