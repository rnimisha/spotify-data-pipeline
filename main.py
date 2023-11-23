from dotenv import load_dotenv

from scripts.utils.tokens.authorize_user import authorize_user

load_dotenv()

authorization_code = authorize_user()

with open(".env", "a") as env_file:
    env_file.write(f"SPOTIFY_AUTHORIZATION_CODE={authorization_code}\n")

print(f"Your authorization code: {authorization_code}")
