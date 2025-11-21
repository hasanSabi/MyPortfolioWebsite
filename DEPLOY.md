# Deployment Guide (Render.com)

This guide will help you deploy your Django Portfolio to **Render**, which offers a free tier and is very easy to set up.

## Prerequisites
1.  **GitHub Account**: Ensure your project is pushed to a GitHub repository.
    -   `git init`
    -   `git add .`
    -   `git commit -m "Ready for deployment"`
    -   `git branch -M main`
    -   `git remote add origin <your-github-repo-url>`
    -   `git push -u origin main`

## Step 1: Create a Render Account
1.  Go to [dashboard.render.com](https://dashboard.render.com/).
2.  Sign up/Log in using your **GitHub** account.

## Step 2: Create a New Web Service
1.  Click on the **"New +"** button and select **"Web Service"**.
2.  Select **"Build and deploy from a Git repository"**.
3.  Connect your GitHub account if prompted, and select your **portfolio repository**.

## Step 3: Configure the Service
Fill in the details as follows:

-   **Name**: `my-portfolio` (or any name you like)
-   **Region**: Choose the one closest to you (e.g., Singapore, Frankfurt).
-   **Branch**: `main`
-   **Root Directory**: Leave empty (defaults to root).
-   **Runtime**: **Python 3**
-   **Build Command**:
    ```bash
    pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
    ```
-   **Start Command**:
    ```bash
    gunicorn portfolio_project.wsgi
    ```
-   **Instance Type**: **Free**

## Step 4: Environment Variables
Scroll down to the **"Environment Variables"** section and add the following:

| Key | Value |
| :--- | :--- |
| `PYTHON_VERSION` | `3.11.5` (or just `3.11`) |
| `SECRET_KEY` | (Generate a random string or use a long random text) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*` (or your render URL like `my-portfolio.onrender.com`) |

## Step 5: Deploy
1.  Click **"Create Web Service"**.
2.  Render will start building your app. You can watch the logs.
3.  Once finished, you will see a green **"Live"** badge and a URL (e.g., `https://my-portfolio.onrender.com`).

## Troubleshooting
-   **Static Files**: If styles are missing, ensure `whitenoise` is in `requirements.txt` and `MIDDLEWARE` in `settings.py` (we already set this up).
-   **Database**: This setup uses SQLite, which is a file. **Note**: On Render's free tier, the filesystem is ephemeral. This means if the server restarts, **any new projects you add via the admin panel will be lost**.
    -   *Solution*: For a persistent database, you would typically use Render's **PostgreSQL** service (available on free tier for 90 days or paid). But for a static portfolio where you don't add projects daily, SQLite is fine if you populate data via the `populate_projects.py` script during the build (add `&& python populate_projects.py` to the Build Command).

## Recommended Build Command for SQLite Portfolio
To ensure your projects are always there even after restart, update your **Build Command** to:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python populate_projects.py
```
