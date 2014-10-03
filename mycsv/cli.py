# coding: utf-8

import sys
import csv

import MySQLdb
import click
from _mysql import OperationalError, ProgrammingError

DEFAULT_CONNECTION_TIMEOUT = 3  # seconds


def get_db(host, port, user, password, database):
    return MySQLdb.connect(host, user, password, database, port=port, connect_timeout=DEFAULT_CONNECTION_TIMEOUT)


def export(db, query, output):

    cursor = db.cursor()
    cursor.execute(query)

    writer = csv.writer(output)
    writer.writerow([col[0] for col in cursor.description])
    for row in cursor:
        writer.writerow(row)

@click.command()
@click.option("-u", "--user", envvar="USER", help="User for login if not current user")
@click.option("-p", "--password", default="", prompt=True, hide_input=True,help="Password to use when connecting to server")
@click.option("-h", "--host", default="localhost", show_default=True, help="Connect to host")
@click.option("-P", "--port", default=3306, type=int, show_default=True, help="Port number to use for connection")
@click.option("-s", "--script", default="-", type=click.File("r"), show_default=True, help="Input SQL script file")
@click.option("-O", "--output", default="-", type=click.File("w"), show_default=True, help="Output CSV file")
@click.argument("database", nargs=1)
def main(user, password, host, port, script, output, database):
    if script.isatty():
        click.echo("ERROR: Nothing to run in stdin", err=True)
        sys.exit(1)

    try:
        db = get_db(host=host, port=port, user=user, password=password, database=database)
    except OperationalError as ex:
        click.echo("ERROR: Cannot connect MySQL Server: {}".format(ex))
        return

    query = script.read()
    try:
        export(db, query, output)
    except ProgrammingError as ex:
        click.echo("ERROR: Script Error: {}".format(ex))
        return

    output.close()
    db.close()
