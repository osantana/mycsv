mycsv
=====

Export MySQL query results to local CSV file.


Usage::

    $ mycsv [-u username] [-p password] [-h hostname] [-p port] [-s query.sql] [-O output.csv]

If you omit `password` option you will got a prompt asking for the password
(password will not be echoed)::

    $ mycsv -O report.csv < report.sql
    Password []:

You can send SQL script using `stdin` and dump CSV results to `stdout`::

    $ mycsv -p Sekr3T < report.sql > report.csv

