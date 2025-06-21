# Sample Data Files

This directory contains sample data files for testing and demonstrating the Merge Sort algorithm.

## Files

### sample_arrays.json
Contains various test cases organized into categories:

- **Educational Examples**: Basic arrays for learning merge sort
- **Performance Test Cases**: Arrays for performance analysis
- **Edge Cases**: Special cases like empty arrays, single elements
- **Complexity Demonstration**: Arrays that highlight algorithmic properties

## Usage

These sample arrays can be loaded programmatically or used as reference for manual testing:

```python
import json

# Load sample arrays
with open('data/sample_arrays.json', 'r') as f:
    sample_data = json.load(f)

# Access specific test case
basic_example = sample_data['educational_examples']['basic_example']['array']
```

## Categories Explained

### Educational Examples
- **Basic Example**: Standard demonstration array
- **Already Sorted**: Shows merge sort behavior on sorted data
- **Reverse Sorted**: Demonstrates worst-case input for comparison-based sorts
- **With Duplicates**: Tests algorithm stability

### Performance Test Cases
- **Small/Medium Random**: Various sizes for performance comparison
- **Nearly Sorted**: Tests performance on partially ordered data

### Edge Cases
- **Single Element**: Minimal valid input
- **Two Elements**: Base case testing
- **All Same Values**: Tests handling of duplicate values
- **Empty Array**: Edge case validation

### Complexity Demonstration
- **Power of Two Size**: Clean recursion depth examples
- **Fibonacci Numbers**: Interesting mathematical sequence
- **Large Range**: Tests with varied value magnitudes