import sys, getopt
from termcolor import colored
import pyfiglet
import time



def print_time(total_seconds):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    print('Time spend: {}h:{}m:{}s'.format(hours, mins, seconds))
    return '{}h:{}m:{}s'.format(hours, mins, seconds)





def per_lap(amount_of_laps):
    #print(colored("Press enter to start the timer", 'yellow'))
    laps = int(amount_of_laps)

    for i in range(laps):
        print(colored("\nLap " + str(i+1),'green'))
        if i == 0:
            input('Press enter to start: ')
            start_time = time.time()
        else:
            start_time = stop_time    

        print('counting time...')

        input('Press enter to stop: ')
        stop_time = time.time()

        timing = print_time(stop_time - start_time)
        print(colored("Time lap " + str(i+1) + ": ",'yellow') + timing)

        

    #print()

def run_timer(variables):
    """Running the timer"""
    timings = variables
    banner = pyfiglet.figlet_format("TimingPortal")

    print(banner)
    for entry in variables:
        print(colored(str(entry), 'green') + ": " + variables.get(entry))
    print('\n')

    per_lap(variables.get("laps"))



    



def main(argv):
    """Deze functie runned als eerste van dit script"""
    boatnumber = ''
    teamname = ''
    laps = ''
    variables = {}

    ## Probeer de command line arguments te parsen
    try:
        opts, args = getopt.getopt(argv,"hbn:l:",["boatnumber=","teamname=", "laps="])
    except getopt.GetoptError:
        print('\n$ python3 timingportal.py -b <boatnumber> -n <teamname> -l <laps>')
        print('$ python3 timingportal.py --boatnumber <boatnumber> --teamname <teamname> --laps <laps>\n')
        sys.exit(2)

    ## Check ff of er argumenten aanwezig zijn, anders opnieuw draaien    
    if argv == []:
        print(colored("\nPlease use the following syntax to use the program:", 'red'))
        print('$ python3 timingportal.py -b <boatnumber> -n <teamname> -l <laps>')
        print('$ python3 timingportal.py --boatnumber <boatnumber> --teamname <teamname> --laps <laps>\n')
        sys.exit()
    else:
        for entry in argv:
            entry_index = argv.index(entry)
            if "-" in argv[0] or argv[2] or argv[4]:
                opt = entry
                if opt == '-h':
                    print(colored("\nUsage of the program:", 'yellow'))
                    print('$ python3 timingportal.py -b <boatnumber> -n <teamname> -l <laps>')
                    print('$ python3 timingportal.py --boatnumber <boatnumber> --teamname <teamname> --laps <laps>\n')
                    sys.exit()
                elif opt in ("-b", "--boatnumber"):
                    arg = argv[entry_index+1]
                    boatnumber = arg
                    variables["boatnumber"] = boatnumber
                elif opt in ("-n", "--teamname"):
                    arg = argv[entry_index+1]
                    teamname = arg
                    variables["teamname"] = teamname
                elif opt in ("-l", "--laps"):
                    arg = argv[entry_index+1]
                    laps = arg     
                    variables["laps"] = laps
            else:
                print(colored("\nPlease use the following syntax to use the program:", 'red'))
                print('$ python3 timingportal.py -b <boatnumber> -n <teamname> -l <laps>')
                print('$ python3 timingportal.py --boatnumber <boatnumber> --teamname <teamname> --laps <laps>\n')
                sys.exit()
    if len(variables) != 3:
        print(colored("\nPlease use all the arguments:", 'red'))
        print('$ python3 timingportal.py -b <boatnumber> -n <teamname> -l <laps>')
        print('$ python3 timingportal.py --boatnumber <boatnumber> --teamname <teamname> --laps <laps>\n')
        sys.exit()

    ## Begin met het timen
    results = run_timer(variables)

    #print(len(variables))
    #print(variables)


if __name__ == "__main__":
   main(sys.argv[1:])