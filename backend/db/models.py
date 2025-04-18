from backend.db.database import cursor, conn
import os

def insert_function(name, language, code, timeout):
    cursor.execute("""
        INSERT INTO functions (name, language, code, timeout)
        VALUES (?, ?, ?, ?)
    """, (name, language, code, timeout))
    conn.commit()
    return cursor.lastrowid

def get_all_functions():
    cursor.execute("SELECT * FROM functions")
    return cursor.fetchall()

def delete_function_by_id(function_id):
    try:
        # Check if function exists first
        cursor.execute("SELECT id FROM functions WHERE id = ?", (function_id,))
        if not cursor.fetchone():
            return False
            
        cursor.execute("DELETE FROM functions WHERE id = ?", (function_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting function: {str(e)}")
        conn.rollback()
        return False

def log_execution(function_id, exec_time, mem_usage, cpu_percent, status):
    cursor.execute("""
        INSERT INTO executions (function_id, execution_time, memory_usage, cpu_percent, status)
        VALUES (?, ?, ?, ?, ?)
    """, (function_id, exec_time, mem_usage, cpu_percent, status))
    conn.commit()

def get_execution_logs(function_id):
    cursor.execute("""
        SELECT * FROM executions WHERE function_id = ? ORDER BY timestamp DESC
    """, (function_id,))
    return cursor.fetchall()

def get_function_id_by_path(file_path):
    cursor.execute("""
        SELECT id FROM functions WHERE file_path = ?
    """, (file_path,))
    row = cursor.fetchone()
    return row[0] if row else None

def get_aggregated_metrics(function_id):
    cursor.execute("""
        SELECT 
            COUNT(*) as total_runs,
            AVG(execution_time) as avg_exec_time,
            AVG(CAST(memory_usage AS FLOAT)) as avg_memory_usage,
            AVG(CAST(cpu_percent AS FLOAT)) as avg_cpu_percent,
            MAX(timestamp) as last_run_time
        FROM executions
        WHERE function_id = ?
    """, (function_id,))
    row = cursor.fetchone()
    if row:
        return {
            "function_id": function_id,
            "total_runs": row[0],
            "avg_exec_time": round(row[1], 4) if row[1] else 0,
            "avg_memory_usage": round(row[2], 2) if row[2] else 0,
            "avg_cpu_percent": round(row[3], 2) if row[3] else 0,
            "last_run_time": row[4]
        }
    return None

def update_function_code(function_id, new_code):
    cursor.execute("""
        UPDATE functions SET code = ? WHERE id = ?
    """, (new_code, function_id))
    conn.commit()

def get_function_code(function_id):
    cursor.execute("""
        SELECT code FROM functions WHERE id = ?
    """, (function_id,))
    row = cursor.fetchone()
    return row[0] if row else None