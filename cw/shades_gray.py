def shades_of_grey(n):
  return ['#' + (('%02x' % i) * 3) for i in xrange(1, min(n + 1, 255))]
