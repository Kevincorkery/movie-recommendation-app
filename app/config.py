import os

class Config:
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")