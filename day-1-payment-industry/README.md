# e-KYC automation

This is a simple tools that can demonstrate how an KYC flow is automated.


## Product I use
- Instill AI VDP Cloud

## Prerequisites
- Python

## Quick Start to Run the App Locally


### Clone the Repository
```bash
git clone https://github.com/chuang8511/30-days-of-ai-pipeline.git && cd 30-days-of-ai-pipeline/day-1-payment-industry
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a Secret File

#### Obtain Instill Cloud API Token
1. Log in to your [Instill Cloud](https://instill.tech) account.
2. Navigate to **Settings > API Tokens** to obtain your API token.

#### Add the Secret for the Demo
1. Create a `.streamlit` directory in your working directory if it doesn't exist.
2. Add a file named `secrets.toml` in the `.streamlit` directory.
3. In the `secrets.toml` file, set your Instill Cloud API token as follows:
    ```toml
    INSTILL_CLOUD_API_TOKEN = "<Your Instill Cloud API Token>"
    ```

### Run the Demo

Run the demo to upload the image with your id card and face:
```bash
streamlit run streamlit_app.py
```
Now, open your browser and go to `http://localhost:8501` to start using the app.

#### Note
1. The model should be changed a better model, which requires the input of AI engineer.
2. The business logic here is easily demonstrated by people_count should be 2 and book_count should be 1. If not, the image should reject automatically.