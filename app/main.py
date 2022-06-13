from typing import Union
from fastapi import FastAPI,Request
from .api.api_v1.api import router as api_router
from .core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(title=PROJECT_NAME)


app.include_router(api_router, prefix=API_V1_STR)

# ---- Rremove in prod ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# ---- Rremove in prod ---