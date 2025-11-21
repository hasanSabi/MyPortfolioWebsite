# Sabihul Hasan - Portfolio

A minimalist, metallic-themed personal portfolio website built with Django, HTML, CSS, and Bootstrap.

## Features
- **Metallic Aesthetic**: Custom CSS with graphite, silver, and blue tint gradients.
- **Dynamic Projects**: Projects loaded from the database.
- **Responsive Design**: Fully responsive layout using Bootstrap 5.
- **Contact Form**: Functional contact form (ready for email backend integration).
- **CI/CD**: GitHub Actions workflow for automated testing.
- **Dockerized**: Ready for containerized deployment.

## Tech Stack
- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (Dev/Prod for lightweight use)
- **Deployment**: Docker, Gunicorn, WhiteNoise

## Setup & Installation

### Prerequisites
- Python 3.11+
- Git

### Local Development
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Populate database with sample projects:**
   ```bash
   python populate_projects.py
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` in your browser.

## Deployment

### Docker
1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

### Render/Railway
1. Push code to GitHub.
2. Connect repository to Render/Railway.
3. Set Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
4. Set Start Command: `gunicorn portfolio_project.wsgi:application`

## Future Improvements
- Integrate email backend (SendGrid/SMTP) for the contact form.
- Add a blog section.
- Implement a dark/light mode toggle.
