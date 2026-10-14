#!/usr/bin/env python3
"""Build the Institute for Extraterrestrial Inquiry site from content/*.md into public/.
Each content file starts with a front-matter block:
---
title: ...
slug: ...
category: Life in the Universe
verdict: Unexplained        (optional: Confirmed, Unexplained, Explained, Disputed)
published: 2026-10-13
updated: 2026-10-13        (optional)
summary: one sentence
---
Body uses a tiny Markdown subset: ## headings, paragraphs, - lists, **bold**, *italic*, [links](https://...),
and images on their own line: ![alt](file.jpg "caption") or ![alt](file.jpg) followed by an *italic caption line*.
Image files live in static/images/ and are copied to public/static/images/.
"""
import html, re, shutil, pathlib, datetime
ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "content", ROOT / "public"
SITE = "Institute for Extraterrestrial Inquiry"
ABBR = "IEI"
CATS = {
 "Life in the Universe": ("life-in-the-universe", "LU", "Astrobiology, exoplanets and the conditions life needs."),
 "The Search": ("the-search", "SR", "SETI, technosignatures, the Fermi paradox and how we listen."),
 "UAP & Encounters": ("uap-encounters", "UA", "UFO/UAP cases, military reports and government disclosures."),
 "Claims & Verdicts": ("claims-verdicts", "CV", "Specific claims, investigated against the evidence."),
}
IMG = re.compile(r'^!\[([^\]]*)\]\(\s*(\S+?)(?:\s+"([^"]*)")?\s*\)$')
VERDICTS = {"confirmed","unexplained","explained","disputed"}
def badge(a):
    v = a.get("verdict","")
    if not v: return ""
    return f'<span class="verdict v-{v.lower() if v.lower() in VERDICTS else "other"}">{html.escape(v).upper()}</span>'

def inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    t = re.sub(r"\[(.+?)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    return t
def md(body):
    out, para, lst = [], [], []
    src = [False]
    def flush():
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
        if lst:
            tag = "ol class=\"notes\"" if src[0] else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in lst) + f"</{tag.split()[0]}>"); lst.clear()
    lines = body.splitlines(); skip = set()
    for n, line in enumerate(lines):
        s = line.strip()
        if n in skip: continue
        m = IMG.match(s)
        if m:
            flush(); alt, path, cap = m.group(1), m.group(2), m.group(3) or ""
            nxt = lines[n+1].strip() if n + 1 < len(lines) else ""
            if not cap and re.fullmatch(r"\*[^*].*\*", nxt): cap = nxt[1:-1]; skip.add(n+1)
            src_ = path if re.match(r"https?://", path) else "../static/images/" + path.removeprefix("images/").removeprefix("static/images/")
            fc = f"<figcaption>{inline(cap)}</figcaption>" if cap else ""
            out.append(f'<figure class="fig"><img src="{html.escape(src_)}" alt="{html.escape(alt)}" loading="lazy">{fc}</figure>')
        elif not s: flush()
        elif s.startswith("## "):
            flush(); src[0] = s[3:].strip().lower() in ("sources","references","notes")
            out.append('<hr class="thin">' + (f'<h2 class="srch">Notes and Sources</h2>' if src[0] else f"<h2>{inline(s[3:])}</h2>"))
        elif s.startswith("- "):
            if para: flush()
            lst.append(s[2:])
        else:
            if lst: flush()
            para.append(s)
    flush(); return "\n".join(out)
def parse(p):
    txt = p.read_text(encoding="utf-8")
    _, fm, body = txt.split("---", 2)
    meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in fm.strip().splitlines() if ":" in l)}
    meta.setdefault("updated", meta["published"]); meta["body"] = body
    meta["words"] = len(body.split())
    if meta["category"] not in CATS: raise SystemExit(f"{p.name}: unknown category {meta['category']}")
    return meta
def fmt(d): return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")


SEAL = """<svg class="seal" viewBox="0 0 100 100" width="84" height="84" aria-label="Institute seal"><defs><path id="ring" d="M50 50 m-36 0 a36 36 0 1 1 72 0 a36 36 0 1 1 -72 0"/></defs>
<circle cx="50" cy="50" r="48" fill="#f4f1e8" stroke="#1f2f5c" stroke-width="2.5"/><circle cx="50" cy="50" r="43" fill="none" stroke="#1f2f5c" stroke-width="1"/>
<text font-family="Times New Roman,serif" font-size="8.6" fill="#1f2f5c" letter-spacing="1.2"><textPath href="#ring">INSTITUTE FOR EXTRATERRESTRIAL INQUIRY &#183; EST. 1996 &#183;</textPath></text>
<circle cx="50" cy="50" r="26" fill="#1f2f5c"/><ellipse cx="50" cy="50" rx="25" ry="8" fill="none" stroke="#c9c2a8" stroke-width="1" transform="rotate(-20 50 50)"/>
<circle cx="50" cy="50" r="7" fill="#c9c2a8"/><circle cx="40" cy="38" r="1.2" fill="#fff"/><circle cx="62" cy="42" r="1" fill="#fff"/><circle cx="57" cy="64" r="1.2" fill="#fff"/><circle cx="38" cy="60" r="0.9" fill="#fff"/>
<path d="M50 24 v6 M50 70 v6 M24 50 h6 M70 50 h6" stroke="#c9c2a8" stroke-width="1.2"/></svg>"""
def ref(a, i=None):
    return f"{ABBR}-{a['published'][:4]}-{a['published'][5:7]}{a['published'][8:]}-{abs(hash(a['slug'])) % 900 + 100 if i is None else i:03d}"
