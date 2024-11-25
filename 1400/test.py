import requests

def accept_referral_code(referral_code: str):
    """
    Function to accept a referral code invitation on the Shein app and create new users.

    Parameters:
    - referral_code: str
        The referral code to be accepted.

    Returns:
    - str:
        A message indicating the success or failure of accepting the referral code.

    Raises:
    - ValueError:
        Raises an error if the referral code is empty or invalid.
    """

    # Checking if the referral code is empty or invalid
    if not referral_code:
        raise ValueError("Referral code cannot be empty.")

    # API endpoint for accepting the referral code invitation
    url = "https://api.shein.com/shein-app-server/api/v2/user/acceptReferralCode"

    # Request payload to accept the referral code
    payload = {
        "referralCode": '6CYQQTY7I'
    }

    try:
        # Sending a POST request to accept the referral code
        response = requests.post(url, json=payload)

        # Checking the response status code
        if response.status_code == 200:
            return "Referral code accepted successfully."
        else:
            return "Failed to accept the referral code."

    except requests.exceptions.RequestException as e:
        return f"Error occurred while accepting the referral code: {str(e)}"


# Example usage of the accept_referral_code function:

referral_code = "rl5hwr"
result = accept_referral_code(referral_code)
print(result)