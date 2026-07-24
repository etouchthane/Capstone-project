# Capstone-project


Project Name: LittleLemon
Application Name: Restaurant
SQL Database Name: LittleLemon


To run the project please use below commands
Step 1 
git clone <YOUR_GITHUB_REPO_URL>
cd Capstone-project

Step 2
python3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip install --upgrade pip

Step 3 
python3.12 -m venv .venv
pip install -r requirements.txt

Step 4 
Current database settings in code use:

- database name: littlelemon
- user: root
- password: qwedsa
- host: 127.0.0.1
- port: 3306

- Step 5
- Login as MySQL admin and run:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'root'@'127.0.0.1' IDENTIFIED BY 'qwedsa';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'root'@'127.0.0.1';
FLUSH PRIVILEGES;
```

If your local MySQL already uses root, you may only need:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Step 6
cd littlelemon
python manage.py migrate
python manage.py createsuperuser

Step 7
python manage.py runserver

Step 8 
App should be available at:

- http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Step 9
Run tests
Inside littlelemon directory:
python manage.py test




- 
