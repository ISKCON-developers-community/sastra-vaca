# Sastra Vaca

Text-to-speech implementation for books about Krishna Consciousness and devotional service.
Built on [Silero TTS](https://github.com/snakers4/silero-models), works fully offline after the first model download.

Supported languages/voices: Russian (`v3_1_ru` model) with speakers **baya**, **kseniya**, **xenia**, **aidar**, **eugene**, **random**.

## Requirements

- Python **3.10 or 3.11** (torch 1.12.1 has no wheels for newer versions; on Windows use **3.10**)
- git
- Internet connection on first run (to download the Silero model, ~60 MB)

## Installation

Clone the repo:

```bash
git clone https://notabug.org/granthin/sastra-vaca.git
cd sastra-vaca
# or GitHub mirror:
# git clone https://github.com/ISKCON-developers-community/sastra-vaca.git
```

Create a virtual environment and install dependencies:

```bash
python -m venv env
source env/bin/activate      # Linux / macOS
# .\env\Scripts\activate     # Windows (PowerShell)
pip install -r requirements.txt
```

### Windows

Step-by-step Windows guide (installing Python, git, venv): see [docs/INSTALL-windows.md](docs/INSTALL-windows.md).

## Usage

```bash
python main.py
```

The program guides you through dialogs:

1. Choose **File** (one `.txt` file, UTF-8) or **Folder** (all `.txt` files inside).
2. Enter the output audio file name (result is saved as `.wav` in the project folder).
3. Pick a voice.
4. Wait — synthesis runs paragraph by paragraph; long paragraphs are split by sentences automatically.

For each file in a folder a separate `.wav` is produced.

### Tips

- Source texts must be plain `.txt` in UTF-8 encoding.
- Synthesis is CPU-based: a whole book may take hours, keep the computer running.
- The Silero model config (`latest_silero_models.yml`) is cached locally after first run.
