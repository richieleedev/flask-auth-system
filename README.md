
# Flask-React Authentication System

This project implements a user authentication system using a Python Flask backend and a React frontend. It covers the full signup, login, protected route validation, and logout flow using JWT tokens stored in the browser's `sessionStorage`.

## Features

- **User Signup:** Register new users with email and password.
- **User Login:** Authenticate users and issue JWT tokens.
- **Protected Routes:** Validate JWT tokens to restrict access to private pages.
- **Logout:** Clear session tokens and redirect to login.
- **Routing:** React Router manages navigation between `/signup`, `/login`, and `/private`.

## Technologies

- Backend: Flask, Flask-JWT-Extended, Flask-CORS, SQLAlchemy, SQLite (or other configured DB)
- Frontend: React, React Router, Vite
- Authentication: JWT tokens stored in `sessionStorage`

## Getting Started

### Backend Setup

1. Navigate to the `backend` folder.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables in `.env` file:
   ```env
   DATABASE_URL=sqlite:///local.db
   JWT_SECRET_KEY=your_secret_key_here
   ```
5. Run the Flask server:
   ```bash
   python src/app.py
   ```

### Frontend Setup

1. Navigate to the `frontend` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm run dev
   ```
4. Open your browser and visit:
   ```
   http://localhost:5173
   ```

## Usage

- Register a new user at `/signup`.
- Login at `/login`.
- Access protected content at `/private` (requires valid login).
- Use the logout button in the navbar to end your session.

## Project Structure

```
backend/
  └─ src/
     ├─ app.py
     ├─ models.py
     ├─ routes/
     └─ utils/
frontend/
  └─ src/
     ├─ components/
     ├─ pages/
     ├─ App.jsx
     ├─ main.jsx
```

## Notes

- JWT tokens are stored in `sessionStorage` for session management.
- Private routes validate token presence and correctness on each page load.
- The backend uses SQLite by default but can be configured for other databases.


