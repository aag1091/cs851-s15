require './file_ngrams'
require './jaccard_index'
require 'csv'
require 'json'
require 'gnuplot'


tweets = CSV.read('tweets.csv')
memento_counts = []
puts tweets.count
tweets.each do |tweet|
  unless tweet[1].nil?
    url = "timemaps_json/#{tweet[1]}"
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
    plot.autoscale "x"
    plot.autoscale "y"
    plot.title  "Plot for CDF for # of mementos for each original URI"
    plot.ylabel "% links"
    plot.xlabel "# of mementos"
    
    x,y = [], []
    memento_counts.uniq.each_with_index do |count, index|
      x += [count]
      mc_count = memento_counts.select{|mc| mc == count}.count
      # puts mc_count
      # puts memento_counts.count
      y += [((mc_count.to_f/memento_counts.count))]
    end

    # puts x
    # puts y

    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end

puts 'created CDF plotted graph'