import feedparser
from flask import Flask, render_template, request
import re
import html

app = Flask(__name__)

# Fonti RSS disponibili da cui poter scegliere
SOURCES = {
    'google': {
        'name': 'Google News',
        'url': 'https://news.google.com/news/rss/headlines/section/topic/TECHNOLOGY?hl=it&gl=IT&ceid=IT%3Ait'
    },
    'ansa': {
        'name': 'ANSA Tech',
        'url': 'https://www.ansa.it/sito/notizie/tecnologia/tecnologia_rss.xml'
    },
    'wired': {
        'name': 'Wired Italia',
        'url': 'https://www.wired.it/feed/rss'
    },
    'hwupgrade': {
        'name': 'Hardware Upgrade',
        'url': 'https://feeds.hwupgrade.it/rss_news.xml'
    },
    'ilsole24ore': {
        'name': 'Il Sole 24 Ore',
        'url': 'https://www.ilsole24ore.com/rss/tecnologia.xml'
    }
}

@app.route('/')
def index():
    # Ottieni la fonte scelta dall'URL (default: google)
    selected_source = request.args.get('source', 'google')
    if selected_source not in SOURCES:
        selected_source = 'google'
        
    rss_url = SOURCES[selected_source]['url']
    
    # Parsing del feed RSS della fonte selezionata
    feed = feedparser.parse(rss_url)
    articles = []
    
    # Prendi solo le prime 5 notizie
    for entry in feed.entries[:5]:
        title = entry.title
        link = entry.link
        
        # Ognuno dei feed potrebbe usare description, summary, eccetera. 
        # Usiamo un fallback in base agli attributi che esistono.
        summary = entry.description if hasattr(entry, 'description') else ""
        
        # Pulizia dell'HTML (molti feed RSS contengono HTML embedded)
        summary = re.sub('<[^<]+>', '', summary)
        summary = html.unescape(summary)
        
        # Accorciamo per mantenere un'interfaccia pulita
        if len(summary) > 200:
            summary = summary[:197] + "..."
            
        # Fallback nel caso in cui la fonte dia summary vuoti
        if not summary.strip():
            summary = "Scopri ulteriori dettagli e leggi l'articolo completo direttamente sulla fonte verificata..."
            
        articles.append({
            'title': title,
            'summary': summary,
            'link': link
        })
        
    # Passiamo sia gli articoli che le configurazioni delle fonti al template
    return render_template('index.html', articles=articles, sources=SOURCES, selected_source=selected_source)

if __name__ == '__main__':
    # Esegue l'app in locale. Il debug attivato fa in modo che ricarichi in automatico
    app.run(debug=True, port=5000)
