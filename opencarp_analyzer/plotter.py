import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import glob
from argparse import ArgumentParser

class glob_vars():
     loc_positions = {
                            'best' : 	0,
                            'upper right': 1,
                            'upper left' : 2,
                            'lower left' : 3,
                            'lower right' : 4,
                            'right': 5,
                            'center left' : 6,
                            'center right' : 7,
                            'lower center' : 8,
                            'upper center'	: 9,
                            'center' : 	10
                            }

def read_data(path):
    fname, ext = os.path.splitext(os.path.basename(path))
    return pd.read_csv(path, names=["Time", fname], delim_whitespace=True)



def main(argv = sys.argv[1:]):

    print("_____________________________________________________")
    print("OpenCARP Plotter 1.0")
    print("Plots multiple txt files created by opencarp at once.")
    print("_____________________________________________________")
    loc_positions = glob_vars.loc_positions
    parser = ArgumentParser()
    parser.add_argument("-f", "--files", help = "Files to Plot", nargs="+")
    parser.add_argument("-o", "--out", help = "Output image name")
    parser.add_argument("-i", "--ignore", help="Ignores a file name if this text exists in file", nargs="+")
    parser.add_argument("-t", "--title", help="Title of plot", nargs="+")
    parser.add_argument("-l", "--legend", help="Legend location in plot. Options: " + ",".join(loc_positions.keys()).upper(), nargs="+")
    parser.add_argument("-v", "--version", help = "Displays current version of the script", nargs="?", const=True)
    args = parser.parse_args()

    if args.version:
        print("Version 1.0, Crossplatfrom compatible build.")
        print("Report Issues,Suggestions opencarp@regdelivery.de")
        exit()


    if not args.files:
        print("[ERROR] Please specify at least one input file created by auswerter.py with -f or --f file.txt")
        exit()

    if args.files:
        for item in args.files:
            if os.path.isdir(item):
                print("Looking for txt files in ", item)
                args.files.remove(item)
                args.files += glob.glob(item + "*.txt")


    if any([x for x in args.files if "*" in x]):   #glob workaround for windows powershell because * is not passed as in darwin.
        for elem in args.files:
         args.files.remove(elem)
         args.files += glob.glob(elem)

    df_sum = pd.DataFrame({})
    for file in args.files:
        if not os.path.isfile(file):
            print("[WARNING]", file, " is not a valid file so it is going to be skipped ...")
            continue
        elif not args.ignore is None and  len([x for x in args.ignore if x in file]) > 0:
            print("[WARNING] Ignore (-i, --ignore) parameter was found in ", file, " skipping...")
            continue
        else:
            print("[INFO] Parsing data in ",file)
        df = read_data(file)
        if len(df_sum.columns) == 0:
            df_sum = df
        else :
            df_sum = pd.merge(df_sum, df, on="Time")

    if not len(df_sum.columns) == 0:
        df_sum.plot(x = "Time", xlabel= "Time(in ms)", ylabel="Voltage(in mV)", kind="line")

        if args.legend:
            leg = ' '.join(args.legend).lower()
            try:
                loc_input = loc_positions[leg]

            except:
                print("[WARNING]", leg, " is not a valid position. Valid positions are : ", ','.join(loc_positions.keys()).capitalize()  ,". Defaulting to UPPER RIGHT.")
                loc_input = 1

        plt.legend(loc=loc_input)
        if args.title:
            args.title = " ".join(args.title) #workaround if user inputs title without using ""
            plt.title(args.title)

        if not args.out:
            plt.show()
        else:
            plt.savefig(args.out)

    print("[EXIT] Done.")



if __name__ == "__main__":
    main()