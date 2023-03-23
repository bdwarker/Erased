import requests
import time
apiKeyNasa = 'HKRwg4WOe6gD7gPOm0NJMvKpSVEQNDBig4wcm9eW'
params = {
  'api_key' : apiKeyNasa,
  'hd':'True'
}
url = 'https://api.nasa.gov/planetary/apod?api_key=HKRwg4WOe6gD7gPOm0NJMvKpSVEQNDBig4wcm9eW'

def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False
def getAPOD():
  request = requests.get(url)
  data = check_valid_status_code(request)

  return data