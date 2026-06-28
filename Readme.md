# Multi-Tenant Analytics Platform

A multi-tenant SaaS analytics platform built with Flask, enabling organizations to upload data, visualize metrics, and share embeddable dashboards — all with real-time updates powered by WebSockets.

## Features

- **Multi-tenant architecture** — isolated data and dashboards per tenant
- **Authentication** — secure login and registration with hashed passwords via Flask-Bcrypt
- **Data uploads** — upload CSV/Excel files for analysis (up to 16MB)
- **Analytics dashboard** — visualize metrics and data sources per tenant
- **Embeddable widgets** — embed dashboards into external sites via the embed module
- **Developer API** — REST API for programmatic access to tenant data
- **Real-time notifications** — live updates via Flask-SocketIO and WebSockets
- **Reports** — generate and export reports using ReportLab
- **Profile & settings** — per-tenant profile and configuration management

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | PostgreSQL (production), SQLite (local dev) |
| ORM | Flask-SQLAlchemy |
| Auth | Flask-Login, Flask-Bcrypt |
| Real-time | Flask-SocketIO, gevent |
| Data | pandas, numpy, openpyxl |
| Reports | ReportLab |
| Server | Gunicorn + gevent worker |
| Deployment | Railway (Nixpacks) |

## Project Structure

```
├── app.py                  # App factory and entry point
├── config.py               # Configuration (env vars, DB URI)
├── extensions.py           # Flask extensions (db, bcrypt, socketio)
├── login_manager.py        # Login manager setup
├── socket_events.py        # WebSocket event handlers
├── models/
│   ├── tenant.py           # Tenant (user) model
│   ├── metric.py           # Metric model
│   └── datasource.py       # DataSource model
├── routes/
│   ├── auth.py             # Login / register
│   ├── dashboard.py        # Main dashboard
│   ├── upload.py           # File uploads
│   ├── api.py              # Developer REST API
│   ├── embed.py            # Embeddable dashboard
│   ├── reports.py          # Report generation
│   ├── notifications.py    # Notification routes
│   ├── profile.py          # Profile management
│   ├── settings.py         # Settings management
│   └── developer.py        # Developer tools
├── static/                 # CSS, JS, assets
├── templates/              # Jinja2 HTML templates
├── requirements.txt
├── Procfile
└── railway.json
```

## Local Development

### Prerequisites

- Python 3.12+
- PostgreSQL (optional — SQLite used by default locally)

### Setup

```bash
# Clone the repo
git clone https://github.com/charanachanta4-beep/Multi-Tenant-Analytics-Platform.git
cd Multi-Tenant-Analytics-Platform

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file
cp .env.example .env  # or create manually
```

### Environment Variables

Create a `.env` file in the root:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/yourdb  # optional, defaults to SQLite
```

### Run

```bash
python app.py
```

The app will be available at `http://localhost:5000`.

## Deployment (Railway)

### 1. Add a PostgreSQL service

In your Railway project, click **+ New → Database → PostgreSQL**. Railway will automatically provide a `DATABASE_URL` environment variable.

### 2. Link DATABASE_URL to your app

In your app service → **Variables**, add a reference to the Postgres service's `DATABASE_URL`.

### 3. Deploy

Push to your connected GitHub branch — Railway will build and deploy automatically using Nixpacks.

The `Procfile` defines the start command:

```
web: gunicorn -k gevent -w 1 --bind 0.0.0.0:$PORT app:app
```

## Environment Variables Reference

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | No | Flask secret key (defaults to a dev value) |
| `DATABASE_URL` | Yes (production) | PostgreSQL connection string |

## License

MIT
