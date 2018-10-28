# FastPlot

Create publication-quality plots with a simple interface over matplotlib.
Are you bored of copying and pasting the code to make a plot every time? Try this!

This module provides only one (highly customizable) function to plot some data. It use `matplotlib` in its internal, but, using arguments, helps in setting all graphical and plot paramenters (tick rotate, font, size, etc.).

For information about this Readme file and this tool please write to
[martino.trevisan@polito.it](mailto:martino.trevisan@polito.it)

## Installation

Simply clone this repo or use:
```
pip install git+https://github.com/marty90/fastplot
```

Dependencies are: `matplotlib numpy pandas statsmodels`.

## Usage
This module has only one function, called `plot`. You must call it to make a plot, providing the data, the output file name, and other parameters. A figure will be saved on disk.

The most important arguments are:
* `data`: the actual data to plot
* `path`: the output path for the plot
* `mode`: which type of plot to create (lines, bars, etc.). More details later.
* `stlye`: which graphical style to use. Can be `serif`, `sans-serif` or `latex`.

## Modes

The modes are the type of plots fastplot allows to use. Some are simple (just a line), other are more advanced (bars, etc.).
 * `line`: plot a simple line. `data` must be a two-sized tuple of lists, for x and y. E.g., ([x1,x2,x3],[y1,y2,y3])
 * `line_multi`: plot multiple lines. Data must have the form [ (line1, ([x1,x2], [y1,y2])), (line2, ([x1,x2], [y1,y2]) ) ]. The names `line1` and `line2` are put in the legend.
 * `CDF`: plot a CDF given the samples. `data` must be a list of scalars.
 * `CDF_multi`: plot many CDFs given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the legend.
  * `boxplot`: plota boxplot given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the xticks labels.
  * `timeseries`: plot a time series. `data` must be a pandas series, with a DateTime index.
  * `timeseries_multi`: plot many time series. `data` must be a list of two-sized tuples like (name, timeseries). `name` is used in the legend.
   * `timeseries_stacked`: plot many time series, stacked. `data` must be a pandas dataframe, with a DateTime index. Each column will be plotted stacked to the others. Column names are used in the legend.
   * `bars`: plot a bar plot. `data` must be a list of (name, value). `name` is used for the legend.
   * `bars_multi`: plot grouped bars. `data` must be a padas dataframe. Each row is results in a group of bars, while columns determine bars within each group.
   * `callback`: call a user function instead of plotting `data`. You must provide a function pointer in the `callback` argument, that will be called passing `plt` as paramenter in order to perform a user defined plot. No matter what you put in `data`.
      
   ## Arguments
   Arguments of the `plot` function are divided in many categories. Only `core` are mandatory.
   
**Core**
* `data`: the input data to plot
* `path`: the output path for the plot
* `mode`: which type of plot to create (lines, bars, etc.). More details later. Default `line`

**Look**
* `style`: which graphical style to use. Can be `serif`, `sans-serif` or `latex`. For latex, it enables matplotlib latex engine. Default `sans-serif`
* `figsize`: the size of the output figure. Default: `(4,2.25)`
* `cycler`: the style cycler to use. By default, it changes across main colors, and different linestyles. Change it if you want to change color, line, or point style. I provide some useful cycler in the code (see Cycler section). Default `CYCLER_LINES`
* `fontsize`: just the overall font size. Default `11`
* `dpi`: DPI for the output image. Default `300`
* `classic_autolimit`: Use classic autolimit feature (find 'nice' round numbers as view limits that enclosed the data limits), instead of v2 (sets the view limits to 5% wider than the data range). Default `True`

**Grid**
* `grid`: whether to display grid. Default `False`
* `grid_which`: ticks for the grid (major/minor). Default `major`
* `grid_axis`: axis for the grid. Default `both`
* `grid_linestyle`: gird linestyle. Default `dotted`
* `grid_color`: grid color. Default `black`

**Scale**
* `xscale`: scale for x axis (linear/log). Default `linear`
* `yscale`: scale for y axis (linear/log). Default `linear`
         
**Axis**
* `xlim`: Optional x limit, as a tuple (low, high)
* `ylim`: Optional y limit, as a tuple (low, high)
* `xlabel`: Label for x axis
* `ylabel`: Label for y axis
* `xticks`: Custom x ticks, in the form ([x1, x2, ...], [label1, label2, ...])
* `yticks`:  Custom y ticks, in the form ([y1, y2, ...], [label1, label2, ...])
* `xticks_rotate`: Rotation for x ticks. Default `0`
* `yticks_rotate`:  Rotation for y ticks. Default `0`
* `xticks_fontsize`: X ticks font size. Default `medium`
* `yticks_fontsize`: Y ticks font size. Default `medium`
* `xtick_direction`: xtick marker direction. Default 'in'
* `xtick_width`: xticks marker width. Default `1`
* `xtick_length`:  xticks marker length. Default `4`
* `ytick_direction`:  ytick marker direction. Default 'in'
* `ytick_width`: yticks marker width. Default `1`
* `ytick_length`:  yticks marker length. Default `4` 
         
