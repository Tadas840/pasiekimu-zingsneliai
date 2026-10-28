import json, base64, glob, os, re, sys
src = sys.argv[1]
cells = json.load(open('cells.json', encoding='utf-8'))
sheets = []
for f in sorted(glob.glob(os.path.join(src, '*.jpg'))):
    name = os.path.basename(f)
    m = re.search(r'(\d)-(\d)_A4', name)
    if not m: continue
    info = cells[name]
    out = []
    for c in info['cells']:
        if c['area'] > 500000: continue  # centrinis baltas laukas
        comp = c['fill'] > 0.78 and c['w'] < 330 and c['h'] < 210 and 800 < c['y'] < 1700 and 950 < c['x'] < 2550
        out.append([c['x'], c['y'], c['w'], c['h'], 1 if comp else 0])
    out.sort(key=lambda r: (r[1], r[0]))
    b64 = base64.b64encode(open(f, 'rb').read()).decode()
    sheets.append(dict(id=f"{m.group(1)}-{m.group(2)}", title=f"Pasiekimų žingsneliai {m.group(1)}–{m.group(2)}",
                       w=info['w'], h=info['h'], cells=out, src='data:image/jpeg;base64,' + b64))
    print(name, len(out), 'langeliai, kompetencijos:', sum(r[4] for r in out))
with open(os.path.join(src, 'pasiekimu_duomenys.js'), 'w', encoding='utf-8') as fh:
    fh.write('// Sugeneruota automatiškai: paveikslėliai ir langelių koordinatės\nwindow.LAPAI = ')
    json.dump(sheets, fh, ensure_ascii=False)
    fh.write(';\n')
