"""Local configuration for the BrainIAK tutorials.

Copy this file to `config.py` (which is git-ignored) and edit `DATA_PATH`
to point at wherever the tutorial datasets live on your machine.

For students in this class the datasets live in the Google Drive shared
folder `Seqhub-Neuro/brainiak_datasets`. Once you have Google Drive for
Desktop installed and the shared drive synced, the path looks like:

    macOS   -> /Users/<you>/Library/CloudStorage/GoogleDrive-<your-email>/Shared drives/Seqhub-Neuro/brainiak_datasets
    Windows -> G:\\Shared drives\\Seqhub-Neuro\\brainiak_datasets   (drive letter may differ)

You can also skip this file and set the BRAINIAK_DATA_PATH environment
variable instead — either one works.
"""

import os

# --- EDIT THIS LINE -----------------------------------------------------------
# Absolute path to the folder that contains vdc/, NinetySix/, Pieman2/, etc.
DATA_PATH = os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-YOUR_EMAIL@example.com/Shared drives/Seqhub-Neuro/brainiak_datasets"
)
# -----------------------------------------------------------------------------
