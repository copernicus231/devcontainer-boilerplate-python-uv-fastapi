import uvicorn
import typer

app = typer.Typer()


@app.command()
def serve(host: str = "0.0.0.0", port: int = 6174):
    """
    Run the FastAPI server.
    """
    #import os
    from .base import app as fastapi_app

    # Set the environment variable for the model path
    #os.environ["MODEL_PATH"] = "/tmp/whisper_model"

    # Run the FastAPI app
    uvicorn.run(fastapi_app, host=host, port=port)
