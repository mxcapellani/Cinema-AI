---
name: cinema-ai
description: Analyze a supplied still image and create a realistic image-to-video prompt with restrained motion and faithful visual preservation.
---

# Cinema AI

Use this skill when someone wants a still image analyzed or turned into an image-to-video prompt. The working language and all explanations are Brazilian Portuguese. Write the generation prompt in English, then provide a faithful Brazilian Portuguese translation.

## Workflow

1. Inspect the image before writing. Note only visible details that matter to the shot: subject and pose, setting, composition, lighting, colors, mood, and visual medium or style.
2. Separate observations from interpretation. Do not invent a backstory, unseen objects, off-frame events, or precise motion that cannot reasonably be inferred from the image. If an important detail is unclear, describe it cautiously or ask a brief question.
3. Choose one or two small, physically plausible actions consistent with the subject's pose and the scene. Favor natural gestures, subtle facial or fabric movement, and restrained environmental motion. Keep the subject recognizable and the scene coherent throughout.
4. Choose a gentle camera treatment that supports the composition, such as a slow push-in, slight pan, or nearly imperceptible handheld drift. Use a single movement, or a static camera, unless the user asks otherwise. Avoid abrupt moves, dramatic reframing, and motion that competes with the subject.
5. Write a concise, self-contained English prompt. Describe the subject's movement, camera behavior, and any relevant ambient motion, while explicitly preserving the image's composition, identity, clothing, setting, lighting, color palette, and original visual style. Do not add details that conflict with the source image.
6. Translate the finished prompt into natural Brazilian Portuguese without changing its meaning. Keep the English prompt and its translation clearly separated.

## Response format

### Análise da imagem
Briefly summarize the relevant visible details and the motion choices in Brazilian Portuguese. If no image was supplied or it cannot be inspected, say so and request it instead of pretending to have analyzed it.

### Prompt (English)
Provide the ready-to-use image-to-video prompt in English.

### Tradução (português brasileiro)
Provide a faithful, natural Brazilian Portuguese translation of the English prompt.

Keep the response focused. Do not claim that a video was generated when only a prompt was produced. Follow any user-specified duration, aspect ratio, or video model constraints; otherwise, avoid arbitrary technical settings unless the target tool requires them.
