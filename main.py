import uvicorn

if __name__ == "__main__":
    # make sure to make reload=False for production
    uvicorn.run("coolor.app:app",reload=True)