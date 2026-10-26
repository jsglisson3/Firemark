import xml.etree.ElementTree as ET, math, json, sys
W_M=float(sys.argv[1]) if len(sys.argv)>1 else 1150
r=ET.parse('map.osm').getroot()
nodes={n.get('id'):(float(n.get('lat')),float(n.get('lon'))) for n in r.iter('node')}
LAT0,LON0=33.08061,-96.89277          # Main St x S Colony Blvd
W,H=1200,720; s=W/W_M
kx=math.cos(math.radians(LAT0))*111320; ky=110574
PX,PY=0.6367*W,0.60*H
def P(nid):
    la,lo=nodes[nid]; return ((lo-LON0)*kx*s+PX, -(la-LAT0)*ky*s+PY)
def inside(p,m=60): return -m<=p[0]<=W+m and -m<=p[1]<=H+m
def rdp(pts,eps=0.8):
    if len(pts)<3: return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1]; dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy) or 1e-9
    dmax,idx=0,0
    for i,(x,y) in enumerate(pts[1:-1],1):
        d=abs(dy*x-dx*y+x2*y1-y2*x1)/L
        if d>dmax: dmax,idx=d,i
    if dmax>eps: return rdp(pts[:idx+1],eps)[:-1]+rdp(pts[idx:],eps)
    return [pts[0],pts[-1]]
def d_of(pts,close=False):
    return "M"+"L".join(f"{x:.0f} {y:.0f}" for x,y in pts)+("Z" if close else "")
groups={'art':[],'col':[],'minor':[],'lake':[],'park':[],'bld':[],'svc':[]}
labels={}
ART={'primary','secondary','primary_link','secondary_link','trunk'}
COL={'tertiary','tertiary_link'}
MIN={'residential','unclassified','living_street'}
ART|={'motorway','motorway_link','trunk_link'}
for w in r.iter('way'):
    t={x.get('k'):x.get('v') for x in w.iter('tag')}
    ns=[n.get('ref') for n in w.iter('nd') if n.get('ref') in nodes]
    if len(ns)<2: continue
    pts=[P(n) for n in ns]
    if not any(inside(p) for p in pts): continue
    raw=pts
    pts=rdp(pts) if ns[0]!=ns[-1] else pts
    h=t.get('highway')
    g='art' if h in ART else 'col' if h in COL else 'minor' if h in MIN else None
    if 'building' in t:
        if all(inside(p,0) for p in pts) or any(inside(p,0) for p in pts):
            q=raw
            if len(q)>=3: groups['bld'].append("M"+"L".join(f"{x:.0f} {y:.0f}" for x,y in q[:-1] if True)+"Z")
        continue
    if h=='service' and t.get('service') in (None,'alley','driveway'):
        groups['svc'].append(d_of(pts)); continue
    if t.get('leisure')=='park' or t.get('landuse') in ('grass','recreation_ground') : groups['park'].append(d_of(pts,True)); continue
    if g:
        groups[g].append(d_of(pts))
        nm=t.get('name')
        if nm in ('Main Street','South Colony Boulevard','State Highway 121','Memorial Drive','Paige Road','Plano Parkway'):
            L=sum(math.hypot(b[0]-a[0],b[1]-a[1]) for a,b in zip(pts,pts[1:]) if inside(a,0) and inside(b,0) and (nm!='South Colony Boulevard' or min(a[0],b[0])>PX+20))
            if L>labels.get(nm,(0,))[0]:
                q=pts[:]
                dx=q[-1][0]-q[0][0]; dy=q[-1][1]-q[0][1]
                if (abs(dx)>=abs(dy) and dx<0) or (abs(dy)>abs(dx) and dy<0): q=q[::-1]
                labels[nm]=(L,q)
# lake: members of the Lewisville Lake relation that are present
wayn={w.get('id'):[n.get('ref') for n in w.iter('nd') if n.get('ref') in nodes] for w in r.iter('way')}
for rel in r.iter('relation'):
    t={x.get('k'):x.get('v') for x in rel.iter('tag')}
    if t.get('name')=='Lewisville Lake':
        for m in rel.iter('member'):
            if m.get('type')=='way' and m.get('ref') in wayn:
                pts=[P(n) for n in wayn[m.get('ref')]]
                if any(inside(p) for p in pts): groups['lake'].append(rdp(pts))
json.dump({k:v for k,v in groups.items()},open('groups.json','w'))
print({k:len(v) for k,v in groups.items()}, {k:round(v[0]) for k,v in labels.items()})
json.dump({k:d_of(v[1]) for k,v in labels.items()},open('labels.json','w'))
