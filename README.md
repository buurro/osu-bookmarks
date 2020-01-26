# Installation

Create a virtual environment and install the required packages

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your [Osu! API Key](https://osu.ppy.sh/p/api/)

Run database migrations

```
python manage.py migrate
```

Run the development server

```
python manage.py runserver
```
