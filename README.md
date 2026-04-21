# Movie Recommendation Application

**IS2209 – Software Development Project**  
*Group Number:* Group 27  

# Team Members

Kevin – 124323191  
Aidan – 124398553  
Artem – 124724095
Harry – 124498384  

# Project Overview

This project is a Flask-based movie search and recommendation application. It integrates the OMDb API for movie data and a Supabase PostgreSQL database for storing favourite movies.
The application allows users to search for movies, view details such as title, year, genre, plot, and rating, and store favourite movies in the database. It includes a simple HTML user interface, API endpoints, Docker support, CI/CD using GitHub Actions, and deployment on Render.

# Live Deployment

App: https://movie-app-7u7p.onrender.com  
Health: https://movie-app-7u7p.onrender.com/health  
Status: https://movie-app-7u7p.onrender.com/status  
Favorites: https://movie-app-7u7p.onrender.com/favorites  

## Setup and Running the Application

# 1. Clone the repository

```bash
git clone https://github.com/Kevincorkery/movie-recommendation-app.git
cd movie-recommendation-app
```

# 2. Install dependencies

```bash
pip install -r requirements.txt
```

# 3. Create environment variables

Create a `.env` file in the root of the project and add:

```env
OMDB_API_KEY=e1132e58
SUPABASE_URL=https://mfbmolmragxfwsmdldxb.supabase.co
SUPABASE_KEY=sb_publishable_gbHGnexNpq4WmprNgR_1NA_SBBkRWC4
```

# 4. Run the application locally

```bash
python run.py
```

Then open in your browser:
http://127.0.0.1:5000/


# Docker

Build the Docker image:

```bash
docker build -t movie-app .
```

Run the container:

```bash
docker run -p 5000:5000 --env-file .env movie-app
```


# CI/CD Overview

GitHub Actions is used for Continuous Integration. The pipeline runs automatically on push and pull requests, installs dependencies, and runs automated tests using pytest to ensure the application is working correctly.
Deployment is handled through Render, where the application is hosted as a live web service.

# API Endpoints

`/` = HTML user interface  
`/health` = health check  
`/status` = system diagnostics  
`/search?title=Inception` = search for a movie  
`/favorites` (GET) = retrieve favourite movies  
`/favorites` (POST) = add a favourite movie  



# Demo Steps

1. Open the deployed application URL  
2. Enter a movie title in the search bar  
3. View movie details such as title, year, genre, plot, and rating  
4. Test API endpoints such as `/health`, `/status`, and `/favorites`

# Tech Stack

Python  
Flask  
OMDb API  
Supabase/PostgreSQL
Git & GitHub  
GitHub Actions  
Docker  
Render  

