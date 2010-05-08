require 'spec'

class Vector
  def initialize(values)
    @values = values
  end

  def values
    @values
  end

  def *(other)
    Vector.new(@values.map{|i| i*other})
  end
end

class Fixnum
  alias mult *
  def *(other)
    if other.is_a?(Vector)
      other * self
    else
      self.mult(other)
    end
  end
end
describe Vector do
  subject {Vector.new([1,3,4])}

  its(:values) {should == [1,3,4]}
  it do
    v = subject * 5
    v.values.should == [5,15,20]
  end

  it do
    v = 5 * subject
    v.values.should == [5,15,20]
  end
end
