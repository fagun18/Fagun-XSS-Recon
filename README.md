# FagunXssRecon

<div align="center">

<p><em>High‑signal, low‑noise recon for XSS. From raw URLs ➜ curated, parameter‑rich test cases.</em></p>

<p>
  <img alt="CI" src="https://img.shields.io/badge/ci-passing-brightgreen" />
  <a href="https://xss0r.medium.com/tool-overview-6c255fe7ec9b"><img alt="Docs" src="https://img.shields.io/badge/docs-medium-1da1f2" /></a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue" />
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

- Extension‑aware filtering (.php, .asp, .aspx, .jsp, .cfm)
- Parameter discovery via Arjun with resilient auto‑detection
- Smart query reduction and de‑duplication
- Performance knobs (FAST_MODE, threads, parallel sort)
- Resumable sessions after interruptions

---

## Table of Contents

- Getting Started
- Configuration & Performance
- Resuming Sessions
- Workflow & Outputs
- Troubleshooting
- Links
- Roadmap

---

## Getting Started

1) Clone

```bash
git clone https://github.com/fagun18/Fagun-XSS-Recon.git
cd Fagun-XSS-Recon
```

2) Make executable

```bash
chmod +x FagunXssRecon.sh
```

3) (Recommended) Use a local venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4) Install Arjun (choose one)

```bash
# In the venv (recommended on Kali/PEP668)
python -m pip install --upgrade pip
python -m pip install arjun

# or pipx (isolated system-wide)
sudo apt -y install pipx
pipx ensurepath
pipx install arjun

# or apt
sudo apt update && sudo apt -y install arjun
```

5) Run

```bash
bash FagunXssRecon.sh
```

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
8. Launch xss0r (optional)

Outputs:

- `<domain>-links.txt` / `urls-ready.txt`: curated URL lists
- `arjun_output.txt` / `arjun-final.txt`: discovered parameters and merges
- `<domain>-query.txt`: reduced, parameter‑focused URLs for XSS testing

---

## Troubleshooting

- Kali/PEP 668 blocks pip installs (externally-managed-environment)

```bash
python3 -m venv .venv && source .venv/bin/activate && python -m pip install arjun
# or
sudo apt -y install pipx && pipx install arjun
```

- dpkg was interrupted

```bash
sudo dpkg --configure -a
sudo apt -y update
sudo apt -y install arjun
```

- Broken `/usr/local/bin/arjun` or `pipx` shim

```bash
sudo rm -f /usr/local/bin/arjun /usr/local/bin/pipx
python3 -m pip install --user pipx && python3 -m pipx ensurepath && python3 -m pipx install arjun
```

- No output from Arjun step

Targets may not expose parameters; pipeline continues with fewer candidates.

---

## Links

- Overview: https://xss0r.medium.com/tool-overview-6c255fe7ec9b
- Store/downloads: https://store.xss0r.com

---

## Roadmap

- Extended resume points for earlier steps
- Pluggable runners for alternative param-finders
- Optional JSON output for integration pipelines

---

If you have questions or issues, open an issue or reach out via the links above.