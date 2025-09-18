const fibonacci = require('./main.js');

describe('Tests for the Fibonacci function', () => {

  // check the first term of the sequence
  test('should return 0 for fibonacci(1)', () => {
    expect(fibonacci(1)).toBe(0);
  });

  // check the second term of the sequence
  test('should return 1 for fibonacci(2)', () => {
    expect(fibonacci(2)).toBe(1);
  });

  // check a standard value in the sequence
  test('should return 3 for fibonacci(5)', () => {
    expect(fibonacci(5)).toBe(3);
  });
  
  // check a higher value in the sequence
  test('should return 34 for fibonacci(10)', () => {
    expect(fibonacci(10)).toBe(34);
  });

  // check edge cases like zero
  test('should return 0 for fibonacci(0)', () => {
    expect(fibonacci(0)).toBe(0);
  });
  
  // check edge cases like negative numbers
  test('should return 0 for negative numbers', () => {
    expect(fibonacci(-10)).toBe(0);
  });
  
  // check that the returned data type is a number
  test('should return a value of type "number"', () => {
    expect(typeof fibonacci(6)).toBe('number');
  });

});
