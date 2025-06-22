# Road2Cary Challenge – Map Builder
![image](https://github.com/user-attachments/assets/1060e5b6-dcaa-426a-b4a7-d0edc9d39ef6)

Track our collective journey from Marlow (UK) to Cary (USA) as teams log daily kilometres over two weeks. This repository contains the code, data, and instructions to generate an interactive Plotly map and host it with GitHub Pages.

## Table of Contents
- [About the Challenge](#aboutthechallenge)
- [Repository Structure](#repositorystructure)
- [Environment Setup (environment.yml)](#repositorystructure)
- [Create / Update a Daily Map](#updatemap)
- [Publish with GitHub Pages](#publishpages)

## About the Challenge <a name="aboutthechallenge"></a>

The Road2Cary initiative encourages employees to stay active. Every kilometre recorded by a participant moves their team marker the same distance along the predefined route:

Marlow → Copenhagen → Helsinki → Stockholm → Oslo → Glasgow → Dublin → Cary

The map lets everyone see their progress throughout the challenge. The map can be updated as often as needed to reach hourly, daily, ... updates.

## Repository Structure <a name="repositorystructure"></a>

```text
.
├── Data/                       # Outputs by date
│   └── MM_DD_YY/               # One folder per challenge day
│       ├── team_progress.csv   # Distances for that specific day
│       └── index.html          # Auto-generated map for the day
│
├── LibRoad2Cary/               # Reusable Python package
│   ├── data/
│   │   └── datasets.py         # CSV loader
│   ├── map/
│   │   └── map.py              # Road2CaryMap class using Plotly
│   └── utility/                # Constants & helper functions
│       ├── constants.py
│       └── functions_calcVals.py
│
├── showcase.ipynb              # Example usage notebook
├── environment.yml             # Conda environment specification
└── index.html                  # Latest map served via GitHub Pages
```

Only index.html at the repo root is used by GitHub Pages; the Data/ copies are kept as an archive of past days.

## Environment Set‑up <a name="repositorystructure"></a>

The project relies on a few geospatial and plotting libraries defined in environment.yml. Create the environment once, then reuse it for all map updates.

1. Create and activate the environment
   conda env create -f environment.yml    # or mamba
   conda activate road2cary

2. (Optional) Jupyter for the demo notebook
   conda install jupyterlab

Prefer pip? Generate a requirements file with conda list --export > requirements.txt and use a virtualenv instead.

## Create / Update a Daily Map <a name="updatemap"></a>

1. **Add new data:**
   Place the latest team_progress.csv inside a new folder named after the date:
   Data/06_23_25/team_progress.csv

   Example:
   | Column                  | Type  | Description                                   | Example      |
   |-------------------------|-------|-----------------------------------------------|--------------|
   | `Team_Name`             | str   | Display name shown in the tooltip             | Flying Geese |
   | `Total_Capped_Duration` | float | Cumulative kilometres recorded by the team    | 235.5        |

2. **Render the map:**
   Run the showcase.ipynb and change the date cell!

3. **Commit & push:**
   git add Data/06_23_25/ index.html
   git commit -m "Add 23 Jun 2025 progress"
   git push origin main

GitHub Pages will redeploy automatically (usually <60 s).

## Publish with GitHub Pages <a name="publishpages"></a>

**One‑time setup**

1. Ensure a root‑level index.html exists (see step 2‑b above) and push it.
2. On GitHub, open Settings → Pages.
3. Configure:
   - Source: Deploy from a branch
   - Branch: main (or your default)
   - Folder: / (root)
4. Click Save.

**Updating the live map**
Just repeat the Create / Update routine—every push containing a new root‑level index.html triggers a Pages redeploy.
