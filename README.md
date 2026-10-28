# Pasiekimų žingsneliai

Naršyklėje veikianti programėlė vaiko pasiekimams žymėti „Pasiekimų žingsnelių“ lentelėse (1–3, 4–5, 5–6).

## Naudojimas

1. Atidarykite programėlę: https://tadas840.github.io/pasiekimu-zingsneliai/Pasiekimu_zingsneliai.html ir prisijunkite Google paskyra.
2. Spauskite „+ Naujas“ ir įrašykite vaiko vardą, pavardę ir datą.
3. Pasirinkite lapą, spalvą ir linijos storį, spauskite langelius (ugdymo sričių langelius arba kompetencijų rėmelius).
4. Spauskite „Išsaugoti šį lapą (JPG)“ arba „Išsaugoti visus 3 (JPG)“.

Galima vesti kelis vaikus: kiekvieno vaiko žymėjimai saugomi atskirai. Vėliau vaiką galima pasirinkti sąraše „Vaikas“ – jo žymėjimai bus parodyti ir juos galima toliau redaguoti. Skliaustuose sąraše rodomas pažymėtų langelių skaičius.

Žymėjimai automatiškai išsaugomi bendroje duomenų bazėje (Firebase Firestore). Juos mato ir redaguoti gali visi žmonės, kuriems suteikta prieiga, iš bet kurio kompiuterio, o vieno žmogaus pakeitimai kitam atsiranda iš karto. Linijos storis ir paskutinis pasirinktas vaikas prisimenami kiekvienoje naršyklėje atskirai.

Jei naršyklėje liko duomenų iš ankstesnės versijos (kai buvo saugoma tik naršyklėje), pirmą kartą prisijungus programėlė pasiūlys juos perkelti į duomenų bazę.

## Duomenų bazė (vienkartinis nustatymas)

1. Eikite į https://console.firebase.google.com → **Create a project** (Google Analytics galima išjungti).
2. **Build → Authentication → Get started → Sign-in method → Google → Enable → Save**.
3. **Authentication → Settings → Authorized domains → Add domain**: `tadas840.github.io`.
4. **Build → Firestore Database → Create database**: vieta Europoje (pvz., `eur3` arba `europe-west3`), **Production mode**.
5. **Firestore Database → Rules**: įklijuokite failo `firestore.rules` turinį, įrašykite abiejų žmonių Google el. pašto adresus ir spauskite **Publish**.
6. **Project settings (krumpliaratis) → General → Your apps → Web (`</>`)** → užregistruokite programėlę ir `firebaseConfig` reikšmes įrašykite į `firebase-config.js`.
7. Įkelkite pakeitimus į GitHub (`git push`).

Norint pridėti ar pašalinti žmogų, pakanka pakeisti el. pašto adresų sąrašą taisyklėse (5 žingsnis). Duomenis galima peržiūrėti Firebase konsolėje: **Firestore Database → Data → vaikai**.

Bandant kompiuteryje, failo negalima atidaryti tiesiai (`file://`). Paleiskite `python -m http.server` ir atidarykite http://localhost:8000/Pasiekimu_zingsneliai.html.

## Duomenų failo atnaujinimas

`pasiekimu_duomenys.js` sugeneruotas iš JPG failų (reikia Python su `numpy`, `Pillow`, `scipy`):

```
python irankiai/aptikti_langelius.py "<aplankas su JPG>"
python irankiai/sukurti_duomenis.py "<aplankas su JPG>"
```

Pirmasis skriptas suranda langelių ribas (`cells.json`), antrasis sukuria `pasiekimu_duomenys.js`.
