require './file_ngrams'
require './jaccard_index'
require 'csv'
require 'gnuplot'


tweets = CSV.read('tweets.csv')
one_gram_change = []
two_gram_change = []
three_gram_change = []

tweets.each do |tweet|
  unless tweet.nil?
    url_new = "sites-new/#{tweet[1]}.txt"
    url_old = "sites-old/#{tweet[1]}.txt"
    3.times do |i|
      grams_new = grams_old = []
      if File.exist?(url_new) && File.exist?(url_old)
        grams_new = FileNgrams.new(url_new, i+1).grams
        grams_old = FileNgrams.new(url_old, i+1).grams
      end
      puts "*"*25
      puts grams_new.count.inspect
      puts grams_old.count.inspect
      change = JaccardIndex.new(grams_old, grams_new).jaccard_index
      one_gram_change << change if i == 0
      two_gram_change << change if i == 1
      three_gram_change << change if i == 2      
    end
    puts "#{tweet} - #{one_gram_change.last}, #{two_gram_change.last}, #{three_gram_change.last}"
  end
end

# puts one_gram_change.inspect
# puts two_gram_change.inspect
# puts three_gram_change.inspect

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    #
    plot.terminal "png"
    plot.output File.expand_path("../one_gram.png", __FILE__)

    # see sin_wave.rb
    plot.autoscale "x"
    plot.autoscale "y"
    plot.title  "Plot for change in 1-gram of boilerpipe data"
    plot.xlabel "change (Jaccard Index) for 1-gram"
    plot.ylabel "population"
    
    x,y = [], []
    one_gram_change.uniq.each_with_index do |link_change, index|
      y += [(one_gram_change.count(link_change)/one_gram_change.count)]
      x += [link_change]
    end

    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end

puts 'created 1-gram graph'

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    #
    plot.terminal "png"
    plot.output File.expand_path("../two_gram.png", __FILE__)

    # see sin_wave.rb
    plot.autoscale "x"
    plot.autoscale "y"
    plot.title  "Plot for change in 2-gram of boilerpipe data"
    plot.xlabel "change (Jaccard Index) for 2-gram"
    plot.ylabel "population"
    
    x,y = [], []
    two_gram_change.uniq.each_with_index do |link_change, index|
      y += [(two_gram_change.count(link_change).to_f/two_gram_change.count)]
      x += [link_change]
    end

    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end
puts 'created 2-gram graph'

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    #
    plot.terminal "png"
    plot.output File.expand_path("../three_gram.png", __FILE__)

    # see sin_wave.rb
    plot.autoscale "x"
    plot.autoscale "y"
    plot.title  "Plot for change in 3-gram of boilerpipe data"
    plot.xlabel "change (Jaccard Index) for 3-gram"
    plot.ylabel "population"
    
    x,y = [], []
    three_gram_change.uniq.each_with_index do |link_change, index|
      y += [((three_gram_change.select{|mc| mc == link_change}).count.to_f/three_gram_change.count)]
      x += [link_change]
    end

    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end

  end
end
puts 'created 3-gram graph'