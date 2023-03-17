from uvicorn import run


if __name__ == '__main__':
    run("pkg.server.handler:app", host="127.0.0.1", port=8071, log_level="error")

