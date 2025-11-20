import jks
from cryptography import x509
from cryptography.hazmat.backends import default_backend

JKS_PATH = "Atividade9/repositorio.jks" 
JKS_PASSWORD = "furb2025"     

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
