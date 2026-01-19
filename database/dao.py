from database.DB_connect import DBConnect
from model.team import Team

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_years_from_1980():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT year 
                    FROM team
                    WHERE year>=1980
                    ORDER BY year
                    
                    """

        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_teams(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id, team_code, name
                    FROM team
                    where year=%s
                    
                        """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_salari(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT team_id, SUM(salary) AS salary
                        FROM salary
                        where year=%s
                        GROUP BY team_id

                            """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result