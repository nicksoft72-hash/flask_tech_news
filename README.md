# Tech News Web App 🚀

Un aggregatore di notizie tecnologiche moderno, iper-veloce e ricco di feature, realizzato con **Flask** e **Tailwind CSS**.

🌐 **[Guarda il sito Live su Vercel](https://flasktechnews.vercel.app)**

## 🌟 Caratteristiche Principali

- **Aggregatore Multi-fonte**: Notizie in tempo reale da Google News, ANSA, Wired, Hardware Upgrade e Il Sole 24 Ore, raccolte e ottimizzate senza pubblicità.
- **Filtro di Ricerca Istantaneo**: Trova subito le notizie che ti interessano nella pagina corrente tramite la barra di ricerca reattiva in Javascript vanilla, senza tempi di caricamento aggiuntivi.
- **Theme Switcher Dinamico**: Scegli tra 4 opzioni di stile che vengono salvate nel tuo browser:
  - 💻 *Sistema*: si adatta al tuo OS.
  - 🌙 *Scuro*: la classica Dark Mode elegante con glassmorphism.
  - ☀️ *Chiaro*: un tema luminoso ad altissimo contrasto per un'ottima leggibilità.
  - 🦄 *Surprise!*: un tema "fuffoso" con unicorno, font Comic Sans MS, arcobaleni pastello e tanto rosa fluo!
- **Design UI Premium**: Animazioni fluide, glassmorphism, gradienti al neon, effetti hover 3D e un footer iper-carico firmato *NICK 2026* con led pulsanti.
- **Deploy-Ready**: Completamente configurato per Vercel serverless.

## 🛠️ Tecnologie Utilizzate

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, Tailwind CSS (via CDN) e Vanilla JS
- **Librerie**: `feedparser` per estrarre sapientemente i dati dai feed RSS

## 🚀 Installazione Locale

1. **Clona il repository:**
   ```bash
   git clone https://github.com/nicksoft72-hash/flask_tech_news.git
   cd flask_tech_news
   ```

2. **Crea un ambiente virtuale:**
   ```bash
   python -m venv venv
   # Su Windows:
   venv\Scripts\activate
   # Su macOS/Linux:
   source venv/bin/activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia l'applicazione:**
   ```bash
   python app.py
   ```
   L'app sarà visibile dal tuo browser preferito all'indirizzo `http://127.0.0.1:5000`.

## 📂 Struttura del Progetto

- `app.py`: Logica principale del server, parse dei feed e routing Flask.
- `templates/index.html`: Tutto il frontend in un colpo solo. Struttura, classi Tailwind ad-hoc e Script JS integrato.
- `static/unicorn.jpg`: Risorsa fondamentale per l'imprescindibile tema surprise 🦄.
- `requirements.txt`: Dipendenze Python del progetto.
- `vercel.json`: Configurazione necessaria per l'hosting gratuito e performante sul cloud rendering di Vercel.

## 📝 Licenza e Autore

Questo progetto è orgogliosamente "Powered & Coded By NICK 2026" e distribuito sotto licenza MIT.
