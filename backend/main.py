import uvicorn

def main():
    uvicorn.run("a11ytagger.asgi:application", host="0.0.0.0", port=3000)


if __name__ == "__main__":
    main()
