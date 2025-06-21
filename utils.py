"""
Utility functions for visualization and data processing
"""

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
from typing import List, Dict, Any
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def create_bar_chart(data: List[int], title: str = "Array Visualization", 
                    highlighted_indices: List[int] = None, 
                    colors: Dict[int, str] = None) -> go.Figure:
    """
    Create an interactive bar chart for array visualization
    
    Args:
        data: List of integers to visualize
        title: Chart title
        highlighted_indices: Indices to highlight
        colors: Dictionary mapping indices to colors
        
    Returns:
        Plotly Figure object
    """
    if not data:
        fig = go.Figure()
        fig.add_annotation(text="No data to display", 
                          xref="paper", yref="paper",
                          x=0.5, y=0.5, showarrow=False)
        return fig
    
    # Default colors
    bar_colors = ['lightblue'] * len(data)
    
    # Apply custom colors if provided
    if colors:
        for idx, color in colors.items():
            if 0 <= idx < len(data):
                bar_colors[idx] = color
    
    # Highlight specific indices
    if highlighted_indices:
        for idx in highlighted_indices:
            if 0 <= idx < len(data):
                bar_colors[idx] = 'red'
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(range(len(data))),
            y=data,
            marker_color=bar_colors,
            text=data,
            textposition='auto',
            hovertemplate='Index: %{x}<br>Value: %{y}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Index",
        yaxis_title="Value",
        showlegend=False,
        height=400
    )
    
    return fig

def create_step_visualization(step_data: Dict[str, Any], step_number: int) -> go.Figure:
    """
    Create visualization for a specific algorithm step
    
    Args:
        step_data: Dictionary containing step information
        step_number: Current step number
        
    Returns:
        Plotly Figure object
    """
    array = step_data.get('array', [])
    step_type = step_data.get('type', '')
    
    # Color coding based on step type
    colors = {}
    
    if step_type == 'divide':
        left = step_data.get('left', 0)
        right = step_data.get('right', len(array) - 1)
        mid = step_data.get('mid', (left + right) // 2)
        
        # Color the division points
        for i in range(left, mid + 1):
            colors[i] = 'lightgreen'
        for i in range(mid + 1, right + 1):
            colors[i] = 'lightcoral'
    
    elif step_type in ['merge_step', 'merge_remaining']:
        position = step_data.get('position')
        if position is not None:
            colors[position] = 'gold'
    
    elif step_type == 'merge_start':
        left = step_data.get('left', 0)
        right = step_data.get('right', len(array) - 1)
        mid = step_data.get('mid', (left + right) // 2)
        
        for i in range(left, mid + 1):
            colors[i] = 'lightgreen'
        for i in range(mid + 1, right + 1):
            colors[i] = 'lightcoral'
    
    title = f"Step {step_number}: {step_data.get('description', 'Algorithm Step')}"
    
    return create_bar_chart(array, title, colors=colors)

def create_complexity_chart() -> go.Figure:
    """
    Create a chart showing time complexity comparison
    
    Returns:
        Plotly Figure object
    """
    n_values = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
    
    # Different complexity functions
    constant = np.ones_like(n_values)
    linear = n_values
    nlogn = n_values * np.log2(n_values)
    quadratic = n_values ** 2
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=n_values, y=constant, mode='lines', name='O(1) - Constant'))
    fig.add_trace(go.Scatter(x=n_values, y=linear, mode='lines', name='O(n) - Linear'))
    fig.add_trace(go.Scatter(x=n_values, y=nlogn, mode='lines', name='O(n log n) - Merge Sort', 
                            line=dict(width=4, color='red')))
    fig.add_trace(go.Scatter(x=n_values, y=quadratic, mode='lines', name='O(n²) - Quadratic'))
    
    fig.update_layout(
        title="Time Complexity Comparison",
        xaxis_title="Input Size (n)",
        yaxis_title="Operations",
        xaxis=dict(type='log'),
        yaxis=dict(type='log'),
        height=500
    )
    
    return fig

def create_performance_metrics_chart(statistics: Dict[str, int], array_size: int) -> go.Figure:
    """
    Create a chart showing performance metrics
    
    Args:
        statistics: Dictionary with performance statistics
        array_size: Size of the sorted array
        
    Returns:
        Plotly Figure object
    """
    metrics = ['Comparisons', 'Array Accesses', 'Steps']
    values = [
        statistics.get('comparisons', 0),
        statistics.get('array_accesses', 0),
        statistics.get('steps', 0)
    ]
    
    # Theoretical values for comparison
    theoretical_comparisons = array_size * np.log2(array_size) if array_size > 0 else 0
    
    fig = go.Figure(data=[
        go.Bar(name='Actual', x=metrics, y=values, marker_color='lightblue'),
    ])
    
    # Add theoretical line for comparisons
    if array_size > 0:
        fig.add_hline(y=theoretical_comparisons, line_dash="dash", 
                     annotation_text=f"Theoretical O(n log n): {theoretical_comparisons:.0f}")
    
    fig.update_layout(
        title=f"Performance Metrics (Array Size: {array_size})",
        yaxis_title="Count",
        height=400
    )
    
    return fig

