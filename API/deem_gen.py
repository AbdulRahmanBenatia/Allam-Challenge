from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

import os
from ibm_watsonx_ai import APIClient
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5WZTRrVnZkc25JUUdrOWs0YzFRMlhrNjBmekhKSW1GUW5NWUJjN3A4ZkkifQ.eyJ1aWQiOiIxMDAwMzMxMDgwIiwidXNlcm5hbWUiOiI2NDE3YTJjZi1jMzM2LTQ2ZjMtYTk1Yi0wZWVhZTA2ZjJjOTIiLCJyb2xlIjoiVXNlciIsInBlcm1pc3Npb25zIjpbInNpZ25faW5fb25seSJdLCJncm91cHMiOlsxMDAzNywxMDAwMF0sInN1YiI6IjY0MTdhMmNmLWMzMzYtNDZmMy1hOTViLTBlZWFlMDZmMmM5MiIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJhcGlfcmVxdWVzdCI6dHJ1ZSwiaWF0IjoxNzMxMDYzNjgwLCJleHAiOjUzMzEwNjAwODB9.UjmuPRQFJpK75Zm9pDuGUvN0xl-Nu6fCFVo3JLU7oqXya_K6Q5fpICT7sGbj2j26N1a6ORPcu5LIZCqYqleo6lT6kHFjIAZigCdDkmJTy2MhAMqaonGRzVvNx_jcwPIemqdqjxcmmdfRt3ub9xygB727sM_oIXSAAq_CetjrTc_uD-jH7zzU6LhtZpkp21ym3h1ujO-O1GT240PeJUezdE5Q6V0Y0kDxJyVUCznHclrAmM_iuJiCSAnidIqR-6-ZDF76hjGaZj87AVw-ZPy-6koNV-ECInJi6FwQ1cdvVezvLzoeUWcyzrwQBG0vwA_gXXXuF2hRYKPyQ33yTFMdOg'

wml_credentials = {
                   "url": "https://ai.deem.sa/",
                   "token": access_token,
                   "instance_id": "openshift",
                   "version": "5.0"
                  }

deployment_inference = ModelInference(
    deployment_id="0ab9f16a-4d3d-47a5-9ac5-ee8873e60454",
    credentials = wml_credentials,
    
    project_id="9a1081dd-6578-4f74-9d69-b36ab00901f4"
    )



def deem_get_response(prompt):
    generated_response = deployment_inference.generate(prompt=prompt)
    return generated_response['results'][0]['generated_text']