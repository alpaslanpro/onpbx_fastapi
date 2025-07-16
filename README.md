# ONPBX FastAPI Downloader

A FastAPI-based interface for downloading call recordings from OnlinePBX (onpbx.ru) using a human-friendly interface.

---

## ✨ Features

* Accepts user-friendly date inputs (like `2025-07-01 00:00`) and converts them to Unix Timestamps
* Communicates with OnlinePBX API
* Downloads archive URL for call recordings over a given date range
* One-week max interval per request (as per OnlinePBX API limits)

---

## ⚡ Quick Start

### 1. Clone and install dependencies

```bash
git clone https://github.com/yourusername/onpbx_fastapi.git
cd onpbx_fastapi
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Create `.env`

```bash
cp .env.example .env
```

Then fill in your OnlinePBX credentials in `.env`:

```env
ONPBX_DOMAIN=your-domain.onpbx.ru
ONPBX_API_KEY=your-api-key
```

---

### 3. Run the server

```bash
uvicorn main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🔗 API Usage

### Endpoint

```
POST http://127.0.0.1:8000/api/v1/download
```

### Request Body (JSON)

```json
{
  "start_date": "2025-07-01 00:00",
  "end_date": "2025-07-07 23:59"
}
```

### Example using curl

```bash
curl -X POST http://127.0.0.1:8000/api/v1/download \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-07-01 00:00", "end_date": "2025-07-07 23:59"}'
```

### Response

```json
{
  "download_url": "https://cdn.onlinepbx.ru/some-uuid/recordings.zip"
}
```

---

## 🔍 Notes

* The date format must be `YYYY-MM-DD HH:MM`
* The time is in your local timezone
* The max date range allowed is 7 days (OnlinePBX API limit)
* If you exceed this, the server will only return data for the first 7 days
* The download URL is valid for a short time: \~200 seconds (1 call) or 1 hour (batch)

---

## 📁 Project Structure

```
onpbx_fastapi/
├── api/
│   └── router.py
├── services/
│   └── onpbx_client.py
├── schemas/
│   └── request.py
├── utils/
│   ├── env.py
│   └── time_utils.py
├── main.py
├── requirements.txt
└── .env.example
```

---

## 🌟 Future Ideas

* Batch download over multiple weeks
* Frontend interface
* Telegram bot integration

---

## ✅ License

MIT or specify as needed.
