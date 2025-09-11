xss0rRecon

Welcome to the xss0rRecon tool repository! 🚀
Installation Guide: https://xss0r.medium.com/tool-overview-6c255fe7ec9b

To use xss0rRecon effectively, it's essential that all required files are downloaded and placed in the same folder. Follow the instructions below to get started.
🛠️ Setup Instructions:

    Download the necessary files:
        Visit https://store.xss0r.com 
        Choose a plan (the PRO plan is free!). - From the 10th to the 15th of each month, we provide a 5-day free license for the Professional plan, allowing users to explore the tool before committing to a purchase. The license details are listed on store.xss0r.com on the popup and will remain active only during this period. After the 15th, the license will expire.

        Download all the tools, wordlists, and the xss0r tool.

    Extract everything:
        Ensure all the downloaded tools, wordlists, and the xss0r tool are extracted into the same folder where the xss0rRecon tool is located.

    Run the tool:
        With everything in place, you’re now ready to run xss0rRecon and start your recon tasks! 💻

If you have any questions or run into issues, feel free to reach out to me.

Additional notes (Arjun dependency):

    xss0rRecon uses Arjun for parameter discovery. The script now auto-detects Arjun via the arjun binary or python -m arjun.

    If you see an error like: cannot execute: required file not found
        Install Arjun with one of the following:
            pip3 install arjun
            # or on Debian/Ubuntu
            sudo apt install arjun

    After installation, simply re-run xss0rRecon. The script will pick up whichever Arjun form is available.