**Legend**
* `legend`: whether to show the legend. Default `False`
* `legend_loc`: location for legend. Default `best`
* `legend_ncol`: number of columns. Default `1`
* `legend_fontsize`: legend fontsize. Default `medium`
* `legend_border`: whether to show legend border. Default `False`
* `legend_frameon`: whether to show legend frame. Default `True`
* `legend_fancybox`: whether to use round corner on legend frame. Default `False`
* `legend_frameon`: Transparency of legend frame. Default `1.0`

**Specific**
This arguments are specific for some `modes`.
* `linewidth`: linewidth when lines are used. Default: `1`
* `boxplot_sym`: symbol for outliers in boxplots. Default `''`
* `boxplot_whis`: whisker spec for boxplot.  Default `[5,95]`
* `timeseries_format`: format for printing dates in timeseries. Default `%Y/%m/%d`
* `bars_width`: width of bars when bars are plotted. Default `0.6`
* `callback`: function to call instead of plotting, when `mode=callback`
   
 ## Cyclers
 
 ## Examples

**line**
```
x = range(11)
y=[4,150,234,465,745,612,554,43,565,987,154]
fastplot.plot((x, y),  '1_line.png', xlabel = 'X', ylabel = 'Y')
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/1_line.png)


**line_multi**
```
x = range(11)
y1=[4,150,234,465,645,612,554,43,565,987,154]
y2=[434,15,24,556,75,345,54,443,56,97,854]
fastplot.plot([ ('First', (x, y1) ), ('Second', (x, y2) )], '2_line_multi.png', mode='line_multi', xlabel = 'X', ylabel = 'Y', xlim = (-0.5,10.5),
                cycler = fastplot.CYCLER_LINESPOINTS, legend=True, legend_loc='upper left', legend_ncol=2)
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/2_line_multi.png)


**CDF**
```
fastplot.plot(np.random.normal(100, 30, 1000), '3_CDF.png', mode='CDF', xlabel = 'Data', style='latex')
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/3_CDF.png)


**CDF_multi**
```
fastplot.plot( [ ('A', np.random.normal(100, 30, 1000)), ('B', np.random.normal(140, 50, 1000)) ], '4_CDF_multi.png', mode='CDF_multi', xlabel = 'Data', legend=True)
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/4_CDF_multi.png)


**boxplot**
```
data=[ ('A', np.random.normal(100, 30, 1000)), ('B', np.random.normal(140, 50, 1000)), ('C', np.random.normal(140, 50, 1000))]
fastplot.plot( data,  '5_boxplot.png', mode='boxplot', ylabel = 'Value')
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/5_boxplot.png)


**timeseries**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
fastplot.plot( ts ,  '6_timeseries.png', mode='timeseries', ylabel = 'Value', style='latex', xticks_rotate=30, xticks_fontsize='small',
               xlim=(pd.Timestamp('1/1/2011'), pd.Timestamp('1/7/2011')))

```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/6_timeseries.png)


**timeseries_multi**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng) + 5
ts2 = pd.Series(np.random.randn(len(rng)), index=rng) + 10
fastplot.plot( [('One', ts), ('Two', ts2)] , '7_timeseries_multi.png', mode='timeseries_multi', ylabel = 'Value', xticks_rotate=30,
                legend = True, legend_loc='upper center', legend_ncol=2, legend_frameon=False, ylim = (0,16), xticks_fontsize='small')
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/7_timeseries_multi.png)


**timeseries_stacked**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
df = pd.DataFrame( np.random.uniform(3,4,size=(len(rng),2)), index=rng, columns=('One', 'Two') )
df = df.divide(df.sum(axis=1), axis=0)*100
fastplot.plot( df , 'examples/8_timeseries_stacked.png', mode='timeseries_stacked', ylabel = 'Value [%]', xticks_rotate=30, ylim=(0,100), legend=True,
                xlim=(pd.Timestamp('1/1/2011'), pd.Timestamp('1/7/2011')))
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/8_timeseries_stacked.png)


**bars**
```
data = [('First',3),('Second',2),('Third',7),('Four',6),('Five',5),('Six',4)]
fastplot.plot(data,  '9_bars.png', mode = 'bars', ylabel = 'Value', xticks_rotate=30, style='serif', ylim = (0,10))
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/9_bars.png)


**bars_multi**
```
data = pd.DataFrame( [[2,5,9], [3,5,7], [1,6,9], [3,6,8], [2,6,8]], index = ['One', 'Two', 'Three', 'Four', 'Five'], columns = ['A', 'B', 'C'] )
fastplot.plot(data,  '10_bars_multi.png', mode = 'bars_multi', style='latex', ylabel = 'Value', legend = True, ylim = (0,12), legend_ncol=3)
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/10_bars_multi.png)


**callback**
```
x = range(11)
y=[120,150,234,465,745,612,554,234,565,888,154]
def my_callback(plt):
    plt.bar(x,y)
fastplot.plot([],  '11_callback.png', mode = 'callback', callback = my_callback, style='latex', xlim=(-0.5, 11.5), ylim=(0, 1000))
```
![alt text](https://github.com/marty90/fastplot/raw/master/examples/11_callback.png)



