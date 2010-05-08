def with_square(x)
  yield x**2
  print "After block #{x}"
end
