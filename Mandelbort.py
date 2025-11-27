import taichi as ti
import time

start = time.time()

arch = None

#try cuda first
if arch is None:
    try:
        arch = ti.cuda
        print("using CUDA/Nvidia card backend")
    except:
        pass

#try OpenGL
if arch is None:
    try:
        arch = ti.opengl
        print("using OpenGL Backend")
    except:
        pass

#try vulkan
if arch is None:
    try:
        arch = ti.vulkan
        print("using Vulkan Backend")
    except:
        pass

#Fallback to CPU 
if arch is None:
        arch = ti.cpu
        print("using cpu backend")

ti.init(arch=arch, default_fp=ti.f64)
from Mandelbort_color import color_map
end = time.time()
print(f"Time elapsed: {end - start} seconds")
# Resolution
W, H = 1000, 1000

pixels = ti.Vector.field(3, dtype=ti.f64 , shape=(W , H))  # RGB now


@ti.kernel
def render(xmin: ti.f64, xmax: ti.f64,
           ymin: ti.f64, ymax: ti.f64,
           max_iter: ti.i32):
    
    for i, j in pixels:
        #Calculating the value of (C)
        x = xmin + (xmax - xmin) * (i / W)# re
        
        y = ymin + (j / H) * (ymax - ymin) #im

        z_re = 0.0
        z_im = 0.0
        it = 0

        while it < max_iter and z_re * z_re + z_im * z_im <= 4:
            new_re = z_re * z_re - z_im * z_im + x
            new_im = 2 * z_re * z_im + y
            z_re = new_re
            z_im = new_im
            it += 1

        t = it / max_iter
        
        pixels[i, j] = color_map(t)


gui = ti.GUI("Mandelbrot Zoom (float64)", res=(W, H))

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 300

while gui.running:

    for e in gui.get_events():
        if e.key == gui.LMB and e.type == ti.GUI.PRESS:
            mx, my = gui.get_cursor_pos()
            cx = xmin + mx * (xmax - xmin)
            cy = ymin + my * (ymax - ymin)

            dx = (xmax - xmin) * 0.5
            dy = (ymax - ymin) * 0.5

            xmin, xmax = cx - dx /2 , cx + dx /2
            ymin, ymax = cy - dy /2 , cy + dy /2
            max_iter += 25

        if e.key == gui.RMB and e.type == ti.GUI.PRESS:
            mx, my = gui.get_cursor_pos()
            cx = xmin + mx * (xmax - xmin)
            cy = ymin + my * (ymax - ymin)

            dx = (xmax - xmin) * 2.0
            dy = (ymax - ymin) * 2.0

            xmin, xmax = cx - dx / 2, cx + dx / 2
            ymin, ymax = cy - dy / 2, cy + dy / 2
            max_iter = max(50, max_iter - 25)

   
    render(xmin, xmax, ymin, ymax, max_iter)
    gui.set_image(pixels)
    gui.show()




