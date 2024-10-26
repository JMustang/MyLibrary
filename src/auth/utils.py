from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"])


def gen_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)
    return hash


def verify_passwd(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)
