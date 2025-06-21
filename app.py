"""
Merge Sort Algorithm Visualization
Interactive Streamlit Application
"""

import streamlit as st
import time
from algorithm import MergeSort, generate_test_cases
from utils import (
    create_bar_chart, create_step_visualization, create_complexity_chart,
    create_performance_metrics_chart, format_array_display, generate_sample_data,
    create_algorithm_comparison_table, display_step_info, export_results
)

# Page configuration
st.set_page_config(
    page_title="Merge Sort Visualizer",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling and readability
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #ffffff;
        color: #FFD700;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .info-box h3 {
        color: #1f77b4;
        margin-top: 0;
    }
    .info-box h4 {
        color: #FFD700;
        margin-top: 1rem;
    }
    .info-box p, .info-box li {
        color: #FFD700;
        line-height: 1.6;
    }
    .success-box {
        background-color: #ffffff;
        color: #FFD700;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #c3e6cb;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .success-box h4 {
        color: #28a745;
        margin-top: 0;
    }
    .success-box p, .success-box li {
        color: #FFD700;
        line-height: 1.6;
    }
    .warning-box {
        background-color: #ffffff;
        color: #FFD700;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #ffb347;
        border-left: 4px solid #ff6b35;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .warning-box h4 {
        color: #ff6b35;
        margin-top: 0;
    }
    .warning-box p, .warning-box li {
        color: #FFD700;
        line-height: 1.6;
    }
    /* Improve general text readability */
    .stMarkdown {
        color: #FFD700;
    }
    /* Make sure all text in info boxes is readable */
    .info-box *, .success-box *, .warning-box * {
        color: #FFD700 !important;
    }
    .info-box h3, .info-box h4 {
        color: #1f77b4 !important;
    }
    .success-box h3, .success-box h4 {
        color: #28a745 !important;
    }
    .warning-box h3, .warning-box h4 {
        color: #ff6b35 !important;
    }
    /* Override for overview text - make it black for better readability */
    .overview-box p, .overview-box li {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🔄 Merge Sort Algorithm Visualizer</h1>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'merge_sort' not in st.session_state:
        st.session_state.merge_sort = MergeSort()
    if 'sorted_array' not in st.session_state:
        st.session_state.sorted_array = None
    if 'steps' not in st.session_state:
        st.session_state.steps = []
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    
    # Sidebar for controls
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Input method selection
        input_method = st.radio(
            "Choose input method:",
            ["Generate Data", "Manual Input", "Predefined Examples"]
        )
        
        if input_method == "Generate Data":
            data_type = st.selectbox(
                "Data type:",
                ["Random", "Sorted", "Reverse Sorted", "Nearly Sorted", "Many Duplicates"]
            )
            array_size = st.slider("Array size:", 5, 50, 10)
            if st.button("Generate Array"):
                st.session_state.input_array = generate_sample_data(data_type, array_size)
                st.session_state.sorted_array = None
                st.session_state.steps = []
                st.session_state.current_step = 0
        
        elif input_method == "Manual Input":
            manual_input = st.text_input(
                "Enter numbers (comma-separated):",
                placeholder="e.g., 64,34,25,12,22,11,90"
            )
            if manual_input and st.button("Use Manual Input"):
                try:
                    st.session_state.input_array = [int(x.strip()) for x in manual_input.split(',')]
                    st.session_state.sorted_array = None
                    st.session_state.steps = []
                    st.session_state.current_step = 0
                except ValueError:
                    st.error("Please enter valid integers separated by commas.")
        
        else:  # Predefined Examples
            test_cases = generate_test_cases()
            selected_case = st.selectbox("Choose example:", list(test_cases.keys()))
            if st.button("Load Example"):
                st.session_state.input_array = test_cases[selected_case].copy()
                st.session_state.sorted_array = None
                st.session_state.steps = []
                st.session_state.current_step = 0
        
        st.markdown("---")
        
        # Algorithm controls
        st.header("🚀 Algorithm Controls")
        
        if 'input_array' in st.session_state and st.session_state.input_array:
            if st.button("🔄 Sort Array", type="primary"):
                with st.spinner("Sorting array..."):
                    # Run merge sort with step tracking
                    input_copy = st.session_state.input_array.copy()
                    st.session_state.sorted_array = st.session_state.merge_sort.merge_sort(
                        input_copy, track_steps=True
                    )
                    st.session_state.steps = st.session_state.merge_sort.steps
                    st.session_state.current_step = 0
                    st.success("Array sorted successfully!")
            
            if st.session_state.steps:
                st.markdown("### 👀 Step-by-Step Visualization")
                
                # Step navigation
                total_steps = len(st.session_state.steps)
                st.session_state.current_step = st.slider(
                    "Step:", 0, total_steps - 1, st.session_state.current_step
                )
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("⏮️ First"):
                        st.session_state.current_step = 0
                        st.rerun()
                with col2:
                    if st.button("⏪ Previous") and st.session_state.current_step > 0:
                        st.session_state.current_step -= 1
                        st.rerun()
                with col3:
                    if st.button("⏩ Next") and st.session_state.current_step < total_steps - 1:
                        st.session_state.current_step += 1
                        st.rerun()
                
                # Auto-play functionality
                if st.checkbox("🎬 Auto-play"):
                    speed = st.slider("Speed (seconds per step):", 0.1, 3.0, 1.0, 0.1)
                    if st.button("▶️ Start Auto-play"):
                        progress_bar = st.progress(0)
                        for i in range(st.session_state.current_step, total_steps):
                            st.session_state.current_step = i
                            progress_bar.progress((i + 1) / total_steps)
                            time.sleep(speed)
                            st.rerun()
    
    # Main content area
    if 'input_array' not in st.session_state:
        st.session_state.input_array = [64, 34, 25, 12, 22, 11, 90]  # Default array
    
    # Display current array
    st.markdown('<h2 class="sub-header">📊 Current Array</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Original Array:**")
        st.code(format_array_display(st.session_state.input_array))
        
        # Display original array visualization
        if st.session_state.input_array:
            fig_original = create_bar_chart(
                st.session_state.input_array, 
                "Original Array"
            )
            st.plotly_chart(fig_original, use_container_width=True)
    
    with col2:
        if st.session_state.sorted_array is not None:
            st.markdown("**Sorted Array:**")
            st.code(format_array_display(st.session_state.sorted_array))
            
            # Display sorted array visualization
            fig_sorted = create_bar_chart(
                st.session_state.sorted_array, 
                "Sorted Array",
                colors={i: '#28a745' for i in range(len(st.session_state.sorted_array))}
            )
            st.plotly_chart(fig_sorted, use_container_width=True)
        else:
            st.info("Click 'Sort Array' to see the sorted result!")
    
    # Step-by-step visualization
    if st.session_state.steps:
        st.markdown('<h2 class="sub-header">🎯 Step-by-Step Visualization</h2>', unsafe_allow_html=True)
        
        current_step_data = st.session_state.steps[st.session_state.current_step]
        
        # Display step visualization
        fig_step = create_step_visualization(current_step_data, st.session_state.current_step + 1)
        st.plotly_chart(fig_step, use_container_width=True)
        
        # Navigation buttons below the visualization
        total_steps = len(st.session_state.steps)
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        
        with col1:
            if st.button("⏮️ First Step", key="first_bottom"):
                st.session_state.current_step = 0
                st.rerun()
        
        with col2:
            if st.button("⏪ Previous", key="prev_bottom") and st.session_state.current_step > 0:
                st.session_state.current_step -= 1
                st.rerun()
        
        with col3:
            st.write(f"**{st.session_state.current_step + 1} / {total_steps}**")
        
        with col4:
            if st.button("⏩ Next", key="next_bottom") and st.session_state.current_step < total_steps - 1:
                st.session_state.current_step += 1
                st.rerun()
        
        with col5:
            if st.button("⏭️ Last Step", key="last_bottom"):
                st.session_state.current_step = total_steps - 1
                st.rerun()
        
        # Display step information
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Step Details")
            display_step_info(current_step_data)
        
        with col2:
            st.markdown("### Progress")
            progress = (st.session_state.current_step + 1) / len(st.session_state.steps)
            st.progress(progress)
            st.write(f"Step {st.session_state.current_step + 1} of {len(st.session_state.steps)}")
    
    # Performance metrics
    if st.session_state.sorted_array is not None:
        st.markdown('<h2 class="sub-header">📈 Performance Analysis</h2>', unsafe_allow_html=True)
        
        statistics = st.session_state.merge_sort.get_statistics()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Performance metrics chart
            fig_metrics = create_performance_metrics_chart(
                statistics, len(st.session_state.input_array)
            )
            st.plotly_chart(fig_metrics, use_container_width=True)
        
        with col2:
            # Statistics display
            st.markdown("### 📊 Statistics")
            st.metric("Array Size", len(st.session_state.input_array))
            st.metric("Comparisons", statistics['comparisons'])
            st.metric("Array Accesses", statistics['array_accesses'])
            st.metric("Total Steps", statistics['steps'])
            
            # Export results
            if st.button("📥 Export Results"):
                results_text = export_results(
                    "Merge Sort", 
                    st.session_state.input_array,
                    st.session_state.sorted_array,
                    statistics
                )
                st.download_button(
                    label="Download Results",
                    data=results_text,
                    file_name="merge_sort_results.txt",
                    mime="text/plain"
                )
    
    # Algorithm information
    st.markdown('<h2 class="sub-header">🧠 Algorithm Information</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📖 Overview", "⚡ Complexity", "🔍 Comparison"])
    
    with tab1:
        st.markdown("""
        <div class="info-box overview-box">
        <h3>Merge Sort Algorithm</h3>
        <p>Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, 
        recursively sorts them, and then merges the sorted halves to produce the final sorted array.</p>
        
        <h4>How it works:</h4>
        <ol>
            <li><strong>Divide:</strong> Split the array into two halves</li>
            <li><strong>Conquer:</strong> Recursively sort both halves</li>
            <li><strong>Combine:</strong> Merge the sorted halves back together</li>
        </ol>
        
        <h4>Key Properties:</h4>
        <ul>
            <li>✅ <strong>Stable:</strong> Maintains relative order of equal elements</li>
            <li>❌ <strong>Not In-Place:</strong> Requires additional memory</li>
            <li>⚡ <strong>Consistent:</strong> Same performance regardless of input</li>
            <li>🔄 <strong>Recursive:</strong> Uses divide-and-conquer approach</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        complexity_info = st.session_state.merge_sort.get_complexity_info()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="info-box overview-box">
            <h4>Time Complexity</h4>
            <ul>
                <li><strong>Best Case:</strong> {complexity_info['best_case']}</li>
                <li><strong>Average Case:</strong> {complexity_info['average_case']}</li>
                <li><strong>Worst Case:</strong> {complexity_info['worst_case']}</li>
            </ul>
            <p>{complexity_info['time_explanation']}</p>
            
            <h4>Space Complexity</h4>
            <p><strong>{complexity_info['space_complexity']}</strong></p>
            <p>{complexity_info['space_explanation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Complexity comparison chart
            fig_complexity = create_complexity_chart()
            st.plotly_chart(fig_complexity, use_container_width=True)
    
    with tab3:
        st.markdown("### Sorting Algorithm Comparison")
        comparison_df = create_algorithm_comparison_table()
        st.dataframe(comparison_df, use_container_width=True)
        
        st.markdown("""
        <div class="info-box overview-box">
        <h4>Why Choose Merge Sort?</h4>
        <ul>
            <li>🎯 <strong>Predictable Performance:</strong> Always O(n log n), regardless of input</li>
            <li>🔄 <strong>Stable Sorting:</strong> Preserves order of equal elements</li>
            <li>📏 <strong>Good for Large Datasets:</strong> Efficient for large arrays</li>
            <li>🧵 <strong>Parallelizable:</strong> Can be easily parallelized</li>
            <li>📚 <strong>External Sorting:</strong> Works well for sorting data that doesn't fit in memory</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()