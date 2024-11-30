import pytest
from tree_sitter import Language, Parser
import tree_sitter_java as tsjava


JAVA_LANGUAGE = Language(tsjava.language())
parser = Parser(JAVA_LANGUAGE)


def test_function_visitor():
  from PathExtractor.function_visitor import FunctionVisitor
  source_code = """
class Example {
      void methodOne() {
          // some code
      }
      
      int methodTwo(int a) {
          return a + 1;
      }
  }
  """

  from tree_sitter import Language, Parser
  import tree_sitter_python as tspython
  import tree_sitter_java as tsjava

  JAVA_LANGUAGE = Language(tsjava.language())

  parser = Parser(JAVA_LANGUAGE)

  # Parse the source code
  tree = parser.parse(bytes(source_code, "utf8"))
  root_node = tree.root_node
  
  # Initialize FunctionVisitor and visit the root node
  visitor = FunctionVisitor()
  visitor.visit(root_node)

  # Retrieve and print the methods collected
  methods = visitor.get_methods()

  assert len(methods) == 2
  assert methods[0].method_name == "methodOne"
  assert methods[0].method_length == 1
  assert methods[1].method_name == "methodTwo"
  assert methods[1].method_length == 2
  assert methods[0].leaves[0].text.decode("utf-8") == "void"
  assert methods[1].leaves[0].text.decode("utf-8") == "int"


def test_single_method_extraction():
  from PathExtractor.path_extractor import PathExtractor
  from PathExtractor.function_visitor import FunctionVisitor
  code = """
public class Example {
  // This is a comment
  public void to_int32() {
    int a = 0; // another comment
    if (a > 0) {
      SystemModule.out_std.println("Hello");
    }
  }
}
"""

  extractor = PathExtractor()
  root_node = extractor._PathExtractor__parse_file(code)
  visitor = FunctionVisitor()
  visitor.visit(root_node)
  methods = visitor.get_methods()

  pathset = extractor.extract_single_method_paths(methods[0])

  assert pathset.name == "to_int32"
  assert len(pathset.paths) == 9
  assert str(pathset.paths[0]) == "public,(public0)^(modifiers)^(method_declaration)_(void_type1),void"

def test_all_methods_all_paths_extraction():
  from PathExtractor.path_extractor import PathExtractor
  from PathExtractor.function_visitor import FunctionVisitor
  code = """
public class Example {
  // This is a comment
  public void to_int32() {
    int a = 0; // another comment
    if (a > 0) {
      SystemModule.out_std.println("Hello");
    }
  }

  int methodTwo(int a) {
    return a + 1;
  }
}
"""
  extractor = PathExtractor()
  root_node = extractor._PathExtractor__parse_file(code)
  visitor = FunctionVisitor()
  visitor.visit(root_node)
  methods = visitor.get_methods()

  methods_paths = extractor.extract_methods_paths(methods)

  print(f"Number of methods: {len(methods_paths)}")
  print(f"Method 1: {methods_paths[1].name}")
  print(f"Number of paths in method 1: {len(methods_paths[1].paths)}")
  for i in methods_paths[1].paths:
    print(f"Path 1: {i}\n")

  assert len(methods_paths) == 2
  assert methods_paths[1].name == "methodTwo"
  assert len(methods_paths[1].paths) == 10
  assert str(methods_paths[1].paths[0]) == "int,(int0)^(integral_type)^(method_declaration)_(identifier1),method|t"
  assert str(methods_paths[1].paths[1]) == "method|t,(identifier1)^(method_declaration)_(formal_parameters)_(formal_parameter)_(integral_type)_(int0),int"
  assert str(methods_paths[1].paths[9]) == "return,(return0)^(return_statement)_(binary_expression:+)_(decimal_integer_literal2),1"
