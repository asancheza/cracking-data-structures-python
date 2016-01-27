#!/usr/bin/python
# -*- coding: utf-8 -*-

def rotate_matrix(m):
  layers = len(m) / 2
  length = len(m) - 1

  for layer in range(layers):
    for i in range(layer, length - layer):
      temp = m[layer][i]
      m[layer][i] = m[length - i][layer]
      m[length - i][layer] = m[length - layer][length - 1]
      m[length - layer][length - i] = m[i][length - layer]
      m[i][length - layer] = temp

def printMatrix(m):
  for row in m:
    print row
  print
    
matrix = [ [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9] ];

printMatrix(matrix)
rotate_matrix(matrix)
printMatrix(matrix)
