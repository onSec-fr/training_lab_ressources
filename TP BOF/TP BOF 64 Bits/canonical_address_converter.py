import sys

def is_canonical(address):
    """
    Vérifie si l'adresse est déjà canonique.
    """
    # Bits 48-63 doivent être soit tous 0, soit tous 1
    upper_bits = address >> 48
    return upper_bits == 0x0 or upper_bits == 0xFFFF

def canonicalize(address):
    """
    Canonicalise une adresse non canonique en appliquant le bit de signe (bit 47).
    """
    if is_canonical(address):
        return address
    # Appliquer l'extension du bit 47
    return (address & 0xFFFFFFFFFFFF) | (0xFFFF << 48 if address & (1 << 47) else 0x0)

def main():
    # Vérifier si une adresse a été fournie en argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <adresse_hex>")
        return
    
    try:
        # Convertir l'argument en entier (base 16)
        address = int(sys.argv[1], 16)
    except ValueError:
        print("Erreur : Veuillez fournir une adresse hexadécimale valide.")
        return

    # Vérification et canonicalisation
    if is_canonical(address):
        print(f"L'adresse {hex(address)} est déjà canonique.")
    else:
        canonical_address = canonicalize(address)
        print(f"L'adresse {hex(address)} n'est pas canonique.")
        print(f"Adresse canonique : {hex(canonical_address)}")

if __name__ == "__main__":
    main()