def format_array_display(array: List[int], max_display: int = 20) -> str:
    """
    Format array for display, truncating if too long
    
    Args:
        array: List to format
        max_display: Maximum number of elements to display
        
    Returns:
        Formatted string representation
    """
    if len(array) <= max_display:
        return str(array)
    else:
        return f"{array[:max_display//2]} ... {array[-max_display//2:]} (length: {len(array)})"

def generate_sample_data(data_type: str, size: int = 10) -> List[int]:
    """
    Generate sample data for testing
    
    Args:
        data_type: Type of data to generate
        size: Size of the array
        
    Returns:
        Generated array
    """
    import random
    
    if data_type == "Random":
        return [random.randint(1, 100) for _ in range(size)]
    elif data_type == "Sorted":
        return list(range(1, size + 1))
    elif data_type == "Reverse Sorted":
        return list(range(size, 0, -1))
    elif data_type == "Nearly Sorted":
        arr = list(range(1, size + 1))
        # Swap a few elements
        for _ in range(max(1, size // 10)):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif data_type == "Many Duplicates":
        return [random.randint(1, size // 3 + 1) for _ in range(size)]
    else:
        return [random.randint(1, 100) for _ in range(size)]

def create_algorithm_comparison_table() -> pd.DataFrame:
    """
    Create a comparison table of sorting algorithms
    
    Returns:
        Pandas DataFrame with algorithm comparisons
    """
    data = {
        'Algorithm': ['Merge Sort', 'Quick Sort', 'Bubble Sort', 'Selection Sort', 'Insertion Sort'],
        'Best Case': ['O(n log n)', 'O(n log n)', 'O(n)', 'O(n²)', 'O(n)'],
        'Average Case': ['O(n log n)', 'O(n log n)', 'O(n²)', 'O(n²)', 'O(n²)'],
        'Worst Case': ['O(n log n)', 'O(n²)', 'O(n²)', 'O(n²)', 'O(n²)'],
        'Space Complexity': ['O(n)', 'O(log n)', 'O(1)', 'O(1)', 'O(1)'],
        'Stable': ['Yes', 'No', 'Yes', 'No', 'Yes'],
        'In-Place': ['No', 'Yes', 'Yes', 'Yes', 'Yes']
    }
    
    return pd.DataFrame(data)

def display_step_info(step_data: Dict[str, Any]) -> None:
    """
    Display detailed information about a step
    
    Args:
        step_data: Dictionary containing step information
    """
    step_type = step_data.get('type', 'unknown')
    description = step_data.get('description', 'No description available')
    
    st.write(f"**Step Type:** {step_type.replace('_', ' ').title()}")
    st.write(f"**Description:** {description}")
    
    if step_type == 'divide':
        st.write(f"- Left index: {step_data.get('left')}")
        st.write(f"- Right index: {step_data.get('right')}")
        st.write(f"- Mid index: {step_data.get('mid')}")
    
    elif step_type == 'merge_step':
        comparing = step_data.get('comparing', [])
        chosen = step_data.get('chosen')
        position = step_data.get('position')
        if comparing and chosen is not None:
            st.write(f"- Comparing: {comparing[0]} and {comparing[1]}")
            st.write(f"- Chosen: {chosen}")
            st.write(f"- Placed at position: {position}")
    
    elif step_type == 'merge_start':
        left_sub = step_data.get('left_subarray', [])
        right_sub = step_data.get('right_subarray', [])
        st.write(f"- Left subarray: {left_sub}")
        st.write(f"- Right subarray: {right_sub}")

def export_results(algorithm_name: str, original_array: List[int], 
                  sorted_array: List[int], statistics: Dict[str, int]) -> str:
    """
    Export results to a formatted string
    
    Args:
        algorithm_name: Name of the algorithm
        original_array: Original unsorted array
        sorted_array: Sorted array
        statistics: Performance statistics
        
    Returns:
        Formatted results string
    """
    result = f"""
{algorithm_name} Results
{'=' * 50}

Original Array: {format_array_display(original_array)}
Sorted Array: {format_array_display(sorted_array)}

Performance Statistics:
- Array Size: {len(original_array)}
- Comparisons: {statistics.get('comparisons', 0)}
- Array Accesses: {statistics.get('array_accesses', 0)}
- Total Steps: {statistics.get('steps', 0)}

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
    return result