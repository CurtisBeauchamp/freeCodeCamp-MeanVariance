import numpy as np

def calculate(list):
    calculations = {}
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    numpy_functions = {
        'mean'              : "mean", 
        'variance'          : "var",
        'standard deviation': "std",
        'max'               : "max", 
        'min'               : "min", 
        'sum'               : "sum",
        }
    data_matrix = np. array(list).reshape(3, 3)
    flat_matrix = np.asarray(list)
    
    for key, value in numpy_functions.items():
        array = []
        lcls = locals()
        axis1_c = (f"axis1 = np.{value}(data_matrix, axis=0)")
        axis2_c = (f"axis2 = np.{value}(data_matrix, axis=1)")
        flat_c  = (f"flat = np.{value}(data_matrix)")
        exec( axis1_c, globals(), lcls )
        axis1 = lcls["axis1"]
        exec( axis2_c, globals(), lcls )
        axis2 = lcls["axis2"]
        exec( flat_c, globals(), lcls )
        flat = lcls["flat"]

        
        array.append(axis1.tolist())
        array.append(axis2.tolist())
        array.append(flat.tolist())
         
        calculations[key] = array
    return calculations
    
    
print(calculate([2,6,2,8,4,0,1,5,7])) 