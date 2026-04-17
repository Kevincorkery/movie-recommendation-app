from flask import Blueprint, jsonify, request, current_app
from app.movie_api import search_movie_by_title
from app.db import get_supabase
import requests

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Movie service running"})

@main.route("/health")
def health():
    return jsonify({"status": "ok"})

@main.route("/search")
def search():
    title = request.args.get("title")

    if not title:
        return jsonify({"error": "title parameter is required"}), 400

    result = search_movie_by_title(title)

    if "error" in result:
        return jsonify(result), 404

    return jsonify(result)

@main.route("/test-db")
def test_db():
    supabase = get_supabase()
    result = supabase.table("favorites").select("*").execute()
    return jsonify(result.data)

@main.route("/favorites", methods=["GET"])
def get_favorites():
    supabase = get_supabase()
    result = supabase.table("favorites").select("*").execute()
    return jsonify(result.data)

@main.route("/favorites", methods=["POST"])
def add_favorite():
    supabase = get_supabase()
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    result = supabase.table("favorites").insert({
        "title": data["title"],
        "imdb_id": data.get("imdb_id"),
        "year": data.get("year"),
        "poster": data.get("poster")
    }).execute()

    return jsonify(result.data)

@main.route("/status")
def status():
    omdb_configured = bool(current_app.config.get("OMDB_API_KEY"))

    database_connected = False

    try:
        supabase = get_supabase()
        response = supabase.table("favorites").select("*").limit(1).execute()

        if response is not None:
            database_connected = True

    except Exception as e:
        print("DB error:", e)

    return jsonify({
        "status": "ok",
        "omdb_configured": omdb_configured,
        "database_connected": database_connected
    })