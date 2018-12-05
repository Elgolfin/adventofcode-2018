# adventofcode-2018

[![CircleCI](https://circleci.com/gh/Elgolfin/adventofcode-2018.svg?style=shield)](https://circleci.com/gh/Elgolfin/adventofcode-2018)

 My humble implementations of the Advent of Code 2018 puzzles in Python (learning playground)

## Day 01

[itertools.cycle](https://docs.python.org/3.6/library/itertools.html#itertools.cycle) would have been a better solution as seen [here](https://github.com/ecly/adventofcode2018/blob/master/day01/calibration.py) afterwards.

## Day 03

Once again, the solution proposed [here](https://github.com/ecly/adventofcode2018/blob/master/day03/sliceit.py) is neat.

1. Create a grid of type ***dict***  
   *The key of the dict being the coordinates of a cell*.
2. Keep track of all claims in a set
3. Each cell of the grid is a set of claims that could overlap themselves
4. Print all the cells of the grid whose the length of the set is greater than 1
5. For each cell of the grid whose has a set length greater than 1,
   remove the related claims from the original set of claims (that has been set at the bullet #2)

### Instantiate an array from a loop

```python
arr = [i for i in range(10)]
print(arr)
```