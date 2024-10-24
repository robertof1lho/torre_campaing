import json
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative

# Carregar as credenciais da API (incluindo o ID da conta sandbox)
with open('config/credentials.json') as cred_file:
    credentials = json.load(cred_file)

access_token = credentials['access_token']
ad_account_id = credentials['ad_account_id']  # Use a conta sandbox

# Inicializar a API com o token de acesso
FacebookAdsApi.init(access_token=access_token)

# Inicializar a conta de anúncios Sandbox
ad_account = AdAccount(ad_account_id)

try:
    # Criar a campanha em modo Sandbox
    campaign = ad_account.create_campaign(params={
        'name': 'Tech Lead Recruitment Campaign (Sandbox)',
        'objective': 'OUTCOME_TRAFFIC',
        'status': 'PAUSED',  # A campanha pode ser ativada posteriormente
        'special_ad_categories': []  # Nenhuma categoria especial
    })
    
    campaign_id = campaign.get_id()
    print(f"Campanha criada com ID: {campaign_id} (Modo Sandbox)")

    # Criar o AdSet com a segmentação em Sandbox
    ad_set = ad_account.create_ad_set(params={
        'name': 'Tech Lead AdSet - Latin America (Sandbox)',
        'campaign_id': campaign_id,
        'daily_budget': 20000,  # $200/dia
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': 'REACH',
        'bid_amount': 100,  # Custo por impressão
        'targeting': {
            # Localização geográfica
            'geo_locations': {
                'countries': ['BR', 'MX', 'AR', 'CL', 'PE'],  # Países da América Latina
            },
            # Faixa etária
            'age_min': 25,
            'age_max': 45,
            # Idiomas
            'locales': [6],  # ID para 'en_US' (Inglês)
            # Plataformas: Facebook e Instagram
            'device_platforms': ['mobile', 'desktop'],
            'publisher_platforms': ['facebook', 'instagram'],
            'facebook_positions': ['feed', 'marketplace'],  # Locais onde o anúncio aparecerá
        },
        'status': 'ACTIVE',
        'start_time': '2024-10-25T00:00:00-0800',  # Data de início
        'end_time': '2024-11-25T23:59:59-0800'     # Data de término
    })
    
    ad_set_id = ad_set.get_id()
    print(f"AdSet criado com ID: {ad_set_id} (Modo Sandbox)")

    # Criar o AdCreative em modo Sandbox
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
            'page_id': '450954828104598'  # Substitua por um page_id real de uma página que você gerencia
        }
    })
    
    ad_creative_id = ad_creative.get_id()
    print(f"AdCreative criado com ID: {ad_creative_id} (Modo Sandbox)")

except Exception as e:
    print(f"Erro durante a execução: {str(e)}")
