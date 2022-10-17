import gnupg
from pathlib import Path


PASSWORD_FILE = Path("passwords.enc")

def write_pass(password):
    if PASSWORD_FILE.exists():
        raise Exception("passwords file exists")

    g = gnupg.GPG()

    # Encrypt the passphrase with itself (so that we know if the password is right)
    encrypted_password = g.encrypt(password, symmetric=True, passphrase=password, recipients=None).data.decode('utf-8')

    with PASSWORD_FILE.open("w") as f:
        f.write(encrypted_password)


def check_password(expected):
    with PASSWORD_FILE.open() as f:
        encrypted = f.read()

    g = gnupg.GPG()
    actual = g.decrypt(encrypted, passphrase=expected).data.decode('utf-8')

    if actual != expected:
        raise Exception("Passwords don't match")

def decrypt(master, encrypted):
    check_password(master)
    g = gnupg.GPG()
    actual = g.decrypt(encrypted, passphrase=master).data.decode('utf-8')
    return actual

def encrypt(password, plain):
    g = gnupg.GPG()
    check_password(password)
    encrypted = g.encrypt(plain, symmetric=True, passphrase=password, recipients=None).data.decode('utf-8')
    return encrypted






