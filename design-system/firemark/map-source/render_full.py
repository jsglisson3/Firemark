"""Renders the whole OSM export around Main St x S Colony Blvd into one styled SVG (for <img>), plus labels.json.
1 unit = 1.125 m (same scale as the v10/v11 hero map)."""
import xml.etree.ElementTree as ET, math, json, sys
SRC = sys.argv[1]
r = ET.parse(SRC).getroot()
b = r.find('bounds'); minlat, minlon, maxlat, maxlon = (float(b.get(k)) for k in ('minlat','minlon','maxlat','maxlon'))
nodes = {n.get('id'): (float(n.get('lat')), float(n.get('lon'))) for n in r.iter('node')}
LAT0 = 33.08061
M = 1.125
kx = math.cos(math.radians(LAT0)) * 111320; ky = 110574
W = round((maxlon - minlon) * kx / M); H = round((maxlat - minlat) * ky / M)
def P(lat, lon): return ((lon - minlon) * kx / M, (maxlat - lat) * ky / M)
AX, AY = P(33.08061, -96.89277)
def PN(i): return P(*nodes[i])
def rdp(pts, eps=0.6):
    if len(pts) > 3 and pts[0] == pts[-1]: return rdp(pts[:-1], eps) + [pts[0]]
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    dmax, idx = 0, 0
    for i, (x, y) in enumerate(pts[1:-1], 1):
        d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / L
        if d > dmax: dmax, idx = d, i
    if dmax > eps: return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]
def d(pts, close=False):
    # relative moves keep the file small: absolute start, then short deltas in whole units
    q = []
    for x, y in pts:
        p = (round(x), round(y))
        if not q or p != q[-1]: q.append(p)
    if len(q) < 2: return ''
    out = f'M{q[0][0]} {q[0][1]}' + 'l' + ' '.join(f'{b[0]-a[0]} {b[1]-a[1]}' for a, b in zip(q, q[1:]))
    return out.replace(' -', '-') + ('z' if close else '')
G = {k: [] for k in ['water','stream','park','wood','pitch','retail','parking','bld','path','svc','minor','ter','sec','mway','mway_case','rail']}
POI = []
ways = {}
for w in r.iter('way'):
    ns = [n.get('ref') for n in w.iter('nd') if n.get('ref') in nodes]
    ways[w.get('id')] = ns
    t = {x.get('k'): x.get('v') for x in w.iter('tag')}
    if len(ns) < 2: continue
    pts = [PN(n) for n in ns]; closed = ns[0] == ns[-1]
    h = t.get('highway')
    if 'building' in t:
        G['bld'].append(d(rdp(pts, 0.4), True))
        if t.get('amenity') or t.get('shop'): POI.append((sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)))
        continue
    if t.get('amenity') == 'parking' and closed: G['parking'].append(d(pts, True)); continue
    if (t.get('amenity') or t.get('shop')) and closed: POI.append((sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)))
    if t.get('natural') == 'water' and closed: G['water'].append(d(rdp(pts), True)); continue
    if t.get('waterway') in ('stream', 'river', 'canal'): G['stream'].append(d(rdp(pts))); continue
    if closed and (t.get('leisure') in ('park', 'recreation_ground', 'golf_course', 'nature_reserve', 'garden', 'playground') or t.get('landuse') in ('grass', 'recreation_ground', 'meadow', 'village_green')):
        G['park'].append(d(rdp(pts), True)); continue
    if closed and (t.get('natural') in ('wood', 'scrub') or t.get('landuse') == 'forest'): G['wood'].append(d(rdp(pts), True)); continue
    if closed and t.get('leisure') in ('pitch', 'stadium', 'swimming_pool', 'water_park', 'track'): G['pitch'].append(d(rdp(pts), True)); continue
    if closed and t.get('landuse') in ('retail', 'commercial'): G['retail'].append(d(rdp(pts), True)); continue
    if h in ('motorway', 'motorway_link', 'trunk', 'trunk_link'): G['mway'].append(d(rdp(pts))); continue
    if h in ('primary', 'primary_link', 'secondary', 'secondary_link'): G['sec'].append(d(rdp(pts))); continue
    if h in ('tertiary', 'tertiary_link'): G['ter'].append(d(rdp(pts))); continue
    if h in ('residential', 'unclassified', 'living_street'): G['minor'].append(d(rdp(pts))); continue
    if h == 'service': G['svc'].append(d(rdp(pts))); continue
    if h in ('footway', 'path', 'cycleway'): G['path'].append(d(rdp(pts))); continue
