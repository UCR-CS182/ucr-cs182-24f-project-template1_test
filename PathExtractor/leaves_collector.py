from tree_sitter import Node
from typing import List
from . import common
import re
from .node_property import NodeProperty

class LeavesCollector:
  """
  Collects the leaves (terminal nodes) of the AST and stores them in the leaves[] list.
  It usually implements the Visitor pattern.
  The root node will be passed to the visit() method.
  It will recursively visit all the nodes in a depth-first manner.
  During the traversal, 
    1 it will set the node child_id through the node_id_manager in common.py.
      (child_id is the index of the node in the parent's children list, i.e., the rank of the node among its siblings)
    2 it will also set the user defined node properties through the node_property_manager in common.py.
  For simplicity:
    1 We will directly neglect the comment nodes.
    2 We will filter out the leaves with a non-alphanumeric name.
  """
  def __init__(self):
    self.leaves = []

  def visit(self, node: Node):

    # TODO: Skip the comment nodes.
    if self.is_comment(node):
      # Your Code here
      pass
    
    common.node_id_manager.set_node_data(node, self.get_child_id(node))

    is_leaf = (not self.has_child(node)) and (not self.is_comment(node))
    if is_leaf:
      node_str = node.text.decode("utf-8")
      if node_str and node_str != "null":
        if re.match(r'[^a-zA-Z0-9]', node.type) is None:
          self.leaves.append(node)
    
    common.node_property_manager.set_node_data(node, NodeProperty(node, is_leaf))

    # TODO: Recursively visit the children of the node.
    for child in node.children:
      # Your Code here
      pass


  # TODO: Return True if a node has child(ren).
  def has_child(self, node):
    # Your Code here
    pass


  # TODO: Get the child_id of a given node.
  # child_id is the index of the node in the parent's children list, 
  # i.e., the rank of the node among its siblings
  def get_child_id(self, node: Node):
    # Your Code here
    pass

  # TODO: Return True if a node is a comment node.
  # Notice there are two types of comments: single line comment and multiline comment.
  def is_comment(self, node):
    # Your Code here
    pass

  def get_leaves(self) -> List[Node]:
    return self.leaves
  




# test
def test():
  from tree_sitter import Language, Parser
  import tree_sitter_python as tspython
  import tree_sitter_java as tsjava

  JAVA_LANGUAGE = Language(tsjava.language())

  parser = Parser(JAVA_LANGUAGE)

  # Parse some Java code
  code = b"""
public class Example {
  // This is a comment
  public void method(Object source, Object target) {
    int a = 0; // another comment
    int b = 1;
    a = b;
    int[] arr = { 1, 2, 3 };
    b = arr[a];
    if (a > 0) {
      System.out.println("Hello");
    }
    for (Object elem : this.elements) {
      if (elem.equals(target)) {
        return true;
      }
    }
  }
}
  """
  tree = parser.parse(code)
  root_node = tree.root_node.child(0).child(3)

  # Collect leaves
  collector = LeavesCollector()
  collector.visit(root_node)

  # Get and print the leaves
  leaves = collector.leaves
  for leaf in leaves:
      print(common.normalize_name(leaf.text.decode('utf-8'), common.BLANK_WORD), end='---')
      print(common.node_id_manager.get_node_data(leaf))

if __name__ == "__main__":
    test()

