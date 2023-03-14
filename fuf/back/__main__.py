import uvicorn

uvicorn.run("back.app:app", host="0.0.0.0", port=8848, reload=True)
