## Roughly write
1. Build a pipeline to read the message in the all channels that will have discussion
2. In code, chunk the conversation text and send text to LLM pipelines
3. Build pipelines with multiple LLM
  - to convert the conversations to bullet points with subject and background
  - to judge if those bullet points are actionable
4. In code, manage the response from LLM and send the request to pipeline to register an issues.
5. Build a pipeline to register an issue in GitHub
## To automate it
. Set up a weekday cron job in Mac
  - https://www.doabledanny.com/cron-jobs-on-mac


### Memo
- use dev-vdp / dev-model channel to demo