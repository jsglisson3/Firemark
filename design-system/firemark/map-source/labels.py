import xml.etree.ElementTree as ET, math, json, sys
r = ET.parse(sys.argv[1]).getroot()
b = r.find('bounds'); minlat, minlon, maxlat, maxlon = (float(b.get(k)) for k in ('minlat','minlon','maxlat','maxlon'))
nodes = {n.get('id'): (float(n.get('lat')), float(n.get('lon'))) for n in r.iter('node')}
kx = math.cos(math.radians(33.08061)) * 111320; ky = 110574; M = 1.125
def P(i): la, lo = nodes[i]; return ((lo - minlon) * kx / M, (maxlat - la) * ky / M)
segs = {}
for w in r.iter('way'):
    t = {x.get('k'): x.get('v') for x in w.iter('tag')}
    if 'highway' in t and t.get('name'):
        pts = [P(n.get('ref')) for n in w.iter('nd') if n.get('ref') in nodes]
        segs.setdefault(t['name'], []).append(pts)
def near(name, tx, ty):
    best = None
    for pts in segs.get(name, []):
        for a, b2 in zip(pts, pts[1:]):
            mx, my = (a[0] + b2[0]) / 2, (a[1] + b2[1]) / 2
            dd = math.hypot(mx - tx, my - ty)
            if best is None or dd < best[0]:
                ang = math.degrees(math.atan2(b2[1] - a[1], b2[0] - a[0]))
                if ang > 90: ang -= 180
                if ang < -90: ang += 180
                best = (dd, mx, my, ang)
    return best
AX, AY = 786, 673
want = [('Main Street', 'Main St', AX, AY - 330), ('Main Street', 'Main St', AX, AY + 420),
        ('South Colony Boulevard', 'S Colony Blvd', AX + 420, AY - 40), ('South Colony Boulevard', 'S Colony Blvd', AX + 1500, AY - 330),
        ('Paige Road', 'Paige Rd', AX + 1330, AY + 50), ('Memorial Drive', 'Memorial Dr', AX + 900, AY + 300),
        ('Sam Rayburn Tollway', 'Sam Rayburn Tollway', AX + 2000, AY + 790)]
out = []
for name, text, tx, ty in want:
    nb = near(name, tx, ty)
    if nb: out.append({'t': text, 'x': round(nb[1]), 'y': round(nb[2]), 'a': round(nb[3], 1), 'kind': 'road'})
out.append({'t': 'Lewisville Lake', 'x': 110, 'y': 640, 'a': 0, 'kind': 'water'})
json.dump(out, open('labels.json', 'w'), indent=0); print(out)
