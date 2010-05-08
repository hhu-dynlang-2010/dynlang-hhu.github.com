require 'spec'

class A
  def initialize()
    @i = 123
  end

  def i()
    @i
  end

  def i=(v)
    @i = v
  end
end

class B < A
  def hi()
    @i + 10
  end
end
describe A do
  its(:i) {should == 123}
  it 'should set the i value' do
    subject.i = 42
    subject.i.should == 42
  end
end

describe B do
  it { should be_an(A)}
  its(:hi) { should == 133 }
end
