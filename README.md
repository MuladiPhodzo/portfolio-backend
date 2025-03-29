# Portfolio Backend

This is the backend service for the Portfolio Web Application, built using Django and Django REST Framework (DRF). The backend handles messages sent by clients and is deployed on AWS.

## 🚀 Features
- API for handling client messages
- Django REST Framework for API management
- Gunicorn as WSGI server
- Nginx for reverse proxy
- Deployed on AWS EC2

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/MuladiPhodzo/portfolio-backend.git
cd portfolio-backend
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


### 4. Run the Development Server
```bash
python manage.py runserver
```
The API will be available at `http://13.60.162.35:8000/`.

## 🚀 Deployment on AWS

### 1. Gunicorn Setup
Start Gunicorn manually:
```bash
gunicorn --bind 0.0.0.0:8000 backend.wsgi:application
```
Or set up a systemd service (`/etc/systemd/system/gunicorn.service`):
```ini
[Unit]
Description=Gunicorn instance to serve portfolio backend
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/portfolio-backend
ExecStart=/home/ubuntu/portfolio-backend/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/portfolio-backend/portfolio.sock backend.wsgi:application

[Install]
WantedBy=multi-user.target
```
Reload and start Gunicorn:
```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 2. Nginx Configuration
Create a configuration file (`/etc/nginx/sites-available/portfolio-backend`):
```nginx
server {
    listen 80;
    server_name 13.60.162.35;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/portfolio-backend/portfolio.sock;
    }
}
```
Enable and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/portfolio-backend /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 📬 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/contact` | Send a message |

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
Developed by **Muladi Phodzo**.

