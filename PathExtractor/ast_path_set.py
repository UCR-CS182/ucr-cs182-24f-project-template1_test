from typing import List

from .ast_path import AstPath


class AstPathSet:
  def __init__(self, name: str):
    self.name = name
    self.paths: List[AstPath] = []

  def is_empty(self):
    # TODO: Returns True if the self.paths is empty
    pass
  
  def add_path(self, source, target, path: str):
    new_path = AstPath(source, target, path)
    # TODO: Append the new_path to self.paths

