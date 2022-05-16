from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=2)
scene.set_floor(-0.85, (1.0, 1.0, 1.0))
scene.set_background_color((0.5, 0.5, 0.4))
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6))

@ti.func
def create_block(pos, size, color, color_noise):
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color + color_noise * ti.random())

@ti.kernel
def initialize_voxels():
    black =  vec3(0, 0, 0)
    pense = vec3(2, 4, 1)
    blue = vec3(0.1, 0.5, 1)
    # 面一层一层的折叠，小到大，大到小
    color_noise = vec3(0.01)
    # 脸
    create_block(ivec3(-9,0,0), ivec3(6, 1, 1), black ,color_noise)
    create_block(ivec3(-3,0,0), ivec3(3, 1, 1), pense ,color_noise)
    create_block(ivec3(0,0,0), ivec3(5, 1, 1), black ,color_noise)
    create_block(ivec3(5,0,0), ivec3(3, 1, 1), pense ,color_noise)
    create_block(ivec3(8,0,0), ivec3(6, 1, 1), black ,color_noise)

    head_high = 5
    create_block(ivec3(-6,1,0), ivec3(17, head_high, 1), black ,color_noise)
    create_block(ivec3(-8,1,0), ivec3(21, 2, 1), black ,color_noise)
    # 耳朵
    create_block(ivec3(-6,6,0), ivec3(5, 1, 1), black ,color_noise)
    create_block(ivec3(6,6,0), ivec3(5, 1, 1), black ,color_noise)
    # 耳朵
    create_block(ivec3(-6,7,0), ivec3(3, 1, 1), black ,color_noise)
    create_block(ivec3(8,7,0), ivec3(3, 1, 1), black ,color_noise)
    # 耳朵
    create_block(ivec3(-6,8,0), ivec3(1, 1, 1), black ,color_noise)
    create_block(ivec3(10,8,0), ivec3(1, 1, 1), black ,color_noise)

    create_block(ivec3(-9,-1,0), ivec3(5, 1, 1), black ,color_noise)
    create_block(ivec3(-4,-1,0), ivec3(13, 1, 1), pense ,color_noise)
    create_block(ivec3(9,-1,0), ivec3(5, 1, 1), black ,color_noise)

    h1 = 4
    create_block(ivec3(-9,-1-h1,0), ivec3(4, h1, 1), black ,color_noise)
    create_block(ivec3(-5,-1-h1,0), ivec3(15, h1, 1), pense ,color_noise)
    create_block(ivec3(10,-1-h1,0), ivec3(4, h1, 1), black ,color_noise)
    h = 6
    create_block(ivec3(-8,-1-h,0), ivec3(3, h, 1), black ,color_noise)
    create_block(ivec3(-5,-1-h,0), ivec3(15, h, 1), pense ,color_noise)
    create_block(ivec3(10,-1-h,0), ivec3(3, h, 1), black ,color_noise)

    create_block(ivec3(-6,-1-h-1,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(-4,-1-h-1,0), ivec3(13, 1, 1), pense ,color_noise)
    create_block(ivec3(9,-1-h-1,0), ivec3(2, 1, 1), black ,color_noise)

    create_block(ivec3(-5,-3-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(-3,-3-h,0), ivec3(11, 1, 1), pense ,color_noise)
    create_block(ivec3(8,-3-h,0), ivec3(2, 1, 1), black ,color_noise)

    create_block(ivec3(-4,-4-h,0), ivec3(13, 1, 1), black ,color_noise)
    create_block(ivec3(-3,-5-h,0), ivec3(11, 1, 1), black ,color_noise)
#     水
    create_block(ivec3(-3,-18+8-h-2,0), ivec3(11, 1, 1), blue ,color_noise)
    create_block(ivec3(-4,-18+7-h-2,0), ivec3(13, 1, 1), blue ,color_noise)
    create_block(ivec3(-5,-18+6-h-2,0), ivec3(15, 1, 1), blue ,color_noise)
    create_block(ivec3(-6,-18+3-h,0), ivec3(17, 1, 1), blue ,color_noise)
    create_block(ivec3(-7,-18+2-h,0), ivec3(19, 1, 1), blue ,color_noise)
    create_block(ivec3(-6,-18+1-h,0), ivec3(17, 1, 1), blue ,color_noise)
    create_block(ivec3(-5,-18-h,0), ivec3(15, 1, 1), blue ,color_noise)
    create_block(ivec3(-4,-18-1-h,0), ivec3(13, 1, 1), blue ,color_noise)
    create_block(ivec3(-3,-18-2-h,0), ivec3(11, 1, 1), blue ,color_noise)
#     腿
    create_block(ivec3(-12,-7+4-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(-11,-7+3-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(-10,-7-h,0), ivec3(1, 3, 1), black ,color_noise)
    create_block(ivec3(-9,-7-h,0), ivec3(8, 1, 1), black ,color_noise)
    create_block(ivec3(-8,-8-h,0), ivec3(5, 1, 1), black ,color_noise)
#     腿
    create_block(ivec3(-3,-14-h,0), ivec3(2, 9, 1), black ,color_noise)
    create_block(ivec3(-4,-14-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(0,-15-h,0), ivec3(2, 11, 1), black ,color_noise)
    create_block(ivec3(-1,-16-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(3,-15-h,0), ivec3(2, 11, 1), black ,color_noise)
    create_block(ivec3(4,-16-h,0), ivec3(2, 1, 1), black ,color_noise)
    create_block(ivec3(6,-14-h,0), ivec3(2, 9, 1), black ,color_noise)
    create_block(ivec3(7,-14-h,0), ivec3(2, 1, 1), black ,color_noise)
    # 眼睛
    create_block(ivec3(-3,-h,0), ivec3(2, 4, 1), vec3(1, 0, 0),color_noise)
    create_block(ivec3(6,-h,0), ivec3(2, 4, 1), vec3(1, 0, 0),color_noise)
    scene.set_voxel(ivec3(2,-7,0), 1, vec3(1, 0, 0) + color_noise * ti.random())

initialize_voxels()

scene.finish()