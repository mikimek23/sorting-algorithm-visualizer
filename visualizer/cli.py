from rich.console import Console
'''
events:
- current
- pivot
- compare
- swap
- partition
- no_swap
- swap_pivot
- pivot_fixed
- left_partition
- right_partition
'''
def display_data(data, indices,sorted_nums, color = 'white'):
    for i in range(len(data)):
        if i in indices:
            console.print(f"[{color}]{data[i]:<2}[/{color}]| {'#'*data[i]}")
        elif i in sorted_nums:
            console.print(f"[green]{data[i]:<2}| {'#'*data[i]}[/green]")
        else:
            print(f"{data[i]:<2}| {'#'*data[i]}")
console = Console()
def cli_visualizer(generator, data):
    sorted_nums = []
    for step, events in enumerate(generator,1):
        event, *indices = events
        match event:
            case 'current':
                print(f"step {step} current range {indices}\n")
                display_data(data, indices,sorted_nums, 'blue')
            case 'pivot':
                print(f'Step {step} pivot {indices}\n')
                display_data(data, indices,sorted_nums, 'green')
            case 'compare':
                print(f'Step {step} compare indices {indices}\n')
                display_data(data, indices,sorted_nums, 'yellow')
            case 'swap':
                print(f'Step {step} swap indices {indices}\n')
                display_data(data, indices,sorted_nums, 'green')
            case 'no_swap':
               console.print(f'Step {step} [orange1] no swap indices {indices}[/orange1]\n')
            case 'swap_pivot':
                sorted_nums.append(indices[0])
                console.print(f'Step {step} [green] pivot swap indices {indices}[/green]\n')
                display_data(data, indices[:len(indices)-1],sorted_nums, 'green')
            case 'left_partition':
                console.print(f'Step {step} [green] recursion in range  {indices}[/green]\n')
            case 'right_partition':
                console.print(f'Step {step} [green] recursion in range  {indices}[/green]\n')

    console.print(f"\n[bold blue]Final result[/bold blue]\n")
    for i in range(len(data)):
        console.print(f"[green]{data[i]:<2}| {'#'*data[i]}[/green]")
        






                

