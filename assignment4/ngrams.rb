class Ngrams

  REGEX = /\w+/

  attr_accessor :target

  def initialize(target)
    @target = target
  end

  def ngrams(n)
    target.downcase.scan(REGEX).each_cons(n).to_a.uniq
  end

end