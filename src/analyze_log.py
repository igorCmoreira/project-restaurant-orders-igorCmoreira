def most_request_maria(data):
    

def save_answers(data, report):



def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extenção inválida '{path_to_file}'")
    with open(path_to_file) as file:
        _data = file.readlines()
    
