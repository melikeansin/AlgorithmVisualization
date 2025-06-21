"""
Unit tests for the Merge Sort algorithm implementation
"""

import unittest
import random
from algorithm import MergeSort, generate_random_array, generate_test_cases

class TestMergeSort(unittest.TestCase):
    """Test cases for the MergeSort class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.merge_sort = MergeSort()
    
    def test_empty_array(self):
        """Test sorting an empty array"""
        result = self.merge_sort.merge_sort([])
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test sorting a single element array"""
        result = self.merge_sort.merge_sort([42])
        self.assertEqual(result, [42])
    
    def test_two_elements_sorted(self):
        """Test sorting two elements that are already sorted"""
        result = self.merge_sort.merge_sort([1, 2])
        self.assertEqual(result, [1, 2])
    
    def test_two_elements_unsorted(self):
        """Test sorting two elements that are unsorted"""
        result = self.merge_sort.merge_sort([2, 1])
        self.assertEqual(result, [1, 2])
    
    def test_already_sorted_array(self):
        """Test sorting an already sorted array"""
        input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_reverse_sorted_array(self):
        """Test sorting a reverse sorted array"""
        input_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_random_array(self):
        """Test sorting a random array"""
        input_array = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_duplicates(self):
        """Test sorting an array with duplicate elements"""
        input_array = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_all_same_elements(self):
        """Test sorting an array where all elements are the same"""
        input_array = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        input_array = [-3, 5, -1, 0, -7, 2]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        """Test sorting an array with large numbers"""
        input_array = [1000000, 999999, 1000001, 500000]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_original_array_unchanged(self):
        """Test that the original array is not modified"""
        input_array = [64, 34, 25, 12, 22, 11, 90]
        original_copy = input_array.copy()
        self.merge_sort.merge_sort(input_array)
        self.assertEqual(input_array, original_copy)
    
    def test_step_tracking(self):
        """Test that step tracking works correctly"""
        input_array = [3, 1, 2]
        self.merge_sort.merge_sort(input_array, track_steps=True)
        
        # Should have recorded some steps
        self.assertGreater(len(self.merge_sort.steps), 0)
        
        # Check that steps contain required fields
        for step in self.merge_sort.steps:
            self.assertIn('type', step)
            self.assertIn('array', step)
            self.assertIn('description', step)
    
    def test_statistics_tracking(self):
        """Test that statistics are tracked correctly"""
        input_array = [64, 34, 25, 12, 22, 11, 90]
        self.merge_sort.merge_sort(input_array, track_steps=True)
        
        stats = self.merge_sort.get_statistics()
        
        # Should have positive counts
        self.assertGreater(stats['comparisons'], 0)
        self.assertGreater(stats['array_accesses'], 0)
        self.assertGreater(stats['steps'], 0)
    
    def test_complexity_info(self):
        """Test that complexity information is correct"""
        complexity = self.merge_sort.get_complexity_info()
        
        # Check required fields exist
        required_fields = [
            'time_complexity', 'space_complexity', 'time_explanation',
            'space_explanation', 'best_case', 'average_case', 'worst_case',
            'stable', 'in_place'
        ]
        
        for field in required_fields:
            self.assertIn(field, complexity)
        
        # Check specific values
        self.assertEqual(complexity['time_complexity'], 'O(n log n)')
        self.assertEqual(complexity['space_complexity'], 'O(n)')
        self.assertEqual(complexity['best_case'], 'O(n log n)')
        self.assertEqual(complexity['average_case'], 'O(n log n)')
        self.assertEqual(complexity['worst_case'], 'O(n log n)')
        self.assertTrue(complexity['stable'])
        self.assertFalse(complexity['in_place'])
    
    def test_stability(self):
        """Test that merge sort is stable (preserves order of equal elements)"""
        # Create array with objects that have values and original positions
        class NumberWithPosition:
            def __init__(self, value, position):
                self.value = value
                self.position = position
            
            def __le__(self, other):
                return self.value <= other.value
            
            def __lt__(self, other):
                return self.value < other.value
            
            def __eq__(self, other):
                return self.value == other.value
            
            def __repr__(self):
                return f"({self.value}, {self.position})"
        
        # Test with simple integer array with duplicates
        input_array = [3, 1, 3, 2, 1]
        result = self.merge_sort.merge_sort(input_array)
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(result, expected)

