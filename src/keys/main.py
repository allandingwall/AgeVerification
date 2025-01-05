from cryptography.hazmat.primitives.asymmetric import ec

def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP521R1())
    public_key = private_key.public_key()
    return private_key, public_key

generate_key_pair()