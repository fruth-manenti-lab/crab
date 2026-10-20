# stuff for dealing with the board config file 
# ik i don't need a WHOLE file for this but like, maybe the board confi file becomes crazy in the future, so it would be nice to have the project be clutter free. also yeah no i don't care about line lengths. sorry.
import json
DEFAULT_BOARD_CONFIG_PATH = 'board_configs/default_board.json'
def board_parser(config_path:str = DEFAULT_BOARD_CONFIG_PATH):
    with open(config_path, 'r') as file:
        contents = file.read()
    try:
        parsed_results = json.loads(contents)
    except:
        print('somethings wrong with the board config file :(')
        raise
    layers = int(parsed_results['layers'])
    if layers == 1:
        layer1 = parsed_results['layer1']
        sipms1 =         layer1['sipms']
        x_positions1 =   layer1['x_positions']
        y_positions1 =   layer1['y_positions']
        channels1 =      layer1['channels']   
    else:
        print('only 1 layer boards are currently supported')
    return(layers, sipms1, x_positions1, y_positions1, channels1)
if __name__ == '__main__':
    board_parser()