for n in r.iter('node'):
    t = {x.get('k'): x.get('v') for x in n.iter('tag')}
    if t.get('shop') or t.get('amenity') in ('restaurant', 'fast_food', 'cafe', 'bank', 'pharmacy', 'fuel', 'dentist', 'doctors', 'post_office'):
        POI.append(P(float(n.get('lat')), float(n.get('lon'))))
# lake: stitch the relation's outer ways into rings, clip to frame by drawing whatever is present
for rel in r.iter('relation'):
    t = {x.get('k'): x.get('v') for x in rel.iter('tag')}
    if t.get('natural') == 'water' or t.get('water') or t.get('name') == 'Lewisville Lake':
        segs = [ways[m.get('ref')] for m in rel.iter('member') if m.get('type') == 'way' and m.get('role') in ('outer', '') and ways.get(m.get('ref'))]
        rings = []
        while segs:
            ring = segs.pop(0)[:]
            changed = True
            while changed and ring[0] != ring[-1]:
                changed = False
                for i, s in enumerate(segs):
                    if s[0] == ring[-1]: ring += s[1:]; segs.pop(i); changed = True; break
                    if s[-1] == ring[-1]: ring += s[::-1][1:]; segs.pop(i); changed = True; break
            rings.append(ring)
        for ring in rings:
            G['water'].append(d(rdp([PN(n) for n in ring]), True))
POI = [p for p in POI if math.hypot(p[0] - AX, p[1] - AY) > 26]   # keep the corner clear for the Firemark pin
STYLE = '''
.land{fill:#F2F1EE}.retail{fill:#F0EBE4}.parking{fill:#ECE9E3}.park{fill:#E2E9D6}.wood{fill:#D9E3CC}.pitch{fill:#D8E2C9}
.water{fill:#CFDCE0}.stream{fill:none;stroke:#CFDCE0;stroke-width:3;stroke-linecap:round}
.bld{fill:#E4DFD7;stroke:#DCD6CC;stroke-width:.6}
.case,.fill{fill:none;stroke-linecap:round;stroke-linejoin:round}
.path{fill:none;stroke:#DAD4CA;stroke-width:1.2;stroke-dasharray:3 3}
.svc.case{stroke:#E1DBD1;stroke-width:4.5}.svc.fill{stroke:#FFFFFF;stroke-width:3}
.minor.case{stroke:#DCD5CA;stroke-width:8}.minor.fill{stroke:#FFFFFF;stroke-width:6}
.ter.case{stroke:#D5CDC0;stroke-width:11}.ter.fill{stroke:#FFFFFF;stroke-width:8.5}
.sec.case{stroke:#CFC6B8;stroke-width:15}.sec.fill{stroke:#FFFFFF;stroke-width:12}
.mway.case{stroke:#E3C3A2;stroke-width:17}.mway.fill{stroke:#F6DFC4;stroke-width:13}
.poi{fill:#9C958B;stroke:#FFFFFF;stroke-width:2.5}
'''
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{STYLE}</style>',
     f'<rect class="land" width="{W}" height="{H}"/>']
def grp(cls, key, close=False): return f'<path class="{cls}" d="{"".join(G[key])}"/>' if G[key] else ''
o += [grp('retail', 'retail'), grp('park', 'park'), grp('wood', 'wood'), grp('pitch', 'pitch'), grp('parking', 'parking'), grp('water', 'water'), grp('stream', 'stream'), grp('bld', 'bld'), grp('path', 'path')]
for k in ('svc', 'minor', 'ter', 'sec', 'mway'): o.append(f'<path class="{k} case" d="{"".join(G[k])}"/>')
for k in ('svc', 'minor', 'ter', 'sec', 'mway'): o.append(f'<path class="{k} fill" d="{"".join(G[k])}"/>')
o.append('<g class="poi">' + ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4.5"/>' for x, y in POI) + '</g>')
o.append('</svg>')
svg = ''.join(o)
open(sys.argv[2], 'w').write(svg)
# anchor + size for CSS; label positions computed from road geometry
json.dump({'W': W, 'H': H, 'AX': round(AX, 1), 'AY': round(AY, 1), 'POI': len(POI)}, open('meta.json', 'w'))
print(W, H, round(AX), round(AY), len(svg), 'bytes', len(POI), 'pois')
