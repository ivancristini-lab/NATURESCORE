# IMÁGENES — Guía de reemplazo

Las 16 imágenes en `assets/images/` y el OG en `assets/og/` son **placeholders generados programáticamente** que ya respetan la paleta y dirección visual del brief. Sirven para demo y se pueden mantener si no llegás a generar las definitivas.

Para reemplazarlas con IA (Midjourney, Flux, DALL-E, Stable Diffusion, Sora, etc.):

1. **Mantené los nombres exactos** y la dimensión (`imagen1.jpg`, 1200×1500, etc.). El HTML las referencia por nombre.
2. **Exportá siempre `.jpg`** (no `.png`, no `.webp` — para no romper Open Graph en algunos clientes y mantener el peso bajo).
3. **Quality 85-90** está bien. Las actuales pesan entre 150-400 KB cada una.
4. Commit y push. Vercel redeploya solo.

---

## Dirección visual transversal (válida para todas)

Estos elementos son los que mantienen la pieza coherente. Si los modificás, modificalos en TODAS o en NINGUNA, nunca en algunas:

- **Paleta**: void `#040404` (negro casi puro, dominante), bone `#F0EBE1` (hueso/crema, NO blanco puro), earth `#C4A882` (tierra), moss `#4A7C59` (musgo, dosificado), blood `#5A1810` (sangre oscura, usar como acento crítico).
- **Textura**: grain analógico siempre presente (~6-12% noise). Las imágenes nunca son perfectamente limpias.
- **Viñeta**: oscurecimiento radial en los bordes. La luz nace del centro o del costado, nunca uniforme.
- **Tipografía in-image**: si agregás texto encima (códigos de catálogo, labels), usar mono o sans muy contenida (DM Mono / IBM Plex Mono / similar). Tamaño pequeño, espaciado generoso, en `#F0EBE1` al 50-65% de opacidad. Esquina superior izq/der + esquina inferior izq/der.
- **Lo que NO**: no neón cyberpunk, no glassmorphism, no people in business clothes, no logos corporativos modernos, no íconos de yoga/lotus/hojas vectoriales, no fondos blancos ni grises claros.
- **Sensación**: ficha de espécimen de museo + radiografía vieja + cuaderno de campo manchado.

---

## Prompt base reutilizable

> Vintage scientific specimen catalog photograph, analog film grain, deep vignette, near-black background `#040404`, bone-cream `#F0EBE1` highlights, earth-tone `#C4A882` mids, sparse moss-green `#4A7C59` accents, dramatic side lighting, 1970s laboratory aesthetic, polygraph / oscilloscope / herbarium reference, NOT cyberpunk, NOT neon, NOT futuristic, slightly unsettling, museum specimen card, **[ESCENA ESPECÍFICA AQUÍ]**, shot on Hasselblad, push-processed Kodak Portra, ultra-detailed texture, asymmetric composition.

Pegale eso adelante de cada prompt específico abajo.

---

## imagen1.jpg — HERO (Pantalla A "intro")

- **Dimensión**: 1200×1500 px (4:5 vertical)
- **Rol narrativo**: la primera imagen que ve el usuario. Tiene que generar la pausa antes de tocar "Iniciar". No es decorativa, es ominosa.

**Prompt**:
> Vertical composition. A dense forest of bare birch trees photographed at twilight, trees as straight black verticals against deep void, faint bone-colored mist between trunks. Asymmetric — most trees clustered toward right side, leaving negative space on left. No path visible. No human. Ground in deep shadow. The forest feels observed, like CCTV footage of a place that does not allow humans. Subtle moss-green tint only in deepest shadows. Film grain heavy.

**Variantes alternativas si querés probar**:
- Una raíz arrancada del suelo, vista desde arriba, sobre fondo negro, iluminada lateralmente como prueba forense.
- Un torso humano en sombra parcial, fragmentado por una rejilla de luz que entra por una persiana.

---

## imagen2.jpg — WARNING (Pantalla B "lo que vas a leer")

- **Dimensión**: 900×900 px (1:1 cuadrado)
- **Rol narrativo**: la última imagen antes del consentimiento. Tiene que sentirse como una pausa, un "respiro antes de la prueba".

**Prompt**:
> Extreme close-up of a closed human eye, eyelashes detailed, skin texture visible (pores, fine wrinkles), bone-cream lighting from the side, deep shadow on the other half of the face. The eye is closed not in sleep but in the moment before something difficult. Asymmetric crop — eye placed at upper-right third, lower-left is just dark skin and shadow. No makeup. No filter. Could be any age, any gender. Specimen card aesthetic. The image should feel like a moment of internal honesty, not romantic.

---

## imagen3.jpg — Q1 NATURALEZA (tacto con tierra)

- **Dimensión**: 1400×600 px (21:9 panorámica)
- **Pregunta**: "¿Cuándo fue la última vez que tocaste tierra, pasto o corteza con las manos? No por accidente."

