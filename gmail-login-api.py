import requests

API_URL = "https://gmail-api.catmmo.com/login"

def login_and_get_cookies(email, password):
    """
    Calls the Gmail login API and returns the session cookies.
    Returns a dictionary of cookies on success, or None on failure.
    """
    payload = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        
        # Success
        if response.status_code == 200:
            data = response.json()
            if data.get("status") in ("success", "edu_success"):
                return data.get("cookies")
                
        # Handle errors
        else:
            try:
                error_msg = response.json()
                print(f"API Error ({response.status_code}): {error_msg}")
            except ValueError:
                print(f"API Error ({response.status_code}): {response.text}")
                
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        
    return None

if __name__ == "__main__":
    # Input credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    print(f"Attempting login for: {email}...")
    cookies = login_and_get_cookies(email, password)
    
    if cookies:
        print("\nLogin successful! Here are your cookies:")
        print(cookies)
    else:
        print("\nLogin failed. No cookies returned.")
