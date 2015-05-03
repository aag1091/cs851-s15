class JaccardIndex

  attr_accessor :a1, :a2

  def initialize(a1, a2)
    @a1 = a1
    @a2 = a2
  end

  def jaccard_index
    abcd = 1.0 - similarity
    abcd = 0 if abcd.nan?
    abcd 
  end

  def similarity
    simi = (a1_n_a2.count.to_f/a1_u_a2.count.to_f)
    simi = 0 if simi.nan?
    simi
  end

  def a1_u_a2
    (a1 | a2)
  end

  def a1_n_a2
    (a1 & a2)
  end

end