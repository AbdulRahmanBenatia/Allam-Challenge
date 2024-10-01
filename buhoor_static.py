import json
from ibm_API import get_reponse, reshape_text

BUHOOR = [
    "السريع",
    "الكامل",
    "المتقارب",
    "المتدارك",
    "المنسرح",
    "المديد",
    "المجتث",
    "الرمل",
    "البسيط",
    "الخفيف",
    "الطويل",
    "الوافر",
    "الهزج",
    "الرجز",
    "المقتضب",
    "الخبب",
]


responses = {}

for bahr in BUHOOR:
    prompt = f"اشرح بحر {bahr} بإيجاز بسيييط مع التفاعيل دون أمثلة"

    response = get_reponse(prompt=prompt)

    responses[bahr] = reshape_text(response)

with open('buhur_responses.json', 'w', encoding='utf-8') as json_file:
    json.dump(responses, json_file, ensure_ascii=False, indent=4)

print("Responses saved to 'buhur_responses.json'")
