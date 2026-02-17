# ArtLive – Backend

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.0-lightgrey?logo=flask)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-336791?logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/auth-JWT-blue)
![Cloudinary](https://img.shields.io/badge/storage-Cloudinary-3448C5?logo=cloudinary&logoColor=white)

**ArtLive Backend** is a RESTful API that powers the ArtLive platform, enabling instructors to create art workshops and students to discover, register, and engage with creative experiences near them.


## Description

This backend service provides secure authentication, workshop management, geolocation support, and student registration functionality.

ArtLive is designed as a creative workshop discovery platform where:
* Instructors can create and manage workshops
* Students can browse workshops by category and level
* Users can register and cancel registrations
* Workshops are geocoded for map visualization
* Images are uploaded securely using Cloudinary

The API follows RESTful conventions and is built to integrate seamlessly with a React frontend.


## Project Links

- **Frontend Repository:**  
  [View the ArtLive Frontend repository on GitHub](https://github.com/Gabyara237/artlive-frontend) 

- **Backend Repository:**  
  [View the ArtLive Backend repository on GitHub](https://github.com/Gabyara237/artlive-backend) 

- **Project Planning (Trello):**  
  [Explore the project planning board on Trello](https://trello.com/b/MadoMymc/project-4-artlive)

- **Deployed Application:**  
  [Visit the live ArtLive application](https://art-live.netlify.app/) <!-- Add Netlify link -->



## Core Features

- JWT-based authentication & role-based authorization
- Instructor and Student roles
- Create, update, and delete workshops (instructor-only)
- Student workshop registration & cancellation
- Automatic workshop capacity tracking
- Geocoding of workshop addresses (latitude & longitude)
- Cloudinary image uploads
- Protected routes using custom decorators
- PostgreSQL relational database with constraints


## Technologies Used

- **Python 3.11** – backend language
- **Flask** – web framework
- **PostgreSQL** – relational database
- **psycopg2** – PostgreSQL adapter
- **JWT (PyJWT)** – authentication & authorization
- **bcrypt** – password hashing
- **Cloudinary** – image upload & storage
- **Pipenv** – dependency management
- **python-dotenv** – environment variable management


## Entity Relationship Diagram (ERD)

![HomePlate ERD](https://trello.com/1/cards/6994ef87a3cc66fa5de6aec3/attachments/6994ef87a3cc66fa5de6aeed/download/ERD_ArtLive.png)

*High-level ERD showing relationships between users, workshops and registrations connections.*

### Schema Enforcement

The database enforces:
- Foreign key relationships
- Capacity constraints
- Role-based data integrity
- Automatic timestamping


## API Routes Overview

### Authentication
- `POST /auth/sign-up` – Register new user
- `POST /auth/sign-in` – User login

### Workshops
- `GET /workshops` – Get all workshops
- `GET /workshops/<workshop_id>` – Get single workshop details
- `POST /workshops` – Create new workshop (instructor only)
- `PUT /workshops/<workshop_id>` – Update workshop (instructor only)
- `DELETE /workshops/<workshop_id>` – Delete workshop (instructor only)

### Registrations
- `POST /workshops/<workshop_id>/registrations` – Register for a workshop (student only)
- `PUT /workshops/<workshop_id>/registrations` – Cancel registration (student only)
- `GET /users/me/registrations` – Get user's registrations
- `GET /users/me/workshops` – Get instructor's workshops
- `GET /users/me/registrations/workshops/<workshop_id>` – Get user's registration status for a specific workshop

> All protected routes require a valid JWT token in the Authorization header.


## Current Implementation Notes

- **Image uploads** are handled via Cloudinary
- **Addresses** are geocoded into latitude & longitude using the geocoding utility
- **Workshop capacity** is automatically updated when students register or cancel
- **Role-based access** is enforced using custom middleware:
  - `auth_middleware.py` – Validates JWT tokens
  - `role_middleware.py` – Restricts access based on user role (instructor/student)
- **Database schema** is defined in `schema.sql` with proper constraints and relationships
- **Database helpers** in `db_helpers.py` manage connections and common queries


## Future Scalability Considerations

In a larger-scale production environment, the following enhancements could be applied:

- Add pagination for workshop listings
- Add full-text search in PostgreSQL
- Implement review & rating system
- Add indexing on `art_type`, `level`, and `city` for faster queries
- Add workshop bookmarking/favorites
- Introduce caching for map-heavy queries
- Add automated tests (pytest)
- Implement instructor analytics dashboard
- Add email notifications for registrations


## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Cloudinary account
- Node.js 20+ (for frontend)

### Backend Setup

#### 1. Clone the repository
```bash
git clone https://github.com/Gabyara237/artlive-backend.git
cd artlive-backend
```

#### 2. Create virtual environment and install dependencies
```bash
pipenv shell
pipenv install
```

#### 3. Configure environment variables

Create a `.env` file in the root directory:
```bash
DATABASE_URL=your-postgres-url
JWT_SECRET=your-secret-key

CLOUD_NAME=your-cloudinary-name
API_KEY=your-cloudinary-api-key
API_SECRET=your-cloudinary-secret
```

#### 4. Run the server
```bash
python app.py
```

The API will be available at `http://localhost:5000`


## Art Type Categories

ArtLive supports the following artistic disciplines:

- **Watercolor Painting**
- **Oil Painting**
- **Acrylic Painting**
- **Drawing**
- **Charcoal & Pastel Drawing**
- **Ink Drawing & Calligraphy**
- **Mixed Media**
- **Ceramics & Pottery**
- **Clay Sculpture**
- **Wood Sculpture & Carving**
- **Mosaic Art**


## Workshop Skill Levels

- **Beginner** – No prior experience required
- **Intermediate** – Some foundational knowledge helpful
- **Advanced** – For experienced artists
- **All Levels** 


## Project Structure
```
artlive-backend/
├── db/
│   ├── db_helpers.py        # Database connection and helper functions
│   └── schema.sql           # Database schema definition
├── middleware/
│   ├── auth_middleware.py   # JWT authentication middleware
│   └── role_middleware.py   # Role-based authorization middleware
├── routers/
│   ├── auth.py             # Authentication endpoints (sign-up, sign-in)
│   ├── users.py            # User-related endpoints
│   └── workshops.py        # Workshop and registration endpoints
├── utils/
│   └── geocoding.py        # Geocoding utilities for address conversion
├── .env                    # Environment variables
├── .gitignore             # Git ignore rules
├── app.py                 # Application entry point
├── main.py                # Main application file
├── Pipfile                # Pipenv dependencies
├── Pipfile.lock           # Locked dependency versions
├── Pipfile.lock           # Locked dependency versions
└── README.md              # Project documentation
```


## Future Improvements

- Add instructor profile pages with bio and portfolio
- Implement review & rating system for workshops
- Add workshop search filters (distance, date)
- Create analytics dashboard for instructors
- Add email notifications for registrations and updates
- Implement real-time availability updates
- Add social features (share workshops, invite friends)
- Implement waitlist functionality when workshops are full
- Add automated integration tests with pytest


## Attributions

- Flask project structure inspired by General Assembly coursework
- Mapbox GL JS for interactive mapping
- Cloudinary for secure image storage
- Icon designs inspired by art education platforms

