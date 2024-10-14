from . import common

# TODO: Complete the BoxedTypes-to-Primitive types mapping.
BoxedTypes = {'Integer': "integral_type", 
              'Double': "", 
              'Float': "", 
              'Long': "", 
              'Short': "", 
              'Byte': "", 
              'Character': "", 
              'Boolean': "boolean_type"}

INTERNAL_SEPARATOR = "|"
NUMERIC_KEEP_VALUES = {"0", "1", "32", "64"}

Max_Label_Length = 8

class NodeProperty:
  """
  This is a wrapper class for a Tree-sitter node in the AST.
  We maintain some useful user defined properties for each tree-sitter node.

  Abstract type: It abstracts the original node.type. 
    For now we only consider abstracting Java boxed types into primitive types.

  Normalized name: It is the normalized version of the node.text.

  is_leaf: It is a boolean value indicating whether the node is a leaf node or not.

  In the initialization, we also append the operator to the abstract type 
    if the node is a binary, unary or assignment expression.

  For simplicity, if the node is a leaf node, 
    we normalize the name of the node
      1 set the separator to "|" of camel case or snake case names to differentiate the separator used in the AST path.
      2 remove the special characters and whitespaces from the name
  """
  def __init__(self, node, is_leaf) -> None:
    self.abstract_type = node.type
    self.normalized_name = node.text.decode("utf-8")
    self.is_leaf = is_leaf

    # TODO: Set the abstract type for Java nodes with boxed types.
    # Your Code here

    operator = ""
    if self.is_unary_expr(node) or self.is_binary_expr(node) or self.is_assign_expr(node):
      # TODO: Get the operator of the expression node.
      # Your Code here
      pass
    
    if operator:
      self.abstract_type += f":{operator}"
    
    if self.is_leaf:
      name_to_split = node.text.decode("utf-8")
      split_name_parts = common.split_to_subtokens(name_to_split)
      nm = INTERNAL_SEPARATOR.join(split_name_parts)
      if nm:
        if self.is_numeric_literal(node) and nm not in NUMERIC_KEEP_VALUES:
          nm = '<NUM>'
        if len(nm) > Max_Label_Length:
          nm = nm[:Max_Label_Length]
        self.normalized_name = nm


  # TODO: Return True if a node is a Java boxed type. 
  # We list Java boxed types in the above BoxedTypes dict.
  def is_java_boxed_type(self, node) -> bool:
    # Your Code here
    pass
  
  # TODO: Return the primitive type of a boxed type. 
  # The mapping between boxed types and primitive types
  #  is defined in the BoxedTypes dict.
  def get_primitive_type(self, node) -> str:
    # Your Code here
    pass

  # TODO: Return True if a node is a binary expression.
  def is_binary_expr(self, node) -> bool:
    # Your Code here
    pass
  
  # TODO: Return True if a node is a unary expression.
  def is_unary_expr(self, node) -> bool:
    # Your Code here
    pass

  # TODO: Return True if a node is an assignment expression.
  def is_assign_expr(self, node) -> bool:
    # Your Code here
    pass
  
  # TODO: Return True if a node is a numeric literal.
  # Numeric literals include integer literals and floating point literals.
  def is_numeric_literal(self, node) -> bool:
    # Your Code here
    pass
  