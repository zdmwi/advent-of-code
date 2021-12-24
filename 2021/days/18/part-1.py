import sys
import math


class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

  def __str__(self) -> str:
      if isinstance(self.value, int):
        return str(self.value)
      return f"[{str(self.left)}, {str(self.right)}]"


def expression(number):
  root = Node()
  if isinstance(number, int):
    root.value = number
    return root

  root.left = expression(number[0])
  root.right = expression(number[1])
  root.left.parent = root
  root.right.parent = root

  return root


def explode(exprsn, depth=0, exploded=False):
  if exprsn is None or isinstance(exprsn.value, int):
    return exploded

  if depth >= 4 and isinstance(exprsn.left.value, int) and isinstance(exprsn.right.value, int):
    # find the closest left node up the tree
    prev = exprsn
    ancestor = exprsn.parent
    while ancestor and (ancestor.left == None or ancestor.left == prev):
      prev = ancestor
      ancestor = ancestor.parent
    closest_left = ancestor.left if ancestor else None

    # find the rightmost node in the left tree
    if closest_left:
      while closest_left.value == None:
        if closest_left.right:
          closest_left = closest_left.right
        else:
          closest_left = closest_left.left

    # find the closest right node up the tree
    prev = exprsn
    ancestor = exprsn.parent
    while ancestor and (ancestor.right == None or ancestor.right == prev):
      prev = ancestor
      ancestor = ancestor.parent
    closest_right = ancestor.right if ancestor else None

    # find the leftmost node in the right tree
    if closest_right:
      while closest_right.value == None:
        if closest_right.left:
          closest_right = closest_right.left
        else:
          closest_right = closest_right.right

    if closest_right and closest_right.value is not None:
      closest_right.value += exprsn.right.value

    if closest_left and closest_left.value is not None:
      closest_left.value += exprsn.left.value
    
    exprsn.value = 0
    exprsn.left = None
    exprsn.right = None

    exploded = True

  return explode(exprsn.left, depth + 1, exploded) or \
    explode(exprsn.right, depth + 1, exploded)


def split(exprsn):
  if exprsn is None:
    return False
  elif exprsn.value is not None:
    if exprsn.value > 9:
      left_node = Node()
      left_node.value = math.floor(exprsn.value/2)
      left_node.parent = exprsn

      right_node = Node()
      right_node.value = math.ceil(exprsn.value/2)
      right_node.parent = exprsn

      exprsn.value = None
      exprsn.left = left_node
      exprsn.right = right_node

      return True


  return split(exprsn.left) or split(exprsn.right)


def simplify(exprsn):
  while True:
    exploded_once = False
    while True:
      exploded = explode(exprsn)
      if not exploded:
        break
      exploded_once = True
    
    splitted = split(exprsn)

    if not exploded_once and not splitted:
      break


def add(e1, e2):
  exprsn = Node()

  exprsn.left = e1
  exprsn.right = e2

  exprsn.left.parent = exprsn
  exprsn.right.parent = exprsn

  simplify(exprsn)

  return exprsn


def magnitude(exprsn):
  if isinstance(exprsn.value, int):
    return exprsn.value

  return 3 * magnitude(exprsn.left) + 2 * magnitude(exprsn.right)


def add_and_get_magnitude(eqns):
  result = expression(eqns[0])
  for i in range(1, len(eqns)):
    result = add(result, expression(eqns[i]))

  return magnitude(result)


if __name__ == '__main__':
  eqns = [eval(line.strip()) for line in sys.stdin.readlines()]

  ans = add_and_get_magnitude(eqns)
  print(ans)