# Tech News Web App 🚀

Un aggregatore di notizie tecnologiche moderno e veloce, realizzato con **Flask** e **Tailwind CSS**.

![Tech News App Preview](https://raw.githubusercontent.com/placeholder/image.png) *(Nota: Sostituisci con uno screenshot reale se necessario)*

## 🌟 Caratteristiche

- **Multi-fonte**: Notizie in tempo reale da Google News, ANSA, Wired, Hardware Upgrade e Il Sole 24 Ore.
- **Design Moderno**: Interfaccia in **Dark Mode** con layout a schede (cards) responsive.
- **Micro-interazioni**: Effetti hover e transizioni fluide realizzate con Tailwind CSS.
- **Parsing Intelligente**: Pulizia automatica dell'HTML dai feed RSS e riassunti ottimizzati.
- **Deploy-Ready**: Configurato per il deployment immediato su **Vercel**.

## 🛠️ Tecnologie Utilizzate

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, Tailwind CSS (via CDN)
- **Librerie**: `feedparser` per la gestione dei feed RSS

## 🚀 Installazione Locale

1. **Clona il repository:**
   ```bash
   git clone <url-del-tuo-repo>
   cd flask_tech_news
   ```

2. **Crea un ambiente virtuale (opzionale ma consigliato):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia l'applicazione:**
   ```bash
   python app.py
   ```
   L'app sarà disponibile all'indirizzo `http://127.0.0.1:5000`.

## 📂 Struttura del Progetto

- `app.py`: Logica principale del server e gestione dei feed RSS.
- `templates/index.html`: Layout frontend unico con design system integrato.
- `requirements.txt`: Dipendenze del progetto.
- `vercel.json`: Configurazione per il deployment cloud.

## 📝 Licenza

Questo progetto è distribuito sotto licenza MIT.
