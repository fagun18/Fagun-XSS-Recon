xss0rRecon

Overview

    xss0rRecon is a guided recon and filtering toolkit that prepares high-signal URL targets for XSS testing. It automates domain enumeration, URL crawling, deep filtering, parameter discovery, and smart reduction so you can focus on impactful XSS validation.

Why use xss0rRecon

    - Save time: automate tedious enumeration, URL dedupe, and parameter discovery.
    - Higher signal: aggressively reduce noise while preserving diverse parameters and interesting extensions.
    - Opinionated workflow: step-by-step flow from discovery to ready-to-test URL lists.
    - Smooth pairing with xss0r: produces inputs formatted for the xss0r XSS testing tool.

Who is this for

    - Bug bounty hunters who want fast, repeatable recon for XSS.
    - Security engineers performing application reconnaissance.
    - Red teamers who need curated URL/parameter inputs quickly.

Key features

    - Domain enumeration and URL crawling
    - Extension-aware filtering (e.g., .php, .asp, .aspx, .jsp, .cfm)
    - Parameter discovery via Arjun (auto-detected)
    - Smart deduplication and reduction of query strings
    - Clean output files ready for XSS testing

Requirements

    - Linux (Debian/Kali/Ubuntu recommended). macOS should work with minor adjustments.
    - bash, coreutils, awk, grep, sort
    - Python 3.9+ recommended
    - Arjun (used for parameter discovery)

Quick start

    1) Clone the repo
        git clone https://github.com/fagun18/Fagun-XSS-Recon.git
        cd Fagun-XSS-Recon

    2) Make the script executable
        chmod +x xss0rRecon.sh

    3) (Recommended) Create a local virtual environment
        python3 -m venv .venv
        source .venv/bin/activate

    4) Install Arjun (choose one)
        - In the venv (recommended on Kali/PEP668):
            python -m pip install --upgrade pip
            python -m pip install arjun
        - Or via pipx (isolated, system-wide):
            sudo apt -y install pipx
            pipx ensurepath
            pipx install arjun
        - Or via apt (system package manager):
            sudo apt update && sudo apt -y install arjun

    5) Run
        bash xss0rRecon.sh

How the workflow works

    The script presents a menu of steps. Typical flow:
        1. Install all tools (optional helper)
        2. Enter domain name
        3. Domain enumeration and filtering
        4. URL crawling and filtering
        5. In-depth URL filtering
        6. HiddenParamFinder / Arjun-based discovery and merge
        7. Prepare files for XSS detection (query-only, reduced set)
        8. Launch xss0r (optional if you use xss0r separately)

    Outputs (high level):
        - <domain>-links.txt / urls-ready.txt: progressively curated URL lists
        - arjun_output.txt / arjun-final.txt: discovered parameters and merged results
        - <domain>-query.txt: deduplicated, parameter-focused URLs for XSS testing

Arjun auto-detection

    The script will try in order:
        - python3 -m arjun (preferred; works inside your venv)
        - pipx run arjun (if pipx is installed)
        - arjun (system binary; used only if runnable)

    If none are available, the script shows install guidance and stops the Arjun step safely.

Troubleshooting

    - Kali/PEP 668 blocks pip system installs (externally-managed-environment)
        Use a venv or pipx instead:
            python3 -m venv .venv && source .venv/bin/activate
            python -m pip install arjun
        or
            sudo apt -y install pipx && pipx install arjun

    - dpkg was interrupted (apt errors)
        sudo dpkg --configure -a
        sudo apt -y update
        sudo apt -y install arjun

    - /usr/local/bin/arjun: cannot execute: required file not found
        Remove any broken shim:
            sudo rm -f /usr/local/bin/arjun
        Then install Arjun via venv or pipx (see above). The script prefers python3 -m arjun.

    - No output from Arjun step
        It can happen when targets don’t expose parameters. The script will proceed but you may have fewer candidate URLs.

Using with xss0r (optional)

    - xss0rRecon produces files tailored for xss0r. Place xss0r and this repo in the same folder, run recon, then launch xss0r with the generated lists.
    - For plans/licenses and downloads, see https://store.xss0r.com

Links and references

    - Tool overview: https://xss0r.medium.com/tool-overview-6c255fe7ec9b
    - Store and downloads: https://store.xss0r.com

Support

    If you have questions or issues, open an issue on GitHub or reach out via the links above.