<<<<<<< HEAD
# Sorting Algorithm Visualizer

An educational Python application that visualizes classic sorting algorithms step-by-step in either a command-line interface or a graphical interface. The project is designed to make sorting behavior observable, not just executable.

## Project Overview

`Sorting Algorithm Visualizer` renders the intermediate states of an array as it is sorted. Instead of returning only the final ordered output, each algorithm emits a sequence of frames representing comparisons, swaps, insertions, partitions, and merges.

This is useful for:
- learning how sorting algorithms transform data over time
- comparing algorithm strategies on identical input
- teaching complexity trade-offs with direct visual feedback
- debugging algorithm implementations at the operation level

## Features

- **Step-by-step visualization** of meaningful sorting events
- **Multiple algorithms**: Bubble Sort, Insertion Sort, QuickSort, and Merge Sort
- **Adjustable speed** for slow instructional playback or faster demonstrations
- **CLI or GUI support** using the same underlying algorithm implementations
- **Clean architecture** with a clear separation between sorting logic and rendering

## Demo / Example

Example CLI execution:

```/dev/null/terminal.sh#L1-1
python main.py --mode cli --algorithm bubble --data 5 3 8 1 4 --speed 0.25
```

In the CLI renderer, each line represents one element and the number of `#` characters corresponds to its value.

```/dev/null/examples/cli-output.txt#L1-22
Step 1  compare indices (0, 1)
5 | #####
3 | ###
8 | ########
1 | #
4 | ####

Step 2  swap indices (0, 1)
3 | ###
5 | #####
8 | ########
1 | #
4 | ####

Step 3  compare indices (2, 3)
3 | ###
5 | #####
8 | ########
1 | #
4 | ####

...
Final result: [1, 3, 4, 5, 8]
```

In GUI mode, the same algorithm states can be rendered as animated bars with highlighted indices, current pivot or merge range, and a configurable frame delay.

## Project Structure

A maintainable implementation keeps algorithm execution independent from visualization:

```/dev/null/tree.txt#L1-11
sorting-algorithm-visualizer/
├── algorithms/
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   └── merge_sort.py
├── visualizer/
│   ├── cli.py
│   └── gui.py
├── main.py
└── README.md
```

- `algorithms/`: generator-based sorting implementations that emit intermediate states
- `visualizer/`: rendering backends for terminal or GUI output
- `main.py`: entry point that parses arguments, selects the algorithm, initializes the renderer, and starts the visualization loop

## Installation

### Requirements

- Python `3.10+`
- CLI mode: no third-party dependency required
- GUI mode: `tkinter` (bundled with most CPython installations)

If your Python build does not include `tkinter`, install the Tk bindings provided by your operating system before using GUI mode.

### Setup

```/dev/null/setup.sh#L1-10
git clone https://github.com/your-username/sorting-algorithm-visualizer.git
cd sorting-algorithm-visualizer

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Run the application:

```/dev/null/run.sh#L1-1
python main.py --help
```

## Usage

### Run in CLI mode

```/dev/null/cli-usage.sh#L1-1
python main.py --mode cli --algorithm merge --data 9 4 7 1 3 --speed 0.15
```

### Run in GUI mode

```/dev/null/gui-usage.sh#L1-1
python main.py --mode gui --algorithm quick --size 30 --speed 0.05
```

### Common options

- `--algorithm`: sorting algorithm to execute (`bubble`, `insertion`, `quick`, `merge`)
- `--mode`: visualization backend (`cli`, `gui`)
- `--speed`: delay between frames in seconds; smaller values produce faster animation
- `--data`: explicit sequence of integers to sort
- `--size`: generate a random dataset when `--data` is not provided

Typical workflow:
1. Choose the interface with `--mode`
2. Choose the algorithm with `--algorithm`
3. Provide input using `--data` or generate it with `--size`
4. Tune playback with `--speed`

## How It Works

### Generators and `yield`

Each sorting algorithm is implemented as a generator. Instead of returning only a final array, it `yield`s the array state after each meaningful event. The visualizer consumes these yielded states and renders them frame by frame.

Minimal example:

```/dev/null/algorithms/bubble_sort.py#L1-13
def bubble_sort(data):
    arr = data[:]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            yield arr[:], {"event": "compare", "indices": (j, j + 1)}

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr[:], {"event": "swap", "indices": (j, j + 1)}

    yield arr[:], {"event": "done"}
```

The copy operation `arr[:]` is important: the generator yields stable snapshots instead of a shared mutable reference, so previously rendered frames are not overwritten by later mutations.

### Separation of concerns

The project is structured so that each layer has a single responsibility:

- **Algorithm layer**: computes sorting behavior and emits structured step data
- **Visualization layer**: renders that data as text bars, colored output, or GUI elements
- **Application layer**: handles configuration, argument parsing, input generation, and execution flow

A consistent event schema lets different renderers consume the same algorithm output without knowing the implementation details of the sort itself.

This separation provides clear benefits:
- algorithms can be unit tested without a UI
- new visualizers can be added without rewriting sorting logic
- new algorithms can plug into the existing rendering pipeline by emitting the same style of step data

## Algorithms Implemented

### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them when they are out of order. It is easy to understand and ideal for showing local swaps and repeated passes through the array.  
**Complexity:** best `O(n)` with early exit, average/worst `O(n²)`  
**Stability:** stable

### Insertion Sort

Insertion Sort builds a sorted prefix from left to right by shifting larger elements and inserting the current value into its correct position. It performs well on small or nearly sorted inputs.  
**Complexity:** best `O(n)`, average/worst `O(n²)`  
**Stability:** stable

### QuickSort

QuickSort uses a pivot to partition the array into smaller and larger elements, then recursively sorts the partitions. It is efficient in practice and visually highlights partitioning behavior.  
**Complexity:** average `O(n log n)`, worst `O(n²)`  
**Stability:** not stable

### Merge Sort

Merge Sort recursively splits the array into halves, sorts each half, and merges them back together. It is a canonical divide-and-conquer algorithm with predictable time complexity.  
**Complexity:** `O(n log n)` in best, average, and worst cases  
**Stability:** stable  
**Space:** `O(n)` auxiliary memory

## Future Improvements

- Add pause, resume, single-step, and reset controls in the GUI
- Improve visual cues for pivots, active subarrays, sorted regions, and merge buffers
- Implement additional algorithms such as Selection Sort, Heap Sort, Shell Sort, and Radix Sort
- Support side-by-side comparison of multiple algorithms on the same dataset
- Track metrics such as comparisons, swaps, elapsed time, and memory usage

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Keep sorting logic generator-based and renderer-independent
4. Add or update tests and documentation for any behavior change
5. Open a pull request with a clear technical summary

Contribution guidelines:
- keep algorithm implementations inside `algorithms/`
- keep rendering code inside `visualizer/`
- prefer focused pull requests over large mixed changes
- document new algorithms, flags, or event types in this README

## License

This project is licensed under the MIT License. See `LICENSE` for details.

=======
# sorting-algorithm-visualizer
>>>>>>> 4717747ccdfaa3536bf8d7e20ffafa94ce18f0d7
