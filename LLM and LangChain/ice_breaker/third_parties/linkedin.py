import os
import requests

response = requests.get("https://gist.githubusercontent.com/it4god/cb7f897dcfcf10586ff3d9a649a086e9/raw/c033a79ba1d040ebc36ad5f1e84a9804c2c66130/jeffrey-lim.json")

def scrape_linkendin_profile(linkedin_profile_url: str):
    api_key = ''
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': linkedin_profile_url,
        'extra': 'include',
        'github_profile_id': 'include',
        'facebook_profile_id': 'include',
        'twitter_profile_id': 'include',
        'personal_contact_number': 'include',
        'personal_email': 'include',
        'inferred_salary': 'include',
        'skills': 'include',
        'use_cache': 'if-present',
        'fallback_to_cache': 'on-error',
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()

def get_data():
    response = requests.get("https://gist.githubusercontent.com/it4god/cb7f897dcfcf10586ff3d9a649a086e9/raw/e9b39981e1de00ea1cc2fbff4f8af933753aa32a/jeffrey-lim.json")
    return response.json()

if __name__ == "__main__":
    profile_url = "https://www.linkedin.com/in/hadipramono/"
    linkenin_data = scrape_linkendin_profile(profile_url)
    print(linkenin_data)