PersonalVault — Knowledge Management API

PersonalVault is a production-style backend system built using Django REST Framework and PostgreSQL for storing, organizing, and managing personal learning resources like notes, links, PDFs, and references securely.

This project demonstrates real-world backend engineering concepts including authentication, authorization, database design, and scalable API development.

🧠 Features
🔐 Authentication & Security

JWT-based authentication (login & refresh)

User-specific resource access

Ownership-based authorization

Secure protected APIs

📂 Resource Management

Create, update, delete learning resources

Tagging system for categorization

File & link storage support

Personal resource library per user

🔎 Smart API Features

Search functionality

Filtering by tags & type

Pagination for performance

Optimized database queries

📘 Developer Experience

Swagger/OpenAPI documentation

Clean REST architecture

PostgreSQL integration

Structured serializers & views

🏗 Tech Stack

Python

Django

Django REST Framework

PostgreSQL

JWT Authentication (SimpleJWT)

drf-spectacular (Swagger/OpenAPI)

🔐 Authentication Flow

Register user

Login to get JWT token

Use Bearer token to access APIs

Refresh token when expired

Example:

Authorization: Bearer <access_token>

📡 API Endpoints
Auth

/api/token/ → login

/api/token/refresh/ → refresh token

Resources

GET /api/resources/ → list resources

POST /api/resources/ → create resource

GET /api/resources/<id>/ → single resource

PUT /api/resources/<id>/ → update

DELETE /api/resources/<id>/ → delete

Tags

Create & assign tags to resources

Docs

/api/docs/ → Swagger documentation

🧠 Key Concepts Implemented

REST API design

JWT stateless authentication

User ownership & permissions

Serializer validation

Pagination & filtering

Many-to-many tag system

File handling in Django

Swagger documentation

💻 Local Setup
git clone <repo-url>
cd personalVault
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Open:

http://127.0.0.1:8000/api/docs/

🎯 Purpose of Project

This project was built to:

Learn real backend development

Understand production API architecture

Practice authentication & database design

Build internship-ready backend skills

📌 Future Improvements

Deployment (Render/Railway)

Frontend integration

Favorites/bookmark system

Caching for performance

Role-based permissions

👨‍💻 Author

Built by: Tushar Saini
Backend Developer (Python/Django)