class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions"""
    
    def test_generate_random_array(self):
        """Test random array generation"""
        size = 10
        min_val = 1
        max_val = 100
        
        result = generate_random_array(size, min_val, max_val)
        
        self.assertEqual(len(result), size)
        self.assertTrue(all(min_val <= x <= max_val for x in result))
    
    def test_generate_test_cases(self):
        """Test test case generation"""
        test_cases = generate_test_cases()
        
        # Check that all expected test cases exist
        expected_cases = [
            'random_small', 'random_medium', 'already_sorted',
            'reverse_sorted', 'duplicates', 'single_element',
            'empty', 'two_elements'
        ]
        
        for case in expected_cases:
            self.assertIn(case, test_cases)
        
        # Check specific test cases
        self.assertEqual(test_cases['empty'], [])
        self.assertEqual(len(test_cases['single_element']), 1)
        self.assertEqual(len(test_cases['two_elements']), 2)
        self.assertEqual(test_cases['already_sorted'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

class TestPerformance(unittest.TestCase):
    """Performance tests for the algorithm"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.merge_sort = MergeSort()
    
    def test_large_array_performance(self):
        """Test performance with large arrays"""
        # Test with different sizes
        sizes = [100, 500, 1000]
        
        for size in sizes:
            with self.subTest(size=size):
                input_array = generate_random_array(size)
                
                # Should complete without timeout
                result = self.merge_sort.merge_sort(input_array)
                
                # Should be correctly sorted
                self.assertEqual(result, sorted(input_array))
                self.assertEqual(len(result), size)
    
    def test_worst_case_performance(self):
        """Test performance in worst case scenarios"""
        # For merge sort, performance is consistent, but test with reverse sorted
        sizes = [50, 100, 200]
        
        for size in sizes:
            with self.subTest(size=size):
                # Reverse sorted array
                input_array = list(range(size, 0, -1))
                
                result = self.merge_sort.merge_sort(input_array, track_steps=True)
                stats = self.merge_sort.get_statistics()
                
                # Should be correctly sorted
                self.assertEqual(result, list(range(1, size + 1)))
                
                # Should have reasonable number of operations
                # For merge sort, comparisons should be approximately n * log(n)
                expected_comparisons = size * (size.bit_length() - 1)  # Rough estimate
                self.assertLessEqual(stats['comparisons'], expected_comparisons * 2)  # Allow some margin

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.merge_sort = MergeSort()
    
    def test_very_large_values(self):
        """Test with very large integer values"""
        input_array = [2**31 - 1, 2**30, 2**31 - 2]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_very_small_values(self):
        """Test with very small (negative) integer values"""
        input_array = [-2**31, -2**30, -2**31 + 1]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_mixed_positive_negative_zero(self):
        """Test with mix of positive, negative, and zero values"""
        input_array = [0, -5, 10, -1, 0, 3, -10]
        expected = sorted(input_array)
        result = self.merge_sort.merge_sort(input_array)
        self.assertEqual(result, expected)

def run_performance_benchmark():
    """Run a simple performance benchmark"""
    merge_sort = MergeSort()
    sizes = [10, 50, 100, 500, 1000]
    
    print("Performance Benchmark Results:")
    print("=" * 50)
    print(f"{'Size':<10} {'Comparisons':<15} {'Array Accesses':<15} {'Steps':<10}")
    print("-" * 50)
    
    for size in sizes:
        # Generate random array
        test_array = generate_random_array(size)
        
        # Sort with tracking
        merge_sort.merge_sort(test_array, track_steps=True)
        stats = merge_sort.get_statistics()
        
        print(f"{size:<10} {stats['comparisons']:<15} {stats['array_accesses']:<15} {stats['steps']:<10}")

if __name__ == '__main__':
    # Run unit tests
    print("Running Unit Tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    print("\n" + "="*60)
    
    # Run performance benchmark
    run_performance_benchmark()