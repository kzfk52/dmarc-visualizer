#!/usr/bin/env python3
"""Pre-generate the Gmail API token (token.json) for parsedmarc.

Run this on a machine with a browser BEFORE starting the containers.
The OAuth consent flow cannot complete inside the headless Docker
container, so the token must be created in advance and mounted in.

Usage:
    pip install google-auth-oauthlib
    python3 generate_token.py
"""
from google_auth_oauthlib.flow import InstalledAppFlow

# Must match the `scopes` value in parsedmarc.ini.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def main() -> None:
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    # Opens a browser automatically. On a headless host, open the printed
    # URL manually (use SSH port forwarding so the redirect reaches the
    # local server, e.g. `ssh -L 8080:localhost:8080 ...`).
    creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())
    print(f"Saved: {TOKEN_FILE}")


if __name__ == "__main__":
    main()
