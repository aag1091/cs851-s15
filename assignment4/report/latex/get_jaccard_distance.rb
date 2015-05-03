require './file_ngrams'
require './jaccard_index'
require 'json'
require 'date'
require 'active_support/time'
require 'gnuplot'

tweets = [
  "564543197783654400", 
  "564543281166831617",
  "564543372531347456",
  "564543427690635264",
  "564543489992818688",
  "564543557311406080",
  "564543635190845440",
  "564543210484432896",
  "564543292239773697",
  "564543395067346944",
  "564543447567052800",
  "564543531168313344",
  "564543584204898304",
  "564543865026539521",
  "564543250149945345",
  "564543330772852738",
  "564543419293249536",
  "564543450801246208",
  "564543557072326656",
  "564543628983664640",
  "564543865445556225"
]
i = 0
tweets.each do |tweet|
  i += 1
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
    mementos.sort_by { |hsh| hsh["datetime"] }
    memento_changes = []
    
    url_old = "choosen_20_boilerpipe/#{tweet}-1.txt"
    mementos[1..-1].each_with_index do |memento, index|
      url_new = "choosen_20_boilerpipe/#{tweet}-#{index+1}.txt"
      unless tweet[1].nil?
        grams_new = grams_old = []
        if File.exist?(url_new) && File.exist?(url_old)
          grams_new = FileNgrams.new(url_new, 1).grams
          grams_old = FileNgrams.new(url_old, 1).grams
        end
        change = JaccardIndex.new(grams_old, grams_new).jaccard_index
        memento_changes << { change: change, datetime: memento["datetime"] }
      end
      url_old = url_new
    end

    Gnuplot.open do |gp|
      Gnuplot::Plot.new( gp ) do |plot|

        #
        plot.terminal "png"
        plot.output File.expand_path("../choosen_20_#{i}.png", __FILE__)

        # see sin_wave.rb
        plot.autoscale "x"
        plot.autoscale "y"
        plot.title  "Plot for change in Mementos of a URL"
        plot.ylabel "% change (Jaccard Index) for 2-gram"
        plot.xlabel "Time Period in days"
        
        # def timefmt;  '%y/%d/%m';  end

        # def fetch_codelines(stat, fields)
        #   return stat.values_at(*fields).map{|values| values['codelines'] }.sum
        # end

        # def ftime(timestamp)
        #   Time.at(timestamp).strftime(timefmt)
        # end

        x,y = [], []
        memento_changes.uniq.each_with_index do |link_change, index|
          puts link_change
          
          x += [(Time.now - Time.parse(link_change[:datetime])).to_i/(24*60*60)]
          y += [link_change[:change]]
        end

        puts x
        puts y

        plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
          ds.with = "linespoints"
          ds.notitle
        end

      end
    end
    puts 'created 2-gram graph'
  end
end