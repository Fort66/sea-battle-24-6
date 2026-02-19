from ursina import *

from ursina.mesh_importer import obj_to_ursinamesh 

app = Ursina()


obj = Entity(
    model='assets/models/newport/newport.glb',
)

# obj.model.save('assets/models/newport/newport.bam')

mesh = obj_to_ursinamesh(name='assets/models/newport/newport.glb', return_mesh=True)  
mesh.save('assets/models/newport/newport.bam')

app.run()

