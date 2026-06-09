from strata.server import Server

def main():
    server = Server(host="127.0.0.1", port=8080)
    server.start()

if __name__ == "__main__":
    main()