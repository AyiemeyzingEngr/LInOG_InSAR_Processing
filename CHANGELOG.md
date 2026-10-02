# CHANGELOG

All notable changes to this repository, manual, and scripts are documented here.

---

## [Y2Q2-2026] - 2026-10-02

### Added
- `docs/y2q2_2026/` — figures prepared for the DOST Year 2, Quarter 2 narrative report:
  - `LInOG_FBSFBD_workflow_v4.0.png`: FBS+FBD processing workflow (pipeline v4.0), each phase with a real output
  - `LInOG_mosaic_12frames_v1.2.png`: deramped LOS velocity mosaic of the 12 FBS+FBD frames (water-masked v1.2 delivery)
  - `LInOG_mosaic_Y1_vs_Y2Q2.png`: Year 1 FBS-only (Path 448) vs Year 2 Q2 FBS+FBD (Paths 447–449) mosaic, same product and ±5 cm/yr scale
  - `LInOG_igrams_P448F0290_Y1_vs_Y2Q2.png`: Path 448 Frame 0290 interferogram report pages, Year 1 FBS-only (36 pairs) vs FBS+FBD (149 formed / 129 inverted)
  - `LInOG_GeoLab_tutorial_route_v4.0.png`: six-step GeoLab tutorial route (manual v4.0, Chapter 11) with three outputs produced on GeoLab (training only)
  - `LInOG_Y2Q2_workflow_slides_editable.pptx`: the workflow, mosaic and GeoLab diagrams as four editable PowerPoint slides
  - `LInOG_KMZ_GoogleEarth_P448_P449_F0290.png`: interactive time-series KMZ of Path 448 and Path 449 Frame 0290 in Google Earth (Cabanatuan)
  - `LInOG_GeoLab_notebook_v2.8_capture.png`: the LInOG notebook as executed on GeoLab (22 Sept 2026), opening and Phase 6 output
  - `README.md`: figure index for the quarter
- `scripts/figures/` — the scripts that produced them (`make_workflow_figure.py`, `make_workflow_icons.py`, `make_mosaic_compare.py`, `make_igram_compare.py`, `make_geolab_figure.py`, `capture_geolab_notebook.py`, `build_workflow_slides.py`), kept as run; input paths point to the synced project drive

### Notes
- Valid-data area of the 12 frames, measured on the v1.2 rasters (temporal coherence ≥ 0.7, water and swath-edge masks, overlaps counted once): 27,893 km²
- FBS+FBD stacks sit on the 4.68 m range grid of an FBS reference date (FBS band-limited to 14 MHz in place; FBD resampled onto it at coregistration), so 28 × 12 looks give ~90 m × 90 m pixels, matching the 1/1200° (~90 m) output grid; 12 range looks are kept over 6 (about twice the independent looks, lower phase noise, no loss in the ~90 m deliverables)
- Workflow figure and slides corrected: Phase 1 no longer says FBS is resampled to the FBD range grid
- Report navigation: headings follow a Heading 2–6 hierarchy, captions are numbered with SEQ fields and in-text figure/table references are cross-reference fields, so the contents, list of tables and list of figures can be refreshed in Word (F9)
- Reference corrected: Werner, Wegmüller, Strozzi, Wiesmann & Santoro (2007), Proc. First Joint PI Symposium of ALOS Data Nodes, Kyoto
- The narrative report itself is not versioned here because it contains participant names and project-drive data

---

## [2.2] - 2026-05-19

### Added
- reusable Path/Frame variable workflow in `README.md`
- `[LOCAL]` and `[FELIX]` run-variable setup examples
- `CHANGELOG.md` to separate version history from `ERRATA.md`
- improved repository introduction and quick-start structure
- clearer repository contents overview in `README.md`

### Changed
- updated manual wording from **students** to **users**
- reworked command examples to use:
  - `PATH_NUM`
  - `FRAME_NUM`
  - `PADDED_PATH`
  - `PADDED_FRAME`
  - `FRAME_TAG`
  - `BASE_DIR`
  - `WORK_DIR`
- reduced hardcoded frame-specific commands in the workflow
- clarified that reference dates must still be reviewed independently by frame
- updated `ERRATA.md` to preserve both the original audit and the repository-state update

### Fixed
- `scripts/linog_save_insar_images.py`
  - fixed `stretch_magnitude()` scalar-boolean indexing bug
  - corrected usage string to the real filename
- `scripts/linog_gen_interactive_kmz.py`
  - moved `matplotlib` import out of repeated helper scope
  - replaced deprecated `plt.cm.jet` access
- `scripts/linog_fbs_processor.sh`
  - fixed MintPy metadata file pattern for stripmap processing
  - fixed interferogram wildcard patterns for stripmap naming
  - fixed Phase 4.5 printed script names to use `linog_` filenames

### Verified
- Python 3.12 support for conda-forge ISCE2
- `linog_create_grid.py` layout logic
- `CORRECTION_MAP` consistency for interactive KMZ generation
- deliverable naming consistency for `demErr` and `demErr_ramp`

---

## [2.1] - 2026-04

### Added
- pre-flight setup section for local WSL/Linux/macOS users
- vim survival guide
- local and felix installation paths
- `isce2_local` visualization environment instructions
- interferogram visualization workflow
- deliverables checklist and troubleshooting sections

### Documented
- ALOS-1 PALSAR FBS stack workflow using ISCE2 + MintPy
- geocoded deliverables workflow
- interactive KMZ generation workflow
- felix server usage assumptions

### Known state at time of original document
- manual contained several hardcoded frame/path examples
- script/manual inconsistencies were later documented in `ERRATA.md`
- repository packaging and audit tracking were not yet separated into dedicated files

---

## [2.0] - 2026-03

### Added
- initial `linog_fbs_processor.sh` automation workflow
- baseline ISCE2 + MintPy operational structure
- Phase 0 to Phase 7 pipeline framing
- LInOG naming conventions for outputs and logs

---

## Notes

- `ERRATA.md` is for bug findings, assumptions, and audit records
- `CHANGELOG.md` is for version-to-version repository and documentation changes
