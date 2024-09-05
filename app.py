# Encrytion and Decryption
from cryptography.fernet import Fernet
from werkzeug.utils import secure_filename
# Fernet is a symmetric encryption method that uses the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode with a 128-bit key for encryption. 
# Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. 
#It also uses the HMAC (Hash-based Message Authentication Code) using SHA256 for verifying the integrity and authenticity of the message. 

#The key used in Fernet is a base64url string of random bytes. 
#It's important to note that while Fernet is secure and suitable for many use cases, it does not provide any form of anonymity or protection against traffic analysis. For sensitive data, additional layers of security may be necessary.
def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# Steganography (Hiding Messages in Images)
import stepic
from PIL import Image

def encode_message(message, img_path):
    img = Image.open(img_path)
    img_with_message = stepic.encode(img, message)
    return img_with_message

def decode_message(img_path):
    img = Image.open(img_path)
    return stepic.decode(img)



# Web App API Endpoints
from flask import Flask, request, send_file , render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    image = request.files['image']

    # Save the uploaded image
    image_path = 'static/' + secure_filename(image.filename)
    image.save(image_path)

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    img_with_message = encode_message(encrypted_message, image_path)

    # Save the image with the encoded message
    encoded_image_path = 'static/output.png'
    img_with_message.save(encoded_image_path)

    # Convert the key to a string
    key_str = key.decode()

    # Render the result template with the key and the image path
    return render_template('result.html', key=key_str, image_path=encoded_image_path)

@app.route('/receive', methods=['POST'])
def receive():
    img_path = request.files['image'].save('received.png')
    encrypted_message = decode_message('received.png')
    key = request.form['key']
    message = decrypt_message(encrypted_message, key)
    return message


# Authentication Logic

# Importing the required libraries
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

# Load the environment variables from the .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Create the Flask app   
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# Configure the OAuth provider
oauth = OAuth(app)

# Register the Auth0 provider
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

# Login Route
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

# Callback Route
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

# Logout Route
@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("index", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


