# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## What this repo is
This repository is a collection of small, standalone Streamlit apps organized by “sessions” (`SESION1` → `SESION4`). Each `.py` file is meant to be run directly with Streamlit and does not rely on a shared internal package.

## Common commands
### Environment setup (no pinned deps in repo)
There is no `requirements.txt`/`pyproject.toml` in the repository, so dependencies need to be installed manually.

Typical local setup:
- Create and activate a virtualenv
- Install the libraries used in the scripts (inferred from imports)

Example (bash):
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install --upgrade pip`
- `pip install streamlit pandas numpy altair matplotlib seaborn`

If you add dependency management later (e.g. `requirements.txt` or `pyproject.toml`), update this section.

### Run an app
Run any example via Streamlit:
- `streamlit run SESION1/hola_mundo.py`
- `streamlit run SESION1/entrada_usuario.py`
- `streamlit run SESION2/cargar_csv.py`
- `streamlit run SESION2/exploracion_basica.py`
- `streamlit run SESION2/filtros_numericos.py`
- `streamlit run SESION3/visualizacion_basica.py`
- `streamlit run SESION3/seleccion_columnas.py`
- `streamlit run SESION3/app_visualizacion_completa.py`
- `streamlit run SESION4/app_visualizacion_avanzada.py`
- `streamlit run SESION4/altair_interactivo.py`
- `streamlit run SESION4/matplotlib_histograma.py`
- `streamlit run SESION4/seaborn_boxplot.py`
- `streamlit run graph_demo.py`
- `streamlit run stlEjemplos.py`

### Tests / lint
No test runner or linter configuration is present in the repo (no `tests/`, `pytest.ini`, `tox.ini`, `pyproject.toml`, etc.).

If you introduce them, prefer documenting:
- the canonical “run all tests” command
- how to run a single test (e.g. `pytest path/to/test_file.py::test_name`)
- the canonical formatter/linter commands (e.g. `ruff`, `black`) and any config locations

## Codebase structure (big picture)
### Session-based standalone Streamlit scripts
- `SESION1/`: simplest Streamlit examples
  - `hola_mundo.py`: minimal “hello world” app
  - `entrada_usuario.py`: basic widgets (`text_input`, `number_input`, `button`)
- `SESION2/`: CSV upload + basic exploration
  - Uses `st.file_uploader` and `pandas.read_csv` to load data
  - Typical patterns: show `df.head()`, `df.describe()`, and basic filtering
- `SESION3/`: interactive visualization with built-in Streamlit charts
  - `multiselect` to pick numeric columns
  - chart selection (`line_chart`, `bar_chart`, `area_chart`)
- `SESION4/`: “advanced” plotting libraries integrated into Streamlit
  - Altair (`st.altair_chart`)
  - Matplotlib (`st.pyplot`)
  - Seaborn (rendered via Matplotlib figure)

### Root-level demos
- `graph_demo.py`: interactive CLT demo (binomial coin flips), using NumPy + Matplotlib
- `stlEjemplos.py`: assorted examples adapted from Streamlit docs (tables, charts, maps, widgets)

## Conventions to be aware of
- Scripts are written as top-to-bottom Streamlit apps (no explicit `main()` entrypoint).
- Most apps expect the user to upload a CSV at runtime; there is no bundled sample data in the repo.
- There is no shared module layer; if you want shared utilities, introduce a `src/` or `app/` package and refactor incrementally (while keeping the session scripts runnable).
