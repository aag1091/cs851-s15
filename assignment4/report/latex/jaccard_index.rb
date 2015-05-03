class JaccardIndex

  attr_accessor :a1, :a2

  def initialize(a1, a2)
    @a1 = a1
    @a2 = a2
  end

  def jaccard_index
    return 0 if (a1.nil? || a1.empty?) || (a1.nil? || a2.empty?)
    (a1_u_a2 - a1_n_a2).count.to_f/a1_u_a2.count.to_f
  end

  def a1_u_a2
    (a1 | a2)
  end

  def a1_n_a2
    (a1 & a2)
  end

end