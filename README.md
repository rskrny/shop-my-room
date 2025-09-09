# Shop My Room

Modular architecture for an AI-powered room design tool.

## Architecture
```
shop-my-room/
├── apps/
│   ├── lovable-frontend/      ← Next.js UI exported from Lovable.dev
│   └── supabase/              ← Supabase backend functions
│       ├── functions/
│       │   ├── generate-layout/
│       │   └── track-affiliate-click/
│       ├── config.toml
│       └── .env
├── services/
│   └── cv-service/            ← Future computer vision microservice
├── .github/
│   └── workflows/
│       └── deploy-supabase.yml
├── .gitignore
└── README.md
```

## Setup
1. Clone the repo and install required tools.
2. Ensure the Lovable frontend and Supabase CLI are installed as needed.
3. Create your own `.env` files where required (they are ignored by git).

## Deploying Supabase Functions
1. Log in to Supabase and set `SUPABASE_ACCESS_TOKEN` in GitHub secrets.
2. Push changes under `apps/supabase/functions/**` to trigger the CI workflow.
3. The workflow links to project `atozmhkawkbtwsdaowhn` and deploys edge functions.

## Future Services
- `cv-service` will host a FastAPI microservice for computer vision tasks.
- Additional services (3D/AR processing, etc.) can be added under `services/`.
