import click

# Command Group
@click.group(name='tools')
def cli_tools():
    """Tool related commands"""
    pass

@cli_tools.command(name='install', help='test install')
@click.option('--test1', default='1', help='test option')
def install_cmd(test1):
    click.echo('Hello world')

@cli_tools.command(name='search', help='test search')
@click.option('--test1', default='1', help='test option')
def search_cmd(test1):
    click.echo('Hello world')

if __name__ == '__main__':
    cli_tools()