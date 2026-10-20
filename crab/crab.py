from board_parser import board_parser, DEFAULT_BOARD_CONFIG_PATH
from holdscan import holdscan, DEFAULT_HOLD_SCAN
from thresholdscan import thresholdscan, DEFAULT_THRESHOLD
from acquisition import acquire, DEFAULT_N_EVENTS
import subprocess

def splash_screen():
    text = '''
     ___           ___           ___           ___                                                                                               
    /\  \         /\  \         /\  \         /\  \                                                                                            
   /::\  \       /::\  \       /::\  \       /::\  \        / <`     '> \                                                                                  
  /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \      (  / @   @ \  )                                                                                 
 /:/  \:\  \   /::\~\:\  \   /::\~\:\  \   /::\~\:\__\      \(_ _\_/_ _)/                                                                                  
/:/__/ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:|__|   (\ `-/     \-' /)                                                                                   
\:\  \  \/__/ \/_|::\/:/  / \/__\:\/:/  / \:\~\:\/:/  /    "===\     /==="                                                                                  
 \:\  \          |:|::/  /       \::/  /   \:\ \::/  /      .==')___(`==.                                                                                  
  \:\  \         |:|\/__/        /:/  /     \:\/:/  /      ' .='     `=.                                                                                   
   \:\__\        |:|  |         /:/  /       \::/__/                                                                                 
    \/__/         \|__|         \/__/         ~~                                                                                                  
    Cosmic         Ray           Atmospheric   BenchmarkUnit                                                                                            
    '''
    print(text)
def main():
    _ = subprocess.run('clear')
    splash_screen()
    board_config_path = input(f"board config path (press enter to use {DEFAULT_BOARD_CONFIG_PATH}): ")
    if board_config_path == '':
        layers, sipms1, x_positions1, y_positions1, channels1 = board_parser()
    else:
        layers, sipms1, x_positions1, y_positions1, channels1 = board_parser(board_config_path)
    print(f'loaded board config with {layers} layers and {sipms1} sipms')

#holdscan input loop

    while True:
        holdscan_input = input(f'do a hold scan? (press y for yes, enter a number if you already have one, or press return for {DEFAULT_HOLD_SCAN} ns): ')
        if holdscan_input == 'y':
            delay = holdscan(channels1)
            break
        elif holdscan_input == '':
            delay = DEFAULT_HOLD_SCAN
            break
        else:
            try:
                holdscan_input = int(holdscan_input)
                if 0 < holdscan_input < 255:
                    delay = holdscan_input
                    break
                else:
                    print(f"you gave a holdscan value of {holdscan_input}, which won't work")
            except:
                print('i need a number for holdscan!')
           #holdscan input loop

    while True:
        threshold_input = input(f'do a threshold scan? (y for yes, number if you have one, or enter for a default of {DEFAULT_THRESHOLD}): ')
        if threshold_input == 'y':
            threshold = thresholdscan(channels1)
            break
        elif threshold_input == '':
            threshold = DEFAULT_THRESHOLD
            break
        else:
            try:
                threshold_input = int(threshold_input)
                if 0<threshold_input<255:
                    threshold = threshold_input
                    break
                else:
                    print(f'you gave a threshold value of {threshold_input}, which is no bueno')
            except:
                print('i need a number for threshold adc!')
    print(threshold)

    while True:
        n_events_input = input(f'how many events you want? (default {DEFAULT_N_EVENTS}): ')            
        if n_events_input == '':
            n_events = DEFAULT_N_EVENTS
            break
        else:
            try:
                n_events_input = int(n_events_input)
                if 0<n_events_input < 1000000:
                        n_events = n_events_input
                        break
                else:
                    print("that's too many events! try again. go under 1000000")
            except:
                print('i need a number!')

                


if __name__ == '__main__':
    main()
