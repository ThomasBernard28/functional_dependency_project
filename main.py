import click

@click.group()
def main():
    """
    DB project 2021-2022.\n\n
    thomas.BERNARD@student.umons.ac.be - theo.GODIN@student.umons.ac.be
    """

@main.command("example")
def example():
    click.echo("This is an example.")

if __name__ == '__main__':
    main()
