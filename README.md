# Ko Kaung — Personal Site & Bot

**Website:** [ko-kaung.pages.dev](https://ko-kaung.pages.dev) (after deploy)  
**Bot:** Telegram bot (Python)  

---

## Deploy Website → Cloudflare Pages

1. Go to <https://dash.cloudflare.com> → Sign up (free, no card)
2. **Workers & Pages** → **Pages** → **Connect to Git**
3. Select this repo → Deploy
4. Done. Your site is live at `ko-kaung.pages.dev`

Every `git push` auto-deploys.

---

## Deploy Bot → PythonAnywhere

1. Sign up at <https://www.pythonanywhere.com> (free, no card)
2. Open a **Bash console**
3. Run:

```bash
git clone https://github.com/dadkaung/ko-kaung-site.git
cd ko-kaung-site/bot
export BOT_TOKEN="your_token_from_BotFather"
python3 bot.py
```

For 24/7: PythonAnywhere → **Tasks** → schedule `python3 bot.py` to run hourly.

---

## Create Telegram Bot

1. Open Telegram → search **@BotFather**
2. Send `/newbot`
3. Choose name and username
4. Copy the **token** — that's your `BOT_TOKEN`
