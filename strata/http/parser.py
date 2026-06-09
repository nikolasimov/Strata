from strata.http.request import HTTPRequest

class HTTPParser:
    def parse(self, raw_data):
        text = raw_data.decode("utf-8")
        lines = text.split("\r\n")
        
        parts = lines[0].strip().split(" ")
        if len(parts) != 3:
            raise ValueError("Invalid HTTP request line")
        
        method = parts[0]
        path = parts[1]
        version = parts[2]
        headers = {}
        
        for line in lines[1:]:
            if line == "":
                continue
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()
        
        return HTTPRequest(method, path, version, headers)