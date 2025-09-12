# FagunXssRecon

<div align="center">

<p><em>High‑signal, low‑noise recon for XSS. From raw URLs ➜ curated, parameter‑rich test cases.</em></p>

<p>
  <img alt="CI" src="https://img.shields.io/badge/ci-passing-brightgreen" />
  <a href="https://fagun.medium.com/tool-overview-6c255fe7ec9b"><img alt="Docs" src="https://img.shields.io/badge/docs-medium-1da1f2" /></a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue" />
  <img alt="Platform" src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey" />
  <img alt="Shell" src="https://img.shields.io/badge/shell-Bash-blue" />
</p>

</div>

---

## ✨ What is it?

FagunXssRecon is a guided recon and filtering toolkit that prepares high‑signal URL targets for XSS testing. It automates domain enumeration, crawling, de‑duplication, parameter discovery, and smart reduction—so you can spend time validating real findings.

## 🤝 Who uses it

- Bug bounty hunters needing repeatable, fast recon
- Security engineers performing application reconnaissance
- Red teamers preparing curated URL/parameter inputs

## 🚀 Highlights

- **Multi-tool Integration**: Combines 15+ reconnaissance tools including subfinder, assetfinder, amass, findomain, chaos, dnsbruter, subdominator, subprober, httpx, httprobe, meg, paramspider, and waybackpy
- **Extension‑aware filtering**: Targets (.php, .asp, .aspx, .jsp, .cfm) for better XSS testing
- **Parameter discovery**: Via Arjun with resilient auto‑detection and fallback mechanisms
- **Smart query reduction**: Advanced de‑duplication and filtering algorithms
- **Performance optimization**: Configurable threads, parallel processing, and FAST_MODE
- **Resumable sessions**: Continue from interruption points with `--resume` flag
- **Cross-platform support**: Works on Linux and Windows environments
- **Robust error handling**: Graceful failure recovery and detailed error logging

