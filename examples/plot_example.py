#!/usr/bin/python3

import fastplot
import numpy as np
import pandas as pd



x = range(11)
y=[4,150,234,465,745,612,554,43,565,987,154]
fastplot.plot((x, y),  '1_line.eps', xlabel = 'X', ylabel = 'Y')




x = range(11)
y1=[4,150,234,465,645,612,554,43,565,987,154]
y2=[434,15,24,556,75,345,54,443,56,97,854]
fastplot.plot([ ('First', (x, y1) ), ('Second', (x, y2) )], '2_line_multi.eps', mode='line_multi', xlabel = 'X', ylabel = 'Y', xlim = (-0.5,10.5),
                cycler = fastplot.CYCLER_LINESPOINTS, legend=True, legend_loc='upper left', legend_ncol=2)




fastplot.plot(np.random.normal(100, 30, 1000), '3_CDF.eps', mode='CDF', xlabel = 'Data', style='latex')




fastplot.plot( [ ('A', np.random.normal(100, 30, 1000)), ('B', np.random.normal(140, 50, 1000)) ], '4_CDF_multi.eps', mode='CDF_multi', xlabel = 'Data', legend=True)




data=[ ('A', np.random.normal(100, 30, 1000)), ('B', np.random.normal(140, 50, 1000)), ('C', np.random.normal(140, 50, 1000))]
fastplot.plot( data,  '5_boxplot.eps', mode='boxplot', ylabel = 'Value')





rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
fastplot.plot( ts ,  '6_timeseries.eps', mode='timeseries', ylabel = 'Value', style='latex', xticks_rotate=30, xticks_fontsize='small',
               xlim=(pd.Timestamp('1/1/2011'), pd.Timestamp('1/7/2011')))





rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng) + 5
ts2 = pd.Series(np.random.randn(len(rng)), index=rng) + 10
fastplot.plot( [('One', ts), ('Two', ts2)] , '7_timeseries_multi.eps', mode='timeseries_multi', ylabel = 'Value', xticks_rotate=30,
                legend = True, legend_loc='upper center', legend_ncol=2, legend_frameon=False, ylim = (0,16), xticks_fontsize='small')





rng = pd.date_range('1/1/2011', periods=480, freq='H')
df = pd.DataFrame( np.random.uniform(3,4,size=(len(rng),2)), index=rng, columns=('One', 'Two') )
df = df.divide(df.sum(axis=1), axis=0)*100
fastplot.plot( df , '8_timeseries_stacked.eps', mode='timeseries_stacked', ylabel = 'Value [%]', xticks_rotate=30, ylim=(0,100), legend=True)




data = [('First',3),('Second',2),('Third',7),('Four',6),('Five',5),('Six',4)]
fastplot.plot(data,  '9_bars.eps', mode = 'bars', ylabel = 'Value', xticks_rotate=30, style='serif', ylim = (0,10))





data = pd.DataFrame( [[2,5,9], [3,5,7], [1,6,9], [3,6,8], [2,6,8]], index = ['One', 'Two', 'Three', 'Four', 'Five'], columns = ['A', 'B', 'C'] )
fastplot.plot(data,  '10_bars_multi.eps', mode = 'bars_multi', style='latex', ylabel = 'Value', legend = True, ylim = (0,12), legend_ncol=3)




x = range(11)
y=[120,150,234,465,745,612,554,234,565,888,154]
def my_callback(plt):
    plt.bar(x,y)
fastplot.plot([],  '10_callback.eps', mode = 'callback', callback = my_callback, style='latex', xlim=(-0.5, 11.5), ylim=(0, 1000))



