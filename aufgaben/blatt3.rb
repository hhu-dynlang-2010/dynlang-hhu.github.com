require 'test/unit'

class TestFibonacci < Test::Unit::TestCase
  def setup
    @hash = make_fibonacci
  end

  def type
    assert_true(@hash.is_a(Hash))
  end
  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610].each_with_index do |item, index|
    define_method("test_value_#{item}") do
      assert_equal(item, @hash[index])
    end
  end
end

