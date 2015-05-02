require './file_ngrams'
require './jaccard_index'
require 'csv'


tweets = CSV.read('tweets.csv')

tweets.each do |tweet|
  unless tweet[1].nil?
    url_new = "sites-new/#{tweet[1]}.txt"
    url_old = "sites-old/#{tweet[1]}.txt"
    3.times do |i|
      grams_new = grams_old = []
      if File.exist?(url_new) && File.exist?(url_old)
        grams_new = FileNgrams.new(url_new, i+1).grams
        grams_old = FileNgrams.new(url_old, i+1).grams
      end
      # puts grams_old.inspect
      # puts grams_new.inspect
      change = JaccardIndex.new(grams_old, grams_new).jaccard_index
      puts "*"*10
      puts "#{i+1} - ngram"
      puts grams_new.count
      puts grams_old.count
      puts change.inspect
      if change > 0
        puts change.inspect
        puts "*"*25
      end
      puts "*"*10
    end
  end
end