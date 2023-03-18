from uvicorn import run


if __name__ == '__main__':
    print("proxy started")
    run("pkg.server.handler:app", host="0.0.0.0", port=80, log_level="error")

