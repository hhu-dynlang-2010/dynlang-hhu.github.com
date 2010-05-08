class Array
  def my_map()
    raise ArgumentError unless block_given?
    a = Array.new(self.length)
    for i in (0...self.length)
        a[i] = yield(self[i])
    end
    a
  end
end
