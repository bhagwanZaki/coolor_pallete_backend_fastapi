# coolor_pallete_backend_fastapi

Coolor pallete saver is a simple website that lets you save your coolor generated pallete so that they don't disappear.

live link: https://coolorpallete.netlify.app/

## setup

### Clone the repository

```bash
  git clone https://github.com/bhagwanZaki/coolor_pallete_backend_fastapi.git
```

### Basic setup
Once the repo is clone create a .env file on main folder and add a variable named ```DATABASE_URL``` and put your database url

**.env**
```bash
  DATABASE_URL = "your postgresql_database_url"
```

After that go to <u> **coolor/app.py** </u> and change ```prod=True``` to ```prod=False```

```python
  prod = False
```

### Run the project

```python
  python main.py

 ```
