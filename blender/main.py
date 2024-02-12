import bpy

# Clear existing scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Add a cube to the scene
bpy.ops.mesh.primitive_cube_add(size=2)

# Set camera position
bpy.ops.object.camera_add(location=(6, -6, 6))
bpy.context.object.rotation_euler[0] = 0.8
bpy.context.object.rotation_euler[1] = 0

# Set render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600
bpy.context.scene.render.filepath = '/path/to/render/output.png'

# Render the scene
bpy.ops.render.render(write_still=True)