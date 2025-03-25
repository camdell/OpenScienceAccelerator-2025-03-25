# A Modern Open Science Project

## Tools/Services Covered

0. Data Search Engines (https://kaggle.com; https://datasetsearch.research.google.com)
1. Pre-registration (https://osf.io/prereg)
2. Archive Repository (https://zeondo.org)
3. Git (https://git-scm.com/)
4. Podman (https://podman.io/) & pixi (https://pixi.sh/dev/)
5. Python (https://www.python.org/)
    - pandas (https://pandas.pydata.org/)
    - matplotlib (https://matplotlib.org/)
    - jupyter (https://jupyter.org/)
6. GitHub (https://github.org/)
7. MystMD (https://mystmd.org/)

## Our Research Question

“2024 was an overall hotter year in Sacramento, California USA than it was from 1950-2000.”

1. **Design**
- Find historical weather online for reuse.
- See if the "hypothesis" holds.

2. **Conduct & Analyze**
- Write a data analysis

3. **Report**
- Build an html website that shares our results

4. **Publish**
- archive our code & results
- archive a copy of the site

## Finding Data

**Remember**
- FAIR (Findable, Accessible, Interoperable, Reusable)
- Provenance

**Let’s Take a Look at**
- Kaggle
- Google Dataset Search
- zenodo
- Open Meteo

## Pre-Registration

“2024 was an overall hotter year in Sacramento, California USA than it was from 1950-2000.”

**Providers**
→ as predicted
→ Open Science Foundation

**Desired Features**
- Searchable      → you can search for others' prereg
- Frozen/Archived → you will have link to ALWAYS go back
- Anonymity       → can one upload registrations anonymously?
- Sandboxed       → there a demo interface/site for users to gain familiarity
    - https://test.osf.io
    - https://sandbox.zenodo.org
For a comparsion of popular pre-registration services see: https://doi.org/10.31222/osf.io/zry2u


## Reproducible Code

### Version Control (Git)

**Nouns**
- Repository ⇒ A computer folder that is under version control
- Commit     ⇒ A “snapshot” of a given repository

**Basic Verbs/Commands**
- init     ⇒ “Begin tracking this folder with version control.”
- status   ⇒ “Do I have pending changes not part of a snapshot?”
- add      ⇒ “In my next snapshot, I want to incorporate these files.”
- restore  ⇒ “Undo pending changes for some file(s).”
- commit   ⇒ “Create a snapshot of the files I have ‘added’.”
- log      ⇒ “View the timeline of all snapshots.”
- checkout ⇒ “Go to a specific snapshot.”
    - can also be used to grab a file from a different snapshot

### Programming Languages

**Open vs Proprietary**

Open Source Languages (Python/R)
- Widely accessible, free to use and modify
- Facilitates collaboration, sharing, and reuse.
- Strong community support and extensive libraries

Proprietary Languages (Matlab)
- Limited to users with licensed access
- Creates barriers to collaboration
- Vendor lock-in

### Containers & Virtual Environments

Tools to avoid “It works on my computer!”

**Docker/Podman**
*High technical overhead*

- Isolated, reproducible environments by containerizing the entire
  application (including OS dependencies), ensuring consistency across platforms.
- Ideal for deploying applications with complex dependencies or in production
  environments where consistency is critical.
- Requires more system resources compared to other tools, as it involves
  running entire containers.


**conda/mamba/pixi**
*Medium technical overhead*

- Manages environments and package dependencies, ensuring reproducibility by
  resolving conflicts and specifying exact package versions.
- Can install nearly any version of Python & R with support for other languages as well
    - Great support for common analytical/scientific Python packages
    - Growing support for R libraries.


**Python virtual env (venv)**
*Medium technical overhead*

- Lightweight tool for creating isolated Python environments, ensuring
  dependencies don't conflict with system-wide installations.
- Ideal for smaller Python-only projects, though it doesn't handle non-Python
  dependencies (e.g., system libraries).
- More suited for local development and prototyping than for complex,
  multi-language or production setups.
- Can only use the version of Python you have installed.


**Renv**
*Medium technical overhead*

- Manages R environments by tracking package dependencies and ensuring
  project-specific versions are used.
- Useful for R-based workflows and data analysis, making it easier to share
  reproducible code across systems.
- Focuses on R-specific needs, providing environment isolation without dealing
  with Python packages or non-R dependencies.
    - Can manage different versions of R

### Core Tools

Environment management
- Podman (for a brief demonstration)
- pixi https://prefix.dev/

Programming Language(s)
- Python

Analytical & Visualization Packages
- pandas
- matplotlib

Code Editing Tools
- Jupyter  (interactive exploration and analysis)
- jupytext (save notebooks as markdown files)

Rendering & Publishing
- MySTmd

### Writing Code & Running Analyses

Let's Dive into some Python, pandas, and matplotlib

## Writing an Article Locally

MyST-MD

## Sharing Your Work

→ Is it ready to share?
- README?
- LICENSE?
- CITATION.cff?

→ sharing
- put code onto GitHub
- create webpage via GitHub
- archive code & data on Zenodo
    - GitHub releases & Zenodo?
- share paper on pre-print server?

