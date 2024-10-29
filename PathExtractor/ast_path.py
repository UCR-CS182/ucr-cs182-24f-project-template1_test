import hashlib
from . import common

class AstPath:
  def __init__(self, source, target, path: str):
    self.source = source
    self.target = target
    self.path = path
    self.hashed_path = self.hash_path(path)

  @staticmethod
  def hash_path(path: str) -> str:
    # Create a hash of the path using SHA-256
    return str(hashlib.sha256(path.encode('utf-8')).hexdigest())

  @classmethod
  def set_no_hash(cls):
    cls.hash_path = staticmethod(lambda x: x)

  def __str__(self) -> str:
    return f"{common.node_property_manager.get_node_data(self.source).normalized_name},{self.path},{common.node_property_manager.get_node_data(self.target).normalized_name}"
  
  def get_hashed_path(self) -> str:
    return self.hashed_path