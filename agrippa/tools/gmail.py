from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

credentials = get_gmail_credentials(
    scopes=["https://mail.google.com/"],
    client_secrets_file="env/google_credentials.json",
)

api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)

def get_gmail_tools():
    return toolkit.get_tools()
