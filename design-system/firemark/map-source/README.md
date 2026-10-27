# Site map source

- `the-colony-main-st.osm`: OpenStreetMap export around Main St and S Colony Blvd, downloaded Oct 26, 2026. © OpenStreetMap contributors, ODbL.
- `render_full.py the-colony-main-st.osm ../../../docs/images/map/the-colony.svg`: draws the whole export (buildings, parks, Lewisville Lake, roads by size, shop dots) into one SVG. One unit is 1.125 m; Main St at S Colony Blvd is at (786, 673), which the CSS uses to put the pin there.
- `labels.py the-colony-main-st.osm`: finds spots and angles for the street names (`labels.json`). The labels are HTML in src/index.html so they use the site's typeface.
- `render.py` and `build_svg.py`: the older, smaller map used up to v11.

Keep the "Map data © OpenStreetMap contributors" credit wherever this map appears.
