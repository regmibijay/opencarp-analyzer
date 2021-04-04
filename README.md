# OpenCARP-Analyzer
```
_____________________________________________________
OpenCARP Analyzer 1.0
Extracts data and multiple txt files from Trace data created by openCARP at once.
_____________________________________________________
usage: opencarp-analyzer [-h] [-c COLUMNS [COLUMNS ...]] [-t TRACE] [-i IION [IION ...]] [-v [VERSION]]

optional arguments:
  -h, --help            show this help message and exit
  -c COLUMNS [COLUMNS ...], --columns COLUMNS [COLUMNS ...]
                        Name of files that contain header data
  -t TRACE, --trace TRACE
                        Trace data file, e.g. Trace_0.dat
  -i IION [IION ...], --iion IION [IION ...]
                        Ion you want to visualize, e.g. -i i_Ks
  -v [VERSION], --version [VERSION]
                        Displays current version of the script
 ```

# OpenCARP-Plotter
```
_____________________________________________________
OpenCARP Plotter 1.0
Plots multiple txt files created by opencarp at once.
_____________________________________________________
usage: opencarp-plotter [-h] [-f FILES [FILES ...]] [-o OUT] [-i IGNORE [IGNORE ...]] [-t TITLE [TITLE ...]]
                        [-l LEGEND [LEGEND ...]] [-v [VERSION]]

optional arguments:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Files to Plot
  -o OUT, --out OUT     Output image name
  -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                        Ignores a file name if this text exists in file
  -t TITLE [TITLE ...], --title TITLE [TITLE ...]
                        Title of plot
  -l LEGEND [LEGEND ...], --legend LEGEND [LEGEND ...]
                        Legend location in plot. Options: BEST,UPPER RIGHT,UPPER LEFT,LOWER LEFT,LOWER
                        RIGHT,RIGHT,CENTER LEFT,CENTER RIGHT,LOWER CENTER,UPPER CENTER,CENTER
  -v [VERSION], --version [VERSION]
                        Displays current version of the script
```

## Installation

Install current version of this toolkit using `pip install opencarp-analyzer` or using `pip install git+https://github.com/regmibijay/opencarp-analyzer`

## Usage
After installation, make sure your pip installation site is in your PATH. If so, you will be able to use `opencarp-analyzer` and `opencarp-plotter` from CLI.

## Examples
`opencarp-analyzer -c header1.txt header2.txt -t Trace_0.dat -i i_Ks V i_NCX `
 will read `header1.txt` and `header2.txt` and append the column names so content of `header1.txt` is before `header2.txt` and then read `Trace_0.dat` and create a dataframe with corrent column names. Then the given `i_Ks`, `V` and `i_NCX` files are generated in `.txt` format with respective values from `Trace_0.dat`.
 
`opencarp-plotter -f data/i_*.txt data_2/*.txt -i MurineMouse header -t Comparision of voltages in mV -legend upper right` will read `data` folder and extract all the files containing `i_` in the name and `.txt` extension. Then it will search for `*.txt` files in `data2` folder and make a list of all files, from with all files containing either `MurineMouse` or `header` in filename are omitted. Now we create a plot with title of `Comparision of voltages in mV` and legends in upper right corner.
