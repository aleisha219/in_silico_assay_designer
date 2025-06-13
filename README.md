# in_silico_assay_designer
AI-powered tool to design and simulate molecular assays in silico (ELISA, qPCR, CRISPR)

##  Setup (Local Development)

1. Clone:
```
git clone https://github.com/aleisha219/in_silico_assay_designer.git
cd in_silico_assay_designer
```

2. Create virtualenv & install:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configure `.env` (use `.env.example` as template).

4. Run migrations & start server:
```
python manage.py migrate
python manage.py runserver
```

5. Visit: `http://127.0.0.1:8000/`