import random

regions = ["DE-HE", "DE-BE", "US-NY", "US-CA", "RU-MOW", "RU-LED", "GB-LND", "FR-PAR"]
campaigns = ["credit_card_offer", "loan_offer", "insurance_offer", "investment_offer", "deposit_offer"]
statuses = ["answered", "no_answer", "busy", "declined"]
responses = ["interested", "not_interested", "call_back", "more_info"]

values = []
for i in range(1, 100001):
    call_id = f"call_{i}"
    call_time = f"DateTime::FromSeconds({1717000000 + i * 100})"
    client_id = f"client_{i % 10000}"
    region = regions[i % len(regions)]
    campaign = campaigns[i % len(campaigns)]
    status = statuses[i % len(statuses)]
    response = responses[i % len(responses)]
    duration = 60 + (i % 600)
    follow_up = "true" if i % 2 == 0 else "false"
    
    values.append(f'("{call_id}", {call_time}, "{client_id}", "{region}", "{campaign}", "{status}", "{response}", {duration}, {follow_up})')

for i in range(0, len(values), 1000):
    chunk = values[i:i+1000]
    query = f'''INSERT INTO transactions_v2 (call_id, call_time, client_id, region_code, campaign_type, call_status, client_response, duration_sec, follow_up_required)
VALUES {", ".join(chunk)}'''
    
    with open(f'insert_part_{i//1000}.sql', 'w') as f:
        f.write(query)