import taichi as ti

@ti.func
def color_map(t):
    # تعریف 44 رنگ به سبک if/elif
    c0  = ti.Vector([0.7, 0.35, 0.0])
    c1  = ti.Vector([0.75, 0.5, 0.0])
    c2  = ti.Vector([0.8, 0.6, 0.0])
    c3  = ti.Vector([0.8, 0.65, 0.05])
    c4  = ti.Vector([0.55, 0.0, 0.1])
    c5  = ti.Vector([0.6, 0.1, 0.15])
    c6  = ti.Vector([0.35, 0.0, 0.35])
    c7  = ti.Vector([0.4, 0.1, 0.4])
    c8  = ti.Vector([0.2, 0.2, 0.5])
    c9  = ti.Vector([0.25, 0.25, 0.55])
    c10 = ti.Vector([0.3, 0.7, 0.7])
    c11 = ti.Vector([0.35, 0.75, 0.75])
    c12 = ti.Vector([0.6, 0.6, 0.2])
    c13 = ti.Vector([0.65, 0.65, 0.25])
    c14 = ti.Vector([0.45, 0.35, 0.25])
    c15 = ti.Vector([0.5, 0.4, 0.3])
    c16 = ti.Vector([0.8, 0.5, 0.4])
    c17 = ti.Vector([0.85, 0.55, 0.45])
    c18 = ti.Vector([0.8, 0.6, 0.7])
    c19 = ti.Vector([0.85, 0.65, 0.75])
    c20 = ti.Vector([0.2, 0.0, 0.35])
    c21 = ti.Vector([0.25, 0.05, 0.4])
    c22 = ti.Vector([0.9, 0.9, 0.95])
    c23 = ti.Vector([0.85, 0.85, 0.9])
    c24 = ti.Vector([0.4, 0.4, 0.45])
    c25 = ti.Vector([0.35, 0.35, 0.4])
    c26 = ti.Vector([0.3, 0.0, 0.25])
    c27 = ti.Vector([0.35, 0.05, 0.3])
    c28 = ti.Vector([0.5, 0.25, 0.4])
    c29 = ti.Vector([0.55, 0.3, 0.45])
    c30 = ti.Vector([0.6, 0.35, 0.5])
    c31 = ti.Vector([0.65, 0.4, 0.55])
    c32 = ti.Vector([0.7, 0.45, 0.6])
    c33 = ti.Vector([0.75, 0.5, 0.65])
    c34 = ti.Vector([0.6, 0.2, 0.3])
    c35 = ti.Vector([0.65, 0.25, 0.35])
    c36 = ti.Vector([0.7, 0.3, 0.4])
    c37 = ti.Vector([0.75, 0.35, 0.45])
    c38 = ti.Vector([0.8, 0.4, 0.5])
    c39 = ti.Vector([0.85, 0.45, 0.55])
    c40 = ti.Vector([0.9, 0.5, 0.6])
    c41 = ti.Vector([0.95, 0.55, 0.65])
    c42 = ti.Vector([1.0, 0.6, 0.7])
    c43 = ti.Vector([0.0, 0.0, 0.0])

    t_scaled = t * 44.0
    idx = int(t_scaled)
    f = t_scaled - idx

    c = ti.Vector([0.0, 0.0, 0.0])

    if idx == 0:
        c = (1 - f) * c0 + f * c1
    elif idx == 1:
        c = (1 - f) * c1 + f * c2
    elif idx == 2:
        c = (1 - f) * c2 + f * c3
    elif idx == 3:
        c = (1 - f) * c3 + f * c4
    elif idx == 4:
        c = (1 - f) * c4 + f * c5
    elif idx == 5:
        c = (1 - f) * c5 + f * c6
    elif idx == 6:
        c = (1 - f) * c6 + f * c7
    elif idx == 7:
        c = (1 - f) * c7 + f * c8
    elif idx == 8:
        c = (1 - f) * c8 + f * c9
    elif idx == 9:
        c = (1 - f) * c9 + f * c10
    elif idx == 10:
        c = (1 - f) * c10 + f * c11
    elif idx == 11:
        c = (1 - f) * c11 + f * c12
    elif idx == 12:
        c = (1 - f) * c12 + f * c13
    elif idx == 13:
        c = (1 - f) * c13 + f * c14
    elif idx == 14:
        c = (1 - f) * c14 + f * c15
    elif idx == 15:
        c = (1 - f) * c15 + f * c16
    elif idx == 16:
        c = (1 - f) * c16 + f * c17
    elif idx == 17:
        c = (1 - f) * c17 + f * c18
    elif idx == 18:
        c = (1 - f) * c18 + f * c19
    elif idx == 19:
        c = (1 - f) * c19 + f * c20
    elif idx == 20:
        c = (1 - f) * c20 + f * c21
    elif idx == 21:
        c = (1 - f) * c21 + f * c22
    elif idx == 22:
        c = (1 - f) * c22 + f * c23
    elif idx == 23:
        c = (1 - f) * c23 + f * c24
    elif idx == 24:
        c = (1 - f) * c24 + f * c25
    elif idx == 25:
        c = (1 - f) * c25 + f * c26
    elif idx == 26:
        c = (1 - f) * c26 + f * c27
    elif idx == 27:
        c = (1 - f) * c27 + f * c28
    elif idx == 28:
        c = (1 - f) * c28 + f * c29
    elif idx == 29:
        c = (1 - f) * c29 + f * c30
    elif idx == 30:
        c = (1 - f) * c30 + f * c31
    elif idx == 31:
        c = (1 - f) * c31 + f * c32
    elif idx == 32:
        c = (1 - f) * c32 + f * c33
    elif idx == 33:
        c = (1 - f) * c33 + f * c34
    elif idx == 34:
        c = (1 - f) * c34 + f * c35
    elif idx == 35:
        c = (1 - f) * c35 + f * c36
    elif idx == 36:
        c = (1 - f) * c36 + f * c37
    elif idx == 37:
        c = (1 - f) * c37 + f * c38
    elif idx == 38:
        c = (1 - f) * c38 + f * c39
    elif idx == 39:
        c = (1 - f) * c39 + f * c40
    elif idx == 40:
        c = (1 - f) * c40 + f * c41
    elif idx == 41:
        c = (1 - f) * c41 + f * c42
    elif idx == 42:
        c = (1 - f) * c42 + f * c43
    else:
        c = c43

    return c