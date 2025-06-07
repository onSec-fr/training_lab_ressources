# PREREQUIS - Pour faciliter l'exploitation, on désactive l'ASLR sur le système
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Executer le programme
./bof64 <input>

# Debugguer le programme dans GDB
gdb ./bof64
run <input>

# Utilitaires
"getenvar" vous permet d'identifier la référence mémoire d'une variable d'environnement au sein d'un programme
Exemple : ./getenvvar <environment variable> <target program name>
"canonical_address_converter" vous permet de vérifier si une addresse mémoire est bien dans l'adressage autorisé de 48 bits, et effectue la conversion si nécessaire.
Exemple : python3 canonical_address_converter.py <addresse_memoire>

# Notes
Le programme a été compilé avec la ligne de commande suivante : gcc -o bof64 -fno-stack-protector -z execstack -no-pie -m64 source.c
Le binaire possède l'attribut SUID est son propriétaire est root :
$sudo chown root:root bof64
$sudo chmod u+s bof64
