from rich.console import Console
console = Console()

def rich_divider(title="", color="magenta", width=20, space_lines=2):
    console.print("\n" * space_lines, end="")


    console.print("=" * (width * 2 + len(title) + 2))


    if title.strip():
        formatted_title = f"[bold {color}]{title}[/bold {color}]"
        total_length = width * 2 + len(title) + 2
        side_length = (total_length - len(title) - 2) // 2
        console.print("=" * side_length + f" {formatted_title} " + "=" * side_length)
    else:
        console.print("=" * (width * 2 + len(title) + 2))


    console.print("=" * (width * 2 + len(title) + 2))
    console.print("\n" * space_lines, end="")