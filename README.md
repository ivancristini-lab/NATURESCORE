# NatureScore™

> *"Esto no mide cuánto sabés. Mide cuánta conexión te queda."*

**Human Reconnection Index** — Una empresa ficticia distópica que mide tu nivel de conexión sensorial con el mundo no-mediado. Pieza interactiva creada para un anti-hackathon estilo Black Mirror.

No es wellness. No es evolución. Es un diagnóstico.

---

## Qué es

Una experiencia web single-page que corre en el celular de cada participante. Estructura:

- **Apertura** — instalación de la premisa (la sala en silencio, vos hablando, el cuento de 90 segundos del archivo `docs/guion-storytelling.md`).
- **App en mobile** — 8 preguntas de tipos mixtos (cards, slider, toggle, texto libre, voz interior). Lectura sensorial simulada con animación de 15 sensores → 8 señales activas.
- **Procesamiento** — 5.6 segundos de "lectura corporal" con livingSignal interferida + microtexts secuenciados.
- **Resultado individual** — score 0-100, clasificación en una de 5 especies (Homo Algorithmicus → Homo Sensorius), diagnóstico, frase final, livingSignal personalizada.
- **Modo presentador** — lectura de sala proyectada: especie dominante + score promedio + dos estadísticas críticas. Triple-tap en `v1.0 — DEMO` para abrirlo en vivo.

Pensada para que funcione tanto en el celular del participante como proyectada al frente.

---

## Stack

Vanilla puro. Nada que compilar.

- HTML / CSS / JS en un solo archivo (`index.html`)
- Tipografía: Playfair Display + DM Sans + DM Mono (Google Fonts)
- Sin frameworks, sin build, sin dependencias

Vercel-deployable de un solo clic. Funciona también abriendo `index.html` directo en el navegador.

---

## Correr localmente

```bash
# opción 1: abrir directo
open index.html

# opción 2: servidor local (recomendado para evitar warnings de CORS con las imágenes)
python3 -m http.server 8000
# después → http://localhost:8000
```

---

## Deploy a Vercel

```bash
# desde la raíz del repo
vercel
# o
vercel --prod
```

El `vercel.json` ya está configurado para servir el sitio como estático con headers de cache razonables.

Alternativa: push a GitHub, conectar el repo en vercel.com, y listo.

---

## Las imágenes (importante)

Las 16 imágenes en `assets/images/imagen1.jpg` … `imagen16.jpg` son **placeholders generados** que ya respetan la dirección visual (paleta, viñetas, tipografía catalográfica, grain). Sirven para presentar.

**Para reemplazarlas con imágenes generadas por IA:**

1. Mantené los mismos nombres de archivo (`imagen1.jpg`, `imagen2.jpg`, etc.) y las mismas dimensiones — están referenciadas directamente desde el HTML.
2. Mirá `IMAGENES.md` — tiene el prompt sugerido, la dimensión y el rol narrativo de cada una.
3. Reemplazá los `.jpg` en `assets/images/` y commiteá. No hay que tocar el HTML.

| Archivo | Uso | Dimensión |
|---|---|---|
| `imagen1.jpg` | Hero pantalla A | 1200×1500 (4:5) |
| `imagen2.jpg` | Warning pantalla B | 900×900 (1:1) |
| `imagen3-11.jpg` | Pregunta 1 a 9 | 1400×600 (21:9) |
| `imagen12-16.jpg` | Especies (Algorithmicus → Sensorius) | 1600×700 (16:7) |
| `assets/og/og-image.jpg` | Open Graph | 1200×630 |

Hay un script en `scripts/generate-placeholders.py` para regenerar los placeholders si querés (necesitás `pillow` y `numpy`).

---

## Modo presentador (proyección)

Para usar en la sala mientras la gente termina de responder:

1. Triple-tap en el tag `v1.0 — DEMO` (esquina inferior derecha de la pantalla A).
2. O tap en los tres puntos `· · ·` que aparecen en la esquina de la pantalla de resultado.
3. Aparece un overlay full-screen con el botón **"Revelar lectura de sala"**.
4. Tocás → secuencia de reveal escalonada (la sala fue clasificada como → estado → especie → score → estadísticas).
5. ESC para salir. **"Otra lectura"** para regenerar con otra semilla aleatoria.

La data de sala es generada con seed determinístico — no necesita conexión a nada. Si querés cambiar el tamaño simulado de la audiencia o tunear el sesgo de scores, está en la función `generateRoom()` del JS.

---

## Estructura del repo

```
naturescore/
├── index.html                      # toda la app
├── README.md                       # esto
├── IMAGENES.md                     # prompts y especificaciones de cada imagen
├── LICENSE                         # MIT
├── vercel.json                     # config de deploy
├── .gitignore
├── docs/
│   ├── guion-storytelling.md      # monólogo de apertura (90s)
│   └── brief-disenador-senior.md  # dirección visual
├── scripts/
│   └── generate-placeholders.py   # regenerar imágenes placeholder
└── assets/
    ├── images/
    │   ├── imagen1.jpg … imagen16.jpg
    │   └── ...
    └── og/
        └── og-image.jpg
```

---

## Decisiones de diseño que ya están tomadas

Por si alguien quiere modificar y no romper el tono:

- **No es dark-mode genérico**: el negro es `#040404`, el texto es `#F0EBE1` (hueso, no blanco). El acento "natural" es musgo, no verde lima.
- **La paleta de 5 colores es dogma**: void / bone / earth / moss / blood. Cualquier color nuevo tiene que justificarse.
- **El elemento vivo es la livingSignal SVG**: una señal biológica/raíz que cambia según el score. No es decoración, es el dato. Si la sacás, sacaste el corazón del proyecto.
- **El tono nunca es optimista**. Esto es un diagnóstico, no una promesa de mejora. El copy y los microtexts respetan eso.
- **Mobile-first real**: la pantalla principal está pensada para verticales de ~380px. El presenter mode es la única vista pensada para proyección.

Lo que pidió el brief explícito y se respetó: no neón cyberpunk, no glassmorphism, no íconos de yoga, no flat illustrations de gente meditando.

---

## QA antes del evento

Checklist rápido para correr en la noche:

- [ ] Probar en 2-3 celulares distintos (iOS y Android).
- [ ] Verificar que las fonts cargan (revisar con red lenta — hay fallback a sans-serif del sistema).
- [ ] Verificar el flujo completo: A → B → C → D (9 preguntas) → E → F.
- [ ] Triple-tap admin → presenter → revelar → reseed → cerrar.
- [ ] Compartir resultado (botón compartir usa `navigator.share` con fallback a clipboard).
- [ ] Probar en pantalla de proyección con el navegador en pantalla completa (F11).
- [ ] Confirmar que `prefers-reduced-motion` no rompe nada (sistema operativo con reduced-motion activado).

---

## Créditos y licencia

Concepto, copy y arquitectura: Federico.
Licencia: MIT (ver `LICENSE`).

NatureScore™ es una empresa ficticia. Cualquier parecido con consultoras reales que efectivamente te midan, es coincidencia.

---

*v1.0 — DEMO*
