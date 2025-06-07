# PREREQUIS - Pour faciliter l'exploitation, on désactive l'ASLR sur le système
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Consignes
Un code d'exploitation (exploit.py) vous a été fourni, il s'agit de le compléter avec les bonnes valeurs.
Le plan est le suivant :
- Injecter des "NOP" (\x90) suivi du shellcode
- Compléter le padding si nécessaire jusqu'à atteindre RIP
- Ecraser RIP avec une adresse mémoire au milieu des NOP

# Notes
Le programme a été compilé avec la ligne de commande suivante : gcc -fno-stack-protector -z execstack -no-pie -std=c99 source.c -o bof64_2
