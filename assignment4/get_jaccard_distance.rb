require './file_ngrams'
require './jaccard_index'
require 'json'
require 'date'
require 'active_support/time'

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
    mementos.sort_by { |hsh| hsh["datetime"] }
    
    url_old = "choosen_20_boilerpipe/#{tweet}-1.txt"
    mementos[1..-1].each_with_index do |memento, index|
      url_new = "choosen_20_boilerpipe/#{tweet}-#{index+1}.txt"
      unless tweet[1].nil?
        grams_new = grams_old = []
        if File.exist?(url_new) && File.exist?(url_old)
          grams_new = FileNgrams.new(url_new, 1).grams
          grams_old = FileNgrams.new(url_old, 1).grams
        end
        # puts grams_old.inspect
        # puts grams_new.inspect
        change = JaccardIndex.new(grams_old, grams_new).jaccard_index
        puts "*"*10
        puts "#{1} - ngram"
        puts grams_new.count
        puts grams_old.count
        puts change.inspect
        if change > 0
          puts change.inspect
          puts "*"*25
        end
        puts "*"*10
      end
      url_old = url_new
    end
  end
end