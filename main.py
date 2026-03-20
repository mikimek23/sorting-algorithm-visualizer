import argparse
from random import randint
from algorithms.quick_sort import quick_Sort
default_data = [randint(1, 100) for _ in range(5)]
parser = argparse.ArgumentParser(
    description="Visualize sorting algorithms step-by-step in CLI or GUI mode.",
    epilog="Example: python main.py --mode cli --algorithm quick --data 5 3 8 1 --speed 0.5",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "-m",
    "--mode",
    type=str,
    choices=["cli", "gui"],
    default="cli",
    help="Visualization mode: 'cli' for terminal output, 'gui' for graphical interface (if implemented).",
)
parser.add_argument(
    "-a",
    "--algorithm",
    type=str,
    choices=["quick", "merge"],
    default="quick",
    help="Sorting algorithm to use: 'quick' (QuickSort) or 'merge' (MergeSort).",
)
parser.add_argument(
    "-d",
    "--data",
    type=int,
    nargs="+",
    default=default_data,
    help="List of integers to sort. Example: --data 5 3 8 1",
)
parser.add_argument(
    "-s",
    "--speed",
    type=float,
    choices=[1.5, 1, 0.5, 0.25],
    default=1,
    help="Delay between steps in seconds. Lower = faster visualization.",
)
user_input=parser.parse_args()
dic_input = vars(user_input)
mode, algorithm, data, speed  = (user_input.mode, user_input.algorithm, user_input.data, user_input.speed)
algorithms = {
    'quick':quick_Sort,
}
selected_algorithm = algorithms[algorithm]
generator = selected_algorithm(data, 0, len(data)-1)
if mode == "cli":
    for result in generator:
        print(result)

else:
    print("coming soon")