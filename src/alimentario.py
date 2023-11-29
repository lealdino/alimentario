import requests
import json
import base64
import pandas as pd
import io

# Constants
CONTENT_TYPE_JSON = "application/json"
COOKIE = "LS-BFZSAEVMKCPRBIUK=ehvcotsuvgjkoff0n91nn2m3um"
USER_AGENT = "insomnia/2023.5.8"

def create_session():
    """Creates a session with predefined headers."""
    session = requests.Session()
    session.headers.update({
        "cookie": COOKIE,
        "Content-Type": CONTENT_TYPE_JSON,
        "User-Agent": USER_AGENT
    })
    return session

def get_session_key(session, url, email, password):
    """Get session key from LimeSurvey API."""
    payload = {
        "method": "get_session_key",
        "params": [email, password],
        "id": 1
    }
    response = session.post(url, json=payload, verify=False)
    return json.loads(response.text)["result"]

def export_responses(session, url, key, survey_id):
    """Export responses from LimeSurvey API."""
    payload_survey = {
        "method": "export_responses",
        "params": [key, survey_id, "csv", None, "complete", "code", "long"],
        "id": 1
    }
    response = session.post(url, json=payload_survey, verify=False)
    return json.loads(response.text)["result"]

def get_limesurvey_data(url, email, password, survey_id):
    """
    Fetches survey data from LimeSurvey and returns it as a pandas DataFrame.

    :param url: URL to LimeSurvey API.
    :param email: Email for authentication.
    :param password: Password for authentication.
    :param survey_id: ID of the survey.
    :return: DataFrame containing survey data.
    """
    session = create_session()
    try:
        key = get_session_key(session, url, email, password)
        survey_encoded = export_responses(session, url, key, survey_id)
        survey_decoded = base64.b64decode(survey_encoded).decode("utf-8")
        return pd.read_csv(io.StringIO(survey_decoded), sep=";")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
# df = get_limesurvey_data("https://your-limesurvey-url", "your-email", "your-password", "survey-id")
