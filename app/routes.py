from flask import Blueprint, jsonify, request
from app.movie_api import search_movie_by_title

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