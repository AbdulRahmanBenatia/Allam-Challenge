from ibm_watsonx_ai.foundation_models import Model
import arabic_reshaper
from bidi.algorithm import get_display
credentials = {
    "url": "https://eu-de.ml.cloud.ibm.com",
    "apikey":"onhPojH5r-y97tpISLwazW5w98J8iPL3pDkGWbvMtngl"
}


PROJECT_ID = "636be447-f2c1-4095-bfe0-0ade403e341d"
MODEL_ID = "sdaia/allam-1-13b-instruct"


parameters = {
    "decoding_method":"greedy",
    "max_new_tokens":70,
    "repetition_penalty":1.05
}


MODEL = Model(
    model_id = MODEL_ID,
    params= parameters,
    credentials = credentials,
    project_id=PROJECT_ID
)

def get_reponse(prompt):
    res = MODEL.generate_text(prompt=prompt)
    
    return res

# Handling Arabic Text
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

if __name__ == "__main__":
    prompt = """
    اشرح البيت في سطر واحد:
    قفا نبك من ذكرى حبيب ومنزل .. بسقط اللوى بين الدخول فحومل
    """
    print(reshape_text(get_reponse(prompt)))




