# Amazon ERP

A FastAPI web server that surfaces Amazon SP-API inventory data as a browser dashboard.

## Requirements

- Python 3.10+
- Amazon SP-API credentials (LWA client ID/secret + refresh token)

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env` and fill in your credentials:

```env
CLIENT_ID=amzn1.application-oa2-client.xxx
CLIENT_SECRET=xxx
REFRESH_TOKEN=Atzr|xxx
SELLER_ID=AxxxXXXXXX
REGION=FE          # NA | EU | FE
TARGET_COUNTRY=JP  # country inside the region
```

## Start

```bash
python server.py
```

Open [http://localhost:8000](http://localhost:8000).

Interactive API docs: [http://localhost:8000/api/docs](http://localhost:8000/api/docs).

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/inventory/` | All active FBA SKUs (fast, no catalog/sales calls) |
| `GET` | `/api/inventory/{sku}` | Full dashboard — inventory, listing, product, sales, fees, replenishment |
| `GET` | `/api/inventory/{sku}?restock=true` | Same, plus official FBA Restock Report (adds 1–5 min) |

## Project Structure

```
server.py                       # entry point
core/
  config.py                     # env vars, marketplace IDs, business defaults
  auth.py                       # LWA token refresh
  api_loader.py                 # dynamic SP-API client loader
modules/inventory/
  router.py                     # FastAPI routes
  dashboard.py                  # orchestration — calls all SP-API services
  replenishment.py              # days-of-supply and reorder recommendation logic
  api/
    fba.py                      # FBA Inventory API
    catalog.py                  # Catalog Items API
    listing.py                  # Listings Items API
    sales.py                    # Sales API
    restock.py                  # FBA Restock Report
clients/                        # auto-generated swagger clients (SP-API)
static/                         # frontend (served at /)
```
