import pytest
from tree_sitter import Language, Parser
import tree_sitter_java as tsjava

from PathExtractor.PathExtractor.leaves_collector import LeavesCollector

JAVA_LANGUAGE = Language(tsjava.language())
parser = Parser(JAVA_LANGUAGE)

def test_leaves_collector():
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
  lc = LeavesCollector()
  lc.visit(tree.root_node)
  leaves = lc.get_leaves()
  assert leaves[0].text.decode("utf-8") == "public"