**Prompt**:
> Panoramic horizontal composition. Two adult hands emerging from the right side of the frame, palms down, fingers spread into wet dark soil. The soil is rich, almost black, with visible texture (small roots, particles, organic matter). Hands are slightly dirty, fingernails have earth under them. The rest of the frame is the soil itself, extending into shadow on the left. Lit from above-right, like a scientific examination. No tools, no plants in frame. Just hands and earth. Bone-cream skin tones, earth-brown soil, almost no other color.

---

## imagen4.jpg — Q2 SILENCIO

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: "¿Cuánto tiempo aguantás en silencio total, sin pantalla, sin auriculares, sin libro? Solo vos."

**Prompt**:
> Panoramic. Empty room interior shot from one corner toward the opposite empty wall. Bare walls, no furniture except a single wooden chair in the middle distance, slightly off-center to the right. Light comes from a window outside the frame (left side), casting a long diagonal of bone-cream light onto the floor. The rest of the room is in deep shadow. Wooden floor, scratched, old. The room feels like a place where someone was supposed to sit and didn't, or sat and left. Faint motes of dust in the light beam. Absolutely no decoration.

---

## imagen5.jpg — Q3 ATENCIÓN (pantalla vs entorno)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: "¿Cuántas veces hoy miraste el celular sin saber por qué?"

**Prompt**:
> Panoramic. Silhouette of a human head and shoulders in profile (right side of frame), only the silhouette visible — pure black against a slightly less black background. Where the eye would be, there is the cold pale light of a phone screen reflecting on the face — a sliver of bone-cream light cutting across the cheekbone. The rest of the body and the entire left side of the frame is total darkness. No phone visible in frame, only its reflection. The composition should feel like a forensic photograph of compulsion, not a lifestyle shot.

---

## imagen6.jpg — Q4 INTEROCEPCIÓN (qué siente tu cuerpo)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: "Cerrá los ojos diez segundos. ¿Qué siente tu cuerpo ahora?"

**Prompt**:
> Panoramic. A human face emerging from deep shadow, eyes closed, head slightly tilted up, mouth in neutral position (not smiling, not tense). The face occupies the left third of the frame. The lighting is from below, very soft, bone-cream warm — like the face is its own dim light source. The rest of the frame fades into pure black. No hair styling, no makeup, no clothing visible. The face should feel like it's listening inward, not posing. Skin texture detailed, age neutral.

---

## imagen7.jpg — Q5 ORIENTACIÓN (mapa interno del mundo)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: "¿Hacia qué punto cardinal estás mirando ahora mismo?"

**Prompt**:
> Panoramic. Aerial night view of a city grid, photographed from very high altitude — like a satellite or aircraft. The grid of streets is visible as faint amber-earth lines against pure black. No labels, no compass, no recognizable landmarks. The composition is slightly rotated, off-axis, disorienting. A single brighter cluster of lights in the lower-left, like a downtown core, but no name. The image should make you realize you can't tell which direction is north. Heavy film grain. No text overlay.

---

## imagen8.jpg — Q6 ABURRIMIENTO (capacidad de no hacer nada)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: "¿Cuándo fue la última vez que te aburriste? Aburrimiento real, sin distraerte."

**Prompt**:
> Panoramic. A waning moon high in the upper-right of the frame, the rest of the sky is deep void-black with very faint stars (almost invisible). The lower third of the frame shows the silhouettes of bare branches reaching up from the bottom, like fingers. Between branches and moon, just empty sky. The image should feel like the moment you realize you've been looking at the sky for ten minutes and your mind didn't run away. Cool tones, bone-cream moon, almost no other color. Could be 1960s astronomy plate.

---

## imagen9.jpg — Q7 TACTO (la piel como sensor)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: Slider de 0 a 10 — "¿Cuánto registra tu piel hoy?"

**Prompt**:
> Panoramic abstract. Concentric arcs of bone-cream and earth-tone radiating from a single point in the right third of the frame — like ripples on dark water seen from below, or the cross-section of a tree, or a fingerprint. The lines are not perfect circles, they tremble slightly, organic. The center point glows faintly. The left half of the frame fades into pure black. The image should feel like a tactile sensation made visible. Slight moss-green tint in the outermost rings.

---

## imagen10.jpg — Q8 INTUICIÓN (escuchar antes de razonar)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: Toggle de 3 opciones — "Cuando algo te da mala espina antes de saber por qué, ¿qué hacés?"

**Prompt**:
> Panoramic. The silhouette of a child (back to camera, lower-left of frame) standing at the edge of a dark treeline, facing into the forest. The child is small in the frame, the forest is huge and tall. Faint bone-cream light comes through the canopy from very far away, almost not reaching the ground. The composition should feel like the moment of deciding whether to step in. No fairytale, no fantasy — closer to a missing-child poster aesthetic. Earth and void tones only.

---

## imagen11.jpg — Q9 VOZ PROPIA (texto libre)

- **Dimensión**: 1400×600 px (21:9)
- **Pregunta**: Input de texto — "Cuando tomaste una decisión importante este año, ¿qué te lo confirmó?"

