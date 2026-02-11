from functools import wraps
from flask import jsonify, g
from db.db_helpers import get_db_connection
import psycopg2.extras

def instructor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        connection =None
        cursor =None
        try:
            user_id = g.user["id"]  
            connection = get_db_connection()
            cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT role FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()

            if user is None:
                return jsonify({"error":"User not found"}), 404

            if user["role"] != "instructor":
                return jsonify({"error":"Access for instructors only"}), 403

            return f(*args, **kwargs)

        except Exception as err:
            return jsonify({"err": str(err)}), 500

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return decorated_function