REFS = {}
def page(title, content, depth=0, newest=None, updated=None):
    r = "../" * depth
    today = datetime.date.today()
    nav = "".join(f'<li><a href="{r}category/{s}.html">{n}</a></li>' for n, (s, i, _) in CATS.items())
    upd = updated or today.isoformat()
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link rel="stylesheet" href="{r}static/style.css"></head><body>
<table class="frame" cellspacing="0" cellpadding="0" align="center"><tr><td colspan="2" class="hdr">
<table width="100%" cellspacing="0" cellpadding="0"><tr><td width="96">{SEAL}</td><td>
<div class="org">{SITE}</div><div class="tagline">An independent archive for the evidence-based study of extraterrestrial life, technosignatures and unidentified aerial phenomena</div></td>
<td class="hdrr" align="right"><small>Document Archive<br>Public Access Edition</small></td></tr></table></td></tr>
<tr><td colspan="2" class="topbar"><a href="{r}index.html">Home</a> | <a href="{r}archive.html">Case Index</a> | <a href="{r}index.html#whatsnew">What's New</a> | <a href="{r}index.html#about">About the Institute</a> | <a href="#contact">Contact</a></td></tr>
<tr><td class="side" valign="top">
<p class="navh">Main Menu</p><ul class="nav"><li><a href="{r}index.html">Home Page</a></li><li><a href="{r}archive.html">Case Index</a></li></ul>
<p class="navh">Research Divisions</p><ul class="nav">{nav}</ul>
<p class="navh">Verdict Key</p><table class="key" cellspacing="0"><tr><td><span class="verdict v-confirmed">CONFIRMED</span></td></tr><tr><td><span class="verdict v-explained">EXPLAINED</span></td></tr><tr><td><span class="verdict v-disputed">DISPUTED</span></td></tr><tr><td><span class="verdict v-unexplained">UNEXPLAINED</span></td></tr></table>
<p class="navh">Search the Archive</p><form onsubmit="return false"><input type="text" size="14"> <input type="submit" value="Go" class="btn"></form>
<p class="sidenote">Research is compiled by the Institute's automated research analyst. Findings are reviewed against published, primary sources.</p>
</td><td class="main" valign="top">{content}
<p class="lu">Last updated: {fmt(upd)}</p></td></tr>
<tr><td colspan="2" class="foot" id="contact"><hr class="thin">
[ <a href="{r}index.html">Home</a> | <a href="{r}archive.html">Case Index</a> | <a href="{r}category/claims-verdicts.html">Claims &amp; Verdicts</a> ]<br>
Webmaster: <a href="#contact">webmaster@iei-archive.org</a> &middot; Comments and corrections are welcome.<br>
&copy; 1996&ndash;{today:%Y} {SITE}. All material is provided for educational and research purposes.<br>
<small>Best viewed at 800x600 or higher.</small></td></tr></table>
</body></html>"""
def card(a, r=""):
    return f"""<tr><td class="d">{REFS[a['slug']]}</td><td><a href="{r}articles/{a['slug']}.html">{html.escape(a['title'])}</a><br><small>{html.escape(a['summary'])}</small></td><td class="d">{fmt(a['published'])}</td><td align="center">{badge(a) or '&mdash;'}</td></tr>"""
TH = '<tr><th>Ref. No.</th><th>Title</th><th>Filed</th><th>Verdict</th></tr>'
def main():
    arts = sorted((parse(p) for p in SRC.glob("*.md")), key=lambda a: (a["updated"], a["published"]), reverse=True)
    for k, a in enumerate(sorted(arts, key=lambda a: (a["published"], a["slug"]))):
        REFS[a["slug"]] = f"{ABBR}-{a['published'][:4]}-{k+1:03d}"
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / "articles").mkdir(parents=True); (OUT / "category").mkdir()
    shutil.copytree(ROOT / "static", OUT / "static")
    latest = arts[0] if arts else None
    lastupd = latest["updated"] if latest else None
    for a in arts:
        s, icon, _ = CATS[a["category"]]
        upd = f"<tr><th>Revised</th><td>{fmt(a['updated'])}</td></tr>" if a["updated"] != a["published"] else ""
        c = f"""<p class="crumb"><a href="../index.html">Home</a> &gt; <a href="../category/{s}.html">{a['category']}</a> &gt; {REFS[a['slug']]}</p>
