# Hero map source

- `the-colony-main-st.osm`: OpenStreetMap export around Main St and S Colony Blvd, downloaded Oct 26, 2026. © OpenStreetMap contributors, ODbL.
- `render.py 1350`: projects the roads, buildings and lake into a 1200x720 frame with the Main St × S Colony Blvd intersection at 63.67% across and 60% down, which is where the hero's pin sits. It reads `map.osm` from the same folder, so copy or rename the export first.
- `build_svg.py`: writes `map.svg`. Paste it over the `<svg class="map-art">` in src/index.html, then run `python tools/build.py`.

Keep the "Map data © OpenStreetMap contributors" credit wherever this map appears.
