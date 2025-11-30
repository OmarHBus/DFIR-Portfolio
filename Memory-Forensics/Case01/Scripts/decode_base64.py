import base64
import sys

def decode_base64(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Error decodificando: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python decode_b64_param.py <cadena_base64>")
        sys.exit(1)

    encoded = sys.argv[1]
    print("\n[+] Cadena Base64:")
    print(encoded)

    print("\n[+] Decodificado:")
    print(decode_base64(encoded))
