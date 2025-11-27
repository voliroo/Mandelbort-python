# Mandelbrot Fractal Renderer (Taichi – GPU Accelerated)

This project renders and interactively zooms into the Mandelbrot fractal, using Taichi for GPU/CPU acceleration and a custom smooth color-mapping module.
It includes:

⦁	Automatic backend selection (CUDA → OpenGL → Vulkan → CPU)

⦁	Float64 precision rendering

⦁	Smooth 46-color gradient

⦁	Real-time mouse-based zooming

⦁	Modular color system (Mandelbort_color.py).

---

## 🚀 Features

⦁	High performance using Taichi kernels

⦁	GPU acceleration when available

⦁	Dynamic iteration increase when zooming in

⦁	Custom color palette for smooth shading

⦁	Clean, modular structure

---

## 📂 Project Structure
```python
.
├── main.py                # Mandelbrot renderer + GUI zoom
├── Mandelbort_color.py    # Color palette & smooth color interpolation
└── README.md
```
---

## 🖼️ Mandelbrot Rendering

The fractal is rendered by iterating:
```python
z = z*z + c
```

until:

⦁	|z| > 2 → escape

⦁	or max_iter is reached

Then we map:
```pythons

t = it / max_iter
```

into a smooth RGB vector using 46 custom colors.

---

## 🎨 Color Mapping (Mandelbort_color.py)

This file defines:

⦁	A list of 46 hand-crafted RGB colors

⦁	A Taichi field (colors_field[]) storing them 

⦁	A smooth interpolation function:

```python
@ti.func
def color_map(t):
    ...
    c = (1 - f) * colors_field[idx] + f * colors_field[idx_next]
```

This allows continuous gradient coloring based on escape ratio.

---

## 🖱️ Controls
|Action | Dcription |
|------ |-----------|
|Left Click |	Zoom in (2×), increase iterations|
|Right Click |	Zoom out (2×), decrease iterations|
|Esc / Close Window |	Exit|

---

## 🧪 Backend Auto-Detection

The renderer attempts to initialize Taichi in this order:

1. CUDA(NVIDIA)

2. OpenGL

3. Vulkan

4. CPU fallback

This ensures maximum performance on the user's hardware.

---

## 📦 Requirements

Install Taichi:
```bash
pip install taichi
```

Make sure both files are placed in the same directory:

- main.py

- Mandelbort_color.py

## ▶️ Run the Program

Simply run:
```bash
python Mandelbort.py
```

A window titled "Mandelbrot Zoom (float64)" will appear.

---

## 📝 Notes

- Rendering uses float64 precision for high detail.

- Zooming in automatically increases max_iter to reduce artifacts.

- The color list can be easily modified for different styles.

---

If you want, I can also:

✅ Add images/GIFs of the fractal
✅ Improve the README with equations & diagrams
✅ Add installation badges / GitHub formatting
Just tell me!