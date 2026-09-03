bl_info = {
    "name": "Mat Npr CrazyDog", #插件名字
    "author": "CrazyDog", #作者名字
    "version": (1, 0, 0, 0), #插件版本
    "blender": (4, 4, 0), #需要的*最低* blender 版本
    "location": "3DView > Tools", #插件所在位置
    "description": "Make npr material for npr branch.", #描述
    "support": 'COMMUNITY', #支持等级（社区支持）
    "category": "Material", #分类
}

import bpy
from . import main_panel

include_files = {
    main_panel,

}

def register():
    for file in include_files:
        file.register()

def unregister():
    for file in include_files:
        file.unregister()

if __name__ == "__main__":
    register()