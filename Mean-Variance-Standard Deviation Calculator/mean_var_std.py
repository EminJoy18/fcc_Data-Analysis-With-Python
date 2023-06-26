import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    
  try:
    ls = np.array(list).reshape((3,3))
    calculations = dict()
  
    mean = []
    mean.append( (ls.mean(axis=0)).tolist() )
    mean.append( (ls.mean(axis=1)).tolist() )
    mean.append( ls.mean() )
  
    variance = []
    variance.append( (ls.var(axis=0)).tolist() )
    variance.append( (ls.var(axis=1)).tolist() )
    variance.append( ls.var() )
  
    std = []
    std.append( (ls.std(axis=0)).tolist() )
    std.append( (ls.std(axis=1)).tolist() )
    std.append( ls.std() )
  
    max = []
    max.append( (ls.max(axis=0)).tolist() )
    max.append( (ls.max(axis=1)).tolist() )
    max.append( ls.max() )
  
    min = []
    min.append( (ls.min(axis=0)).tolist() )
    min.append( (ls.min(axis=1)).tolist() )
    min.append( ls.min() )
    
    sum = []
    sum.append( (ls.sum(axis=0)).tolist() )
    sum.append( (ls.sum(axis=1)).tolist() )
    sum.append( ls.sum() )
  
    calculations['mean'] = mean
    calculations['variance'] = variance
    calculations['standard deviation'] = std
    calculations['max'] = max
    calculations['min'] = min
    calculations['sum'] = sum
    # print(calculations)
    return calculations

  except ValueError:
    print("List must contain nine numbers.")
