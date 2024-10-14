from typing import List
from tree_sitter import Node
import re

BLANK_WORD = "BLANK"

class NodeDataManager:
  def __init__(self) -> None:
    self.node_data = {}
  
  def set_node_data(self, node: Node, data):
    self.node_data[node] = data
  
  def get_node_data(self, node: Node):
    return self.node_data[node]


def normalize_name(original, default_string):
    original = (original.lower()
                  .replace("\\n", "")  # escaped new lines
                  .replace(r'\s+', "")  # whitespaces
                  .replace(r'["\',]', "")  # quotes, apostrophes, commas
                  .replace(r'[^\x20-\x7E]', ""))  # unicode weird characters
    stripped = re.sub(r'[^A-Za-z]', '', original)
    if len(stripped) == 0:
        careful_stripped = original.replace(" ", "_")
        return careful_stripped if len(careful_stripped) > 0 else default_string
    else:
        return stripped

def split_to_subtokens(input_str):
  # Trim the input string
  str2 = input_str.strip()
  
  # Define the regex pattern for splitting
  pattern = r"(?<=[a-z])(?=[A-Z])|_|[0-9]|(?<=[A-Z])(?=[A-Z][a-z])|\s+"
  
  # Split the string based on the pattern
  subtokens = re.split(pattern, str2)
  
  # Normalize and filter out empty subtokens
  result = [
      normalize_name(token, '') for token in subtokens if token
  ]
  
  return result

node_id_manager = NodeDataManager()
node_property_manager = NodeDataManager()
