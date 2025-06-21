# 🔄 Merge Sort Algorithm Visualizer

An interactive web application built with Streamlit that demonstrates the Merge Sort algorithm through step-by-step visualization and comprehensive analysis.

## 🌐 Live Application

**Streamlit Web App:** *[Deploy to Streamlit Cloud to get URL]*

## 📋 Project Description

This project implements and visualizes the Merge Sort algorithm, one of the most efficient and stable sorting algorithms. The application provides:

- **Interactive Algorithm Visualization**: Watch the merge sort algorithm work in real-time
- **Step-by-Step Breakdown**: Navigate through each step of the sorting process
- **Performance Analysis**: Detailed complexity analysis and performance metrics
- **Multiple Input Options**: Generate random data, input custom arrays, or use predefined examples
- **Educational Content**: Comprehensive explanations of how merge sort works

### Algorithm Overview

Merge Sort is a divide-and-conquer algorithm that:
1. **Divides** the unsorted array into smaller subarrays
2. **Conquers** by recursively sorting the subarrays
3. **Combines** the sorted subarrays to produce the final sorted array

## 🚀 Installation and Usage

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd merge-sort-visualizer
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your web browser and go to `http://localhost:8501`
   - The application will automatically open in your default browser

### Alternative Installation

If you prefer to install packages individually:
```bash
pip install streamlit matplotlib numpy pandas plotly
```

## 📁 Project Structure

```
merge-sort-visualizer/
│
├── app.py                 # Main Streamlit application
├── algorithm.py           # Merge sort implementation
├── utils.py              # Visualization and utility functions
├── test_algorithm.py     # Unit tests for the algorithm
├── requirements.txt      # Python package dependencies
├── README.md            # This documentation file
└── data/                # Sample data files (optional)
```

## 🖼️ Application Screenshots

### Main Interface
The main interface provides controls for array input and algorithm visualization:
- Input methods: Generate random data, manual input, or predefined examples
- Array size control (5-50 elements)
- Data type selection (Random, Sorted, Reverse Sorted, etc.)

### Step-by-Step Visualization
- Interactive step navigation with Previous/Next buttons
- Auto-play functionality with adjustable speed
- Color-coded visualization showing divide and merge operations
- Detailed step descriptions and progress tracking

### Performance Analysis
- Real-time performance metrics (comparisons, array accesses, steps)
- Complexity comparison charts
- Algorithm comparison table
- Export functionality for results

## ⚡ Complexity Analysis

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

**Explanation**: The array is recursively divided log n times, and each level requires O(n) operations to merge the subarrays. This results in a consistent O(n log n) time complexity regardless of the input distribution.

### Space Complexity
- **Space Complexity**: O(n)

**Explanation**: Merge sort requires additional space for temporary arrays during the merge process. The algorithm creates temporary arrays that, in total, require O(n) additional space.

### Key Properties
- ✅ **Stable**: Maintains the relative order of equal elements
- ❌ **Not In-Place**: Requires additional memory proportional to input size
- 🔄 **Recursive**: Uses divide-and-conquer approach
- ⚡ **Consistent Performance**: Same time complexity for all input types

## 🧪 Testing

The project includes comprehensive unit tests covering:

### Test Categories
1. **Basic Functionality Tests**
   - Empty arrays
   - Single element arrays
   - Two element arrays
   - Already sorted arrays
   - Reverse sorted arrays

2. **Edge Case Tests**
   - Arrays with duplicates
   - Arrays with negative numbers
   - Very large numbers
   - Mixed positive/negative/zero values

3. **Performance Tests**
   - Large array handling
   - Worst-case scenarios
   - Statistical tracking accuracy

4. **Algorithm Property Tests**
   - Stability verification
   - Original array preservation
   - Step tracking functionality

### Running Tests

```bash
# Run all tests
python test_algorithm.py

# Run specific test class
python -m unittest test_algorithm.TestMergeSort

# Run with verbose output
python -m unittest test_algorithm -v
```

