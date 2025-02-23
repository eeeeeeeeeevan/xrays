import json
from datetime import datetime, timedelta

now = datetime.now()
start = now.strftime("%Y-%m-%d %H:%M:%S")
end = (now + timedelta(days=3650)).strftime("%Y-%m-%d %H:%M:%S")

license = {
    "header": {"version": 1},
    "payload": {
        "name": "JohnPork", 
        "email": "jpork@nsa.gov",  
        "licenses": [{
            "id": "48-2437-ACBD-29",
            "license_type": "named",
            "product": "IDA",
            "product_id": "IDAPRO",
            "edition_id": "ida-pro",
            "seats": 1,
            "start_date": start,
            "end_date": end,
            "issued_on": start,
            "owner": "JohnPork",  
            "add_ons": [{
                "id": f"48-1337-DEAD-{i}",
                "code": code,
                "owner": "48-2437-FUCK-29",
                "start_date": start,
                "end_date": end
            } for i, code in enumerate([
                "HEXX86", "HEXX64", "HEXARM", "HEXARM64", "HEXMIPS", "HEXMIPS64",
                "HEXPPC", "HEXPPC64", "HEXRV64", "HEXARC", "HEXARC64"
            ])],
            "features": []
        }]
    },
    "signature": "3238353E900849B6547801BBF8AF31E7822CB4B74A6F54DE03F5E9DFF96AC5DA981B50A62EAAF021F2052CC44498107B36C2D3B34C86B7B48084313189274A1D5D1F45C1F512820C508EA22ABA43EC584E6FEFF6BA9969DD428268F40859AFFE8A2E5BB66CA9C71E78FCAC14E3168D26D11952A71C0F330251D9D74FFC67BD24"
}

try:
    with open("idapro.hexlic", "w", encoding="utf-8") as f:
        json.dump(license, f, separators=(',', ':'))
    print("generated license")
except Exception as e:
    print(e)
