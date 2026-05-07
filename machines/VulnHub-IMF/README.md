# 🚩 VulnHub-IMF

**Estado**: 🛠️ En Progreso | ⚖️ Dificultad: [Nivel]
**IP Objetivo**: 192.168.18.254
**SO**: Linux 

---

## 🎯 Resumen Técnico
*   **Vectores de Ataque**: [Ej. Bypass de WAF, RCE]
*   **Escalada de Privilegios**: [Ej. Buffer Overflow, SUID]
*   **Habilidades Clave**: [Ej. Estabilización de TTY, GDB-Peda]

---

## 📑 Metodología de Resolución

### 1. Reconocimiento (Recon)
> Documentación de puertos y servicios con Nmap
Una vez identificada la IP de la maquina víctima podemos utilizar comandos de reconocimiento con Nmap
Con el comando ```bash nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn 192.168.18.254 -oG Allports ``` obtenemos los puertos abiertos y exportamos el resultado al archivo "Allports" descubriendo que solo existe el puerto 80 abierto lo que significa que se trata de una pagina web. Se aplico el comando de reconocimiento ```bash nmap -sCV -p80 192.168.18.254 -oN target``` el cual nos devolvio la información de que se trata de un servicio http con apache/2.4.18. Por lo que ahora pasaremos a el reconocimiento de la página web.
*   

### 2. Análisis de Vulnerabilidades
> Identificación de fallos y vectores de entrada.
*   

### 3. Explotación
> Ejecución de payloads y obtención de acceso inicial.
*   

### 4. Post-Explotación
> Enumeración interna y escalada de privilegios a Root.
*   

### 5. Reporte y Mitigación
> Propuestas de endurecimiento (Hardening) del sistema.
*   

---

## 📂 Archivos Relacionados
*   **Scripts**: [Enlace a scripts/VulnHub-IMF]
*   **Evidencia**: [Enlace a assets/VulnHub-IMF]
