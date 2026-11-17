"""Generate an illustrative standalone review mockup; not a Jekyll build.
Requires PyYAML and a Node installation with marked (NODE_PATH or runtime bundle).
"""
import base64,html,json,os,re,subprocess
from pathlib import Path
import yaml
root=Path(__file__).resolve().parents[1]
css=(root/'_sass/_modern.scss').read_text()
# Expand the only theme-dependent mixins with equivalent review-layout rules.
css=re.sub(r'  @include breakpoint\(\$large\) \{.*?\n  \}', '', css, flags=re.S)
base='''*{box-sizing:border-box}body{margin:0}a{color:inherit}h1,h2,h3,p{margin-top:0}button,input{font:inherit}img{max-width:100%}.masthead{z-index:10}.masthead__inner-wrap{max-width:1180px;margin:auto;padding:18px 24px}.greedy-nav{display:flex;align-items:center;justify-content:space-between;gap:24px}.navlinks{display:flex;gap:24px;flex-wrap:wrap}.navlinks a{text-decoration:none;font-size:14px}.brand{text-decoration:none;font-weight:bold;font-family:Georgia,serif}#main{margin:56px auto;max-width:1180px;padding:0 24px}.home-grid{display:grid;grid-template-columns:190px minmax(0,1fr);gap:48px}.sidebar{align-self:start;position:sticky;top:100px;font-size:14px}.author__avatar img{width:150px;height:150px;object-fit:cover;border-radius:50%}.author__name{font-weight:bold}.author__urls{list-style:none;padding:0}.author__urls a{text-decoration:none}.author__urls li{margin:10px 0}.page__content img{max-width:100%;height:auto}.page__footer{padding:36px max(24px,calc((100% - 1132px)/2));font-size:13px}.home-page .page__content >ol:first-of-type{font-size:14px}.page__content{overflow-wrap:anywhere}.home-hero__lead{line-height:1.65}.page__content>ol{padding-left:22px}.publication-search{margin:0}.publication-tools{align-items:center}.publication-card h2{font-family:Georgia,serif}.preview-note{background:#f5f7f6;padding:8px 24px;font-size:12px;text-align:center;color:#536771}.page__content iframe{max-width:100%}@media(max-width:900px){.home-grid{grid-template-columns:1fr;gap:28px}.sidebar{position:static;display:none}.greedy-nav{align-items:start;flex-direction:column;gap:12px}.navlinks{gap:16px}#main{margin-top:28px}.page__footer{margin-top:48px}}'''
content=(root/'_pages/about.md').read_text().split('---',2)[2]
content=re.sub(r'<!--.*?-->', '',content,flags=re.S)
content=re.sub(r'{{\s*"([^"]+)"\s*\|\s*relative_url\s*}}',r'\1',content)
content=content.replace('<div class="home-intro" markdown="1">','').replace('</div>\n\n## Research','\n\n## Research',1)
modules=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE_MODULES','')
js="import {marked} from '"+modules+"/marked/lib/marked.esm.js'; let s='';for await(const c of process.stdin)s+=c;process.stdout.write(marked(s));"
body=subprocess.run(['node','--input-type=module','-e',js],input=content,text=True,capture_output=True,check=True).stdout
cards=[]
pubs=yaml.safe_load((root/'_data/publications.yml').read_text())
e=html.escape
for p in pubs:
 search=e(' '.join(str(p[k]) for k in ['title','authors','venue','year']).lower(),quote=True)
 authors=e(p['authors']).replace('Moritz Schwarz','<strong>Moritz Schwarz</strong>')
 cards.append(f'''<article class="publication-card" data-publication data-type="{p['type']}" data-search="{search}"><div><div class="publication-year">{p['year']}</div><div class="publication-type">{p['type_label']}</div></div><div><h2><a href="https://moritzschwarz.org{p['detail_url']}">{e(p['title'])}</a></h2><p class="publication-authors">{authors}</p><p class="publication-venue">{e(p['venue'])}</p></div><div class="publication-actions"><a href="{p['paper_url']}">Paper</a><a href="https://moritzschwarz.org{p['detail_url']}">Details</a></div></article>''')
intro=(root/'_pages/publications.md').read_text().split('---',2)[2].split('<div class="publication-list"')[0]
intro=intro.replace('{{ site.author.googlescholar }}','https://scholar.google.com/citations?user=-j4hwZAAAAAJ').replace('{{ site.data.publications | size }}',str(len(pubs)))
photo=base64.b64encode((root/'images/profile_small.jpg').read_bytes()).decode()
script=(root/'assets/js/publications.js').read_text()
page=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Moritz P. Schwarz — redesign mockup</title><style>{base}\n{css}</style><body class="home-page"><div class="preview-note">Design preview · Homepage and Publications · Live website unchanged</div><header class="masthead"><div class="masthead__inner-wrap"><nav class="greedy-nav" aria-label="Main"><a class="brand" href="#home">Dr Moritz P. Schwarz</a><div class="navlinks"><a href="#publications">Publications</a><a href="https://moritzschwarz.org/teaching/">Teaching</a><a href="https://moritzschwarz.org/coding/">Coding</a><a href="https://moritzschwarz.org/getspanel/">getspanel package</a><a href="https://moritzschwarz.org/osem/">OSEM Model</a></div></nav></div></header><main id="main"><section id="home-view"><div class="home-grid"><aside class="sidebar"><div class="author__avatar"><img src="data:image/jpeg;base64,{photo}" alt="Moritz P. Schwarz"></div><p class="author__name">Dr Moritz P. Schwarz</p><p class="author__bio">Applied Economist<br>Econometrics &amp; Forecasting<br>Climate &amp; Energy Policy</p><p>Between Berlin, Vienna<br>and Oxford</p><ul class="author__urls"><li><a href="mailto:moritz.schwarz@scmo.eu">Email ↗</a></li><li><a href="https://scholar.google.com/citations?user=-j4hwZAAAAAJ">Google Scholar ↗</a></li></ul></aside><article class="page"><div class="page__content">{body}</div></article></div></section><section id="publications-view" hidden><h1 class="page__title">Publications</h1>{intro}<div class="publication-list">{''.join(cards)}</div><p class="publication-empty" data-publication-empty hidden>No publications match this search.</p></section></main><footer class="page__footer">© Moritz P. Schwarz · AcademicPages / Jekyll</footer><script>{script}
function route(){{var pub=location.hash==='#publications';document.getElementById('home-view').hidden=pub;document.getElementById('publications-view').hidden=!pub;document.body.className=pub?'publications-page':'home-page';window.scrollTo(0,0)}}window.addEventListener('hashchange',route);route();document.querySelectorAll('a[href="/publications/"]').forEach(a=>a.href='#publications');document.querySelectorAll('a[href^="/files/"]').forEach(a=>a.href='https://moritzschwarz.org'+a.getAttribute('href'));</script></body></html>'''
(root/'docs/redesign-mockup.html').write_text(page)
print('Built mockup:',len(pubs),'publications')
