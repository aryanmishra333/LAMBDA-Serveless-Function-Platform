import sqlite3
from typing import Union
from fastapi import APIRouter, Form, HTTPException
from backend.schemas.function_schema import FunctionCreate
from backend.db.models import insert_function, get_all_functions, delete_function_by_id
from backend.schemas.function_schema import FunctionUpdate
from backend.db.models import update_function_code, get_function_code
from backend.db.models import get_aggregated_metrics
from backend.core.docker_executor import run_function_in_container
from backend.db.models import get_execution_logs

router = APIRouter()

conn = sqlite3.connect("functions.db", check_same_thread=False)
cursor = conn.cursor()

@router.post("/functions/")
async def upload_function(data: FunctionCreate):
    function_id = insert_function(data.name, data.language, data.code, data.timeout)
    return {"message": "Function uploaded successfully", "function_id": function_id}


@router.get("/functions/")
async def list_functions():
    return get_all_functions()

@router.post("/functions/{function_id}/run")
async def run_function(function_id: int, use_gvisor: bool = False):
    cursor.execute("SELECT language, timeout FROM functions WHERE id = ?", (function_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Function not found")
    
    language, timeout = row
    performance_data = run_function_in_container(function_id, language, timeout, use_gvisor)
    return performance_data


@router.delete("/functions/{function_id}")
async def delete_function(function_id: int):
    try:
        success = delete_function_by_id(function_id)
        if success:
            return {"message": f"Function {function_id} deleted successfully"}
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Function with ID {function_id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error deleting function: {str(e)}"
        )

@router.put("/functions/{function_id}")
async def update_function(function_id: int, update: FunctionUpdate):
    try:
        update_function_code(function_id, update.code)
        return {"message": "Function code updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/functions/{function_id}/logs")
def fetch_logs(function_id: int):
    logs = get_execution_logs(function_id)
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found for the specified function ID")
    return logs

@router.get("/functions/{function_id}/metrics")
def aggregated_metrics(function_id: Union[int, None]):
    if function_id is None:
        return {
            "total_runs": 0,
            "avg_exec_time": 0,
            "avg_memory_usage": 0,
            "avg_cpu_percent": 0,
            "last_run_time": None
        }
    metrics = get_aggregated_metrics(function_id)
    if not metrics:
        return {
            "total_runs": 0,
            "avg_exec_time": 0,
            "avg_memory_usage": 0,
            "avg_cpu_percent": 0,
            "last_run_time": None
        }
    return metrics

@router.get("/functions/{function_id}/code")
async def get_function_code_view(function_id: int):
    code = get_function_code(function_id)
    if code is None:
        raise HTTPException(status_code=404, detail="Function not found")
    return {"function_id": function_id, "code": code}