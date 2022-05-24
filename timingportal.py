import sys, getopt
from colorama import init, Fore, Back
from termcolor import colored
import json
import pyfiglet
from datetime import datetime



def per_lap(amount_of_laps):
    #print(colored("Press enter to start the timer", 'yellow'))
    laps = int(amount_of_laps)
    laptimes = {}

    for i in range(laps):
        print(colored("\nLap " + str(i+1),'green'))
        if i == 0:
            input('Press enter to start: ')
            start_time = datetime.now()
        else:
            start_time = stop_time    

        print('counting time...')

        input('Press enter to stop: ')
        stop_time = datetime.now()

        timing = stop_time - start_time
        print(colored("Time lap " + str(i+1) + ": ",'yellow') + str(timing))
        laptimes["lap-"+str(i+1)] = str(timing)

    return laptimes    

    #print()


def write_results(results_dictionary):
    print(results_dictionary)
    with open('results.json', 'a') as outfile:
        outfile.write(results_dictionary)


def run_timer(variables):
    """Running the timer"""
    timings = variables
    banner = pyfiglet.figlet_format("TimingPortal")

    print(banner)
    boat_timings = {}
    for entry in variables:
        print(colored(str(entry), 'green') + ": " + variables.get(entry))
        boat_timings[entry] = variables.get(entry)
        if entry == "laps":
            lap_timings = per_lap(variables.get("laps"))
            boat_timings["lap_timings"] = lap_timings
    write_results(json.dumps(boat_timings, indent=4))
    print('\n')

   

def main(argv):
    """Deze functie runned als eerste van dit script"""
    boatnumber = ''
    teamname = ''
    laps = ''
    variables = {}

    ## Init colorama, zodat kleurtjes ook werken op windows
    init()

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