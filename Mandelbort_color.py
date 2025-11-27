import taichi as ti
colors_field = ti.Vector.field(3 , dtype=ti.f64 , shape = 46)
colors_list = [
    ti.Vector([0.7, 0.35, 0.0]), ti.Vector([0.75, 0.5, 0.0]), ti.Vector([0.8, 0.6, 0.0]), ti.Vector([0.8, 0.65, 0.05]),
    ti.Vector([0.55, 0.0, 0.1]), ti.Vector([0.6, 0.1, 0.15]), ti.Vector([0.35, 0.0, 0.35]), ti.Vector([0.4, 0.1, 0.4]),
    ti.Vector([0.2, 0.2, 0.5]), ti.Vector([0.25, 0.25, 0.55]), ti.Vector([0.3, 0.7, 0.7]), ti.Vector([0.35, 0.75, 0.75]),
    ti.Vector([0.6, 0.6, 0.2]), ti.Vector([0.65, 0.65, 0.25]), ti.Vector([0.45, 0.35, 0.25]), ti.Vector([0.5, 0.4, 0.3]),
    ti.Vector([0.8, 0.5, 0.4]), ti.Vector([0.85, 0.55, 0.45]), ti.Vector([0.8, 0.6, 0.7]), ti.Vector([0.85, 0.65, 0.75]),
    ti.Vector([0.2, 0.0, 0.35]), ti.Vector([0.25, 0.05, 0.4]), ti.Vector([0.9, 0.9, 0.95]), ti.Vector([0.85, 0.85, 0.9]),
    ti.Vector([0.4, 0.4, 0.45]), ti.Vector([0.35, 0.35, 0.4]), ti.Vector([0.3, 0.0, 0.25]), ti.Vector([0.35, 0.05, 0.3]),
    ti.Vector([0.5, 0.25, 0.4]), ti.Vector([0.55, 0.3, 0.45]), ti.Vector([0.6, 0.35, 0.5]), ti.Vector([0.65, 0.4, 0.55]),
    ti.Vector([0.7, 0.45, 0.6]), ti.Vector([0.75, 0.5, 0.65]), ti.Vector([0.6, 0.2, 0.3]), ti.Vector([0.65, 0.25, 0.35]),
    ti.Vector([0.7, 0.3, 0.4]), ti.Vector([0.75, 0.35, 0.45]), ti.Vector([0.8, 0.4, 0.5]), ti.Vector([0.85, 0.45, 0.55]),
    ti.Vector([0.9, 0.5, 0.6]), ti.Vector([0.95, 0.55, 0.65]), ti.Vector([1.0, 0.6, 0.7]), ti.Vector([0.0, 0.0, 0.0]) ,
    ti.Vector([0.02, 0.1, 0.15]), ti.Vector([0.05, 0.12, 0.18]), ti.Vector([0.08, 0.15, 0.2]),]
    
  
for i , col in enumerate(colors_list):
    colors_field[i] = col

@ti.func
def color_map(t):
    
   
    n = len(colors_list)
    t_scaled = t * n
    idx = int(t_scaled)
    f = t_scaled - idx
    idx_next = min(idx + 1 , n)
    c = (1 - f) * colors_field[idx] + f * colors_field[idx_next]
    return c
