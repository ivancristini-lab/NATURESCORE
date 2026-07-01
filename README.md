# NatureScore™

> *No mide inteligencia. Mide cuánta señal humana te queda.*

**Human Reconnection Index** — experiencia web ficticia, distópica y cercana para medir presencia cotidiana: cuerpo, silencio, atención, naturaleza, tacto y hábitos automáticos.

Esta versión está optimizada para evento: arranca rápido, no pide registro y evita fricción antes del test.

---

## Qué cambió en esta versión

- **Arranque directo:** una sola pantalla inicial y botón **Empezar lectura**. Ya no hay tres validaciones antes de empezar.
- **Preguntas más cercanas:** despertar, caminar, esperar, comer, barrio, ansiedad, tacto y noche.
- **Menos formulario, más espejo:** todas las preguntas principales son cards simples, sin sliders raros.
- **Imágenes más fáciles de reemplazar:** los archivos usados por la app tienen nombres semánticos (`hero.jpg`, `q01-despertar.jpg`, etc.). No hay dimensión obligatoria.
- **El diseño sigue siendo NatureScore:** oscuro, editorial, místico-corporativo, con livingSignal y modo sala.

---

## Flujo actual

1. **Inicio directo** — NatureScore explica en una frase qué hace y empieza.
2. **8 señales cotidianas** — preguntas simples, reconocibles, rápidas.
3. **Pregunta abierta opcional** — una frase del cuerpo.
4. **Procesamiento** — lectura visual tipo diagnóstico.
5. **Resultado individual** — score, estado de señal, especie, diagnóstico, sensor dominante/crítico.
6. **Modo sala** — lectura colectiva simulada para proyectar.

---

## Stack

Vanilla puro. Nada que compilar.

- `index.html` contiene HTML + CSS + JS.
- No usa framework.
- No usa backend.
- Funciona local o en Vercel/Netlify/GitHub Pages.

---

## Correr localmente

```bash
# opción directa
open index.html

# opción servidor local
python3 -m http.server 8000
# abrir http://localhost:8000
```

---

## Deploy rápido

### Vercel

Subí el repo a GitHub y conectalo desde Vercel. El `vercel.json` ya está incluido.

### GitHub Pages

También puede correr como sitio estático. Publicá la raíz del repo o la carpeta que contiene `index.html`.

---

## Reemplazar imágenes

La app usa archivos con nombres semánticos en:

```text
assets/images/
```

Podés reemplazarlos por imágenes nuevas manteniendo el mismo nombre. No hay medida obligatoria: la interfaz recorta y adapta con `object-fit: cover`.

También podés cambiar extensiones o nombres editando el objeto `IMG` dentro de `index.html`.

Leé la guía completa en:

```text
assets/images/README.md
```

---

## Modo presentador

Sirve para proyectar una lectura colectiva de sala.

Cómo abrirlo:

- Tap en **Modo sala** desde la pantalla inicial.
- Triple tap en `v1.1 — COTIDIANA`.
- Tap en `· · ·` desde el resultado.

La data es simulada y no requiere backend. Eso está bien para demo escénica: la webapp no intenta ser un sistema clínico real, sino una experiencia Black Mirror.

---

## Estructura

```text
naturescore/
├── index.html
├── README.md
├── IMAGENES.md
├── LICENSE
├── vercel.json
├── docs/
│   ├── brief-disenador-senior.md
│   └── guion-storytelling.md
├── assets/
│   ├── images/
│   │   ├── README.md
│   │   ├── hero.jpg
│   │   ├── q01-despertar.jpg
│   │   ├── q02-caminar.jpg
│   │   ├── q03-espera.jpg
│   │   ├── q04-mesa.jpg
│   │   ├── q05-barrio-verde.jpg
│   │   ├── q06-ansiedad.jpg
│   │   ├── q07-tacto.jpg
│   │   ├── q08-noche.jpg
│   │   ├── q09-voz-propia.jpg
│   │   ├── result-01-senal-apagada.jpg
│   │   ├── result-02-conexion-intermitente.jpg
│   │   ├── result-03-reconexion-parcial.jpg
│   │   ├── result-04-conexion-activa.jpg
│   │   └── result-05-homo-sensorius.jpg
│   └── og/
│       └── og-image.jpg
└── scripts/
    └── README.md
```

---

## QA antes de subir

- [ ] Abrir `index.html` y tocar **Empezar lectura**.
- [ ] Completar las 8 preguntas + texto opcional.
- [ ] Verificar que aparece resultado.
- [ ] Probar botón **Compartir resultado**.
- [ ] Probar **Modo sala**.
- [ ] Revisar en celular real.
- [ ] Confirmar que todas las imágenes cargan.

---

## Tono que hay que cuidar

No wellness. No yoga app. No motivación vacía.

NatureScore tiene que sentirse como una lectura incómoda pero cercana: lo cotidiano mostrando algo más profundo.

*v1.1 — cotidiana*
