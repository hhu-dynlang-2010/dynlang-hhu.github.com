
require 'spec'

class PyObject
  def initialize(values)
    @values = values
  end

  def method_missing(name, *args)
    if name.to_s[-1] == '='
        @values[name.to_s[0...-1]] = args[0]
    elsif @values.include?(name.to_s)
      @values[name.to_s]
    else
      super
    end
  end
end
describe PyObject do
  subject {PyObject.new({'name' => 'foo', 'value' => 'bar'})}

  its(:name) {should == 'foo'}
  its(:value) {should == 'bar'}

end
