# PREREQUIS - Pour faciliter l'exploitation, on désactive l'ASLR sur le système
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Executer le programme
./bof32 <input>

# Debugguer le programme dans GDB
gdb ./bof32
run <input>

# Notes
Le programme a été compilé avec la ligne de commande suivante : gcc -o bof32 -fno-stack-protector -z execstack -no-pie -m32 source.c
