# FunctionalProgramingWithPython

## Directory Structure

```text
Contents
    code
        python
        haskel
    images
    text
Draft
    chapters.md
Workthrough
    chapters.md
```

## LaTeX Environment Setup

This textbook uses LaTeX for typesetting. Below are the command-line instructions to set up a functional LaTeX environment on different operating systems.

### macOS
You can install MacTeX via Homebrew (`brew`):
```bash
# Install the minimal CLI version of MacTeX:
brew install --cask mactex-no-gui

# Or install the full MacTeX distribution (includes GUI applications):
# brew install --cask mactex
```

### Linux (Ubuntu/Debian)
You can use the `apt` package manager to install TeX Live:
```bash
sudo apt update
sudo apt install texlive-full
```

### Windows
You can install TeX Live using Windows Package Manager (`winget`):
```powershell
winget install --id=TeXUsersGroup.TeXLive.Full -e
```
Alternatively, if you use Chocolatey (`choco`):
```powershell
choco install texlive
```