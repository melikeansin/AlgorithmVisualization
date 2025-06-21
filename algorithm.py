"""
Merge Sort Algorithm Implementation
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class MergeSort:
    def __init__(self):
        self.steps = []
        self.comparisons = 0
        self.array_accesses = 0
    
    def merge_sort(self, arr, track_steps=False):
        """
        Main merge sort function
        
        Args:
            arr: List of elements to sort
            track_steps: Boolean to track steps for visualization
            
        Returns:
            Sorted array
        """
        if track_steps:
            self.steps = []
            self.comparisons = 0
            self.array_accesses = 0
        
        if len(arr) <= 1:
            return arr
        
        result = self._merge_sort_recursive(arr.copy(), 0, len(arr) - 1, track_steps)
        return result
    
    def _merge_sort_recursive(self, arr, left, right, track_steps):
        """
        Recursive merge sort implementation
        
        Args:
            arr: Array to sort
            left: Left index
            right: Right index
            track_steps: Track steps for visualization
            
        Returns:
            Sorted portion of array
        """
        if left >= right:
            return arr
        
        mid = (left + right) // 2
        
        if track_steps:
            self.steps.append({
                'type': 'divide',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'mid': mid,
                'description': f'Dividing array from index {left} to {right} at mid {mid}'
            })
        
        # Recursively sort left and right halves
        self._merge_sort_recursive(arr, left, mid, track_steps)
        self._merge_sort_recursive(arr, mid + 1, right, track_steps)
        
        # Merge the sorted halves
        self._merge(arr, left, mid, right, track_steps)
        
        return arr
    
    def _merge(self, arr, left, mid, right, track_steps):
        """
        Merge two sorted subarrays
        
        Args:
            arr: Main array
            left: Left index
            mid: Middle index
            right: Right index
            track_steps: Track steps for visualization
        """
        # Create temporary arrays for left and right subarrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        if track_steps:
            self.steps.append({
                'type': 'merge_start',
                'array': arr.copy(),
                'left': left,
                'mid': mid,
                'right': right,
                'left_subarray': left_arr.copy(),
                'right_subarray': right_arr.copy(),
                'description': f'Merging subarrays: {left_arr} and {right_arr}'
            })
        
        i = j = 0  # Initial indices for left and right subarrays
        k = left   # Initial index for merged subarray
        
        # Merge the temporary arrays back into arr[left..right]
        while i < len(left_arr) and j < len(right_arr):
            self.comparisons += 1
            self.array_accesses += 2
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                if track_steps:
                    self.steps.append({
                        'type': 'merge_step',
                        'array': arr.copy(),
                        'comparing': [left_arr[i], right_arr[j]],
                        'chosen': left_arr[i],
                        'position': k,
                        'description': f'Comparing {left_arr[i]} <= {right_arr[j]}, placing {left_arr[i]} at position {k}'
                    })
                i += 1
            else:
                arr[k] = right_arr[j]
                if track_steps:
                    self.steps.append({
                        'type': 'merge_step',
                        'array': arr.copy(),
                        'comparing': [left_arr[i], right_arr[j]],
                        'chosen': right_arr[j],
                        'position': k,
                        'description': f'Comparing {left_arr[i]} > {right_arr[j]}, placing {right_arr[j]} at position {k}'
                    })
                j += 1
            k += 1
            self.array_accesses += 1
        
        # Copy remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            if track_steps:
                self.steps.append({
                    'type': 'merge_remaining',
                    'array': arr.copy(),
                    'element': left_arr[i],
                    'position': k,
                    'description': f'Copying remaining element {left_arr[i]} to position {k}'
                })
            i += 1
            k += 1
            self.array_accesses += 1
        
        # Copy remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            if track_steps:
                self.steps.append({
                    'type': 'merge_remaining',
                    'array': arr.copy(),
                    'element': right_arr[j],
                    'position': k,
                    'description': f'Copying remaining element {right_arr[j]} to position {k}'
                })
            j += 1
            k += 1
            self.array_accesses += 1
        
        if track_steps:
            self.steps.append({
                'type': 'merge_complete',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'description': f'Completed merging from index {left} to {right}'
            })
    
    def get_complexity_info(self):
        """
        Return complexity analysis information
        
        Returns:
            Dictionary with complexity information
        """
        return {
            'time_complexity': 'O(n log n)',
            'space_complexity': 'O(n)',
            'time_explanation': 'The array is recursively divided log n times, and each level requires O(n) operations to merge.',
            'space_explanation': 'Additional space is needed for temporary arrays during the merge process.',
            'best_case': 'O(n log n)',
            'average_case': 'O(n log n)',
            'worst_case': 'O(n log n)',
            'stable': True,
            'in_place': False
        }
    
    def get_statistics(self):
        """
        Get performance statistics from last run
        
        Returns:
            Dictionary with statistics
        """
        return {
            'comparisons': self.comparisons,
            'array_accesses': self.array_accesses,
            'steps': len(self.steps)
        }

# Utility functions for testing and demonstration
def generate_random_array(size, min_val=1, max_val=100):
    """Generate a random array for testing"""
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_test_cases():
    """Generate various test cases"""
    return {
        'random_small': [64, 34, 25, 12, 22, 11, 90],
        'random_medium': generate_random_array(15),
        'already_sorted': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'reverse_sorted': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'duplicates': [5, 2, 8, 2, 9, 1, 5, 5],
        'single_element': [42],
        'empty': [],
        'two_elements': [3, 1]
    }