import numpy as np


def calculate(list):
  calculations = np.array(list)
  if len(calculations) < 9:
    raise ValueError("List must contain nine numbers.")
  calculations = calculations.reshape(3,3)


  mean = [calculations.mean(axis=0).tolist(), calculations.mean(axis=1).tolist(), calculations.mean().tolist()]
  variance = [calculations.var(axis=0).tolist(), calculations.var(axis=1).tolist(), calculations.var().tolist()]
  standar_deviation = [calculations.std(axis=0).tolist(), calculations.std(axis=1).tolist(), calculations.std().tolist()]
  max = [calculations.max(axis=0).tolist(), calculations.max(axis=1).tolist(), calculations.max().tolist()]
  min = [calculations.min(axis=0).tolist(), calculations.min(axis=1).tolist(), calculations.min().tolist()]
  sum = [calculations.sum(axis=0).tolist(), calculations.sum(axis=1).tolist(), calculations.sum().tolist()]
  output = {'mean': mean, 'variance': variance, 'standard deviation': standar_deviation, 'max': max, 'min': min, 'sum': sum}

  return output
