from data_utils.connect_db import DB
from sqlalchemy import text
import pandas as pd
import time

import os

class FromDB:
    """
    Runs queries against a database.

    Args:
        db_type (string): The type of database e.g. postgres.
        db (string): The database credential in the .env file.

    Attributes:
        connector (object): An SQLAlchemy engine object.
        engine (object): The sqlalchemy engine object for running queries.
    """
    def __init__(self, db_type, db):
        self.engine = DB(db_type, db).engine

    def RunQuery(self, sqlquery, to_csv=False, filename=None):
        """
        Runs a text query, returns data, and gives the option of saving it to a CSV.

        Args:
           sqlquery (string): Multi line string query.
           to_csv (boolean): If True, data is stored to CSV.

        Returns:
            data (dataframe): A pandas dataframe
            file (CSV): Writes a CSV with the specified filename
        """

        # create the connection and run the query
        conn = self.engine.connect()
        query = text(sqlquery)
        data = pd.read_sql_query(query, conn)

        # close the connection
        conn.close()

        if to_csv == True:
            if filename is None:
                raise ValueError('CSV filename cannot be blank.')
            else:
                data.to_csv(filename, encoding='utf-8')
                return data

        return data