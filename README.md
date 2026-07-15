# SEQHUB NEURO BrainIAK Tutorials

A hands-on introduction to advanced fMRI analysis using [BrainIAK](https://brainiak.org).
These notebooks are used as course materials — this README is written for **students setting up on their own laptop for the first time**. Follow it top-to-bottom.

- **You will need:** git, Python 3.11+, ~10 GB of free disk, and access to the `Seqhub-Neuro` Google shared drive.
- **You will get:** a working JupyterLab environment where every notebook in `tutorials/` runs against the class datasets synced from Google Drive.

If you get stuck, jump to [Troubleshooting](#troubleshooting).

---

## 1. Install the prerequisites

### 1a. Git
- **macOS:** run `xcode-select --install` in Terminal (installs the Apple command-line tools, which include `git`).
- **Windows:** install [Git for Windows](https://git-scm.com/download/win). During install, accept the defaults.
- **Linux:** `sudo apt install git` (Ubuntu/Debian) or your distro's equivalent.

Verify:
```bash
git --version
```

### 1b. Python 3.11 or newer
Check whether you already have it:
```bash
python3 --version
```
If it prints `3.11.x`, `3.12.x`, or `3.13.x` you're set. Otherwise:
- **macOS:** the easiest path is [Miniforge](https://github.com/conda-forge/miniforge#miniforge3) or `brew install python@3.11`.
- **Windows:** install [Python 3.11+ from python.org](https://www.python.org/downloads/) and tick **"Add Python to PATH"** during setup. (Windows users who want the smoothest install of `mpi4py` should use [Miniforge](https://github.com/conda-forge/miniforge#miniforge3) instead — see the note in step 4.)
- **Linux:** `sudo apt install python3.11 python3.11-venv`.

### 1c. MPI (needed by `mpi4py`)
Several tutorials use MPI-based BrainIAK routines. Install an MPI implementation *before* installing Python packages:
- **macOS:** `brew install open-mpi` (install [Homebrew](https://brew.sh) first if you don't have it).
- **Ubuntu/Debian:** `sudo apt install -y libopenmpi-dev openmpi-bin`.
- **Windows:** use conda/miniforge instead of pip — `conda install -c conda-forge mpi4py` avoids compiling MPI from source. See step 4.

---

## 2. Install Google Drive for Desktop and mount the shared folder

The class datasets (~10 GB) live in the `Seqhub-Neuro` Google shared drive under `brainiak_datasets/`. Instead of downloading each dataset separately, we mount the shared drive on your laptop so the notebooks read directly from Google Drive.

1. **Download Google Drive for Desktop:** https://www.google.com/drive/download/ — pick the installer for your OS and run it.
2. **Sign in with the Google account that has access** to the `Seqhub-Neuro` shared drive. (If you don't have access, email the instructor with your Google account address.)
3. **Confirm the shared drive is available.** After Google Drive finishes syncing, you should see something like:
   - **macOS:** `/Users/<you>/Library/CloudStorage/GoogleDrive-<your-email>/Shared drives/Seqhub-Neuro/brainiak_datasets`
   - **Windows:** `G:\Shared drives\Seqhub-Neuro\brainiak_datasets` (the drive letter may differ)
4. **Prefer "Stream files" over "Mirror files"** in Google Drive Preferences. Streaming means files download on demand instead of taking 10 GB of local disk. (Streaming is the default.)
5. **Sanity check** by opening the folder in Finder/Explorer. You should see subfolders `vdc/`, `Pieman2/`, `NinetySix/`, `face_scene/`, `latatt/`, `raider/`, `Sherlock_processed/`, and `02-data-handling-simulated-dataset/`.

> **Tip:** The first time a notebook touches a large dataset (e.g. `vdc`), Google Drive will stream it down on demand — the first cell may take a minute. To avoid that, right-click the dataset folder in Finder/Explorer → **"Make available offline"** for the datasets you're about to use.

---

## 3. Clone this repository

Pick a location on your local disk (**not inside Google Drive** — put it somewhere like `~/Documents` or `~/Desktop/`):

```bash
cd ~/Desktop
git clone https://github.com/<owner>/brainiak-tutorials.git
cd brainiak-tutorials
```

Replace `<owner>` with the correct GitHub owner/org for this repo.

---

## 4. Create a Python environment and install the dependencies

Pick **one** of the two options below. If you're on Windows or `pip install mpi4py` fails, use Conda.

### MACOS / LINUX

From the repo root:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### WINDOWS

Install [Miniforge](https://github.com/conda-forge/miniforge#miniforge3) if you haven't already. Then, from the repo root:
```bash
conda create -n brainiak python=3.11 -y
conda activate brainiak
conda install -c conda-forge mpi4py -y
pip install -r requirements.txt
```
Installing `mpi4py` from conda-forge pulls in a prebuilt MPI, so you skip step 1c.

Either way, verify the install by running the smoke-test notebook:
```bash
jupyter lab tutorials/00-all-imports-test.ipynb
```
Run every cell — if none error, you're set.

---

## 5. Point the notebooks at the Google Drive datasets

The tutorials read a variable called `data_path` from `tutorials/utils.py`. `utils.py` looks in three places, first match wins:

1. The `BRAINIAK_DATA_PATH` environment variable
2. A `DATA_PATH` variable inside `config.py` at the repo root
3. (optional) Fallback: a `brainiak_datasets/` folder inside the repo (only used if you download the data locally)

From the repo root:
```bash
cp config.example.py config.py
```
Then open `config.py` in a text editor and replace `YOUR_EMAIL@example.com` with the Google account you used for Google Drive:

```python
DATA_PATH = os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-jane.doe@uchicago.edu/Shared drives/Seqhub-Neuro/brainiak_datasets"
)
```
`config.py` is git-ignored, so your personal path never gets committed.

---

## 6. Launch JupyterLab or VScode and start the tutorials

From the repo root, with your environment activated:

```bash
code .
```
This opens vscode in the current directory. OR(depending which you have installed)

```bash
jupyter lab
```

This opens JupyterLab in your browser. Open `tutorials/01-setup.ipynb` and work through the notebooks in order.

---

## Repository layout

```
brainiak-tutorials/
├── README.md               <- you are here
├── requirements.txt        <- Python dependencies
├── config.example.py       <- copy to config.py and edit DATA_PATH
├── config.py               <- (git-ignored) your local dataset path
├── .gitignore
└── tutorials/
    ├── utils.py            <- resolves data_path; do not hardcode paths in notebooks
    ├── 00-all-imports-test.ipynb   <- run first to sanity-check your install
    ├── 01-setup.ipynb
    ├── 02-data-handling.ipynb
    ├── 03-classification.ipynb
    ├── 04-dimensionality-reduction.ipynb
    ├── 05-classifier-optimization.ipynb
    ├── 06-rsa.ipynb
    ├── 07-searchlight.ipynb
    ├── 08-connectivity.ipynb
    ├── 09-fcma.ipynb
    ├── 10-isc.ipynb
    ├── 11-srm.ipynb
    ├── 12-hmm.ipynb
    └── 13-real-time.ipynb
```

Which notebook uses which dataset:

| Dataset (Google Drive)                       | Used by notebooks           |
| -------------------------------------------- | --------------------------- |
| `02-data-handling-simulated-dataset/`        | 02                          |
| `vdc/`                                       | 02, 03, 04, 05              |
| `NinetySix/`                                 | 06 (RSA)                    |
| `face_scene/`                                | 07 (searchlight), 09 (FCMA) |
| `latatt/`                                    | 08 (connectivity)           |
| `Pieman2/`                                   | 10 (ISC), 11 (SRM)          |
| `raider/`                                    | 11 (SRM)                    |
| `Sherlock_processed/`                        | 12 (HMM)                    |

---

## Solutions

Solutions are available on a seperate branch.

```bash
git checkout solutions
```

and to return to the tutorials

```bash
git checkout main
```


## Troubleshooting

- BrainIAK docs & original tutorials: https://brainiak.org/tutorials
- Email: atulkrishnan@uchicago.edu
