import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/?rapidapi-key=b64807b78cmshed53143ff20034fp1e358ajsndde24512dae3"

def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_quote():
    request = requests.get(url)
    data = check_valid_status_code(request)
    return data