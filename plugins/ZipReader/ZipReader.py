from UM.Mesh.MeshReader import MeshReader

class ZipReader(MeshReader):
    def __init__(self):
        super().__init__()
        self._supported_extensions = [".zip"]
