from functions_to_optimise import * 

def config_pso():

    params = {
        "nb_part" : 2000, 
        "vit" : 0.05, 
        "c1" : 0.1, 
        "c2" : 0.6,
        "max_ite" : 5000, 
        "nb_simulation_MC" : 50 , 
        "min_x" : 0, 
        "max_x" : 15, 
        "Dim" : 2, 
        "min_max" : "min", 
        "function" : Function_test_1,
        }
    
    return params

# Function_test_1(np.array([ 0, 5]))