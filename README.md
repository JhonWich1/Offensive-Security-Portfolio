# 🔴 Offensive-Security-Portfolio

Este repositorio es un laboratorio documentado de **Seguridad Ofensiva**. Su objetivo es registrar el proceso de identificación, explotación y análisis de vulnerabilidades en entornos controlados, sirviendo como bitácora técnica para mi preparación hacia las certificaciones **eJPTv2** y **eCPPTv2**.

---

## 🎯 Objetivos del Repositorio
*   **Documentación Técnica**: Crear *writeups* detallados que sirvan como referencia de explotación y post-explotación.
*   **Desarrollo de Exploits**: Almacenar scripts personalizados (Python, Bash, C) para automatizar fases del Pentesting.
*   **Análisis de Vulnerabilidades**: Estudiar fallos comunes (OWASP Top 10) y vectores de ataque complejos como **Buffer Overflows**.
*   **Mentalidad de Consultor**: No solo explotar, sino proponer medidas de mitigación y *hardening* para cada hallazgo.

---

## 📂 Estructura y Flujo de Trabajo

| Directorio | Contenido | Finalidad |
| :--- | :--- | :--- |
| **`/vulnhub`** | Writeups de máquinas (ej. **IMF**) | Documentar el paso a paso de la resolución. |
| **`/scripts`** | Exploits y herramientas de automatización | Almacenar código como scripts de Port Knocking o Fuzzers. |
| **`/methodologies`** | Guías de procesos (Cheatsheets) | Estandarizar mi flujo de trabajo en enumeración y escalada. |
| **`/assets`** | Capturas de pantalla y evidencia | Respaldar técnicamente los hallazgos documentados. |

---

## 📑 Metodología de Operación
Para cada reto, sigo un ciclo de vida de Pentesting estructurado:

1.  **Reconocimiento (Recon)**: Escaneo de puertos y servicios con Nmap, enumeración de directorios y OSINT básico.
2.  **Análisis de Vulnerabilidades**: Identificación de puntos de entrada, desde fallos web (RCE, LFI/RFI) hasta servicios desactualizados.
3.  **Explotación**: Obtención de acceso inicial mediante el desarrollo o adaptación de payloads y exploits.
4.  **Post-Explotación**: Estabilización de la shell (TTY), enumeración interna y escalada de privilegios a Root.
5.  **Reporte y Mitigación**: Documentación del ataque y propuesta de endurecimiento del sistema (Hardening).

---

## 🛠️ Entorno de Trabajo
Mi laboratorio ofensivo está optimizado para la eficiencia en la terminal:
*   **Sistema Operativo**: Parrot Security OS.
*   **Editor de Código**: Neovim (LazyVim / NvChad) para edición rápida de scripts y writeups.
*   **Terminal**: Kitty con bspwm para gestión avanzada de ventanas.
*   **Lenguajes**: Python, Bash, JavaScript (Node.js).

---
*Este repositorio es mantenido por **Jhon Nash**. La información aquí contenida es estrictamente para fines educativos y de entrenamiento en ciberseguridad.*
