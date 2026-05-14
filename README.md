# Mi primer repositorio

Nombre: Andres Gutierrez

Desarrollador de Software

Especializado en Backend

🚀 MicroJobs Local

Una plataforma web inspirada en servicios freelance como Workana o Fiverr, enfocada en conectar personas que necesitan ayuda con tareas rápidas y trabajadores locales disponibles.

✨ Características
🔐 Autenticación de usuarios
💼 Publicación de trabajos
🔎 Exploración de ofertas laborales
📄 Vista detallada de cada trabajo
📨 Sistema de postulaciones
💬 Chat entre cliente y trabajador
🗄️ Backend con FastAPI + PostgreSQL
⚡ Frontend moderno con React + Vite + TailwindCSS

🛠️ Tecnologías utilizadas

Frontend
⚛️ React
⚡ Vite
🎨 TailwindCSS
🧭 React Router

Backend
🐍 FastAPI
🗃️ PostgreSQL
🔥 SQLAlchemy
🔐 JWT Authentication

# 1. ¿Qué son las Ramas (Branches)?

En Git, una rama es un puntero móvil y ligero hacia uno de los commits (instantáneas del proyecto). Piensa en ella como una línea de tiempo alternativa o un "mundo paralelo" en tu repositorio. La rama por defecto es main (antes conocida como master), que representa la versión estable y principal del código.

# 2. ¿Para qué sirven?

Las ramas permiten a los desarrolladores trabajar en paralelo sin interrumpirse ni afectar la versión estable del proyecto. Sus principales utilidades son:Aislamiento: Crear nuevas características o solucionar errores (bugs) sin dañar el código base funcionando.Colaboración: Múltiples desarrolladores pueden trabajar en diferentes funciones al mismo tiempo.Experimentación: Probar ideas nuevas. Si el experimento falla, la rama se borra sin consecuencias para la rama main.Flujo de trabajo limpio: Solo el código revisado y probado se une a la rama principal (fusionar/merge).

3. ¿Cómo las usaremos en nuestro proyecto?

Adoptaremos un modelo de GitHub Flow, caracterizado por ser sencillo y rápido, ideal para equipos pequeños.Rama Principal (main):Siempre contiene código listo para producción y estable.Prohibido hacer cambios directamente en ella.Ramas de Características (feature):Para desarrollar una nueva funcionalidad, crearemos una rama nueva a partir de main.