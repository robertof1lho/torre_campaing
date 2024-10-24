# Process of Creating a Campaign in Sandbox Mode Using Meta Marketing API

## Introduction

This was my first experience with the **Meta for Developers Marketing API**. Given my basic-intermediate level of programming skills and being new to using the Meta Marketing API tools, the process was challenging but extremely enriching. While I was unable to proceed to the stage where I needed to switch the app mode from "Development" to "Public," I made the most of my knowledge and reached the stage of creating a campaign in **Sandbox** mode.

## Steps Followed in the Process

### 1. Initial Configuration and Credentials

I created a JSON file to store the API credentials, including the access token and the sandbox ad account ID.

```json
{
    "access_token": "YOUR_ACCESS_TOKEN",
    "ad_account_id": "act_1223156088951292"
}
```

These credentials are loaded into the Python script to initialize the API and perform operations.

### 2. Initializing the API

The first step was to initialize the API using the provided access token:
````python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# Load API credentials
with open('config/credentials.json') as cred_file:
    credentials = json.load(cred_file)

access_token = credentials['access_token']
ad_account_id = credentials['ad_account_id']

# Initialize API with access token
FacebookAdsApi.init(access_token=access_token)

# Initialize the Sandbox ad account
ad_account = AdAccount(ad_account_id)
````

### 3. Creating a Campaign in Sandbox Mode
The campaign was created in sandbox mode with the objective of OUTCOME_TRAFFIC. The campaign was initially paused.
````python
# Create campaign in Sandbox mode
campaign = ad_account.create_campaign(params={
    'name': 'Tech Lead Recruitment Campaign (Sandbox)',
    'objective': 'OUTCOME_TRAFFIC',
    'status': 'PAUSED',  # Campaign can be activated later
    'special_ad_categories': []  # No special category
})

campaign_id = campaign.get_id()
print(f"Campaign created with ID: {campaign_id} (Sandbox Mode)")
````

### 4. Creating an Ad Set
The AdSet segmentation was defined for Latin American countries, targeting individuals between the ages of 25 and 45 who use mobile or desktop devices.

```python
# Create the AdSet with segmentation in Sandbox
ad_set = ad_account.create_ad_set(params={
    'name': 'Tech Lead AdSet - Latin America (Sandbox)',
    'campaign_id': campaign_id,
    'daily_budget': 20000,  # $200/day
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'bid_amount': 100,  # Cost per impression
    'targeting': {
        'geo_locations': {
            'countries': ['BR', 'MX', 'AR', 'CL', 'PE']
        },
        'age_min': 25,
        'age_max': 45,
        'locales': [6],  # ID for 'en_US' (English)
        'device_platforms': ['mobile', 'desktop'],
        'publisher_platforms': ['facebook', 'instagram'],
        'facebook_positions': ['feed', 'marketplace']  # Ad positions
    },
    'status': 'ACTIVE',
    'start_time': '2024-10-25T00:00:00-0800',
    'end_time': '2024-11-25T23:59:59-0800'
})

ad_set_id = ad_set.get_id()
print(f"AdSet created with ID: {ad_set_id} (Sandbox Mode)")
```

### 5. Creating an Ad Creative
The ad creative was created with the details of a mock ad for the Tech Lead position at Torre. A valid page_id was added.

```python
# Create the AdCreative in Sandbox mode
ad_creative = ad_account.create_ad_creative(params={
    'name': 'Tech Lead Creative (Sandbox)',
    'object_story_spec': {
        'link_data': {
            'caption': 'torre.ai',
            'description': 'Join Torre as a Tech Lead and lead a global team!',
            'link': 'https://torre.ai/post/awyJqjad-torre-product-minded-tech-lead',
            'message': 'We are hiring a Product-Minded Tech Lead! Apply now.',
            'name': 'Tech Lead at Torre - Product Leadership'
        },
        'page_id': '450954828104598'  # Replace with a valid page_id
    }
})

ad_creative_id = ad_creative.get_id()
print(f"AdCreative created with ID: {ad_creative_id} (Sandbox Mode)")
```

6. Error Encountered
While creating the AdCreative, the following error was encountered:

```python
Error during execution:
Message: Call was not successful
Method: POST
Path: https://graph.facebook.com/v21.0/act_1223156088951292/adcreatives
Response: {
  "error": {
    "message": "Invalid parameter",
    "type": "OAuthException",
    "code": 100,
    "error_subcode": 1885183,
    "error_user_title": "The ad creative's publication was created by an app in development mode",
    "error_user_msg": "The ad creative's publication was created by an app in development mode. It must be in public mode to create this ad.",
    "fbtrace_id": "A1u8YDea1q7YuzQw8XcJvHd"
  }
}
```

This error indicates that the app is in development mode and needs to be switched to public mode to create the ad.

### 7. Next Steps
Switching from Development Mode to Public: The next step is to switch the app mode to public. This involves reviewing all app settings in the Meta for Developers and ensuring it is ready for production.

## Conclusion
This process was a cool learning experience, as I was able to configure, create and explore a tool that I had never used, with campaigns and ad sets in sandbox mode using the Meta Marketing API. Despite the difficulties and my basic-intermediate level of programming, I managed to achieve part of the objective.