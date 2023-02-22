# Spotify API Backend

This is a simple Flask app that uses the Spotipy library to interact with the Spotify API. It provides endpoints for searching tracks, albums, and artists, as well as getting recommendations based on a seed track.

## Getting Started
To get started, you'll need to set up a few things:

## Prerequisites
 - Python
 - pip
 - A Spotify developer account and app credentials (client ID and client secret)

## Installation
1. Clone the repository and install the dependencies:
```Bash
git clone https://github.com/yourusername/spotipy-flask-api.git
cd spotipy-flask-api
```
2. Create a virtual environment and activate it:
```Bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```Bash
pip install -r requirements.txt
```
4. Create a `.env` file and add your Spotify app credentials:
```Bash
CLIENT_ID="CLIENT_ID"
CLIENT_SECRET="CLIENT_SECRET"
REDIRECT_URI="http://localhost:8000/callback"
SCOPES="user-library-read user-library-modify user-read-private user-read-email user-read-playback-state user-modify-playback-state playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative user-read-playback-position user-read-recently-played user-top-read user-read-currently-playing user-follow-read user-follow-modify app-remote-control"
```
5. Run the app:
```Bash
python main.py
```