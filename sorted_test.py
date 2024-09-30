import sorting
import random

nums = [random.randint(1,100) for x in range(random.randint(1,100))]

def test_bubble():
  assert sorting.bubble(nums) == sorted(nums)

def test_selection():
  assert sorting.bubble(nums) == sorted(nums)

def test_insertion():
  assert sorting.bubble(nums) == sorted(nums)
