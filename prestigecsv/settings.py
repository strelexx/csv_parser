from psycopg2.extras import *
from prestigecsv.config import config, logger


def db_connect(sql_vals):
    """
    Connecting to the PostgreSQL database server
    """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        logger.debug("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        sql = 'INSERT INTO prop_land (line, file_name) VALUES %s'
        execute_values(cur=cur, sql=sql, argslist=sql_vals)
        # close the communication with the PostgreSQL
        conn.commit()
        logger.debug('Data inserted in DB...')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            logger.error('Database connection closed.')
