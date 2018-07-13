import base64

from Crypto.Cipher import AES


def _add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)  # 返回bytes


def aes_encrypt(key: str, text: str):
    aes = AES.new(_add_to_16(key), AES.MODE_ECB)
    encrypted = str(base64.encodebytes(aes.encrypt(_add_to_16(text))), encoding='utf8').replace(
        '\n', '')  # 加密
    return encrypted


def aes_decrypt(key: str, text: str):
    aes = AES.new(_add_to_16(key), AES.MODE_ECB)
    decrypted = str(
        aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).rstrip(
            b'\0').decode("utf8"))  # 解密
    return decrypted
