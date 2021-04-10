from dataclasses import dataclass
import requests
import json

class RequestType:
    GET = "GET"
    POST = "POST"

@dataclass
class Request:
    method: str
    url: str
    data: str = ''
    headers: str = ''

reqs = [
    Request(RequestType.GET, "https://thatcopy.pw/catapi/rest"),
    Request(RequestType.GET, "http://api.postcodedata.nl/v1/postcode/?postcode=1017GC&streetnumber=60&ref=domeinnaam.nl&type=json")
    # TODO: find a POST request
]

def print_response(req: Request, resp: requests.Response):
    data = resp.json()
    output = {'request': req.__dict__, 'response': data}
    print(json.dumps(output, sort_keys=True, indent=2))

def do_req(req: Request):
    if req.method == RequestType.GET:
        resp = requests.get(req.url)
        return resp
    return None

def main():
    for r in reqs:
        resp = do_req(r)
        print_response(r, resp)

if __name__ == '__main__':
    main()
