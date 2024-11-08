import pandas as pd
from ibm_API import get_response

import arabic_reshaper
from bidi.algorithm import get_display
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

generation_data_df = pd.read_json("test_gen.json", encoding="utf-8")
generation_data_df["MGT"] = "MGT"

print(generation_data_df.iloc[10,0])
bait  = "إِن صَوَّروكَ فَإِنَّما قَد صَوَّروا تاجَ الفَخارِ وَمَطلَعَ الأَنوارِ"
prompt = generation_data_df.iloc[10,0]
print(get_response(generation_data_df.iloc[10,0]))
