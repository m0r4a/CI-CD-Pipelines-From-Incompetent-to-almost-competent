function fibonacci(a) {
  if (a <= 1)
    return 0;

  if (a == 2)
    return 1;
  
  return fibonacci(a - 1) + fibonacci(a - 2)
}

module.exports = fibonacci;
