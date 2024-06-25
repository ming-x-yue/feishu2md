from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

