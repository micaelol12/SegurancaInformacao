import jks
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

JKS_PATH = "Atividade9/repositorio.jks" 
JKS_PASSWORD = "furb2025"     
FURB_CERT_ALIAS = "*.furb.br (rnp icpedu ov ssl ca 2019)" 


def show_certificates_info():
    keystore = jks.KeyStore.load(JKS_PATH, JKS_PASSWORD)

    for alias, cert in keystore.certs.items():
        print("\n==============================")
        print(f"Alias: {alias}")
        print("==============================")

        cert_obj = x509.load_der_x509_certificate(cert.cert, default_backend())

        print("a) Proprietário (Subject):")
        print("   ", cert_obj.subject)

        print("b) Emissor (Issuer):")
        print("   ", cert_obj.issuer)

        print("c) Autoassinado?: ", "SIM" if cert_obj.subject == cert_obj.issuer else "NÃO")

        print("d) Período de validade:")
        print("   Não válido antes de:", cert_obj.not_valid_before)
        print("   Não valido depois de:", cert_obj.not_valid_after)

    print("\nFinalizado.")

def cipher_key():
    keystore = jks.KeyStore.load(JKS_PATH, JKS_PASSWORD)
    cert_der = keystore.certs[FURB_CERT_ALIAS].cert
    cert_obj = x509.load_der_x509_certificate(cert_der, default_backend())
    public_key = cert_obj.public_key()
    aes_key = b"A" * 16     

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("key.aes", "wb") as f:
        f.write(encrypted_key)
