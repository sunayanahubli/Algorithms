# import DeepWalkAlgorithm as dp
import importlib
# algos = {'Deep Walk': 'dp', 'BFS': 'bfs'}

def check_input_validity(name):
    print(f'Algorithm entered: {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # ToDo:  Add functionality to verify the user input against the list of available algorithms
    return name


def execute_algorithm(name):
    print(f'Executing Algorithm : {name}')
    algo = importlib.import_module(name)
    algo.execute()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        algorithm = input()
        algorithm = check_input_validity(algorithm)
        if algorithm:
            execute_algorithm(algorithm)
        else:
            break