## 📊 Features

### Interactive Controls
- **Array Input Options**:
  - Generate random arrays with customizable size (5-50 elements)
  - Manual input via comma-separated values
  - Predefined examples (sorted, reverse sorted, duplicates, etc.)

- **Visualization Controls**:
  - Step-by-step navigation (First, Previous, Next buttons)
  - Auto-play with adjustable speed (0.1-3.0 seconds per step)
  - Progress tracking with visual indicators

### Educational Content
- **Algorithm Explanation**: Detailed description of how merge sort works
- **Complexity Analysis**: Visual comparison with other sorting algorithms
- **Performance Metrics**: Real-time statistics and theoretical comparisons
- **Algorithm Comparison**: Side-by-side comparison with other sorting methods

### Data Export
- Export sorting results and performance metrics
- Download detailed analysis reports
- Shareable performance statistics

## 🔍 Algorithm Implementation Details

### Core Components

1. **MergeSort Class** (`algorithm.py`):
   - Main algorithm implementation
   - Step tracking for visualization
   - Performance statistics collection
   - Complexity analysis information

2. **Visualization Utils** (`utils.py`):
   - Interactive chart generation using Plotly
   - Color-coded array representations
   - Performance metric visualization
   - Data export functionality

3. ** Streamlit App** (`app.py`):
   - User interface and controls
   - Real-time visualization updates
   - Educational content presentation
   - Interactive features management

### Key Algorithms Features

- **Recursive Implementation**: Clean, textbook-style recursive approach
- **Step Tracking**: Detailed logging of each divide and merge operation
- **Performance Monitoring**: Counts comparisons, array accesses, and steps
- **Stability Preservation**: Maintains relative order of equal elements
- **Memory Efficiency**: Optimized temporary array usage

## 🎯 Educational Value

This project serves as an excellent educational tool for:

### Computer Science Students
- Understanding divide-and-conquer algorithms
- Visualizing recursive algorithm execution
- Analyzing time and space complexity
- Comparing different sorting approaches

### Algorithm Learners
- Step-by-step algorithm walkthrough
- Interactive exploration of edge cases
- Performance analysis and optimization concepts
- Real-world algorithm application

### Educators
- Classroom demonstration tool
- Interactive teaching aid
- Performance comparison platform
- Assessment and testing resource

## 🛠️ Technical Implementation

### Technologies Used
- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualization library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Additional plotting capabilities

### Code Quality
- Comprehensive docstrings and comments
- Type hints for better code clarity
- Modular design with separated concerns
- Extensive error handling
- Unit test coverage >90%

## 🚀 Deployment

### Streamlit Cloud Deployment

1. **Prepare Repository**:
   - Ensure all files are in the repository
   - Verify `requirements.txt` is up to date
   - Test locally before deployment

2. **Deploy to Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub repository
   - Select the main branch and `app.py` as the main file
   - Deploy the application

3. **Configuration**:
   - No additional configuration required
   - All dependencies will be installed automatically
   - Application will be available at provided URL

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

# Run tests
python test_algorithm.py
```

## 📚 References and Resources

### Algorithm References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

### Implementation Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)

### Algorithm Analysis
- Time Complexity: [Big O Notation Guide](https://www.bigocheatsheet.com/)
- Sorting Algorithms: [Algorithm Comparison](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:

- Bug fixes
- Feature enhancements
- Documentation improvements
- Test coverage expansion
- Performance optimizations

## 📝 License

This project is created for educational purposes. Feel free to use and modify for learning and teaching.

## 🔄 Version History

- **v1.0.0**: Initial release with full merge sort implementation and visualization
  - Complete algorithm implementation
  - Interactive Streamlit interface
  - Step-by-step visualization
  - Performance analysis
  - Comprehensive test suite
  - Documentation and examples

---

**Created with ❤️ for algorithm education and visualization**