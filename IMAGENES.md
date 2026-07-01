# Imágenes NatureScore — guía simple de reemplazo

La app ya no depende de `imagen1.jpg`, `imagen2.jpg`, etc. Ahora usa nombres semánticos para que sea más fácil trabajar.

No hay dimensión obligatoria. Usá la proporción que tengas. La interfaz adapta el encuadre.

## Archivos usados por la app

| Archivo | Uso narrativo |
|---|---|
| `hero.jpg` | Primera impresión / entrada a la lectura |
| `q01-despertar.jpg` | Despertar / primer gesto del día |
| `q02-caminar.jpg` | Caminar sin estímulo |
| `q03-espera.jpg` | Fila, espera, aburrimiento |
| `q04-mesa.jpg` | Comida, presencia, celular en la mesa |
| `q05-barrio-verde.jpg` | Naturaleza cercana / barrio |
| `q06-ansiedad.jpg` | Cuerpo, tensión, ansiedad |
| `q07-tacto.jpg` | Tocar algo real con atención |
| `q08-noche.jpg` | Cierre del día / pantalla antes de dormir |
| `q09-voz-propia.jpg` | Pregunta abierta / voz del cuerpo |
| `result-01-senal-apagada.jpg` | Resultado 0–20 |
| `result-02-conexion-intermitente.jpg` | Resultado 21–40 |
| `result-03-reconexion-parcial.jpg` | Resultado 41–60 |
| `result-04-conexion-activa.jpg` | Resultado 61–80 |
| `result-05-homo-sensorius.jpg` | Resultado 81–100 |

## Cómo reemplazar

1. Exportá la imagen nueva como `.jpg`, `.png` o `.webp`.
2. Si mantenés el mismo nombre exacto, no tocás código.
3. Si cambiás el nombre o la extensión, editá el objeto `IMG` en `index.html`.
4. Subí a GitHub y redeploy.

## Dirección visual recomendada

La app acepta estilos distintos, pero conviene que cada imagen sostenga el viaje:

1. **Humano saturado** — pantallas, cansancio, ruido, notificaciones.
2. **Caminar / silencio** — calle, auriculares, pausa, ciudad.
3. **Espera** — fila, ascensor, asiento, mano que busca el celular.
4. **Mesa** — comida, conversación, celular presente o ausente.
5. **Barrio vivo** — árbol, vereda, pájaro, planta, detalle cercano.
6. **Cuerpo** — respiración, pecho, manos, tensión, sombra.
7. **Tacto** — madera, tierra, agua, tela, cocina, herramienta.
8. **Noche** — cama, luz azul, ventana, silencio.
9. **Voz propia** — cuaderno, mano escribiendo, rostro quieto.
10. **Resultados** — señal, cuerpo, escaneo, raíces, diagnóstico.

## Qué evitar

- imágenes wellness genéricas
- yoga/loto/hojas vectoriales
- neón cyberpunk exagerado
- texto grande dentro de la imagen
- fotos demasiado felices o publicitarias
- estética infantil

## Prompt base opcional

> Cinematic editorial image, dark premium mood, human reconnection, ordinary daily scene, subtle dystopian undertone, deep black shadows, bone-cream highlights, earth tones, slight film grain, no big text, no wellness cliché, no cyberpunk neon, realistic and emotionally close.

