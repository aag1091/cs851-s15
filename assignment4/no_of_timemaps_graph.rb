require './file_ngrams'
require './jaccard_index'
require 'csv'
require 'gnuplot'


tweets = CSV.read('tweets.csv')
memento_counts = []

tweets.each do |tweet|
  unless tweet.nil?
    url = "choosen_20/#{tweet}"
    abcd = {}
    if File.exist?(url)
      content = File.read(url)
      if content && content != ''
        abcd = JSON.parse(File.read(url))
      end
    end
    mementos = []
    if abcd.count > 0
      if abcd["mementos"]
        mementos = abcd["mementos"]["list"]
      end
    end
    memento_counts << mementos.count
  end
end

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    #
    plot.terminal "png"
    plot.output File.expand_path("../no_of_mementos.png", __FILE__)

    # see sin_wave.rb
    plot.xrange "[0:100]"
    plot.yrange "[0:1000]"
    plot.title  "Plot for CDF for # of mementos for each original URI"
    plot.ylabel "% links"
    plot.xlabel "# of mementos"
    plot.linecolor = "red"

    x,y = [], []
    memento_counts.uniq.each_with_index do |link_change, index|
      x += [(memento_counts.count(link_change)/memento_counts.count)*100]
      y += [link_change]
    end

    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end

puts 'created CDF plotted graph'