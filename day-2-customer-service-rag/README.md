# Customer Service Automation

This is a simple tools that can demonstrate how you can build a pipeline by scraping web data.


## Product I use
- Instill VDP 
- Instill Artifact

## Prerequisites
- Python

## Quick Start to Run the App Locally
No, you only can view the notebook code block by code block

### Clone the Repository
```bash
git clone https://github.com/chuang8511/30-days-of-ai-pipeline.git && cd 30-days-of-ai-pipeline/day-2-customer-service-rag
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a Secret File

#### Obtain Instill Cloud API Token
1. Log in to your [Instill Cloud](https://instill.tech) account.
2. Navigate to **Settings > API Tokens** to obtain your API token.
3. Navigate to ** Artifacts > Create Catalog** to obtain your catalog storage.
4. clone the pipelines to your namespace
  - https://instill.tech/chunhao094/pipelines/get-links/playground
  - https://instill.tech/chunhao094/pipelines/upload-web-data/playground
  - https://instill.tech/chunhao094/pipelines/talk-to-aftee/playground 
  - https://instill.tech/chunhao094/pipelines/get-all-files-in-catalog/playground

#### Add the Secret for the Demo
- Please follow the instruction in the notebokk.

#### Note
1. The accuracy is still not good out of several reasons including data quality, lack of model fine-tuning, no support image, and no chat history yet.
2. Some specific questions required users' sensitive data, which will need human-in-loop system design in the demo

### Thanks to @kuroxx for co-programming