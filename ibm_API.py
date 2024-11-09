from ibm_watsonx_ai.foundation_models import Model
import arabic_reshaper
from bidi.algorithm import get_display

# Handling Arabic Text
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

credentials = {
    "url": "https://eu-de.ml.cloud.ibm.com",
    "apikey":"onhPojH5r-y97tpISLwazW5w98J8iPL3pDkGWbvMtngl"
}


PROJECT_ID = "636be447-f2c1-4095-bfe0-0ade403e341d"
MODEL_ID = "sdaia/allam-1-13b-instruct"


parameters = {
    "decoding_method":"greedy",
    "max_new_tokens":200,
    "repetition_penalty":1.05
}


MODEL = Model(
    model_id = MODEL_ID,
    params= parameters,
    credentials = credentials,
    project_id=PROJECT_ID
)

def get_response(prompt):
    res = MODEL.generate_text(prompt=prompt)
    
    # print("RESPONSE IN API FUNCTION: ")
    # print(res)
    # print("Reshaped RESPONSE IN API FUNCTION: ")
    # print(reshape_text(res))
    
    return res

import pandas as pd
import re
def remove_tashkeel(verse):
    return re.sub(r'[\u0617-\u061A\u064B-\u0652]', '', verse)  # Remove Tashkeel


# if __name__ == "__main__":
    
    # prompt = """
    # اشرح البيت في سطر واحد:
    # قفا نبك من ذكرى حبيب ومنزل .. بسقط اللوى بين الدخول فحومل
    # """
    # print(reshape_text(get_reponse(prompt)))
    
    # prompt =f"""
    #         اشرح هذا البيت شرحا موجزا جدا:
    #         {reshape_text('ﺰﻨﻣﻭ ﺐﻴﺒﺣ ﻯﺮﻛﺫ ﻦﻣ ﻚﺒﻧ ﺎﻔﻗ')}
    # """
    # print(prompt)
    # # print(reshape_text(get_reponse(prompt)))
    # generation_data_df = pd.read_json("test_gen.json", encoding="utf-8")
    # generation_data_df["MGT"] = "MGT"

    # print(generation_data_df.iloc[10,0])
    # bait  = "إِن صَوَّروكَ فَإِنَّما قَد صَوَّروا تاجَ الفَخارِ وَمَطلَعَ الأَنوارِ"
    # bait_no_tashkeel = remove_tashkeel(bait)
    # print(bait_no_tashkeel)
    # prompt = bait
    # print(get_response(bait_no_tashkeel))