**Prompt**:
> Panoramic. A hand (right side of frame, fingers visible from the wrist down) writing with a pen in a worn notebook on a dark wooden surface. The notebook page is bone-cream, slightly yellowed, with faint ruled lines. The pen is old, metal, no logo. The writing on the page is unreadable, just suggested by ink strokes. Light comes from the upper-left at a low angle, casting long shadow from the hand. The left half of the frame is the dark wood surface with faint texture, almost empty. No coffee cup, no laptop, no phone. Just the act of writing.

---

## imagen12.jpg — ESPECIE: Homo Algorithmicus (score 0-20)

- **Dimensión**: 1600×700 px (16:7)
- **Diagnóstico**: "Señal Apagada" — el sistema te lee, vos no.

**Prompt**:
> Wide horizontal. A flat horizontal line stretching across the entire frame, like an EKG flatline. The line is faint bone-cream, slightly trembling but with no rhythm — random noise, no signal. Above and below the line, total void-black. To the right side, a single small dot of blood-red `#5A1810`, like a warning indicator that has stopped mattering. The composition should feel medical, terminal. No human, no nature, just the failed signal. Faint grid behind the line, like polygraph paper.

---

## imagen13.jpg — ESPECIE: Homo Comfortis (score 21-40)

- **Dimensión**: 1600×700 px (16:7)
- **Diagnóstico**: "Conexión Intermitente" — vivís cómodo, no del todo presente.

**Prompt**:
> Wide horizontal. A horizontal signal line across the frame, but with frequent dropouts — sections where the line breaks into dashes, then comes back, then breaks again. The signal is bone-cream against void. Some peaks try to rise but get cut off. The overall feeling is of something that turns on and off, never sustained. Earth-tone tint in the broken sections. Polygraph paper grid behind, faded.

---

## imagen14.jpg — ESPECIE: Homo Sapiens Fragmentado (score 41-60)

- **Dimensión**: 1600×700 px (16:7)
- **Diagnóstico**: "Reconexión Parcial" — sentís a ratos, en intervalos.

**Prompt**:
> Wide horizontal. A wavy signal line across the frame, with real peaks and valleys — but the wave is irregular, asymmetric, sometimes strong, sometimes weak. Some peaks tall, some barely visible. Bone-cream line on void background. Faint moss-green appears where the peaks are strongest, faint earth-tone where they're weakest. The signal is alive but uneven. Polygraph paper grid, more visible than imagen13.

---

## imagen15.jpg — ESPECIE: Homo Sensorialis (score 61-80)

- **Dimensión**: 1600×700 px (16:7)
- **Diagnóstico**: "Conexión Activa" — el cuerpo te llega clara.

**Prompt**:
> Wide horizontal. A strong, rhythmic signal line — regular peaks, consistent amplitude, like a healthy heartbeat or a steady oscilloscope wave. Bone-cream main line, with a moss-green secondary line shadowing it slightly offset. The image should feel calm, steady, ALIVE. Polygraph paper grid clearly visible. The signal extends off both edges of the frame, continuous.

---

## imagen16.jpg — ESPECIE: Homo Sensorius (score 81-100)

- **Dimensión**: 1600×700 px (16:7)
- **Diagnóstico**: "Plena Conexión" — anomalía estadística. El sistema no esperaba tu lectura.

**Prompt**:
> Wide horizontal. A complex composite signal across the frame: a main bone-cream wave, a moss-green wave below it, and a subtle earth-tone wave above — three layers harmonizing. From the main wave, small organic branches emerge upward and downward, like roots or veins, suggesting the signal is no longer just electrical but biological, growing. The image should feel anomalous, beautiful, slightly unnerving — like a measurement that shouldn't be possible. Polygraph grid present but partly overgrown.

---

## og-image.jpg — OPEN GRAPH (compartir en redes)

- **Dimensión**: 1200×630 px (1.91:1)
- **Aparece cuando alguien comparte el link**.

**Prompt**:
> Wide horizontal social card. Centered: the text "NatureScore™" in elegant serif (Playfair Display style), in bone-cream, very large. Below it, smaller mono text: "HUMAN RECONNECTION INDEX". Below that, even smaller: "15 sensores · 8 señales · 1 diagnóstico". Background: deep void-black with a subtle livingSignal wave running horizontally behind the text, faint bone-cream and moss-green. Corners have specimen-card labels: "NS · CAT. 0417" top-left, "MMXXVI" top-right. Heavy film grain.

(Si lo generás en otra herramienta, alternativa: hacelo en Figma con la paleta y exportá a JPG 85% quality.)

---

## Si querés mantener consistencia entre todas

El truco no es generar una imagen perfecta — es generar las 16 con el **mismo seed/prompt base** y solo cambiar la escena específica. Eso mantiene la coherencia visual.

En Midjourney: usá `--sref` con un mood-board común y `--style raw`.
En Flux: pasá la primera imagen como reference para las siguientes.

Si una imagen no sale como esperabas pero respeta la paleta y el tono, dejala. La incomodidad visual a veces viene de imperfecciones.
