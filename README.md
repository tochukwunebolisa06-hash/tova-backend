# Tova — Backend

Django + Django REST Framework API for Tova. Postgres is expected to come
from a Railway Postgres plugin linked to this service (Railway injects
`DATABASE_URL` automatically — you don't add it to the code or an env file
yourself). Locally, it falls back to sqlite if `DATABASE_URL` isn't set.

## Run it locally

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # edit if needed
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API is at `http://localhost:8000/api/`, admin at `http://localhost:8000/admin/`.

## Endpoints

| Method | URL                 | What it does                                             |
|--------|---------------------|------------------------------------------------------------|
| GET    | `/api/health/`      | Health check — returns `{"status": "ok"}`                 |
| POST   | `/api/waitlist/`    | Join the waitlist. Body: `{"email": "...", "name": "..."}` (`name` optional). Re-submitting the same email returns a friendly "already joined" response instead of an error. |
| GET    | `/api/faqs/`        | List published FAQs, in the order set in the admin.        |
| POST   | `/api/faqs/ask/`    | Submit a question. Body: `{"question": "...", "email": "..."}` (`email` optional). |

## Managing FAQ content

Everything shown on the live FAQs page is managed from the Django admin at
`/admin/`, under **Faqs → FAQs**: add a question/answer, set the `order` it
appears in, and toggle `is_published` to hide/show it without deleting it.

Questions visitors submit through the "ask a question" box land in
**Faqs → Submitted questions** — a separate inbox, not shown on the site —
where you can mark them answered and turn good ones into real FAQ entries.

The waitlist itself is under **Waitlist → Waitlist entries**.

## Deploying to Railway

1. Push this folder to a GitHub repo (or connect the repo Railway already
   has).
2. In Railway, add a Postgres plugin to the project and link it to this
   service — that's what sets `DATABASE_URL` for you.
3. Set these variables on the service (Railway → Variables):
   - `SECRET_KEY` — any long random string
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — your Railway domain, e.g. `tova-backend.up.railway.app`
   - `CORS_ALLOWED_ORIGINS` — your deployed frontend's URL, e.g.
     `https://tova.vercel.app` (comma-separate more than one)
4. Railway detects the `Procfile` and runs it as the start command — it
   runs migrations, collects static files, then starts gunicorn. No release
   step to configure separately.
5. Once it's live, create an admin user with `python manage.py createsuperuser`
   via `railway run` (Railway's CLI) so you can log into `/admin/`.

## Project layout

```
config/       settings, root urls, wsgi/asgi
waitlist/     WaitlistEntry model + /api/waitlist/
faqs/         FAQ + FAQQuestion models + /api/faqs/ and /api/faqs/ask/
```
