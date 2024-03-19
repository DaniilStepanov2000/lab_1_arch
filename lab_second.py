import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import requests



# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('500x350')

FILENAME = []

HASH_FILE = []


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private_key.txt", 'w') as file:
        file.write(private_key.decode())

    with open("public_key.txt", 'w') as file:
        file.write(public_key.decode())


def generate_hash():
    with open(FILENAME[-1], 'rb') as file:
        hash_data = hashlib.file_digest(file, 'sha256').hexdigest()
        print(hash_data)

    with open(f'{FILENAME[-1]}' + 'hash.txt', 'wb') as file:
        with open("public_key.txt", 'rb') as file_second:
            data = file_second.read()
        private_key = RSA.importKey(data)
        cipher = PKCS1_OAEP.new(private_key)
        cipher_text = cipher.encrypt(hash_data.encode())
        file.write(cipher_text)
    print("Generated hash")


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('word files', '*.docx'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    FILENAME.append(filename[0])


def send_data():
    response = requests.post(
        "http://127.0.0.1:5000/check_file", files={
            "file": (FILENAME[-1], open(FILENAME[-1], 'rb')),
            "public_key": ("public_key.txt", open("private_key.txt", 'rb')),
            "hash_data": (f'{FILENAME[-1]}' + 'hash.txt', open(f'{FILENAME[-1]}' + 'hash.txt', 'rb'))
        }
    )

    showinfo(message=response.content.decode())


def get_public_key():
    response = requests.get(
        "http://127.0.0.1:5000/get_public_key"
    )

    with open("public_key_from_server.txt", "wb") as file:
        file.write(response.content)
    print()


def check():
    response = requests.get(
        "http://127.0.0.1:5000/check"
    )

    with open("new_hash_from.txt", "wb") as file:
        file.write(response.content)

    with open("new_hash_from.txt", "rb") as file:
        hash_ = file.read()
        with open("public_key_from_server.txt", "rb") as file:
            data = file.read()
            key = RSA.importKey(data)
            cipher = PKCS1_OAEP.new(key)
            decrypted_message = cipher.decrypt(hash_).decode()

    with open("../new_message.txt", "rb") as file:
        hash_data = hashlib.file_digest(file, 'sha256').hexdigest()
        print(hash_data)

    if decrypted_message == hash_data:
        message = "message is ok"
    else:
        message = "message is broken"
    showinfo(message=message)


def get_message():
    response = requests.get(
        "http://127.0.0.1:5000/get_message"
    )

    with open("../new_message.txt", "wb") as file:
        file.write(response.content)



open_button = ttk.Button(
    root,
    text='Open File',
    command=select_files
)

generate_hash = ttk.Button(
    root,
    text='Generate hash',
    command=generate_hash
)

generate_keys = ttk.Button(
    root,
    text='Generate keys',
    command=generate_keys
)

send_data = ttk.Button(
    root,
    text='Send data',
    command=send_data
)

get_public_key = ttk.Button(
    root,
    text='Get public key',
    command=get_public_key
)
get_phrase = ttk.Button(
    root,
    text='Check get phrase',
    command=check
)
get_message = ttk.Button(
    root,
    text='Get message',
    command=get_message
)

get_message.pack(expand=True)
get_message.place(x=200, y=80)
get_phrase.pack(expand=True)
get_phrase.place(x=200, y=110)
get_public_key.pack(expand=True)
get_public_key.place(x=200, y=50)
send_data.pack(expand=True)
send_data.place(x=40, y=140)
generate_keys.pack(expand=True)
generate_keys.place(x=40, y=80)
generate_hash.pack(expand=True)
generate_hash.place(x=40, y=110)
open_button.pack(expand=True)
open_button.place(x=40, y=50)

root.mainloop()
