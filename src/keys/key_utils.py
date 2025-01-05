import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_ec_key_pair():
    # Generates an elliptic curve private and public key pair.
    private_key = ec.generate_private_key(ec.SECP521R1())
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_key_pair_to_pem(private_key, public_key):
    # Serializes EC key pair to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_key_pem, public_key_pem

def pem_to_base64(pem_data):
    return base64.b64encode(pem_data).decode('utf-8')

def base64_to_pem(base64_data):
    return base64.b64decode(base64_data).decode('utf-8')

def privatepem_to_private_key(pem_data):
    return serialization.load_pem_private_key(
        pem_data.encode('utf-8'),
        password=None
    )

def publicpem_to_public_key(pem_data):
    return serialization.load_pem_public_key(
        pem_data.encode('utf-8')
    )

if __name__ == "__main__":
    # Generate key pair
    private_key, public_key = generate_ec_key_pair()

    # Serialize to PEM
    private_key_pem, public_key_pem = serialize_key_pair_to_pem(private_key, public_key)
    print("Private Key PEM:\n", private_key_pem.decode('utf-8'))
    print("Public Key PEM:\n", public_key_pem.decode('utf-8'))

    # Convert PEM to Base64 for database storage
    private_key_base64 = pem_to_base64(private_key_pem)
    public_key_base64 = pem_to_base64(public_key_pem)
    print("Private Key Base64:\n", private_key_base64)
    print("Public Key Base64:\n", public_key_base64)

    # Convert Base64 back to PEM
    restored_private_pem = base64_to_pem(private_key_base64)
    restored_public_pem = base64_to_pem(public_key_base64)
    print("Restored Private Key PEM:\n", restored_private_pem)
    print("Restored Public Key PEM:\n", restored_public_pem)

    # Convert PEM back to key objects
    restored_private_key = privatepem_to_private_key(restored_private_pem)
    restored_public_key = publicpem_to_public_key(restored_public_pem)
    print("Restored Private Key Object:", restored_private_key)
    print("Restored Public Key Object:", restored_public_key)