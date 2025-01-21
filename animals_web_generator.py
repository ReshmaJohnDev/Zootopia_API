import requests

URL = "https://api.api-ninjas.com/v1/animals"
KEY_VALUE = "X-Api-Key=u0e9t1G4TQm22fEUoeK10Q==bEhGG2YX3v10GQrY"

#?name=&X-Api-Key=u0e9t1G4TQm22fEUoeK10Q==bEhGG2YX3v10GQrY


def get_animal_data(url):
    res = requests.get(url)
    return res.json()



def main() :
    """
    This is the main function through which the sub functions get invoked .
    """
    animal_name = "fox"
    req_url = URL+"?name="+f"{animal_name}"+"&"+f"{KEY_VALUE}"
    animal_data = get_animal_data(req_url)
    print(animal_data)


if __name__ == "__main__":
    main()