#!/usr/bin/env python
"""MD -> HTML -> PDF for AI History Reborn product files. Copy-adapted from Skyline Reborn."""
import sys, os, io, subprocess, pathlib
import markdown

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = pathlib.Path(__file__).parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = """
@page { size: A4; margin: 20mm 18mm; }
* { box-sizing: border-box; }
body {
  font-family: -apple-system, "Segoe UI", "Noto Sans Devanagari", Roboto, Helvetica, Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.55; color: #1a1a1a; max-width: 100%;
}
h1 { font-size: 22pt; color: #6b2c00; border-bottom: 3px solid #d4a017; padding-bottom: 6pt; margin-top: 24pt; }
h2 { font-size: 16pt; color: #6b2c00; margin-top: 18pt; border-left: 4px solid #d4a017; padding-left: 10pt; }
h3 { font-size: 13pt; color: #8a3b00; margin-top: 14pt; }
h4, h5, h6 { font-size: 11.5pt; color: #555; }
p { margin: 8pt 0; }
code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: "Consolas", "Courier New", monospace; font-size: 9pt; color: #b8860b; }
pre { background: #2a1a0a; color: #f0e6c8; padding: 12pt; border-radius: 6pt; overflow: auto; font-size: 8.5pt; line-height: 1.4; }
pre code { background: transparent; color: inherit; padding: 0; }
ul, ol { margin: 8pt 0 8pt 22pt; }
li { margin: 3pt 0; }
strong { color: #6b2c00; }
em { color: #8a3b00; }
blockquote { border-left: 3px solid #d4a017; padding-left: 12pt; color: #555; margin: 8pt 0; font-style: italic; }
table { border-collapse: collapse; margin: 10pt 0; width: 100%; font-size: 9.5pt; }
th, td { border: 1px solid #ccc; padding: 5pt 8pt; text-align: left; }
th { background: #6b2c00; color: #f0e6c8; }
tr:nth-child(even) { background: #fafafa; }
hr { border: none; border-top: 2px dashed #d4a017; margin: 18pt 0; }
.footer { position: fixed; bottom: 10mm; left: 18mm; right: 18mm; text-align: center; font-size: 8pt; color: #999; border-top: 1px solid #eee; padding-top: 4pt; }
"""

def md_to_html(md_path, title):
    md_text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["extra", "tables", "fenced_code", "toc"])
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head>
<body>{html_body}
<div class="footer">AI History Reborn &bull; {title}</div>
</body></html>"""

def html_to_pdf(html_path, pdf_path):
    user_data = ROOT / "_chrome_profile"
    user_data.mkdir(exist_ok=True)
    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={user_data}",
        "--no-pdf-header-footer",
        "--virtual-time-budget=2000",
        f"--print-to-pdf={pdf_path}",
        f"file:///{html_path.as_posix()}"
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print("  STDERR:", result.stderr[:500])
        raise subprocess.CalledProcessError(result.returncode, result.args)

# Auto-discover all .md files in root (except README by default — include it if you want)
MD_FILES = sorted([p for p in ROOT.glob("*.md")])

out_dir = ROOT / "PDF"
out_dir.mkdir(exist_ok=True)
html_dir = ROOT / "_html"
html_dir.mkdir(exist_ok=True)

for md_path in MD_FILES:
    title = md_path.stem.replace("-", " ").title()
    html = md_to_html(md_path, title)
    html_path = html_dir / (md_path.stem + ".html")
    html_path.write_text(html, encoding="utf-8")
    pdf_path = out_dir / (md_path.stem + ".pdf")
    print(f"Building {pdf_path.name} ...")
    html_to_pdf(html_path, pdf_path)
    print(f"  OK {pdf_path.stat().st_size // 1024} KB")

print("Done.")
