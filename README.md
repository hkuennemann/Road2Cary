# Road2Cary Challenge – Map Builder
![image](https://github.com/user-attachments/assets/1060e5b6-dcaa-426a-b4a7-d0edc9d39ef6)

Track our collective journey from Marlow (UK) to Cary (USA) as teams log daily kilometres over two weeks. This repository contains the code, data, and instructions to generate an interactive Plotly map and host it with GitHub Pages.

## Table of Contents
- [About the Challenge](#About the challenge)
- [Repository Structure](#Repository Structure)
- [Environment Setup (environment.yml)](#Environment Setup (environment.yml))
- [Create / Update a Daily Map](#Create / Update a Daily Map)
- [Publish with GitHub Pages](#Publish with GitHub Pages)

## About the Challenge

The Road2Cary initiative encourages employees to stay active. Every kilometre recorded by a participant moves their team marker the same distance along the predefined route:

Marlow → Copenhagen → Helsinki → Stockholm → Oslo → Glasgow → Dublin → Cary

The map lets everyone see daily progress.

## Repository Structure

.<br />
├── Data/<br />
│   └── MM_DD_YY/               # one folder per challenge‑day<br />
│       ├── team_progress.csv   # distances for that day<br />
│       └── index.html          # auto‑generated map for the day<br />
│<br />
├── LibRoad2Cary/               # reusable Python package<br />
│   ├── data/datasets.py        # CSV loader<br />
│   ├── map/map.py              # Road2CaryMap class (Plotly)<br />
│   └── utility/                # constants & helper functions<br />
│<br />
├── showcase.ipynb              # example notebook<br />
├── environment.yml             # conda environment spec<br />
└── index.html                  # **latest** map served by GitHub Pages<br />

Only index.html at the repo root is used by GitHub Pages; the Data/ copies are kept as an archive of past days.

## Environment Set‑up

The project relies on a few geospatial and plotting libraries defined in environment.yml. Create the environment once, then reuse it for all map updates.

1. Create and activate the environment
   conda env create -f environment.yml    # or mamba
   conda activate road2cary

2. (Optional) Jupyter for the demo notebook
   conda install jupyterlab

Prefer pip? Generate a requirements file with conda list --export > requirements.txt and use a virtualenv instead.

## Create / Update a Daily Map

1. **Add new data:**
   Place the latest team_progress.csv inside a new folder named after the date:
   Data/06_23_25/team_progress.csv

2. **Render the map:**
   Run the showcase.ipynb and change the date cell!

3. **Commit & push:**
   git add Data/06_23_25/ index.html
   git commit -m "Add 23 Jun 2025 progress"
   git push origin main

GitHub Pages will redeploy automatically (usually <60 s).

## Publish with GitHub Pages

**One‑time setup**

1. Ensure a root‑level index.html exists (see step 2‑b above) and push it.
2. On GitHub, open Settings → Pages.
3. Configure:
   - Source: Deploy from a branch
   - Branch: main (or your default)
   - Folder: / (root)
4. Click Save. Your map will be live at: https://<username>.github.io/<repository>/

**Updating the live map**
Just repeat the Create / Update routine—every push containing a new root‑level index.html triggers a Pages redeploy.
