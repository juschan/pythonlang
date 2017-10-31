from die import Die
import pygal

die = Die()

#simulate dice rolls
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#count frequencies
freq=[]
for value in range(1, die.num_sides+1):
    f=results.count(value)
    freq.append(f)
    
    
#visualize frequencies in histogram
hist=pygal.Bar()
hist.title="Results of rolling one D6 1000 times"
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('D6', freq)
hist.x_labels = map(str, range(1, 7))
hist.render_to_file('die_visual.svg')
