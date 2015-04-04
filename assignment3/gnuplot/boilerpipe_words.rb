require "gnuplot"
require "csv"

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    #
    plot.terminal "png"
    plot.output File.expand_path("../boilerpipe.png", __FILE__)

    # see sin_wave.rb
    plot.xrange "[0:60]"
    plot.yrange "[0:50000]"
    plot.title  "Plot for Collection1"
    plot.ylabel "# of occurrences"
    plot.xlabel "word rank"

    words = CSV.read('boilerpipe_words.csv')

    x,y = [], []
    words.each_with_index do |word, index|
      x += [index+1]
      y += [word[1]]
    end
    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end
puts 'created sin_wave.gif'


