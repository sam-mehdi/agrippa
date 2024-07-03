# agrippa
[Agrippa](https://en.wikipedia.org/wiki/Marcus_Vipsanius_Agrippa) AI. For doing everything that [Octavian](https://en.wikipedia.org/wiki/Augustus) doesn't feel like doing.

## Setup

```bash
# Create a virtual env and activate it
python -m venv .venv
.venv\Scripts\activate

# WINDOWS ONLY - for setting PYTHONPATH env var. Need to do this in PowerShell with elevated privileges
setx PYTHONPATH "$env:PYTHONPATH;<path to repository>" -m

# Install requirements
pip install -r requirements.txt
```

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=<your_openai_api_key>
OPENWEATHERMAP_API_KEY=<openweather_api_key>
```

For other credentials, create an `env` folder in the root directory.

Tools requiring credentials:
- **Google credentials** - `google-credentials.json`. For `tools/gmail.py`
	- Follow instructions [here](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) to get `credentials.json`
	- Rename it to `google_credentials.json` and put it in `env/google_credentials.json`
- **OpenWeather API**
	- Click "Subscribe" [here](https://openweathermap.org/api/). Go through the process until you get an API key. In `.env`, set `OPENWEATHERMAP_API_KEY="<key>"`

You can always remove the tool from `tools/all_tools.py`. Currently, there are three supported tools:
- Gmail
- Weather
- YouTube

## Run
```
python ./agrippa/main.py
```
