
set terminal pngcairo size 1024,768 enhanced font 'Verdana,15'
#set dpi 120
set output 'Deviation.png'
set samples 100000
set grid
set angles degrees
set title 'Deviation en fonction de l incidence'
# Line width of the axes
set border linewidth 1.5
# Line styles
set style line 1 linecolor rgb '#0060ad' linetype 1 linewidth 2
#set style line 2 linecolor rgb '#dd181f' linetype 1 linewidth 2
# Legend
set key at 6.1,1.3
# Axes label
set xlabel 'i, angle incidence en degres'
set ylabel 'D, deviation en degrees'
# Axes ranges
set xrange [-20:90]
set yrange [15:45]
# Axes tics
set xtics 20 #('-2p' -2*pi, '-p' -pi, 0, 'p' pi, '2p' 2*pi)
set ytics 5
set tics scale 0.75
A = 30
n = 1.5
f(x) = x + asin(n*sin(A-asin(sin(x)/n)))-A
#g(x) = a * cos(x)
#Labels
set label 'Minimum (22.8, 15.7)' at 20,18
set arrow from 24,17.5 to 22.8,15.7
set label 'Maximum 42.1' at 22,42
set arrow from 20,42 to -17,42.1
set arrow from 40,42 to 89,42.1
# Plot
plot f(x) title 'D(i)' with lines linestyle 1
