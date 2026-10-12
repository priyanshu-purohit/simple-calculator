# Simple Calculator

This repository contains two minimal calculator implementations:

- `calculator.py` — a command-line calculator written in Python 3.
- `index.html` — a small web-based calculator (HTML/CSS/JavaScript) you can open in a browser.

I added both files so you can preview locally or host the web UI using GitHub Pages.

Preview locally
---------------

1) Python CLI

- Run the CLI calculator:

  python3 calculator.py

2) Web UI

- Open `index.html` directly in your browser (double-click the file).
- Or serve the folder with a simple local server and open http://localhost:8000:

  python3 -m http.server 8000

Preview on GitHub (GitHub Pages)
-------------------------------

To host the web calculator at a public URL, enable GitHub Pages for this repository:

1. Go to: https://github.com/priyanshu-purohit/simple-calculator
2. Settings → Pages (or Code & automation → Pages in the new UI).
3. Under "Build and deployment", choose "Deploy from a branch".
4. Select Branch: `main`, Folder: `/ (root)` and Save.

Within a minute or two your site should be available at:

https://priyanshu-purohit.github.io/simple-calculator

Notes
-----

- The web UI supports keyboard input: numbers, + - * /, Enter for equals, Backspace, and `c` to clear.
- If you'd like, I can enable Pages for you automatically (requires additional permissions) or add a GitHub Action to publish the site. Let me know which you prefer.
