import click

# Command Group
@click.group(name='evaluation')
def cli_evaluation():
    """Tool related commands"""
    pass

@cli_evaluation.command(name='install2', help='test install')
@click.option('--test1', default='1', help='test option')
def install_cmd(test1):
    click.echo('Hello world')

@cli_evaluation.command(name='search2', help='test search')
@click.option('--test1', default='1', help='test option')
def search_cmd(test1):
    click.echo('Hello world')

if __name__ == '__main__':
    cli_evaluation()