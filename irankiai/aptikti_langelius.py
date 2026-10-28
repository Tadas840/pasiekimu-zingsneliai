import sys, json, glob, os
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
src = sys.argv[1]
out = {}
for f in sorted(glob.glob(os.path.join(src, '*.jpg'))):
    im = Image.open(f).convert('L'); a = np.asarray(im)
    H, W = a.shape
    dark = a < 110
    dark = ndi.binary_dilation(dark, iterations=2)
    lab, n = ndi.label(~dark)
    sizes = ndi.sum(np.ones_like(lab), lab, range(1, n+1))
    objs = ndi.find_objects(lab)
    cells = []
    for i, sl in enumerate(objs):
        if sl is None: continue
        area = sizes[i]
        y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
        w, h = x1-x0, y1-y0
        if area < 15000: continue
        if w > W*0.9 or h > H*0.9: continue  # outer background
        fill = area / (w*h)
        cells.append(dict(x=int(x0), y=int(y0), w=int(w), h=int(h), area=int(area), fill=round(float(fill),2)))
    print(os.path.basename(f), W, H, len(cells))
    for c in sorted(cells, key=lambda c:(c['y'],c['x'])): print('  ', c)
    vis = Image.open(f).convert('RGB'); d = ImageDraw.Draw(vis)
    for c in cells: d.rectangle([c['x'],c['y'],c['x']+c['w'],c['y']+c['h']], outline=(255,0,0), width=8)
    vis.resize((W//2, H//2)).save('vis_' + os.path.basename(f)[-10:])
    out[os.path.basename(f)] = dict(w=W, h=H, cells=cells)
json.dump(out, open('cells.json','w',encoding='utf-8'), ensure_ascii=False)
