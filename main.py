import uvicorn

def main():
    uvicorn.run("a11ytagger.asgi:application", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
