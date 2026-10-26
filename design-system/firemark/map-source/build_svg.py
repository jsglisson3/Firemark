import json
g=json.load(open('groups.json')); lab=json.load(open('labels.json'))
def dd(pts): return "M"+"L".join(f"{x:.0f} {y:.0f}" for x,y in pts)
out=['<svg class="map-art" width="1200" height="720" viewBox="0 0 1200 720" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">']
for pts in g['lake']: out.append(f'<path class="m-lake" d="{dd(pts)}Z"/>')
out.append('<g class="m-bld">'+''.join(f'<path d="{d}"/>' for d in g['bld'])+'</g>')
out.append('<g class="m-svc">'+''.join(f'<path d="{d}"/>' for d in g['svc'])+'</g>')
out.append('<g class="m-park">'+''.join(f'<path d="{d}"/>' for d in g['park'])+'</g>')
out.append('<g class="m-minor">'+''.join(f'<path d="{d}"/>' for d in g['minor'])+'</g>')
out.append('<g class="m-col">'+''.join(f'<path d="{d}"/>' for d in g['col'])+'</g>')
out.append('<g class="m-art-case">'+''.join(f'<path d="{d}"/>' for d in g['art'])+'</g>')
out.append('<g class="m-art">'+''.join(f'<path d="{d}"/>' for d in g['art'])+'</g>')
ids={'Main Street':'r-main','South Colony Boulevard':'r-scb','State Highway 121':'r-121'}
out.append('<defs>'+''.join(f'<path id="{ids[k]}" d="{v}"/>' for k,v in lab.items() if k in ids)+'</defs>')
out.append('<g class="m-label">'+''.join(f'<text><textPath href="#{ids[k]}" startOffset="{o}">{t}</textPath></text>' for k,t,o in [('Main Street','Main St','30%'),('South Colony Boulevard','S Colony Blvd','40%')] if k in lab)+'</g>')
out.append('</svg>')
open('map.svg','w').write("\n".join(out)); print(sum(len(x) for x in out),'bytes')
