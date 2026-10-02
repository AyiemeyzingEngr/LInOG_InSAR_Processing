# Year 2, Quarter 2 (2026) — report figures

Figures prepared for the DOST/PCIEERD Year 2, Quarter 2 narrative progress report of the LInOG Project. The scripts that generate them are in [`scripts/figures/`](../../scripts/figures/). The report itself is not versioned here because it contains participant names and project-drive data.

| Report figure | File | Script |
|---|---|---|
| Figure 7: FBS+FBD processing workflow (pipeline v4.0) | `LInOG_FBSFBD_workflow_v4.0.png` | `make_workflow_figure.py`, `make_workflow_icons.py` |
| Figure 10: Year 1 vs Year 2 Q2 LOS velocity mosaic | `LInOG_mosaic_Y1_vs_Y2Q2.png` | `make_mosaic_compare.py` |
| Figure 12: interactive time-series KMZ in Google Earth (Cabanatuan, P448/P449 F0290) | `LInOG_KMZ_GoogleEarth_P448_P449_F0290.png` | screen captures, 29 Sept 2026 |
| Figure 14: P448 F0290 interferograms, before and after FBS+FBD | `LInOG_igrams_P448F0290_Y1_vs_Y2Q2.png` | `make_igram_compare.py` |
| Figure 16: GeoLab tutorial route (manual v4.0, Ch. 11) | `LInOG_GeoLab_tutorial_route_v4.0.png` | `make_geolab_figure.py` |
| Figure 17: the GeoLab notebook (v2.8, run of 22 Sept 2026) | `LInOG_GeoLab_notebook_v2.8_capture.png` | `capture_geolab_notebook.py` |
| Twelve-frame mosaic (v1.2, water-masked) | `LInOG_mosaic_12frames_v1.2.png` | `make_mosaic_compare.py` |
| Editable slides of all diagrams | `LInOG_Y2Q2_workflow_slides_editable.pptx` | `build_workflow_slides.py` |

## FBS+FBD processing workflow (v4.0)
![FBS+FBD workflow](LInOG_FBSFBD_workflow_v4.0.png)

## Progression of the velocity mosaic
![Year 1 vs Year 2 Q2 mosaic](LInOG_mosaic_Y1_vs_Y2Q2.png)

## Interferograms before and after FBS+FBD (Path 448 Frame 0290)
![Interferogram comparison](LInOG_igrams_P448F0290_Y1_vs_Y2Q2.png)

## GeoLab tutorial route
The outputs in the lower row came from a four-date demonstration stack and are for training only; four dates are too few for a reliable deformation rate.

![GeoLab tutorial route](LInOG_GeoLab_tutorial_route_v4.0.png)

## Interactive KMZ in Google Earth
Balloon values are single pixels relative to each frame's reference point, not the bowl depth (3.7 and 3.3 cm/yr LOS). Imagery © 2026 Airbus, via Google Earth.

![KMZ in Google Earth](LInOG_KMZ_GoogleEarth_P448_P449_F0290.png)

## The GeoLab notebook
The saved notebook from the GeoLab run of 22 September 2026, opened in JupyterLab and captured with Playwright.

![GeoLab notebook](LInOG_GeoLab_notebook_v2.8_capture.png)
