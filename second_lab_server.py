import hashlib
import json
import random

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/check_file", methods=["GET", "POST"])
def index():
    a = request.files.to_dict()
    data = a["file"].read()
    public_key = a["public_key"].read()
    hash_data_client = a["hash_data"].read()
    with open(a["file"].filename.split('/')[-1], "wb") as file:
        file.write(data)

    with open(a["file"].filename.split('/')[-1], 'rb') as file:
        hash_data = hashlib.file_digest(file, 'sha256').hexdigest()

    with open('server' + a["public_key"].filename.split('/')[-1], "wb") as file:
        file.write(public_key)

    with open('server' + a["public_key"].filename.split('/')[-1], "rb") as file:
        public_key = file.read()
        key = RSA.importKey(public_key)
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(hash_data_client).decode()

    return "File is ok" if hash_data == decrypted_message else "File is broken"


@app.route("/get_public_key", methods=["GET", "POST"])
def get_public_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("srver_public_key.txt", 'w') as file:
        file.write(private_key.decode())

    with open("srver_private_key.txt", 'w') as file:
        file.write(public_key.decode())

    return send_file(
        "srver_public_key.txt",
    )


@app.route("/check", methods=["GET", "POST"])
def check():
    with open("new_message.txt", 'rb') as file:
        hash_data = hashlib.file_digest(file, 'sha256').hexdigest()
        print(f"Hash data: {hash_data}")

    with open("new_message.txt" + 'hash.txt', 'wb') as file:
        with open("srver_private_key.txt", 'rb') as file_second:
            data = file_second.read()
        private_key = RSA.importKey(data)
        cipher = PKCS1_OAEP.new(private_key)
        cipher_text = cipher.encrypt(hash_data.encode())
        file.write(cipher_text)

    return send_file(
        "new_message.txt" + 'hash.txt',
    )


@app.route("/get_message", methods=["GET", "POST"])
def get_message():
    random_message = str(random.randint(0, 10 ** 3))
    print(f"Generated random message: {random_message}")
    with open("new_message.txt", "w") as file:
        file.write(random_message)
    return send_file(
        "new_message.txt",
    )


if __name__ == "__main__":
    app.run()