<h1>{html.escape(a['title'])}</h1>
<table class="docinfo" cellspacing="0"><tr><th>Document No.</th><td>{REFS[a['slug']]}</td><th>Division</th><td>{a['category']}</td></tr>
<tr><th>Filed</th><td>{fmt(a['published'])}</td><th>Verdict</th><td>{badge(a) or 'Not assessed'}</td></tr>{upd}</table>
<p class="abstract"><b>Abstract.</b> {html.escape(a['summary'])}</p>
<div class="prose">{md(a['body'])}</div>
<hr class="thin"><p class="ret">[ <a href="../archive.html">Return to Index</a> ] &nbsp; [ <a href="../category/{s}.html">Return to {a['category']}</a> ] &nbsp; [ <a href="#">Top of Page</a> ]</p>"""
        (OUT / "articles" / f"{a['slug']}.html").write_text(page(f"{REFS[a['slug']]}: {html.escape(a['title'])}", c, 1, latest, a["updated"]), encoding="utf-8")
    counts = {n: sum(a["category"] == n for a in arts) for n in CATS}
    divs = "".join(f'<tr><td><a href="category/{s}.html"><b>{n}</b></a></td><td>{d}</td><td align="center">{counts[n]}</td></tr>' for n, (s, i, d) in CATS.items())
    news = "".join(f'<li><b>{fmt(a["updated"])}</b> &mdash; {"Revised" if a["updated"]!=a["published"] else "Added"}: <a href="articles/{a["slug"]}.html">{html.escape(a["title"])}</a> ({REFS[a["slug"]]})</li>' for a in arts[:8])
    feat = ""
    if latest:
        feat = f'<table class="notice" cellspacing="0" width="100%"><tr><td><b>Latest Report:</b> <a href="articles/{latest["slug"]}.html">{html.escape(latest["title"])}</a> &nbsp;<small>({REFS[latest["slug"]]}, {fmt(latest["updated"])})</small><br>{html.escape(latest["summary"])}</td></tr></table>'
    home = f"""<h1>Welcome to the Institute</h1>
<p id="about">The {SITE} maintains a public archive of research on a single question: <i>is there life, or intelligence, beyond Earth?</i> Each report examines a discovery, signal, sighting or claim and assigns a verdict based on the published evidence. The archive takes no position in advance; claims are judged on their sources.</p>
<p>A new report is filed, or an existing report revised, each day.</p>
{feat}
<h2 id="whatsnew">What's New</h2><ul class="news">{news}</ul>
<h2>Research Divisions</h2><table class="idx" cellspacing="0" width="100%"><tr><th>Division</th><th>Scope</th><th>Reports</th></tr>{divs}</table>
<h2>Case Index (Recent)</h2><table class="idx" cellspacing="0" width="100%">{TH}{"".join(card(a) for a in arts[:10])}</table>
<p class="ret">[ <a href="archive.html">View the complete Case Index</a> ]</p>"""
    (OUT / "index.html").write_text(page(SITE, home, 0, latest, lastupd), encoding="utf-8")
    ar = "".join(card(a) for a in sorted(arts, key=lambda a: REFS[a["slug"]], reverse=True))
    (OUT / "archive.html").write_text(page("Case Index &middot; " + SITE, f'<p class="crumb"><a href="index.html">Home</a> &gt; Case Index</p><h1>Case Index</h1><p>All reports held by the archive, by reference number. {len(arts)} documents on file.</p><table class="idx" cellspacing="0" width="100%">{TH}{ar}</table><hr class="thin"><p class="ret">[ <a href="index.html">Return to Home Page</a> ]</p>', 0, latest, lastupd), encoding="utf-8")
    for n, (s, i, d) in CATS.items():
        items = [a for a in arts if a["category"] == n]
        body = f'<table class="idx" cellspacing="0" width="100%">{TH}{"".join(card(a, "../") for a in items)}</table>' if items else "<p>No reports filed in this division yet.</p>"
        (OUT / "category" / f"{s}.html").write_text(page(f"{n} &middot; {SITE}", f'<p class="crumb"><a href="../index.html">Home</a> &gt; {n}</p><h1>Division: {n}</h1><p>{d}</p>{body}<hr class="thin"><p class="ret">[ <a href="../archive.html">Return to Index</a> ]</p>', 1, latest, items[0]["updated"] if items else lastupd), encoding="utf-8")
    print(f"Built {len(arts)} articles into {OUT}")
if __name__ == "__main__": main()
