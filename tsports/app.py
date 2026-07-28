import os
import re
from flask import Flask, redirect
import requests

app = Flask(__name__)


@app.route("/tsports")
def tsports():
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
        }
        res = requests.get(
            "http://murgi.live/live-tv/tsports-2.html",
            headers=headers,
            timeout=5,
        )

        match = re.search(
            r'(http://[^\'"\s]+\.m3u8\?token=[^\'"\s]+)', res.text
        )
        if match:
            return redirect(match.group(1), code=302)
    except Exception as e:
        return f"Error: {e}", 500

    return "Token not found", 404


if __name__ == "__main__":
    # Render assigns dynamic port numbers via environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)