require './ngrams'

class FileNgrams

  attr_accessor :path, :n

  def initialize(path, n)
    @path = path
    @n = n
  end

  def sentences
    @sentences ||= File.open(path) do |file|
      file.each_line.each_with_object([]) do |line, acc|
        stripped_line = line.strip

        unless stripped_line.nil? || stripped_line.empty?
          acc << line.split(' ').map do |word|
            word.split('/').first
          end.join(' ')
        end
      end
    end
  end

  def grams
    Ngrams.new(sentences.join(' ')).ngrams(n)
  end

end