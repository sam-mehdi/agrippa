# agrippa
Agrippa AI. For doing everything that Octavian doesn't feel like doing.

## Setup

```bash
# Create a virtual env and activate it
python -m venv .venv
.venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=<your_openai_api_key>
```

For other credentials, create an `env` folder in the root directory. Include the following files:
- **Google credentials** - `google-credentials.json`
	- Follow instructions [here](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) to get `credentials.json`
	- Rename it
