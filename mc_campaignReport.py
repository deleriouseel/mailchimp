import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import json
import os


try:
  client = MailchimpMarketing.Client()
  mailchimp_api = os.environ.get('MAILCHIMP_API_KEY')
  client.set_config({
  "api_key": mailchimp_api,
  "server": str(mailchimp_api[-4:])
})
  response = client.reports.get_all_campaign_reports()
  latest_campaign = response["reports"][0]["id"]
  print(latest_campaign)
  response = client.reports.get_campaign_report(latest_campaign)
  with open("mailchimp_campaignReport.json", "w") as f:
    data = {
        "campaign_title": response["campaign_title"], 
        "subject_line" : response["subject_line"],
        "emails_sent": response["emails_sent"], 
        "abuse_reports" : response["abuse_reports"], 
        "hard_bounces" : response["bounces"]["hard_bounces"], 
        "soft_bounces" : response["bounces"]["soft_bounces"], 
        "open_rate" : response["opens"]["open_rate"],
      }
    
    f.write(json.dumps(data, indent=4))
    print(data)

except ApiClientError as error:
    print("Error: {}".format(error.text))