---

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Configuration & Performance](#configuration--performance)
- [Resuming Sessions](#resuming-sessions)
- [Workflow & Outputs](#workflow--outputs)
- [Troubleshooting](#troubleshooting)
- [Recent Updates](#recent-updates)
- [Links](#links)
- [Roadmap](#roadmap)

---

## Getting Started

### 1) Clone the Repository

```bash
git clone https://github.com/fagun18/Fagun-XSS-Recon.git
cd Fagun-XSS-Recon
```

### 2) Make Script Executable

```bash
chmod +x FagunXssRecon.sh
```

### 3) (Recommended) Set Up Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4) Install Required Dependencies

#### Install Arjun (choose one method):

```bash
# Method 1: In the venv (recommended on Kali/PEP668)
python -m pip install --upgrade pip
python -m pip install arjun

# Method 2: Using pipx (isolated system-wide)
sudo apt -y install pipx
pipx ensurepath
pipx install arjun

# Method 3: Using apt package manager
sudo apt update && sudo apt -y install arjun
```

#### Install Other Required Tools:

```bash
# Domain Discovery Tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/owasp-amass/amass/v4/...@master
go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest

# URL Discovery Tools
go install -v github.com/hakluke/hakrawler@latest
go install -v github.com/jaeles-project/gospider@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/subprober@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/tomnomnom/httprobe@latest
go install -v github.com/tomnomnom/meg@latest

# Additional Tools
pip install paramspider waybackpy --break-system-packages --root-user-action=ignore

# Findomain (manual download)
wget -O findomain.zip https://github.com/Findomain/Findomain/releases/latest/download/findomain-linux.zip
unzip findomain.zip && chmod +x findomain && sudo mv findomain /usr/local/bin/
```

### 5) Run the Script

```bash
bash FagunXssRecon.sh
```

### Windows 11 (WSL2) Setup

If you are on Windows, run FagunXssRecon inside WSL2 (Ubuntu) for full Linux tooling compatibility.

1) Install WSL and Ubuntu (PowerShell as Administrator):

```powershell
wsl --install -d Ubuntu
wsl --set-default-version 2
```

Launch Ubuntu from Start Menu and create your Linux user.

2) Access your Windows files from WSL:

- Windows drives are mounted under `/mnt`. Example: `H:\xssorRecon` → `/mnt/h/xssorRecon`

```bash
cd /mnt/h/xssorRecon
```

3) Fix line endings and permissions (first run only):

```bash
sed -i 's/\r$//' FagunXssRecon.sh
chmod +x FagunXssRecon.sh
```

4) Handle noexec mounts (if you see “cannot execute: required file not found”):

```bash
# Option A: run via bash
bash ./FagunXssRecon.sh

# Option B: copy to Linux home and run
mkdir -p ~/xssorRecon && cp -f /mnt/h/xssorRecon/FagunXssRecon.sh ~/xssorRecon/
cd ~/xssorRecon
chmod +x FagunXssRecon.sh
bash ./FagunXssRecon.sh
```

Tip: You can run from `~/xssorRecon` and read/write inputs/outputs under `/mnt/h/...` paths.

## Prerequisites

- **Operating System**: Linux (Ubuntu/Debian/Kali) or Windows with WSL
- **Python**: 3.7+ with pip
- **Go**: 1.19+ (for installing Go-based tools)
- **Tools**: The script will guide you through installing missing dependencies
- **Permissions**: Some tools may require sudo access for installation

---

## Configuration & Performance

Environment variables (optional):

- FAST_MODE=1: favor higher concurrency where safe
- ARJUN_THREADS: override Arjun thread count (default depends on FAST_MODE)
- ARJUN_STABLE=0|1: toggle Arjun --stable mode (default depends on FAST_MODE)

Under the hood:

- Parallel sorting via `sort --parallel=<nproc>` when available
- Adaptive polling intervals for background analysis
- Resilient `arjun` launcher prefers `python3 -m arjun` ➜ `python3 -m pipx run arjun` ➜ `arjun`

Example fast run:

```bash
FAST_MODE=1 ARJUN_THREADS=12 ARJUN_STABLE=0 bash FagunXssRecon.sh
```

---

## Resuming Sessions

If your machine powers off or network drops, resume from saved state (supported from step 7 onward):

```bash
bash FagunXssRecon.sh --resume
```

Clear the saved state:

```bash
bash FagunXssRecon.sh --clear-state
```

---

## Workflow & Outputs

Typical flow:

1. Install all tools (optional helper)
2. Enter domain name
3. Domain enumeration and filtering
4. URL crawling and filtering
5. In‑depth URL filtering
6. HiddenParamFinder / Arjun discovery and merge
7. Prep URLs with query strings for XSS testing
8. Launch FagunXss (optional)

Outputs:

- `<domain>-links.txt` / `urls-ready.txt`: curated URL lists
- `arjun_output.txt` / `arjun-final.txt`: discovered parameters and merges
- `<domain>-query.txt`: reduced, parameter‑focused URLs for XSS testing

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Kali/PEP 668 blocks pip installs (externally-managed-environment)

```bash
python3 -m venv .venv && source .venv/bin/activate && python -m pip install arjun
# or
sudo apt -y install pipx && pipx install arjun
```

#### 2. dpkg was interrupted

```bash
sudo dpkg --configure -a
sudo apt -y update
sudo apt -y install arjun
```

#### 3. Broken `/usr/local/bin/arjun` or `pipx` shim

```bash
sudo rm -f /usr/local/bin/arjun /usr/local/bin/pipx
python3 -m pip install --user pipx && python3 -m pipx ensurepath && python3 -m pipx install arjun
```

#### 4. No output from Arjun step

Targets may not expose parameters; pipeline continues with fewer candidates.

#### 5. "Error occurred during the execution of grep valid domains"

This error has been fixed in the latest version. The script now includes robust error handling for subprober output processing.

#### 6. Permission denied errors

```bash
# Make sure the script is executable
chmod +x FagunXssRecon.sh

# For Windows users, ensure WSL is properly configured
```

#### 7. Go tools not found

```bash
# Add Go bin to PATH
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc
```

#### 8. Virtual environment issues

```bash
# Recreate the virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install arjun
```

#### 9. Windows line ending errors (`$'\r': command not found`)

If you're on Windows and get line ending errors, convert the script to Unix format:

```bash
# Using PowerShell (Windows)
$content = Get-Content FagunXssRecon.sh -Raw
$content = $content -replace "`r`n", "`n"
Set-Content FagunXssRecon.sh -Value $content -NoNewline

# Using WSL/Linux
dos2unix FagunXssRecon.sh

# Using Git (if available)
git config core.autocrlf false
git add FagunXssRecon.sh
git reset --hard
```

---

## 🛠️ Integrated Tools

### Domain Discovery Tools
- **Subfinder**: Fast subdomain discovery using passive sources
- **Assetfinder**: Subdomain discovery using certificate transparency logs
- **Amass**: Comprehensive attack surface mapping and external asset discovery
- **Findomain**: Fast and cross-platform subdomain discovery tool
- **Chaos**: Fast and reliable subdomain discovery using passive sources
- **Dnsbruter**: DNS brute forcing with wildcard detection
- **Subdominator**: Advanced subdomain enumeration with multiple techniques

### URL Discovery Tools
- **GoSpider**: Fast web spider written in Go
- **Hakrawler**: Fast web crawler for gathering URLs and JavaScript file locations
- **URLFinder**: Fast web crawler for gathering URLs and JavaScript file locations
- **Katana**: Fast web crawler with advanced filtering capabilities
- **Waybackurls**: Fetch all URLs that the Wayback Machine has for a domain
- **Gau**: Get All URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl
- **Httpx**: Fast and multi-purpose HTTP toolkit
- **Httprobe**: Take a list of domains and probe for working HTTP and HTTPS servers
- **Meg**: Fetch many paths for many hosts without overwhelming them
- **Paramspider**: Mining parameters from dark corners of Web Archives
- **Waybackpy**: Python package for interacting with the Internet Archive's Wayback Machine

### Processing & Filtering Tools
- **Uro**: URL normalization and deduplication
- **Arjun**: HTTP parameter discovery suite
- **Subprober**: Fast subdomain probe for checking subdomain status

---

## Recent Updates

### Latest Version Improvements

- **🔧 Fixed grep error**: Resolved "Error occurred during the execution of grep valid domains" issue
- **🛡️ Enhanced error handling**: Added robust fallback mechanisms for subprober output processing
- **📝 Improved documentation**: Updated README with comprehensive troubleshooting guide
- **🔄 Better file validation**: Added checks for empty or missing output files
- **⚡ Performance optimizations**: Improved regex patterns and error recovery
- **🆕 Added 10+ new tools**: Integrated subfinder, assetfinder, amass, findomain, chaos, httpx, httprobe, meg, paramspider, and waybackpy
- **🔗 Enhanced domain discovery**: Now uses 7 different domain discovery tools for comprehensive coverage
- **🌐 Improved URL collection**: Added 5 additional URL discovery and probing tools
- **📊 Better merging logic**: Enhanced file merging and deduplication across all tools

### Version History

- **v3.1.0**: Added 10+ new reconnaissance tools, enhanced domain/URL discovery, improved merging logic
- **v3.0.1**: Fixed critical grep command failure, enhanced error handling
- **v3.0.0**: Major rewrite with improved tool integration and performance
- **v2.x**: Initial release with basic XSS reconnaissance capabilities

---

## Links

- Overview: https://fagun.medium.com/tool-overview-6c255fe7ec9b
- Store/downloads: https://store.fagun.com

---

## Roadmap

- Extended resume points for earlier steps
- Pluggable runners for alternative param-finders
- Optional JSON output for integration pipelines

---

If you have questions or issues, open an issue or reach out via the links above.