from typing import List, Optional, Tuple

from .common import MethodContents
from .ast_path import AstPath
from .common import NodeDataManager
from . import common

from tree_sitter import Language, Parser, Node
import tree_sitter_python as tspython
import tree_sitter_java as tsjava
JAVA_LANGUAGE = Language(tsjava.language())


MinCodeLen = 2
MaxCodeLen = 1000
MaxPathLen = 8
MaxPathWidth = 2
MaxChildId = float('inf')

UpSymbol = '^'
DownSymbol = '_'
LParen = '('
RParen = ')'
PathSeparator = ''

ParentTypeToAddChildId = {"assignment_expression", "array_access", "method_invocation"}


# Extracts AST paths for each method in the code file
class PathExtractor():

  def __init__(self):
    self.parser = Parser(JAVA_LANGUAGE)

  
  def extract_path(self, source: Node, target: Node, separator: str) -> str:
    # path should contain the common prefix only once

    source_stack = self.__get_path_stack(source)
    target_stack = self.__get_path_stack(target)

    len_common_prefix, idx_src, idx_tar = self.__len_common_prefix(source_stack, target_stack)

    # TODO: Calculate the length of the path using the common prefix length and the indices of the first nodes that differ
    # check if the path length is within the limits (< MaxPathLen), else return empty string
    # Your Code here
    
    # check path width
    # TODO: Calculate the path width using the source and target stacks and the indices of the first nodes that differ
    # the path width is the difference between the child ids of the first nodes that differ
    # You may use the node_id_manager to get the child id of a node
    # check if the path width is within the limits (< MaxPathWidth), else return empty string
    if idx_src >= 0 and idx_tar >=0:
      # Your Code here
      pass

    # construct the path
    p = ''
    cp_idx = len(source_stack) - len_common_prefix


    # construct the src half 
    for i in range(cp_idx):
      src_child_id = ''
      # TODO: For each node in the source stack, get the child id if the node is a leaf node or a node of type in ParentTypeToAddChildId
      # At the same time, saturate the child id to MaxChildId if it exceeds the limit (using the __saturate_id method implemented below)
      if i == 0 or source_stack[i].parent in ParentTypeToAddChildId:  
        # Your Code here
        pass
      # Construct the source half of the path with the abstract type and the child id
      p += f"({common.node_property_manager.get_node_data(source_stack[i]).abstract_type}{src_child_id}){UpSymbol}"
    

    # construct the common prefix
    cp_node = source_stack[cp_idx]
    cp_child_id = ''
    # TODO: Get the child id of the common prefix node if the node is a leaf node or a node of type in ParentTypeToAddChildId
    # At the same time, saturate the child id to MaxChildId if it exceeds the limit (using the __saturate_id method implemented below)
    # Your Code here
    # Construct the common prefix of the path with the abstract type and the child id
    p += f"({common.node_property_manager.get_node_data(cp_node).abstract_type}{cp_child_id})"


    # TODO: Similar to the source half and the common prefix, construct the target half of the path
    # Iterate over the target stack in reverse order
    # Construct the target half of the path with the abstract type and the child id
    # Get the child id of the target node if the node is a leaf node or a node of type in ParentTypeToAddChildId
    # Make sure the child id saturated to MaxChildId if it exceeds the limit
    # Each node in the target half should be separated by DownSymbol
    # Your Code here
    

    return p
  
  # Given a leaf node as input, returns a list of nodes from the leaf to the root
  def __get_path_stack(self, node: Node) -> List[Node]:
    path_stack = []
    while node:
      # TODO: Push nodes to the stack
      # Your Code here
      pass
    return path_stack
  
  # Given two stacks of nodes, returns the length of the common prefix of the two stacks and the indices of the first nodes that differ
  def __len_common_prefix(self, source_stack: List[Node], target_stack: List[Node]) -> Tuple[int, int, int]:

    i = len(source_stack) - 1
    j = len(target_stack) - 1
    len_cp = 0

    while i >= 0 and j >= 0 and source_stack[i] == target_stack[j]:
      # TODO
      # Your Code here
      pass
    
    return len_cp, i, j
  

  def __saturate_id(self, id: str) -> str:
    return min(int(id), MaxChildId)



def test():
  pass 


if __name__ == "__main__":
  test()
