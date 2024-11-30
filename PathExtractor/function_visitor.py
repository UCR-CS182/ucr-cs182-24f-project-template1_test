from tree_sitter import Node

from typing import List

from .leaves_collector import LeavesCollector
from .common import MethodContents

class FunctionVisitor:

  def __init__(self):
    self.methods: List[MethodContents] = []

  def visit(self, program_node: Node) -> None:
    for child in program_node.children:
      # TODO: Visit each method in the program
      # That is, visit each node of type "method_declaration" using the visitMethod method
      # Your code here
      pass
    
      # Recursively visit the children of the current node
      self.visit(child)

  def visitMethod(self, method_declaration_node: Node) -> None:
    
    leaves_collector = LeavesCollector()
    leaves_collector.visit(method_declaration_node)
    leaves = leaves_collector.get_leaves()
    method_name = method_declaration_node.child_by_field_name("name").text.decode("utf-8")
    method_length = self.get_method_length(method_declaration_node)
    self.methods.append(MethodContents(leaves, method_name, method_length))


  def get_methods(self) -> List[MethodContents]:
    return self.methods
  

  def get_method_length(self, method_declaration_node: Node) -> int:
    # line of code without comments (single-line and comment blocks) and empty lines (including line with only "{" or "}")
    method_code = method_declaration_node.text.decode("utf-8")
    clean_code = method_code.replace('\r\n', '\n').replace('\t', ' ')

    if len(clean_code) == 0:
      return 0

    lines = clean_code.split('\n')
    code_length = sum(
      1 for line in lines 
      if line.strip() and 
      line.strip() not in ['{', '}'] and 
      not line.strip().startswith('/') and 
      not line.strip().startswith('*')
    )
    
    return code_length