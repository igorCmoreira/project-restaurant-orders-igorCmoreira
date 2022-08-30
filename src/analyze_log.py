from src.track_orders import TrackOrders


def init_trackOrders(data):
    list_orders = TrackOrders()
    list_orders.__fill__(data)
    return list_orders


def save_answers(data):
    list_or = init_trackOrders(data)
    maria_most_ordered = list_or.get_most_ordered_dish_per_customer('maria')
    times_ham = list_or. get_number_of_times_orderd('arnaldo', 'hamburguer')
    joao_never_order = list_or.get_never_ordered_per_customer('joao')
    joao_never_came = list_or.get_days_never_visited_per_customer('joao')
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(maria_most_ordered) + '\n')
        file.write(str(times_ham) + '\n')
        file.write(str(joao_never_order) + '\n')
        file.write(str(joao_never_came) + '\n')


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida '{path_to_file}'")
    try:
        with open(path_to_file, 'r') as file:
            _data = file.readlines()
        save_answers(_data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
