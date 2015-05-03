require './file_ngrams'
require './jaccard_index'
require 'csv'
require 'json'
require 'date'
require 'active_support/time'

tweets = CSV.read('tweets.csv')
urls = []

tweets.each do |tweet|
  unless tweet[1].nil?
    url = "timemaps_json/#{tweet[1]}"
    abcd = {}
    if File.exist?(url)
      content = File.read(url)
      # puts content
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
    if mementos.count > 0 && mementos.first["datetime"] < 2.years.ago
      if mementos.count > 20 && mementos.count < 30
        urls << (tweet[0][-1] == '/' ? tweet[0] : tweet[0]+'/')
      end
    end
  end
end

puts urls.uniq
puts urls.uniq.count