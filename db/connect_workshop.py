from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connect_workshop_2():
    conn = connect(user="oleksandrvovk", password="coderslab", host="localhost", database="warsztat_war_pyt_s_12")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn